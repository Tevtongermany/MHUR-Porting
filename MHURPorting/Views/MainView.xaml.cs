using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using CUE4Parse.UE4.Assets.Exports;
using CUE4Parse.UE4.Assets.Exports.Texture;
using CUE4Parse.UE4.Assets.Objects;
using CUE4Parse.UE4.Objects.Core.i18N;
using CUE4Parse.UE4.Objects.Engine;
using MHURPorting.AppUtils;
using MHURPorting.Services;
using MHURPorting.ViewModels;
using MHURPorting.Views.Controls;
using MHURPorting.Export;
using MHURPorting.Export.Blender;
using MHURPorting.Views.Extensions;
using Serilog;
using StyleSelector = MHURPorting.Views.Controls.StyleSelector;
using CUE4Parse.UE4.Assets.Exports.SkeletalMesh;

namespace MHURPorting.Views;

public partial class MainView
{
    public MainView()
    {
        InitializeComponent();
        AppVM.MainVM = new MainViewModel();
        DataContext = AppVM.MainVM;

        AppLog.Logger = LoggerRtb;
    }

    private async void OnLoaded(object sender, RoutedEventArgs e)
    {
        if (string.IsNullOrWhiteSpace(AppSettings.Current.ArchivePath))
        {
            AppHelper.OpenWindow<StartupView>();
            return;
        }
        
        await AppVM.MainVM.Initialize();
    }

    private async void OnAssetTabSelectionChanged(object sender, SelectionChangedEventArgs e)
    {
        if (sender is not TabControl tabControl) return;
        if (AppVM.AssetHandlerVM is null) return;

        var assetType = (EAssetType) tabControl.SelectedIndex;
        var handlers = AppVM.AssetHandlerVM.Handlers;
        foreach (var (handlerType, handlerData) in handlers)
        {
            if (handlerType == assetType)
            {
                handlerData.PauseState.Unpause();
            }
            else
            {
                handlerData.PauseState.Pause();
            }
        }

        if (!handlers[assetType].HasStarted)
        {
            await handlers[assetType].Execute();
        }

        DiscordService.Update(assetType);
        AppVM.MainVM.CurrentAssetType = assetType;
    }

    private async void OnStyleSelectionChanged(object sender, SelectionChangedEventArgs e)
    {
        if (sender is not ListBox listBox) return;
        if (listBox.SelectedItem is null) return;
        var selected = (AssetSelectorItem)listBox.SelectedItem;

    }
    private void OnSearchTextChanged(object sender, TextChangedEventArgs e)
    {
        var searchBox = (TextBox) sender;
        foreach (var tab in AssetControls.Items.OfType<TabItem>())
        {
            var listBox = (ListBox) tab.Content;
            listBox.Items.Filter = o => ((AssetSelectorItem) o).Match(searchBox.Text);
            listBox.Items.Refresh();
        }
    }
    private async void OnAssetSelectionChanged(object sender, SelectionChangedEventArgs e)
    {
        if (sender is not ListBox listBox) return;
        if (listBox.SelectedItem is null) return;
        var selected = (AssetSelectorItem)listBox.SelectedItem;
        AppVM.MainVM.Styles.Clear();
        AppVM.MainVM.CurrentAsset = selected;
        var current_asset = selected;
        var styles = selected.MainAsset.GetOrDefault<UScriptMap>("_costumeMeshs").Properties.ToArray();
        var NStyles = new List<UObject>();
        var NSkeleton = new List<UObject>();
        foreach (var skeletons in styles)
        {
            if (current_asset != selected)
            {
                AppVM.MainVM.Styles.Clear();
            }
            Console.WriteLine("doing Style thingie {0}", skeletons);
            var skeleton = await AppVM.CUE4ParseVM.Provider.TryLoadObjectAsync<UObject>(skeletons.Value.GenericValue.ToString());
            if (skeleton is not null) 
            {
                Console.WriteLine("added skeleton");
                NStyles.Add(selected.UIAsset);
                NSkeleton.Add(skeleton);
            }

        }

    }

    private void StupidIdiotBadScroll(object sender, MouseWheelEventArgs e)
    {
        if (sender is not ScrollViewer scrollViewer) return;
        switch (e.Delta)
        {
            case < 0:
                scrollViewer.ScrollToVerticalOffset(scrollViewer.VerticalOffset + 88);
                break;
            case > 0:
                scrollViewer.ScrollToVerticalOffset(scrollViewer.VerticalOffset - 88);
                break;
        }
    }
    
    private async void AssetFolderTree_OnSelectedItemChanged(object sender, RoutedPropertyChangedEventArgs<object> e)
    {
        var treeView = (TreeView) sender;
        var treeItem = (TreeItem) treeView.SelectedItem;
        if (treeItem is null) return;
        if (treeItem.AssetType == ETreeItemType.Folder) return;

        await AppVM.MainVM.SetupMeshSelection(treeItem.FullPath!);
    }


    // private async void AssetFlatView_OnSelectionChanged(object sender, SelectionChangedEventArgs e)
    // {
    //     var listBox = (ListBox) sender;
    //     var selectedItem = (AssetItem) listBox.SelectedItem;
    //     if (selectedItem is null) return;
    //     
    //     await AppVM.MainVM.SetupMeshSelection(listBox.SelectedItems.OfType<AssetItem>().ToArray());
    // }

    private void AssetFlatView_OnMouseDoubleClick(object sender, MouseButtonEventArgs e)
    {
        var listBox = (ListBox) sender;
        var selectedItem = (AssetItem) listBox.SelectedItem;
        if (selectedItem is null) return;
        
        JumpToAsset(selectedItem.PathWithoutExtension);
    }
    
    private void JumpToAsset(string directory)
    {
        var children = AppVM.MainVM.Meshes;

        var i = 0;
        var folders = directory.Split('/');
        while (true)
        {
            foreach (var folder in children)
            {
                if (!folder.Header.Equals(folders[i], StringComparison.OrdinalIgnoreCase))
                    continue;

                if (folder.AssetType == ETreeItemType.Asset)
                {
                    folder.IsSelected = true;
                    return;
                }

                folder.IsExpanded = true;
                children = folder.Children;
                break;
            }

            i++;
            if (children.Count == 0) break;
        }
    }
}