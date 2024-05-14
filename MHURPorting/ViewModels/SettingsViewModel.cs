using CommunityToolkit.Mvvm.ComponentModel;
using CUE4Parse.UE4.Versions;
using MHURPorting.AppUtils;
using System;

namespace MHURPorting.ViewModels;

public class SettingsViewModel : ObservableObject
{
    public bool IsRestartRequired = false;
    private string _useTime = "Hs";

    public bool IsLocalInstall => InstallType == EInstallType.Local;

    public EInstallType InstallType
    {
        get => AppSettings.Current.InstallType;
        set
        {
            AppSettings.Current.InstallType = value;
            OnPropertyChanged();
            OnPropertyChanged(nameof(IsLocalInstall));
            IsRestartRequired = true;
        }
    }

    public string ArchivePath
    {
        get => AppSettings.Current.ArchivePath;
        set
        {
            AppSettings.Current.ArchivePath = value;
            OnPropertyChanged();
            IsRestartRequired = true;
        }
    }

    public ELanguage Language
    {
        get => AppSettings.Current.Language;
        set
        {
            AppSettings.Current.Language = value;
            OnPropertyChanged();
            IsRestartRequired = true;
        }
    }

    public ERichPresenceAccess DiscordRPC
    {
        get => AppSettings.Current.DiscordRPC;
        set
        {
            AppSettings.Current.DiscordRPC = value;
            OnPropertyChanged();
        }
    }



    public string UseTime
    {
        get
        {
            float current_time_float = 0.0f;
            float.TryParse(AppVM.MainVM.usetime.Elapsed.TotalSeconds.ToString(), out current_time_float);
            Int64 current_time = AppSettings.Current.UseTime + (Int64)current_time_float;
            TimeSpan timeSpan = TimeSpan.FromSeconds(current_time);
            return $"{timeSpan.Days}:{timeSpan.Hours}:{timeSpan.Minutes}:{timeSpan.Seconds}";
        }
    }
}



