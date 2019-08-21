Attribute VB_Name = "BAMSEC"
Option Explicit
'@register(('{3F4DACA7-160D-11D2-A8E9-00104B365C9F}', 5, 5)) # regex
'@register(('{420B2830-E718-11CF-893D-00A0C9054228}', 1, 0)) # scripting dictionary
'ShellExecute originally from
'https://wellsr.com/vba/2016/excel/use-vba-shellexecute-to-open-url-in-default-browser/
Private Declare PtrSafe Function ShellExecute _
                            Lib "shell32.dll" _
                            Alias "ShellExecuteA" ( _
                            ByVal hWnd As Long, _
                            ByVal lpOperation As String, _
                            ByVal lpFile As String, _
                            ByVal lpParameters As String, _
                            ByVal lpDirectory As String, _
                            ByVal nShowCmd As Long) _
                            As Long

'LaunchWebsite originally from
'https://wellsr.com/vba/2016/excel/use-vba-shellexecute-to-open-url-in-default-browser/
Private Sub LaunchWebsite(strUrl As String)
    On Error GoTo wellsrLaunchError
        Dim r As Long
        r = ShellExecute(0, "open", strUrl, 0, 0, 1)
        If True Or r = 5 Then 'if access denied, try this alternative
                r = ShellExecute(0, "open", "rundll32.exe", "url.dll,FileProtocolHandler " & strUrl, 0, 1)
        End If
        Exit Sub
wellsrLaunchError:
    MsgBox "Error encountered while trying to launch URL." & vbNewLine & vbNewLine & "Error: " & Err.Number & ", " & Err.Description, vbCritical, "Error Encountered"
End Sub

'Written by Andy Terra on 8/22/2018
'@ribbon({'tab':'Terra', 'group':'Productivity', 'label':'Open link from comment', 'keytip':'B', 'image':'FileLinksToFiles'})
Sub OpenLinkFromComment()
    Dim Cell As Range
    Dim cell_comment As String
    Dim launch_multiple As VbMsgBoxResult

    Set Cell = ActiveCell
    On Error GoTo ExitSub 'Cell may not have comment
    cell_comment = Cell.Comment.text
    On Error GoTo 0

    Dim re As RegExp
    Dim matches As MatchCollection, i As Long
    Set re = CreateObject("VBScript.RegExp")
    re.Pattern = "(?:[\r\n\t\f\v]*)(https?:\/\/\S+)(?:[\r\n\t\f\v]*)?"

    Set matches = re.Execute(cell_comment)
    launch_multiple = vbNo
    'Debug.Print TotalMatches(matches)
    If matches.Count > 0 Then
        If matches.Count > 1 Then
            launch_multiple = MsgBox("There are " & matches.Count & _
            " addresses in this cell comment. Open all of them?", vbYesNoCancel, "Open link from comment")
        End If
        If launch_multiple = vbCancel Then Exit Sub
        For i = 0 To matches.Count
            If i = 0 Or launch_multiple = vbYes Then
                Call LaunchWebsite(matches(i).Value)
                'Debug.Print matches(i).Value
            End If
            i = i + 1
        Next
        'Call LaunchWebsite(matches(0).Value)
    End If


ExitSub:
End Sub

Private Function TotalMatchesInRegex(matches As Object) As Long
    Dim total As Long, m As match, N As match, subm As submatches

    total = 0
    For Each m In matches
        If m.submatches.Count > 0 Then
            total = total + m.submatches.Count
        Else
            total = total + 1
        End If
    Next
    TotalMatchesInRegex = total

End Function

Private Function TotalMatches(matches As MatchCollection) As Long
    Dim match As match
    Dim total As Long, i As Long
    For Each match In matches
        For i = 0 To (match.submatches.Count - 1)
            total = total + 1
        Next
        total = total + 1
    Next
End Function

