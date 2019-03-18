Attribute VB_Name = "LooprModule"
Option Explicit
' Module:      Loopr
' Written by:  Andy Terra (andy@andyterra.com)
' Version:     0.6 (2019-03-18 16:08)
    
Private Const LOOPR_NAME As String = "Loop"       'Defined named range prefix to search for in workbook.
Private Const MODULE_SPEED As String = "00:00:00" 'Increase HH:MM:ss to make module slower. Default (fastest) is "00:00:00"
Private Const VERBOSE As Boolean = False          'Change to True to see debug messages
Private Const UPDATE_SCREEN As Boolean = False    'Change to True to see cells changing during loop
Private Const CURSOR As String = "··•·· ···•· ····• ····· •···· ·•···" 'For Statusbar. Must be separated by space.

' ROASTING
' To assist in checking whether the current value of a brewed named range is the same as its default value,
' "roasting" will create ranges named ranges that return True or False for that comparison.
' For example, if the ROAST_PREFIX is "Base." and you create ranges named "Proto.Synergies" and "Synergies",
' then "Base.Synergies" will return True for when those two named ranges have the same value
Private Const ROAST_PREFIX As String = "Base."

' BREWING
' Every named range starting with this prefix will be "brewed" into the equivalent name sans prefix.
' For example, if the BREW_PREFIX is "Proto." and you create ranges named "Proto.Synergies" and "Synergies",
' then every time you call Brew() (for instance, when changing to a different scenario / case), the value of
' "Proto.Synergies" will be hardcoded into the value of "Synergies"
Private Const BREW_PREFIX As String = "Proto."

Public Type ModelInput
    Choices As Variant
    Count As Long
    Current As Variant
    InputCell As Range
End Type

Private LooprTotal As Long
Private LooprCounter As Long

Sub Sleep(ByVal TimeString As String)
    Call Application.Wait(Now + TimeValue(TimeString))
End Sub

Public Sub Roast()
    'TO-DO: Implement generating '<ROAST_PREFIX>.' defined named ranges comparing '<BREW_PREFIX>.<Name>'
    'to '<Name>'
End Sub

Public Sub Brew()
    Dim Nm As Name, Nm2 As Name
    Dim C As Long, SU As Long
    C = Application.Calculation
    SU = Application.ScreenUpdating
    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual
    On Error Resume Next
    [Circ] = 0
    On Error GoTo 0
    For Each Nm In ActiveWorkbook.Names
        If Left(Nm.Name, Len(BREW_PREFIX)) = BREW_PREFIX Then
TrySheetScope:
            On Error GoTo NoNameInSheet
            Set Nm2 = ActiveSheet.Names(Mid(Nm.Name, Len(BREW_PREFIX) + 1, 999))
TryWorkbookScope:
            On Error GoTo ErrHandler
            Set Nm2 = ActiveWorkbook.Names(Mid(Nm.Name, Len(BREW_PREFIX) + 1, 999))

            On Error GoTo 0
            If VERBOSE Then Debug.Print "Assign " & Nm.RefersToRange.Value & " to " & Nm2.Name
            If InStr(Nm.RefersTo, "#") > 0 Then GoTo NextName
            If Not IsError(Nm.RefersToRange.Value) Then
                Nm2.RefersToRange.Value = Nm.RefersToRange.Value
            Else
                'Nm2.RefersToRange.Value = 0 'Uncomment this line to set values to zero when their base value is #N/A
            End If
NextName:
        End If
    Next
    GoTo ExitSub
    
ErrHandler:
    On Error Resume Next
    If VERBOSE Then Debug.Print "Couldn't find " & Mid(Nm.Name, Len(BREW_PREFIX) + 1, 999)
    Resume NextName
    
NoNameInSheet:
    Resume TryWorkbookScope
    
ExitSub:
    On Error Resume Next
    [Circ] = 1
    On Error GoTo 0
    Application.Calculation = C
    Application.ScreenUpdating = SU
End Sub

Public Sub Loopr()
    Dim C As Long, SU As Long
    SU = Application.ScreenUpdating
    Application.ScreenUpdating = UPDATE_SCREEN
    On Error Resume Next
    Call LooprFor
    Application.ScreenUpdating = True
End Sub

Public Sub LooprFor(Optional ByVal LooprName As String = "!") '! is a safe "null" equivalent since named ranges can't use it
    Dim Nm As Name, Nm2 As Name, Inputs As Collection, CurrentSheet As Worksheet
    Set CurrentSheet = ActiveSheet
    For Each Nm In ActiveWorkbook.Names
        Set Nm2 = Nm
        If Left(Nm.Name, Len(LOOPR_NAME)) = LOOPR_NAME Then
            If LooprName <> "!" And Left(Nm.Name, Len(LOOPR_NAME & LooprName)) <> (LOOPR_NAME & LooprName) Then GoTo NextName
            On Error Resume Next
            Set Nm2 = ActiveSheet.Names(Nm.Name)
            If VERBOSE Then Debug.Print "Looping " & Nm.Name
            On Error GoTo 0
            Set Inputs = NameAsCollection(Nm2, Selection)
            Call Loopr_(Inputs)
NextName:
        End If
    Next
    CurrentSheet.Activate
End Sub

Private Sub Loopr_(ByRef Inputs As Collection)
    On Error Resume Next
    [Circ] = 0
    [Circ] = 1
    
    On Error GoTo 0
    Dim n As Long, C As Range, i As Long, j As Long, k As Long, Counter As Long, total As Long
    LooprCounter = 0
    LooprTotal = 1
    
    Dim ModelInputs() As ModelInput
    For n = 1 To Inputs.Count
        Set C = Inputs(n)
        Dim ThisInput As ModelInput
        ThisInput.Choices = ValidationValues(C.Validation)
        ThisInput.Count = UBound(ThisInput.Choices)
        LooprTotal = LooprTotal * ThisInput.Count
        ThisInput.Current = C.Value
        Set ThisInput.InputCell = C
        ReDim Preserve ModelInputs(1 To n)
        ModelInputs(n) = ThisInput
    Next

    
    Call RecursiveLoop(ModelInputs)
    
    On Error GoTo ExitSub
    For n = 1 To UBound(ModelInputs)
        ModelInputs(n).InputCell.Value = ModelInputs(n).Current
    Next
    GoTo ExitSub
    
NoInputsCell:
    Call MsgBox("" _
        + "No cell named Inputs. Create one before trying again.", _
        vbCritical)
    GoTo ExitSub
        
ExitSub:
    Application.OnTime Now() + TimeValue("00:00:03"), "LooprModule.ResetStatusBar"
    Exit Sub

End Sub
Private Sub RecursiveLoop(ByRef ModelInputs() As ModelInput)
    Dim n As Long, i As Long, CURSOR_LENGTH As Long
    CURSOR_LENGTH = UBound(Split(CURSOR)) + 1
    Dim ThisInput As ModelInput
    On Error GoTo ErrorNoInputsSelected
    ThisInput = ModelInputs(1)
        
    Dim RemainingModelInputs() As ModelInput, RemainingCount As Long
    RemainingCount = UBound(ModelInputs) - LBound(ModelInputs)
    If RemainingCount > 0 Then
        ReDim Preserve RemainingModelInputs(1 To RemainingCount) As ModelInput
        For i = 1 To RemainingCount
            RemainingModelInputs(i) = ModelInputs(i + 1)
        Next
    End If
    
    For i = LBound(ThisInput.Choices) To UBound(ThisInput.Choices)
        Sleep MODULE_SPEED
        ThisInput.InputCell.Value = ThisInput.Choices(i)
        If RemainingCount = 0 Then
            LooprCounter = LooprCounter + 1
            If VERBOSE Then Debug.Print Format(LooprCounter, "00") & "/" & Format(LooprTotal, "00") & " " & ThisInput.InputCell.Address & ": " & String(3 - RemainingCount, vbTab) & i & " -> " & ThisInput.Choices(i)
        Else
            If VERBOSE Then Debug.Print String(6, " ") & ThisInput.InputCell.Address & ": " & String(3 - RemainingCount, vbTab) & i & " -> " & ThisInput.Choices(i)
        End If
        Application.StatusBar = "Loopr: " & LooprCounter & "/" & LooprTotal & " " & IIf(LooprCounter = LooprTotal, "", Split(CURSOR)(LooprCounter Mod CURSOR_LENGTH))
        
        If RemainingCount > 0 Then Call RecursiveLoop(RemainingModelInputs)
    Next

ExitSub:
    Exit Sub

ErrorNoInputsSelected:
    Application.StatusBar = "Loopr ERROR: No inputs selected."
    Resume ExitSub
End Sub

Private Function NameAsCollection(ByRef Nm As Name, ByRef Selection_ As Range) As Collection
    Dim coll As Collection
    Set coll = New Collection
    
    Dim NameFormula() As String, CellAddress As Variant, NamedCell As Range, Cell As Range
    NameFormula = Split(Replace(Nm.RefersTo, "=", ""), ",")
    
    Dim Intersection As Range, SelectionSize As Long
    SelectionSize = Selection_.Cells.Count
    
    For Each CellAddress In NameFormula
        Set NamedCell = Evaluate(CellAddress)
        For Each Cell In NamedCell.Parent.Range(NamedCell.Address).Cells
            On Error Resume Next
            Set Intersection = Nothing
            Set Intersection = Intersect(Selection_, Cell) 'Will error out if in different sheets
            On Error GoTo 0
            If SelectionSize > 1 And Intersection Is Nothing Then
            Else
                coll.Add Cell
            End If
        Next
    Next
    
    Set NameAsCollection = coll
End Function

Public Function ValidationValues(ByRef v As Validation) As Variant
    Dim Results As Variant
    Dim CurrentSheet As Worksheet
    Set CurrentSheet = ActiveSheet
    v.Parent.Parent.Activate
    
    Select Case v.Type
    
    Case xlValidateList
        If Left(v.Formula1, 1) = "=" Then 'Validation is an actual formula
            If InStr(v.Formula1, ":") = 0 And InStr(v.Formula1, ",") = 0 Then
                ReDim Results(1 To 1) As Variant
                Results(1) = Evaluate(v.Formula1)
            Else
                Results = Evaluate(v.Formula1)
            End If
            Dim i As Long, tmp As Long
            Do While True
                i = i + 1
                Results = WorksheetFunction.Transpose(Results)
                On Error GoTo ExitLoop
                tmp = UBound(Results, i)
            Loop
        Else 'Validation is a list of numbers
            Results = Application.WorksheetFunction.Index(Split(v.Formula1, ","), 0)
        End If
    
    Case xlValidateWholeNumber
        Results = Evaluate("Transpose(Row(A" & v.Formula1 & ":A" & v.Formula2 & "))")
        
    Case xlValidateDecimal
        Call MsgBox("Not implemented", vbCritical)
        Results = False
        
    End Select
    
ExitLoop:
    CurrentSheet.Activate
    ValidationValues = Results
End Function

Private Sub ResetStatusBar()
    Application.StatusBar = False
End Sub

Public Sub NextCase()
    Dim SU As Long
    SU = Application.ScreenUpdating
    Application.ScreenUpdating = UPDATE_SCREEN
    On Error Resume Next
    Dim CurrentCase As Long, xCase As Long, Cases As Variant
    CurrentCase = [Case]
    Cases = ValidationValues([Case].Validation)
    For xCase = LBound(Cases) To UBound(Cases)
        If Cases(xCase) = CurrentCase Then [Case] = Cases(xCase Mod UBound(Cases) + 1)
    Next
    Application.StatusBar = "Current Case: " & [Case] & " (" & [CaseName] & ") "
    Call SetTimer("NextCase_exit", "00:00:03")
    Application.ScreenUpdating = SU
End Sub

Private Sub NextCase_exit()
    Application.StatusBar = False
End Sub
