Attribute VB_Name = "ChartHelper"
Option Explicit

Sub LabelsFromRange()
Attribute LabelsFromRange.VB_ProcData.VB_Invoke_Func = "E\n14"
    'Sets value of currently selected data labels from a specified range
    Dim LabelRange As Range, cell As Range, i As Long
    Dim Labels As DataLabels
    
    On Error GoTo NoLabelSelected
    Set Labels = Selection 'Must select labels first
    
    On Error GoTo ExitSub 'Trap errors for cancelled inputs
    Set LabelRange = Application.InputBox(prompt:="Select range", Type:=8)
    
    On Error GoTo 0
    i = 0
    For Each cell In LabelRange
        i = i + 1
        On Error Resume Next
        Labels(i).Text = Application.WorksheetFunction.Text(cell.Value, cell.NumberFormat)
        If i >= Labels.Count Then Exit Sub
    Next
    
    Exit Sub
    
NoLabelSelected:
    Call MsgBox("Please select data labels and try again.", vbCritical, "Error")
    
ExitSub:
    
End Sub

Sub FindReplaceinChart()
Attribute FindReplaceinChart.VB_ProcData.VB_Invoke_Func = "F\n14"
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
Attribute LastPointLabel.VB_ProcData.VB_Invoke_Func = "L\n14"
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

Sub HideAxis()
Attribute HideAxis.VB_ProcData.VB_Invoke_Func = "X\n14"
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
    
ErrHandler:
    If Err.Number = 13 Then
        MsgBox "You need to select the chart axis. Try again.", vbCritical, "No Axis Selected"
        Exit Sub
    Else
        Resume Next
    End If
End Sub
