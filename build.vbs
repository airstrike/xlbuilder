Option Explicit

Const BUILD_TAGS = "Name, Author, E-mail, Website, Version, Timestamp"

Const LONG_NAME = "Terra Add-in"
Const BUILD_NAME = "Terra"
Const VERSION = "0.2.0"
Const AUTHOR = "Andy Terra"
Const EMAIL = "andy@andyterra.com"
Const WEBSITE = "https://excel.andyterra.com"
Dim TIMESTAMP
TIMESTAMP = Now()

Dim Tags, TagValues
Tags = Split(BUILD_TAGS, ", ")
TagValues = Array(LONG_NAME, AUTHOR, EMAIL, WEBSITE, VERSION, TIMESTAMP)

Dim FSO, CurrentDirectory, FilePath, SourceFolder, BinFolder, SourceFile, XLSMFilePath, XLAMFilePath
Set FSO = CreateObject("Scripting.FileSystemObject")
CurrentDirectory = FSO.GetAbsolutePathName(".")

Dim XL, WB
Set XL = CreateObject("Excel.Application")
XL.Application.DisplayAlerts = False

Sub Main()
    Call Build()
End Sub

Sub Build()
    WScript.Echo "Initiating build " & VERSION & " (" & TIMESTAMP & ")"

    Set SourceFolder = FSO.GetFolder(FSO.BuildPath(CurrentDirectory, "src"))
    Set BinFolder = FSO.GetFolder(FSO.BuildPath(CurrentDirectory, "bin"))
    XLSMFilePath = FSO.BuildPath(BinFolder, BUILD_NAME & ".xlsm")
    XLAMFilePath = FSO.BuildPath(BinFolder, BUILD_NAME & ".xlam")

    Set WB = XL.Workbooks.Add()

    'Add metadata to file
    WScript.Echo "Generating metadata"
    Dim i
    For i = 0 to UBound(Tags) 'Assumes Tags and TagValues have the same length
        WB.Sheets(1).Cells(i + 1,1).Value = Tags(i)
        WB.Sheets(1).Cells(i + 1,2).Value = TagValues(i)
    Next

    'Load .bas modules onto new workbook
    Dim VBProj, VBComp, ComponentType, Extension
    Set VBProj = WB.VBProject
    For Each SourceFile in SourceFolder.Files
        Extension = LCase(FSO.GetExtensionName(SourceFile.Name))

        If Extension = "cls" or Extension = "frm" or Extension = "bas" Then _
            WB.VBProject.VBComponents.Import SourceFile.Path

    Next

    'Delete old build files
    On Error Resume Next
    FSO.DeleteFile(XLSMFilePath)
    FSO.DeleteFile(XLAMFilePath)
    On Error GoTo 0
    If Err.Number = vbEmpty Then
        Wscript.Echo "Removed old files"
    Else
        Wscript.Echo "Error Removing old files: " & Err.Number
    End If

    'Save new binaries
    WB.IsAddin = False
    WB.SaveAs XLSMFilePath, 52 'xlOpenXMLWorkbookMacroEnabled
    WB.IsAddin = True
    WB.SaveAs XLAMFilePath, 55 'xlOpenXMLAddin
    If Err.Number = vbEmpty Then
        WScript.Echo "Built new binaries"
    Else
        Wscript.Echo "Error Removing old files: " & Err.Number
    End If

    WB.Close
    Wscript.Echo "Build successful!"
    WScript.Quit

End Sub

' From https://www.mrexcel.com/forum/excel-questions/1048272-adding-custom-ribbon-workbook-using-vba.html
Private Function sGetEmptyTempFolder(sTempFolderName As String) As String
 '--returns path to empty folder in users temp folder
 Dim sPath As String
 Dim oFSO As Object

 Set oFSO = CreateObject("Scripting.FileSystemObject")

 sPath = Environ$("temp") & "\" & sTempFolderName

 If oFSO.FolderExists(sPath) Then
   '--delete any files and subfolders in existing temp folder
   On Error Resume Next
   oFSO.DeleteFile sPath & "\*.*", True
   oFSO.DeleteFolder sPath & "\*.*", True
   On Error GoTo 0
 Else
   oFSO.CreateFolder (sPath)
 End If

ExitProc:
 If oFSO.FolderExists(sPath) Then
   sGetEmptyTempFolder = sPath
 Else
   sGetEmptyTempFolder = vbNullString
   msErrMsg = "Temporary folder could not be created."
 End If
End Function

Private Sub MakeNewZip(sPath As String)
'--create empty Zip File
 Dim oFSO As Object
 Dim oFile As Object

 Set oFSO = CreateObject("Scripting.FileSystemObject")

 Set oFile = oFSO.CreateTextFile(sPath, True)
 oFile.WriteLine (Chr$(80) & Chr$(75) & Chr$(5) & Chr$(6) & String(18, 0))
 oFile.Close
End Sub

Private Sub Unzip(sSourceFilePath As String, sTargetFolderPath As String)
'--unzips file as source path and copys contents to target folder
'--assumes Source file and Target folder already validated

'--based on code by Ron de Bruin
'  https://www.rondebruin.nl/win/s7/win002.htm

 Dim XL As Object

 'Extract the files into the newly created folder
 Set XL = CreateObject("Shell.Application")

 XL.Namespace("" & sTargetFolderPath).CopyHere _
   XL.Namespace("" & sSourceFilePath).Items

End Sub

Private Sub UpdateRels(sTopFolderOfItems As String, _
    sCustomUI_Filename As String)

   '--handle no relationships node?

    Dim oXmlDoc As Object
    Dim oXmlNode As Object, oXmlNewNode As Object
    Dim oXmlNodes As Object
    Dim sRelsFilePath As String, sNS As String

    sRelsFilePath = sTopFolderOfItems & "\_rels\.rels"

    Set oXmlDoc = CreateObject("Microsoft.XMLDOM")
    oXmlDoc.Load sRelsFilePath

    With oXmlDoc.SelectSingleNode("/Relationships")
        sNS = .NamespaceURI

        '--remove any existing nodes that would conflict with new relationship
        Set oXmlNodes = oXmlDoc.SelectNodes( _
        "//Relationship[@Id='customUIRelID' or  @Target='" _
            & ATT_TARGET_2007 & "' or  @Target='" & ATT_TARGET_2010 & "']")

        For Each oXmlNode In oXmlNodes
            Debug.Print "Deleting.." & oXmlNode.Attributes.getNamedItem("Target").Text
            oXmlNode.ParentNode.RemoveChild oXmlNode
        Next oXmlNode

   '--add new node by cloning existing
   Set oXmlNewNode = .ChildNodes(0).CloneNode(True)
   oXmlNewNode.Attributes.getNamedItem("Id").Text = "customUIRelID"

   Select Case sCustomUI_Filename
      Case "customUI.xml" '2007
         oXmlNewNode.Attributes.getNamedItem("Type").Text = ATT_TYPE_2007
         oXmlNewNode.Attributes.getNamedItem("Target").Text = ATT_TARGET_2007

      Case "customUI14.xml" '2010
         oXmlNewNode.Attributes.getNamedItem("Type").Text = ATT_TYPE_2010
         oXmlNewNode.Attributes.getNamedItem("Target").Text = ATT_TARGET_2010

      Case Else
         msErrMsg = "XML filename for Custom Ribbon is unrecognized version."
         GoTo ExitProc
   End Select

   .appendChild oXmlNewNode

 End With
 oXmlDoc.Save sRelsFilePath

ExitProc:

End Sub

Private Sub WriteCustomUI_XML_ToFile(sRibbonXML As String, _
    sCustomUI_FolderPath As String, sCustomUI_Filename As String)
    '--creates a new xml file with specified folder and filename
    Dim oFSO As Object
    Dim oFile As Object
    Dim sCustomUI_Filepath As String

    Set oFSO = CreateObject("Scripting.FileSystemObject")

    sCustomUI_Filepath = sCustomUI_FolderPath & "" & sCustomUI_Filename

    If oFSO.FolderExists(sCustomUI_FolderPath) = False Then
      oFSO.CreateFolder (sCustomUI_FolderPath)
    End If

    Set oFile = oFSO.CreateTextFile(sCustomUI_Filepath, True)
    oFile.WriteLine (sRibbonXML)
    oFile.Close

End Sub

Private Sub Zip(sSourceFolderPath As String, sTargetFilePath As String)
   '--zips all files in source folder and its subfolders. Copies the zip to target file
   '--based on code by Ron de Bruin
   '  https://www.rondebruin.nl/win/s7/win001.htm

    Dim XL
    Dim vFileNameZip

    vFolderName = sSourceFolderPath
    vFileNameZip = sTargetFilePath

    '--create empty zip file
    MakeNewZip (vFileNameZip)

    '--Copy the files to the compressed folder
    XL.Namespace(vFileNameZip).CopyHere XL.Namespace(vFolderName).Items

    '--keep script waiting until compressing is done
    On Error Resume Next
       Do Until XL.Namespace(vFileNameZip).Items.Count = _
      XL.Namespace(vFolderName).Items.Count
      Application.Wait (Now + TimeValue("0:00:01"))
    Loop
    On Error GoTo 0

End Sub



Call Main()
