import os


print(
"""
welcome to Buildy :D
Select Build Mode
Release 0
Debug 1
"""
      )

buildmode = int(input(""))

if buildmode == 0:
    os.system('dotnet publish MHURPorting '
              '-c Release --no-self-contained '
              '-r win-x64 -o "./Release" '
              '-p:PublishSingleFile=true '
              '-p:DebugType=None '
              '-p:DebugSymbols=false '
              '-p:IncludeNativeLibrariesForSelfExtract=true')
if buildmode == 1:
    os.system('dotnet publish MHURPorting '
              '-c Debug --no-self-contained '
              '-r win-x64 -o "./Debug" '
              '-p:PublishSingleFile=true '
              '-p:DebugType=portable '
              '-p:DebugSymbols=true '
              '-p:IncludeNativeLibrariesForSelfExtract=true')
    
print("\n\nDone :D")
