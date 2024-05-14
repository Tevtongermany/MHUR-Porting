using System.Windows;
using MHURPorting.ViewModels;
using MHURPorting.AppUtils;
using MHURPorting.Services;

namespace MHURPorting.Views;

public partial class BlenderView
{
    public BlenderView()
    {
        InitializeComponent();
        AppVM.BlenderVM = new BlenderViewModel();
        DataContext = AppVM.BlenderVM;
    }
    private void OnClickOK(object sender, RoutedEventArgs e)
    {
        if (AppVM.BlenderVM.IsRestartRequired)
        {
            AppVM.RestartWithMessage("A restart is required.", "An option has been changed that requires a restart to take effect.");
        }
        
        Close();
    }
}