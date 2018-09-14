Attribute VB_Name = "Main"
Option Explicit

Sub ResetStatusBar()
    Application.StatusBar = False
End Sub

Sub DelayedResetStatusBar(Optional ByVal t As String = "00:00:03")
    Call SetTimer("ResetStatusBar", t)
End Sub

Sub HideCurrentMarker()
    'On Error GoTo ExitSub
    Dim P As Point
    Set P = Selection
    P.MarkerStyle = xlMarkerStyleNone
    
ExitSub:
End Sub

