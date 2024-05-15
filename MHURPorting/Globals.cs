global using static MHURPorting.Services.ApplicationService;
global using Serilog;
using System.Reflection;
using CUE4Parse.UE4.Objects.Core.Misc;
using MHURPorting.models;
using Newtonsoft.Json;
using System.IO;

namespace MHURPorting;

public static class Globals
{
    public static readonly string APP_VERSION = "1.2.0";

    public const string DISCORD_URL = "https://discord.gg/AkQjH3yH5q";
    public const string GITHUB_URL = "https://github.com/Tevtongermany/MHUR-Porting";

    public const int BLENDER_PORT = 24290;
    public const int UNREAL_PORT = 24291;
    public const int BUFFER_SIZE = 4096;

    public const string UDPClient_Ping = "Ping";

    public const string WHITE = "#e1e9f2";
    public const string BLUE = "#4b8ad1";
    public const string RED = "#d14b68";
    public const string YELLOW = "#d1c84b";
    public const string GREEN = "#03fc5e";

    public static readonly FGuid ZERO_GUID = new();
    public static readonly string ZERO_CHAR = "0x0000000000000000000000000000000000000000000000000000000000000000";

    public static MHURPortingDefault CharacterMapping = JsonConvert.DeserializeObject<MHURPortingDefault>(File.ReadAllText("MHURPortingDefault.json"));
}