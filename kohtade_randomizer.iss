; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Kohtade randomizer"
#define MyAppVersion "1.1.0"
#define MyAppPublisher "Nikita Radionov"
#define MyAppExeName "Kohtade randomizer.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{057C65E5-6132-4F5F-B8F4-8A1553C2680A}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
OutputDir=E:\nikit\PycharmProjects\kohad\dist
OutputBaseFilename=kohtade_randomizer
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "E:\nikit\PycharmProjects\kohad\dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "E:\nikit\PycharmProjects\kohad\dist\readme.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "E:\nikit\PycharmProjects\kohad\dist\restore.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "E:\nikit\PycharmProjects\kohad\dist\config.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "E:\nikit\PycharmProjects\kohad\dist\klass.txt"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Dirs]
Name: "{app}\saves";

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

