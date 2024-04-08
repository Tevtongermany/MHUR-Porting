using System.ComponentModel;

namespace MHURPorting;

public enum EInstallType
{
    [Description("Local")]
    Local,
    
}

public enum ERichPresenceAccess
{
    [Description("Always")]
    Always,
    
    [Description("Never")]
    Never
}
public enum EMeshType
{
    [Description("Base")]
    Base,

    [Description("Overriden")]
    Overriden
}


public enum EAssetType
{
    [Description("Characters")]
    Character,
    [Description("Mesh")]
    Mesh

    /*[Description("Props")]
    Prop,
    
    [Description("Meshes")]
    Mesh,*/
}

public enum ETreeItemType
{
    Folder,
    Asset
}