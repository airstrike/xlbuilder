Attribute VB_Name = "ChartHelper"
Option Explicit

'@ribbon({'tab': 'TerraChart', 'group': 'Productivity', 'label': 'Labels from Range', 'keytip': 'L', 'image': 'PivotShowDetails'})
Sub LabelsFromRange()
    'Sets value of currently selected data labels from a specified range
    Dim LabelRange As Range, Cell As Range, i As Long
    Dim Labels As DataLabels, Label As DataLabel

    On Error GoTo NoLabelSelected
    Set Labels = Selection 'Must select labels first

    On Error GoTo ExitSub 'Trap errors for cancelled inputs
    Set LabelRange = Application.InputBox(prompt:="Select range", Type:=8)

    On Error GoTo 0
    If Labels.Count = LabelRange.Count Then
        i = 0
        For Each Cell In LabelRange
            i = i + 1
            On Error Resume Next
            Labels(i).Text = Application.WorksheetFunction.Text(Cell.Value, Cell.NumberFormat)
            If i >= Labels.Count Then Exit Sub
        Next

        Exit Sub

    ElseIf Labels.Count > LabelRange.Count Then
        i = 0
        For Each Label In Labels
            If Label.ShowValue Or Label.ShowCategoryName Or Label.ShowPercentage Or Label.ShowSeriesName Then
                i = i + 1
                Label.Text = Application.WorksheetFunction.Text(LabelRange(i).Value, LabelRange(i).NumberFormat)
            End If
        Next

        Exit Sub

    End If

Exit Sub
NoLabelSelected:
    Call MsgBox("Please select data labels and try again.", vbCritical, "Error")

ExitSub:
End Sub

Sub LabelsAboveStack()
    'Moves labels above stacked columns
    Dim LabelRange As Range, Cell As Range, i As Long
    Dim Labels As DataLabels, L As DataLabel

    On Error GoTo NoLabelSelected
    Set Labels = Selection 'Must select labels first

    On Error GoTo 0
    i = 0
    For Each L In Labels
        L.Position = xlLabelPositionCenter
        L.Top = L.Parent.Top - L.Height - 2
    Next

    Exit Sub

NoLabelSelected:
    Call MsgBox("Please select data labels and try again.", vbCritical, "Error")

ExitSub:

End Sub

Sub FindReplaceinChart()
    Dim mySrs As Series
    Dim iPts As Long
    Dim iSrs As Long
    Dim aLAbel As DataLabel
    Dim sFormula As String
    If ActiveChart Is Nothing Then
        MsgBox "Select a chart and try again.", vbExclamation, "No Chart Selected"
    Else
        Dim old_ As String, new_ As String
        old_ = Application.InputBox("Replace:", "Find-Replace in Series")
        If Trim(old_ & vbNullString) = vbNullString Or Trim(old_ & vbNullString) = False Then GoTo ExitSub
        new_ = Application.InputBox("Replace """ & old_ & """ with:", "Find-Replace in Series")
        If Trim(new_ & vbNullString) = vbNullString Or Trim(new_ & vbNullString) = False Then GoTo ExitSub
        For Each mySrs In ActiveChart.SeriesCollection
            sFormula = WorksheetFunction.Substitute(mySrs.Formula, old_, new_)
            mySrs.Formula = sFormula
        Next
    End If

ExitSub:
End Sub

Sub LastPointLabel()
    Dim mySrs As Series
    Dim iPts As Long
    Dim themeColor As MsoThemeColorIndex
    Dim bLabeled As Boolean
    Dim iSrs As Long
    Dim finalDataLabel As DataLabel, finalPoint As Point
    If ActiveChart Is Nothing Then
        MsgBox "Select a chart and try again.", vbExclamation, "No Chart Selected"
    Else
        Dim subtract100 As VbMsgBoxResult
        subtract100 = MsgBox("Subtract 100% from each label?", vbYesNo, "Last Point Label")
        For Each mySrs In ActiveChart.SeriesCollection
            iSrs = iSrs + 1
        bLabeled = False
            With mySrs
                For iPts = .Points.Count To 1 Step -1
                    On Error Resume Next 'point isn't plotted
                    If bLabeled Then
                        ' remove existing label if it's not the last point
                        mySrs.Points(iPts).HasDataLabel = False
                        On Error GoTo 0
                    Else

                        On Error Resume Next 'point isn't plotted
                        mySrs.Points(iPts).ApplyDataLabels

                        'add series name
                        'mySrs.Points(iPts).ApplyDataLabels _
                        'ShowSeriesName:=True, _
                        'ShowCategoryName:=False, ShowValue:=False, _
                        'AutoText:=True, LegendKey:=False

                        ' bolds the font
                        Select Case iSrs

                        Case 1 To 5
                            themeColor = msoThemeColorAccent1
                        Case 6 To 13
                            themeColor = msoThemeColorAccent2
                        Case 14 To 20
                            themeColor = msoThemeColorAccent3
                        Case 21 To 22
                            themeColor = msoThemeColorAccent4
                        Case Else
                            themeColor = msoThemeColorAccent6

                        'mySrs.Point(iPts).Interior.ThemeColor =
                        'mySrs.Format.Fill.ForeColor.SchemeColor = ActiveWorkbook.Theme.ThemeColorScheme.Colors(msoThemeAccent1)

                        End Select
                        mySrs.Format.Fill.ForeColor.ObjectThemeColor = themeColor

                        If mySrs.ChartType = 15 Then
                            mySrs.DataLabels.Font.Color = mySrs.Fill.ForeColor
                                mySrs.Points(iPts).ApplyDataLabels _
                                ShowSeriesName:=True, _
                                ShowCategoryName:=False, ShowValue:=False, _
                                AutoText:=True, LegendKey:=False
                        Else
                            'makes the font color be the same color as the line
                            mySrs.DataLabels.Font.Color = mySrs.Border.Color
                        End If
                        mySrs.DataLabels.Font.Bold = True
                        bLabeled = (Err.Number = 0)
                        If bLabeled Then
                            If subtract100 = vbYes Then
                                Set finalDataLabel = mySrs.DataLabels(iPts)
                                finalDataLabel.Text = Application.WorksheetFunction.Text(Val(mySrs.Values(iPts) - 1), finalDataLabel.NumberFormat)
                            End If
                        End If
                    End If
                    On Error GoTo 0
                Next
            End With
        Next
    End If
End Sub

Sub FirstAndLastPointLabel()
    Dim mySrs As Series
    Dim iPts As Long
    Dim themeColor As MsoThemeColorIndex
    Dim bLabeled As Boolean
    Dim iSrs As Long
    Dim finalDataLabel As DataLabel, finalPoint As Point
    If ActiveChart Is Nothing Then
        MsgBox "Select a chart and try again.", vbExclamation, "No Chart Selected"
    Else
        Dim subtract100 As VbMsgBoxResult
        subtract100 = MsgBox("Subtract 100% from each label?", vbYesNo, "Last Point Label")
        For Each mySrs In ActiveChart.SeriesCollection
            iSrs = iSrs + 1
            bLabeled = False
            With mySrs
                For iPts = .Points.Count To 1 Step -1
                    If iPts = 1 Then bLabeled = False
                    On Error Resume Next 'point isn't plotted
                    If bLabeled Then
                        ' remove existing label if it's not the last point
                        mySrs.Points(iPts).HasDataLabel = False
                        On Error GoTo 0
                    Else

                        On Error Resume Next 'point isn't plotted
                        mySrs.Points(iPts).ApplyDataLabels

                        'add series name
                        'mySrs.Points(iPts).ApplyDataLabels _
                        'ShowSeriesName:=True, _
                        'ShowCategoryName:=False, ShowValue:=False, _
                        'AutoText:=True, LegendKey:=False

                        ' bolds the font
                        Select Case iSrs

                        Case 1 To 5
                            themeColor = msoThemeColorAccent1
                        Case 6 To 13
                            themeColor = msoThemeColorAccent2
                        Case 14 To 20
                            themeColor = msoThemeColorAccent3
                        Case 21 To 22
                            themeColor = msoThemeColorAccent4
                        Case Else
                            themeColor = msoThemeColorAccent6

                        'mySrs.Point(iPts).Interior.ThemeColor =
                        'mySrs.Format.Fill.ForeColor.SchemeColor = ActiveWorkbook.Theme.ThemeColorScheme.Colors(msoThemeAccent1)

                        End Select
                        mySrs.Format.Fill.ForeColor.ObjectThemeColor = themeColor

                        If mySrs.ChartType = 15 Then
                            mySrs.DataLabels.Font.Color = mySrs.Fill.ForeColor
                                mySrs.Points(iPts).ApplyDataLabels _
                                ShowSeriesName:=True, _
                                ShowCategoryName:=False, ShowValue:=False, _
                                AutoText:=True, LegendKey:=False
                        Else
                            'makes the font color be the same color as the line
                            mySrs.DataLabels.Font.Color = mySrs.Border.Color
                        End If
                        mySrs.DataLabels.Font.Bold = True
                        bLabeled = (Err.Number = 0)
                        If bLabeled Then
                            If subtract100 = vbYes Then
                                Set finalDataLabel = mySrs.DataLabels(iPts)
                                finalDataLabel.Text = Application.WorksheetFunction.Text(Val(mySrs.Values(iPts) - 1), finalDataLabel.NumberFormat)
                            End If
                        End If
                    End If
                    On Error GoTo 0
                Next
            End With
        Next
    End If
End Sub

'@ribbon({'tab': 'TerraChart', 'group': 'Chart Tools', 'label': 'Hide Axis', 'keytip': 'X', 'image': 'Delete'})
Sub HideAxis()
    Dim ActiveAxis As Axis
    If ActiveChart Is Nothing Then
        MsgBox "Select a chart axis and try again.", vbExclamation, "No Chart Selected"
    Else
    On Error GoTo ErrHandler
        Set ActiveAxis = Selection
        With ActiveAxis
            .Format.Line.Visible = msoFalse
            .TickLabelPosition = xlNone
        End With
    End If

    Exit Sub

ErrHandler:
    If Err.Number = 13 Then
        MsgBox "You need to select the chart axis. Try again.", vbCritical, "No Axis Selected"
        Exit Sub
    Else
        Resume Next
    End If
End Sub

Sub DeleteObjectsFromChart()
    Dim Obj As Object
    Dim Cht As Chart
    If ActiveChart Is Nothing Then
        MsgBox "Select a chart axis and try again.", vbExclamation, "No Chart Selected"
    Else
        Set Cht = ActiveChart
        On Error GoTo ErrHandler
        For Each Obj In ActiveChart.Shapes
            Obj.Delete
        Next
    End If

ErrHandler:
    If Err.Number = 13 Then
        MsgBox "You need to select the chart axis. Try again.", vbCritical, "No Axis Selected"
        Exit Sub
    Else
        Resume Next
    End If
End Sub

