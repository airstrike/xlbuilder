Attribute VB_Name = "Module1"
Option Explicit

'Callback for btnCircSwitch onAction
Sub callCircSwitch(control As IRibbonControl)
    Call CircSwitch
End Sub

'Callback for btnAutoFit onAction
Sub callAutoFit(control As IRibbonControl)
    Call AutoFit
End Sub

'Callback for btnCycleAccentBackground onAction
Sub callCycleAccentBackground(control As IRibbonControl)
    Call CycleAccentBackground
End Sub

'Callback for btnSelectCurrentPAge onAction
Sub callSelectCurrentPage(control As IRibbonControl)
    Call SelectCurrentPage
End Sub

'Callback for btnTogglePageBreaks onAction
Sub callTogglePageBreaks(control As IRibbonControl)
    Call TogglePageBreaks
End Sub

'Callback for btnUnhideEverySheet onAction
Sub callUnhideEverySheet(control As IRibbonControl)
    Call UnhideEverySheet
End Sub

'Callback for btnDropEveryStyle onAction
Sub callDropEveryStyle(control As IRibbonControl)
    Call DropEveryStyle
End Sub

'Callback for btnDropUnusedStyle onAction
Sub callDropUnusedStyles(control As IRibbonControl)
    Call DropUnusedStyles
End Sub

'Callback for btnRemoveUnusedFormats onAction
Sub callRemoveUnusedNumberFormats(control As IRibbonControl)
    Call RemoveUnusedNumberFormats
End Sub

'Callback for btnResetComments onAction
Sub callResetComments(control As IRibbonControl)
    Call ResetComments
End Sub

'Callback for btnResetZoom onAction
Sub callResetZoom(control As IRibbonControl)
    Call ResetZoom
End Sub

'Callback for btnLastPointLabel onAction
Sub callLastPointLabel(control As IRibbonControl)
    Call LastPointLabel
End Sub

'Callback for btnLabelsFromRange onAction
Sub callLabelsFromRange(control As IRibbonControl)
    Call LabelsFromRange
End Sub

'Callback for btnFindReplaceInChart onAction
Sub callFindReplaceInChart(control As IRibbonControl)
    Call FindReplaceinChart
End Sub

'Callback for customButton13 onAction
Sub callToggleAxis(control As IRibbonControl)
    Call HideAxis
End Sub

'Callback for btnAxis1 onAction
Sub callAxisPV(control As IRibbonControl)
    Call MsgBox("Not implemented yet.", vbInformation)
End Sub

'Callback for btnAxis2 onAction
Sub callAxisPH(control As IRibbonControl)
    Call MsgBox("Not implemented yet.", vbInformation)
End Sub

'Callback for btnAxis3 onAction
Sub callAxisSV(control As IRibbonControl)
    Call MsgBox("Not implemented yet.", vbInformation)
End Sub

'Callback for btnAxis4 onAction
Sub callAxisSH(control As IRibbonControl)
    Call MsgBox("Not implemented yet.", vbInformation)
End Sub

'Callback for btnApplyDefaults onAction
Sub callApplyChartDefaults(control As IRibbonControl)
    Call MsgBox("Not implemented yet.", vbInformation)
End Sub


