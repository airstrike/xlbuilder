Attribute VB_Name = "PasswordBreaker"
'@ribbon({'tab':'Terra', 'group':'Sheets', 'label':'Force Unprotect Sheet', 'keytip': 'SP', 'image':'MasterDocumentLockSubdocument'})
Private Sub UnprotectActiveSheet()
    Dim i As Integer, j As Integer, k As Integer
    Dim l As Integer, m As Integer, n As Integer
    Dim i1 As Integer, i2 As Integer, i3 As Integer
    Dim i4 As Integer, i5 As Integer, i6 As Integer

    Dim counter As Long
    Dim pw As String

    On Error Resume Next

    For i = 65 To 66: For j = 65 To 66: For k = 65 To 66:
    For l = 65 To 66: For m = 65 To 66: For i1 = 65 To 66:
    For i2 = 65 To 66: For i3 = 65 To 66: For i4 = 65 To 66:
    For i5 = 65 To 66: For i6 = 65 To 66: For n = 32 To 126:

    pw = Chr(i) & Chr(j) & Chr(k) & _
        Chr(l) & Chr(m) & Chr(i1) & Chr(i2) & Chr(i3) & Chr(i4) & Chr(i5) & Chr(i6) & Chr(n)
    ActiveSheet.Unprotect pw

    counter = counter + 1
    Application.StatusBar = "Attempt " & counter & " [" & pw & "]"
    If counter Mod 10 = 0 Then DoEvents

    If ActiveSheet.ProtectContents = False Then GoTo ExitSub

    Next: Next: Next: Next: Next: Next:
    Next: Next: Next: Next: Next: Next:

ExitSub:
    ActiveSheet.Range("b1").Value = pw

End Sub



