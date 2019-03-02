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

WScript.Echo "Initiating build " & VERSION & " (" & TIMESTAMP & ")"

Dim FSO, CurrentDirectory, FilePath, SourceFolder, BinFolder, SourceFile, XLSMFilePath, XLAMFilePath
Set FSO = CreateObject("Scripting.FileSystemObject")
CurrentDirectory = FSO.GetAbsolutePathName(".")
Set SourceFolder = FSO.GetFolder(FSO.BuildPath(CurrentDirectory, "src"))
Set BinFolder = FSO.GetFolder(FSO.BuildPath(CurrentDirectory, "bin"))
XLSMFilePath = FSO.BuildPath(BinFolder, BUILD_NAME & ".xlsm")
XLAMFilePath = FSO.BuildPath(BinFolder, BUILD_NAME & ".xlam")

Dim XL, WB
Set XL = CreateObject("Excel.Application")
XL.Application.DisplayAlerts = False
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
