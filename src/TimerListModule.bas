Attribute VB_Name = "TimerListModule"
Option Explicit

Private pTimerList As Scripting.Dictionary

Public Property Get TimerList() As Scripting.Dictionary

    If pTimerList Is Nothing Then
        Set pTimerList = New Scripting.Dictionary
    End If

    Set TimerList = pTimerList

End Property
