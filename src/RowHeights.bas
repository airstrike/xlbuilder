Attribute VB_Name = "RowHeights"
Option Explicit

Private SourceSelection As Range
Private Heights() As Long

Sub PasteRowHeights()
    Dim i As Long
    Dim numrows As Long
    On Error GoTo ExitSub
    numrows = Selection.Rows.Count
    
    For i = 1 To Selection.Rows.Count
        
    Next
    
ExitSub:
    
End Sub
