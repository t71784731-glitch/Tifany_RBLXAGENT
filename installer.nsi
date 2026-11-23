; NovaAgent - Script NSIS para instalador
!include "MUI2.nsh"
!include "LogicLib.nsh"

Name "NovaAgent"
OutFile "NovaAgent-Setup-1.0.0.exe"
InstallDir "$PROGRAMFILES64\NovaAgent"
InstallDirRegKey HKLM "Software\NovaAgent" "InstallDir"
RequestExecutionLevel user

!define VERSION "1.0.0"
!define MUI_ABORTWARNING
!define MUI_ICON "..\assets\icon.ico"
!define MUI_UNICON "..\assets\icon.ico"

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!define MUI_FINISHPAGE_RUN "$INSTDIR\NovaAgent.exe"
!define MUI_FINISHPAGE_RUN_TEXT "Iniciar NovaAgent ahora"
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_LANGUAGE "Spanish"

Section "Instalar"
    SectionIn RO
    SetOutPath $INSTDIR
    File "..\dist\NovaAgent.exe"
    SetOutPath $INSTDIR\config
    File /r "..\config\*"
    SetOutPath $INSTDIR\docs
    File /r "..\docs\*"
    SetOutPath $INSTDIR\assets
    File /r "..\assets\*"
    CreateDirectory "$APPDATA\NovaAgent\models"
    CreateDirectory "$APPDATA\NovaAgent\logs"
    CreateDirectory "$SMPROGRAMS\NovaAgent"
    CreateShortcut "$SMPROGRAMS\NovaAgent\NovaAgent.lnk" "$INSTDIR\NovaAgent.exe" "" "$INSTDIR\assets\icon.ico" 0
    CreateShortcut "$SMPROGRAMS\NovaAgent\Desinstalar.lnk" "$INSTDIR\Uninstall.exe"
    CreateShortcut "$DESKTOP\NovaAgent.lnk" "$INSTDIR\NovaAgent.exe" "" "$INSTDIR\assets\icon.ico" 0
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NovaAgent" \
        "DisplayName" "NovaAgent ${VERSION}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NovaAgent" \
        "UninstallString" "$INSTDIR\Uninstall.exe"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NovaAgent" \
        "InstallLocation" "$INSTDIR"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NovaAgent" \
        "DisplayIcon" "$INSTDIR\assets\icon.ico"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NovaAgent" \
        "DisplayVersion" "${VERSION}"
    WriteUninstaller "$INSTDIR\Uninstall.exe"
SectionEnd

Section "Uninstall"
    RMDir /r "$INSTDIR"
    Delete "$DESKTOP\NovaAgent.lnk"
    Delete "$SMPROGRAMS\NovaAgent\NovaAgent.lnk"
    Delete "$SMPROGRAMS\NovaAgent\Desinstalar.lnk"
    RMDir "$SMPROGRAMS\NovaAgent"
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\NovaAgent"
SectionEnd

Function .onInit
    ${IfNot} ${RunningX64}
        MessageBox MB_ICONSTOP "NovaAgent requiere Windows 64 bits."
        Abort
    ${EndIf}
    ${IfNot} ${AtLeastWin10}
        MessageBox MB_ICONSTOP "NovaAgent requiere Windows 10 o superior."
        Abort
    ${EndIf}
FunctionEnd
