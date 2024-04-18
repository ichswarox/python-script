#SingleInstance, Force
#Persistent

;admin
; If the script is not elevated, relaunch as administrator and kill current instance:

full_command_line := DllCall("GetCommandLine", "str")

if not (A_IsAdmin or RegExMatch(full_command_line, " /restart(?!\S)"))
{
    try ; leads to having the script re-launching itself as administrator
    {
        if A_IsCompiled
            Run *RunAs "%A_ScriptFullPath%" /restart
        else
            Run *RunAs "%A_AhkPath%" /restart "%A_ScriptFullPath%"
    }
    ExitApp
}

;https://www.autohotkey.com/boards/viewtopic.php?style=19&t=98016


<^BackSpace::
send,^c
sleep 500
Run, %ComSpec% /k C:/Python311/python.exe c:/ahkahk/aeae-script/clipboard.py,,Hide
;Process, Close, cmd.exe
;Process, Close, ApplicationFrameHost.exe
sleep 1000
Run, C:\downloads\#\ae-capture
return
