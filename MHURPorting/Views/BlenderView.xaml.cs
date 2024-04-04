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

}