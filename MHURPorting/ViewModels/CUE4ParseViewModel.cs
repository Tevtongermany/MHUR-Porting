using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using CommunityToolkit.Mvvm.ComponentModel;
using CUE4Parse.Encryption.Aes;
using CUE4Parse.FileProvider;
using CUE4Parse.MappingsProvider;
using CUE4Parse.UE4.AssetRegistry;
using CUE4Parse.UE4.AssetRegistry.Objects;
using CUE4Parse.UE4.Assets.Objects;
using CUE4Parse.UE4.Assets.Utils;
using CUE4Parse.UE4.Objects.Core.Math;
using CUE4Parse.UE4.Objects.Core.Misc;
using CUE4Parse.UE4.Readers;
using CUE4Parse.UE4.Versions;
using MHURPorting.AppUtils;
using MHURPorting.Services;
using MHURPorting.Services.Endpoints;
using MHURPorting.Services.Endpoints.Models;

namespace MHURPorting.ViewModels;

public class CUE4ParseViewModel : ObservableObject
{
    private ApiEndpointViewModel _apiEndpointView => ApplicationService.ApiEndpointView;
    public readonly MHURPortingFileProvider Provider;

    public FAssetRegistryState? AssetRegistry;

    public readonly List<FAssetData> AssetDataBuffers = new();

    public static readonly VersionContainer Version = new(EGame.GAME_UE4_LATEST);
    
    public HashSet<string> MeshEntries;
    private static readonly string[] MeshRemoveList = {
        "/Sounds",
        "/Playsets",
        "/UI",
        "/2dAssets",
        "/Textures",
        "/Audio",
        "/Sound",
        "/Materials",
        "/Icons",
        "/Anims",
        "/DataTables",
        "/TextureData",
        "/ActorBlueprints",
        "/Physics",
        "/_Verse",
        
        "/PPID_",
        "/MI_",
        "/MF_",
        "/NS_",
        "/T_",
        "/P_",
        "/TD_",
        "/MPC_",
        "/BP_",
        
        "Engine/",
        
        "_Physics",
        "_AnimBP",
        "_PhysMat",
        "_PoseAsset",
        
        "PlaysetGrenade",
        "NaniteDisplacement"
    };
    
    public CUE4ParseViewModel(string directory, EInstallType installType)
    {
        if (installType is EInstallType.Local && !Directory.Exists(directory))
        {
            AppLog.Warning("Installation Not Found, Valorant installation path does not exist or has not been set. Please go to settings to verify you've set the right path and restart. The program will not work properly on Local Installation mode if you do not set it.");
            return;
        }
        Provider = installType switch
        {
            EInstallType.Local => new MHURPortingFileProvider(new DirectoryInfo(directory), SearchOption.AllDirectories, true, Version),
            EInstallType.Live => new MHURPortingFileProvider(true, Version),
        };
    }
    
    public async Task Initialize()
    {
        if (Provider is null) return;
        
        await InitializeProvider();
        await InitializeKeys();
        
        Provider.LoadVirtualPaths();

        var assetArchive = await Provider.TryCreateReaderAsync("HerovsGame/AssetRegistry.bin");
        if (assetArchive is not null)
        {
            AssetRegistry = new FAssetRegistryState(assetArchive);
            AssetDataBuffers.AddRange(AssetRegistry.PreallocatedAssetDataBuffers);
        }
                
        var allEntries = AppVM.CUE4ParseVM.Provider.Files.ToArray();
        var removeEntries = AppVM.CUE4ParseVM.AssetDataBuffers.Select(x => AppVM.CUE4ParseVM.Provider.FixPath(x.ObjectPath) + ".uasset").ToHashSet();
        MeshEntries = new HashSet<string>();
        for (var idx = 0; idx < allEntries.Length; idx++)
        {
            var entry = allEntries[idx];
            if (!entry.Key.EndsWith(".uasset")) continue;
            if (MeshRemoveList.Any(x => entry.Key.Contains(x, StringComparison.OrdinalIgnoreCase))) continue;
            if (removeEntries.Contains(entry.Key)) continue;
            MeshEntries.Add(entry.Value.Path);
        }
    }
    
    private async Task InitializeKeys()
    {
        var keyResponse = AppSettings.Current.AesResponse;
        var keyString = "0xB65A5EF761739F55923ECAE30C87159593C89FFC420AC6C7DD5264CC10D7EDD8";
        await Provider.SubmitKeyAsync(Globals.ZERO_GUID, new FAesKey(keyString));
    }
    
    
    private async Task InitializeProvider()
    {
        switch (AppSettings.Current.InstallType)
        {
            case EInstallType.Local:
            {
                Provider.InitializeLocal();
                break;
            }
            case EInstallType.Live:
            {
                var manifestInfo = _apiEndpointView.ValorantApi.GetManifest(CancellationToken.None);
                if (manifestInfo == null)
                {
                    throw new Exception("Could not load latest Valorant manifest, you may have to switch to your local installation.");
                }
                for (var i = 0; i < manifestInfo.Paks.Length; i++)
                {
                    Provider.Initialize(manifestInfo.Paks[i].GetFullName(), new Stream[] { manifestInfo.GetPakStream(i) });
                }
                break;
            }
        }
    }
}