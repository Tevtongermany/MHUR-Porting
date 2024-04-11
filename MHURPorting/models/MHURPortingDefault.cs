using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using AdonisUI;
using Newtonsoft.Json;

namespace MHURPorting.models;

public class MHURPortingDefault
{

    [JsonProperty("character")]
    public List<Character> Character;
}

public class Character
{
    [JsonProperty("CharacterID")]
    public string ID;

    [JsonProperty("CharacterName")]
    public string Name;

    [JsonProperty("Styles")]
    public List<MHURStyle> styles;
}

public class MHURStyle
{
    [JsonProperty("Style")]
    public StyleDefenition styles;
}

public class StyleDefenition
{
    [JsonProperty("SkeletonPath")]
    public string SkeletonPath;

    [JsonProperty("StyleImagePath")]
    public string StyleImagePath;

}