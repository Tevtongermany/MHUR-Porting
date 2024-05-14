using CommunityToolkit.Mvvm.ComponentModel;
using CUE4Parse.UE4.Versions;
using MHURPorting.AppUtils;

namespace MHURPorting.ViewModels;

public class BlenderViewModel : ObservableObject
{
    public bool IsRestartRequired = false;
    public bool UseIk
    {
        get => AppSettings.Current.UsingIk;
        set
        {
            AppSettings.Current.UsingIk = value;
            OnPropertyChanged();
        }
    }
}