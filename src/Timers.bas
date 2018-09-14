Attribute VB_Name = "Timers"
Option Explicit

Function GenerateSignature() As Long
    GenerateSignature = Rnd() * 1000000000
End Function


'Callback As String, Optional ByVal t As Variant = "00:00:03"
Sub SetTimer(ByVal Callback As String, ByVal Time As String, ParamArray Args() As Variant)
    Dim Signature As Long
    Signature = GenerateSignature() ' Generate timer signature
    Dim List As Scripting.Dictionary
    Set List = TimerList() ' load list of callbacks and signatures
    List(Callback) = Signature ' store signature in list
    'Debug.Print "Inserted: " & Callback, Signature
    
    ' Prepare arguments for Application.OnTime / CheckAndExecute
    Dim LB As Long, UB As Long
    If (UBound(Args) < LBound(Args)) Then 'Args() is empty
        LB = 1
        UB = 0
    Else
        LB = UBound(Args)
        UB = UBound(Args)
    End If

    ReDim ExtendArgs(0 To UB + 2) As String
    ExtendArgs(0) = Callback
    ExtendArgs(1) = Signature
    
    If UB > LB Then 'Non-empty Args()
        Dim X As Long
        For X = LB To UB
            ExtendArgs(X + 2) = Args(X)
        Next
    End If

    Application.OnTime Now + TimeValue(Time), "'CheckAndExecute " & ArgsAsString(ExtendArgs) & "'"

End Sub

Sub CheckAndExecute(ByVal Callback As String, ByVal Signature As Long, ParamArray Args() As Variant)
    Dim List As Scripting.Dictionary
    Set List = TimerList() ' load list of callbacks and signatures
    
    'Debug.Print "Looking for: " & Callback, Signature
    'Dim v As Variant
    'For Each v In List
    '    Debug.Print "             " & v, List(v)
    'Next
    
    Dim ArgsString As String
    ArgsString = ArgsAsString(Args)
    If List(Callback) = Signature Then
        Application.Run "'" & Callback & " " & ArgsString & "'"
    End If
    Debug.Print
End Sub

Function ArgsAsString(ParamArray Arr() As Variant) As String
    Dim sa As String
    sa = ""
    If TypeName(Arr) = "Variant()" Then
        sa = Join(Arr(0), """, """)
        On Error Resume Next
        sa = """" & Left(sa, Len(sa) - 3) & ""
        On Error GoTo 0
    ElseIf TypeName(Arr) = "String()" Then
        sa = Join(Arr, """, """)
        sa = """" & Left(sa, Len(sa) - 3) & ""
    End If
    
    ArgsAsString = sa
End Function
