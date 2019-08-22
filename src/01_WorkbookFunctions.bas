Attribute VB_Name = "WorkbookFunctions"
Option Explicit
'@register(('{3F4DACA7-160D-11D2-A8E9-00104B365C9F}', 5, 5)) # regex
    
Type StoreRangeInfo
    'TODO: Store workbook name, file name.
    Columns() As Variant
    Widths() As Variant
End Type
Public AutoFitUndoData As StoreRangeInfo

Type FlipSignRangeInfoType
    OriginalRange As Range
    Cells() As Variant
    Formulas() As Variant
End Type
Public FlipSignRangeInfo As FlipSignRangeInfoType

Private Sub PrepareAutoFitUndo(Rng As Range)
    ReDim AutoFitUndoData.Columns(1 To Rng.Columns.Count)
    ReDim AutoFitUndoData.Widths(1 To Rng.Columns.Count)
    Dim X As Long
    X = 1
    For X = 1 To Rng.Columns.Count
        AutoFitUndoData.Columns(X) = Rng.Columns(X).Column
        AutoFitUndoData.Widths(X) = Rng.Columns(X).ColumnWidth
    Next
End Sub

'@ribbon({'tab':'Terra', 'group':'Productivity', 'label':'Circularity Toggle', 'keytip':'C', 'image':'CircularReferences'})
Sub CircSwitch()
    On Error Resume Next
    [Circ] = 1 - [Circ]
    Application.StatusBar = "Circularity: " & IIf([Circ], "on", "off")
    Call DelayedResetStatusBar

End Sub

'@ribbon({'tab':'Terra', 'group':'Productivity', 'label':'Auto Fit Columns', 'keytip':'W', 'image':'ColumnWidth'})
Sub AutoFit()
    If TypeName(Selection) <> "Range" Then Exit Sub

    Dim SU As Boolean
    Dim Sht As Worksheet
    Set Sht = ActiveSheet

    With Application
        Call PrepareAutoFitUndo(Selection)
        SU = .ScreenUpdating
        .ScreenUpdating = False

        With Selection
            .EntireColumn.AutoFit
        End With

        If Selection.Columns.Count > 1 Then
                Dim X As Long, max As Long

                For X = 1 To Selection.Columns.Count
                    If Selection.Columns(X).ColumnWidth > max Then _
                        max = Selection.Columns(X).ColumnWidth
                Next

                Dim r As Range
                For X = 1 To Selection.Columns.Count
                    Set r = Selection.Columns(X)
                    r.ColumnWidth = max
                Next

                Application.ScreenUpdating = SU
        End If
    End With

    Application.OnUndo "Undo the AutoFit macro", "AutoFitUndo"

End Sub

Private Sub AutoFitUndo()
    Dim SU As Long, X As Long
    SU = Application.ScreenUpdating
    Application.ScreenUpdating = False

    Dim z As Variant

    With AutoFitUndoData
        For X = 1 To UBound(.Columns)
            z = ActiveSheet.Columns(.Columns(X)).Column
            ActiveSheet.Columns(.Columns(X)).ColumnWidth = .Widths(X)
        Next

    End With

    Application.ScreenUpdating = SU

End Sub

'@ribbon({'tab':'Terra', 'group':'Productivity', 'label':'Fill Toggle', 'keytip':'K', 'image':'AppointmentColorDialog'})
Sub CycleAccentBackground()
    Dim NextColor As Integer
    Dim FillRGB As Long
    Dim CurrentThemeColor As Variant

    With Selection.Interior
        CurrentThemeColor = .themeColor

        'If the selection has more than one fill color, .ThemeColor is vbNull
        If IsNull(CurrentThemeColor) Then CurrentThemeColor = -4142

        Select Case CurrentThemeColor
        Case xlThemeColorAccent6 'last color in the palette
            'Reset to no background, automatic foreground
            .Pattern = xlNone
            .TintAndShade = 0
            .PatternTintAndShade = 0

            Selection.Font.ColorIndex = xlAutomatic
            Selection.Font.TintAndShade = 0

        Case -4142 'No fill color
            .Pattern = xlSolid
            .PatternColorIndex = xlAutomatic
            .themeColor = xlThemeColorLight2 'Gold
            Selection.Font.themeColor = xlThemeColorDark1

        Case xlThemeColorLight2
            .Pattern = xlSolid
            .PatternColorIndex = xlAutomatic
            .themeColor = xlThemeColorDark2
            Selection.Font.themeColor = xlThemeColorDark1

        Case Else
            NextColor = CurrentThemeColor + 1
            If CurrentThemeColor = xlThemeColorDark2 Then NextColor = xlThemeColorAccent1
            .Pattern = xlSolid
            .PatternColorIndex = xlAutomatic
            .themeColor = NextColor
            Selection.Font.themeColor = xlThemeColorDark1
        End Select

    FillRGB = .Color 'ActiveWorkbook.Theme.ThemeColorScheme.Colors (NextColor)
    If (FillRGB Mod 256) + (FillRGB \ 256 Mod 256) + (FillRGB \ 256 ^ 2 Mod 256) = 469 Then 'Evercore Blue 2 Exception
        Selection.Font.themeColor = xlThemeColorDark1 'xlThemeColorDark1
    ElseIf (FillRGB Mod 256) + (FillRGB \ 256 Mod 256) + (FillRGB \ 256 ^ 2 Mod 256) >= 383 Then
        Selection.Font.themeColor = xlThemeColorLight1 'xlThemeColorDark1
    Else
    End If

    End With

End Sub

'@ribbon({'tab':'Terra', 'group':'Productivity', 'label':'Select Current Page', 'keytip':'A', 'image':'ZoomFitToWindow'})
Sub SelectCurrentPage()
    Dim Pages As Areas
    Dim Page As Variant

    On Error GoTo ExitSub
    Set Pages = ActiveSheet.Names("Print_Area").RefersToRange.Areas

    On Error Resume Next
    For Each Page In Pages
        If TypeName(Selection) = "Range" Then
            If Not (Application.Intersect(Selection, Page) Is Nothing) Then
                Page.Select
                GoTo ExitSub
            End If
        End If
    Next

ExitSub:
End Sub

'@ribbon({'tab':'Terra', 'group':'Cleanup', 'label':'Remove Unused Number Formats', 'keytip':'!F', 'image':'ClearFormatting'})
Sub RemoveUnusedNumberFormats()
  Dim strOldFormat As String
  Dim strNewFormat As String
  Dim aCell As Range
  Dim Sht As Worksheet
  Dim strFormats() As String
  Dim fFormatsUsed() As Boolean
  Dim i As Integer

  If ActiveWorkbook.Worksheets.Count = 0 Then
    MsgBox "The active workbook doesn't contain any worksheets.", vbInformation
    Exit Sub
  End If

  On Error GoTo Exit_Sub
  Application.CURSOR = xlWait
  ReDim strFormats(1000)
  ReDim fFormatsUsed(1000)
  Set aCell = Range("A1")
  aCell.Select
  strOldFormat = aCell.NumberFormatLocal
  aCell.NumberFormat = "General"
  strFormats(0) = "General"
  strNewFormat = aCell.NumberFormatLocal
  i = 1
  Do
    ' Dialog requires local format
    SendKeys "{TAB 3}{DOWN}{ENTER}"
    Application.Dialogs(xlDialogFormatNumber).Show strNewFormat
    strFormats(i) = aCell.NumberFormat
    strNewFormat = aCell.NumberFormatLocal
    i = i + 1
  Loop Until strFormats(i - 1) = strFormats(i - 2)
  aCell.NumberFormatLocal = strOldFormat
  ReDim Preserve strFormats(i - 2)
  ReDim Preserve fFormatsUsed(i - 2)
  For Each Sht In ActiveWorkbook.Worksheets
    For Each aCell In Sht.UsedRange
      For i = 0 To UBound(strFormats)
        If aCell.NumberFormat = strFormats(i) Then
          fFormatsUsed(i) = True
          Exit For
        End If
      Next i
    Next aCell
  Next Sht
  ' Suppress errors for built-in formats
  On Error Resume Next
  For i = 0 To UBound(strFormats)
    If Not fFormatsUsed(i) Then
      ' DeleteNumberFormat requires international format
      ActiveWorkbook.DeleteNumberFormat strFormats(i)
    End If
  Next i

Exit_Sub:
  Set aCell = Nothing
  Set Sht = Nothing
  Erase strFormats
  Erase fFormatsUsed
  Application.CURSOR = xlDefault
End Sub

'@ribbon({'tab':'Terra', 'group':'Sheets', 'label':'Toggle Page Breaks', 'keytip':'SB', 'image':'PrintTitles'})
Sub TogglePageBreaks()
    With ActiveSheet
        ActiveSheet.DisplayPageBreaks = Not ActiveSheet.DisplayPageBreaks
    End With
End Sub

'@ribbon({'tab':'Terra', 'group':'Sheets', 'label':'Unhide Every Sheet', 'keytip':'SU', 'image':'ReviewCompareMenu'})
Sub UnhideEverySheet()
    Dim Sht As Worksheet
    For Each Sht In ActiveWorkbook.Sheets
        Sht.Visible = xlSheetVisible
    Next
End Sub

'@ribbon({'tab':'Terra', 'group':'Cleanup', 'label':'Delete Hidden Sheets', 'keytip':'!S', 'image':'SheetDelete'})
Sub DeleteHiddenSheets()
    If MsgBox("This will delete every hidden sheet without confirmation! Are you sure?", vbYesNo) = vbNo Then Exit Sub
    Dim Sht As Worksheet
    For Each Sht In ActiveWorkbook.Sheets
        If Sht.Visible <> xlSheetVisible Then Sht.Delete
    Next
End Sub

'@ribbon({'tab':'Terra', 'group':'Sheets', 'label':'Reset Zoom (Current)', 'keytip':'SZ', 'image':'FilePrintPreview', 'screentip':"Reset this sheet's zoom level to 85% and toggle view mode"})
Sub ResetPageZoom()
    On Error Resume Next
    Dim SU As Long
    SU = Application.ScreenUpdating
    Application.ScreenUpdating = False
    ActiveWindow.Zoom = 85
    ActiveWindow.View = IIf(ActiveWindow.View = xlPageBreakPreview, xlNormalView, xlPageBreakPreview)
    ActiveWindow.Zoom = 85
    ActiveSheet.DisplayPageBreaks = ActiveSheet.DisplayPageBreaks 'Refreshes view in some weird instances
    Application.ScreenUpdating = SU
End Sub

'@ribbon({'tab':'Terra', 'group':'Sheets', 'label':'Reset Zoom (All)', 'keytip':'SA', 'image':'First10RecordsPreview', 'screentip':"Reset every sheet's zoomlevel to 85%"})
Sub ResetEveryZoom()
    On Error Resume Next
    Dim SU As Long
    Dim Sht As Worksheet, Current As Worksheet
    SU = Application.ScreenUpdating
    Set Current = ActiveSheet
    Application.ScreenUpdating = False

    For Each Sht In ActiveWorkbook.Worksheets
        Sht.Activate
        ActiveWindow.Zoom = 85
        ActiveWindow.View = IIf(ActiveWindow.View = xlPageBreakPreview, xlNormalView, xlPageBreakPreview)
        ActiveWindow.Zoom = 85
        ActiveWindow.View = IIf(ActiveWindow.View = xlPageBreakPreview, xlNormalView, xlPageBreakPreview)
    Next
    Current.Activate
    Application.ScreenUpdating = SU
End Sub

'@ribbon({'tab':'Terra', 'group':'Edit Cells', 'label':'Fix Comments', 'keytip':'EM', 'image':'ReviewNewComment'})
Sub ResetComments()
    Dim pComment As Comment
    For Each pComment In Application.ActiveSheet.Comments
        pComment.Shape.Top = pComment.Parent.Top + 5
        pComment.Shape.Left = pComment.Parent.Offset(0, 1).Left + 5
        pComment.Shape.TextFrame.AutoSize = True
    Next
End Sub

'@ribbon({'tab':'Terra', 'group':'Cleanup', 'label':"Remove ' Prefix", 'keytip':'!P', 'image':'DataValidationClearValidationCircles'})
Sub RemovePrefix()
    Dim r As Range
    Dim TEMP As String
    For Each r In Selection
        If r.PrefixCharacter <> vbNullString Then
            TEMP = r.Text
            r.Clear
            r.Value = TEMP
        End If
    Next
End Sub

Private Sub PrepareFlipSignRangeInfo(ByRef Rng As Range)
    Set FlipSignRangeInfo.OriginalRange = Rng
    ReDim FlipSignRangeInfo.Formulas(1 To Rng.Count)
    Dim i As Long
    i = 1
    For i = 1 To Rng.Count
        FlipSignRangeInfo.Formulas(i) = Rng.Cells(i).Formula
    Next
End Sub

Private Sub FlipSignUndo()
    Dim i As Long, FlippedFormula As String, CurrentFormula As String
    For i = 1 To UBound(FlipSignRangeInfo.Formulas)
        CurrentFormula = FlipSignRangeInfo.OriginalRange.Cells(i).Formula
        FlippedFormula = FlipSignRangeInfo.Formulas(i)
        FlipSignRangeInfo.OriginalRange.Cells(i) = FlippedFormula
        FlipSignRangeInfo.Formulas(i) = CurrentFormula
    Next

    Application.OnUndo "Undo sign flipping", "FlipSign"
    Application.OnRepeat "Redo sign flipping", "FlipSign"
End Sub

'@ribbon({'tab':'Terra', 'group':'Edit Cells', 'label':'Flip Sign', 'keytip':'E-', 'image':'PivotPlusMinusButtonsShowHide'})
Sub FlipSign()
    Dim Rng As Range, Cell As Range
    Set Rng = Selection

    If FlipSignRangeInfo.OriginalRange Is Nothing Then
    Else
        If Rng.Address = FlipSignRangeInfo.OriginalRange.Address Then
            Call FlipSignUndo
            GoTo EndSub
        End If
    End If

    Call PrepareFlipSignRangeInfo(Rng)
    For Each Cell In Rng
        Cell.Formula = FlipCellFormula(Cell.Formula)
    Next

EndSub:
    Application.OnUndo "Undo sign flipping", "FlipSignUndo"
End Sub

Private Function FlipCellFormula(ByVal Formula As String)
    If Left(Formula, 1) = "-" Then
        FlipCellFormula = Mid(Formula, 2, Len(Formula) - 1)
    ElseIf Left(Formula, 1) <> "=" And Formula <> "" Then
        FlipCellFormula = "-" & Formula
    ElseIf Left(Formula, 2) = "=-" Then
        FlipCellFormula = "=" & Mid(Formula, 3, Len(Formula) - 2)
    ElseIf (InStr(Formula, "+") + InStr(Formula, "(")) > 0 Then
        FlipCellFormula = "=-(" & Mid(Formula, 2, Len(Formula) - 1) & ")"
    ElseIf Formula = "" Then
        FlipCellFormula = ""
    Else
        FlipCellFormula = "=-" & Mid(Formula, 2, Len(Formula) - 1)
    End If
    
    'Dim parentheses As RegExp
    'Set parentheses = CreateObject("VBScript.RegExp")
    'parentheses.Pattern = "=\((?>\((?<c>)|[^()]+|\)(?<-c>))*(?(c)(?!))\)"
    'Dim matches As MatchCollection, i As Long
    'Set matches = parentheses.Execute(FlipCellFormula)
    'If matches.Count > 0 Then
    '    Debug.Print Formula, FlipCellFormula
    'End If
End Function

'@ribbon({'tab':'Terra', 'group':'Edit Cells', 'label':'Toggle Underline', 'keytip':'EU', 'image':'UnderlineWords'})
Sub UnderlineToggle()
    Dim UnderlineState As XlUnderlineStyle
    UnderlineState = Selection.Cells(1, 1).Font.Underline

    On Error Resume Next

    With Selection.Font
    Select Case UnderlineState

    Case xlUnderlineStyleSingle
        .Underline = xlUnderlineStyleSingleAccounting

    Case xlUnderlineStyleSingleAccounting
        .Underline = xlUnderlineStyleNone

    Case xlUnderlineStyleNone
        .Underline = xlUnderlineStyleSingle

    End Select
    End With
End Sub

