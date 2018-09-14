Attribute VB_Name = "Formatting"
' Borrowed largely from http://www.jkp-ads.com/Articles/styles06.asp
Public Sub DropUnusedStyles()
    Dim styleObj As Style
    Dim rngCell As Range
    Dim wb As Workbook
    Dim wsh As Worksheet
    Dim str As String
    Dim iStyleCount As Long, BeforeCount As Long, DeletedCount As Long
    Dim dict As New Scripting.Dictionary    ' <- from Tools / References... / "Microsoft Scripting Runtime"
                                            ' Alternatively, implement http://www.vbaexpress.com/kb/getarticle.php?kb_id=267
                                            ' using {420B2830-E718-11CF-893D-00A0C9054228} as the guid
 
    ' wb := workbook of interest.  Choose one of the following
    ' Set wb = ThisWorkbook ' choose this module's workbook
    Set wb = ActiveWorkbook ' the active workbook in excel
 
    BeforeCount = wb.Styles.Count
    Application.StatusBar = "[Dropping WB styles] Before: " & BeforeCount
 
    ' dict := list of styles
    For Each styleObj In wb.Styles
        str = styleObj.NameLocal
        iStyleCount = iStyleCount + 1
        If (str <> "Normal") And (str <> "Currency") And (str <> "Comma") And (str <> "Percent") Then
            Call dict.Add(str, 0)    ' First time:  adds keys
        End If
    Next styleObj
 
    ' Traverse each visible worksheet and increment count each style occurrence
    For Each wsh In wb.Worksheets
        If wsh.Visible Then
            For Each rngCell In wsh.UsedRange.Cells
                str = rngCell.Style
                dict.Item(str) = dict.Item(str) + 1     ' This time:  counts occurrences
            Next rngCell
        End If
    Next wsh
    ' Status, dictionary styles (key) has cell occurrence count (item)
 
 
    ' Try to delete unused styles
    Dim aKey As Variant
    On Error Resume Next    ' wb.Styles(aKey).Delete may throw error
 
    For Each aKey In dict.Keys
         If dict.Item(aKey) = 0 Then
            ' Occurrence count (Item) indicates this style is not used
            Call wb.Styles(aKey).Delete
            If Err.Number <> 0 Then
                Debug.Print vbTab & "^-- failed to delete"
                Err.Clear
            Else
                DeletedCount = DeletedCount + 1
                Application.StatusBar = "[Dropping WB styles] Before: " & BeforeCount & " / Deleted: " & DeletedCount
                Application.DoEvents
            End If
            Call dict.Remove(aKey)
        End If
 
    Next aKey
 
    Application.StatusBar = "[Dropping WB styles] Before: " & BeforeCount & " / Deleted: " & DeletedCount & " / Remaining: " & wb.Styles.Count & ". FINISHED!"
    Call DelayedResetStatusBar("00:00:03")
 
End Sub

Public Sub DropEveryStyle()
    With ActiveWorkbook
        Dim styleObj As Style
        Dim BeforeCount As Long, DeletedCount As Long
        Dim Calc As Long
        
        Calc = Application.Calculation
        BeforeCount = .Styles.Count
        Application.StatusBar = "[Dropping WB styles] Before: " & BeforeCount
        
        Calc = Application.Calculation
     
        On Error GoTo SkipStyle
        For Each styleObj In .Styles
            Select Case styleObj.NameLocal
            
            Case "Normal", "Currency", "Comma", "Percent"
                GoTo NoSkip
            
            Case Else
                Call styleObj.Delete
                DeletedCount = DeletedCount + 1
                Application.StatusBar = "[Dropping WB styles] Before: " & BeforeCount & " / Deleted: " & DeletedCount
                If DeletedCount Mod 1000 = 0 Then DoEvents
                GoTo NoSkip
            End Select
SkipStyle:
Resume Next

NoSkip:
        Next styleObj
        On Error GoTo 0
        Application.StatusBar = "[Dropping WB styles] Before: " & BeforeCount & " / Deleted: " & DeletedCount & " / Remaining: " & .Styles.Count & ". FINISHED!"
    
    End With
    Application.Calculation = Calc
    Call DelayedResetStatusBar
    
End Sub

