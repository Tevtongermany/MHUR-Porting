using MHURPorting.ViewModels;

namespace MHURPorting.Services;

public static class ApplicationService
{
    public static ApplicationViewModel AppVM = new();
    public static ApiEndpointViewModel ApiEndpointView { get; } = new();
}