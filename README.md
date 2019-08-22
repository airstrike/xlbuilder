## Installation

1. Close Excel
2. Copy Terra.xlam to %APPDATA%\Microsoft\Addins
3. Reopen Excel and browse the available functions in the ribbon.


## Usage
- Excel Workbook macros can be easily accessed by pressing `/` twice, followed by a hotkey

## Hotkeys available in this version

### Productivity

`c`  Toggle circularity on / off. Assumes there's a cell called "Circ" with a number
     1 or 0 in it. Fails silently otherwise

`w`  Autofits multiple columns to the minimum width needed for all of them to show their
     contents. Due to Excel's idiosyncrassies you might (rarely) need to run this command
     multiple times

`k`  Toggle cell fill through colors in current Theme, setting foreground font color to
     white / black depending on brightness of fill color

`a`  If the current selected range is within a delimited workbook page, select the entire
     page

`b`  Opens the first link from the active cell's comment

### Cleanup

`!f` Remove unused number formats (slow -- please wait for it to finish)

`!s` Delete every hidden sheet

`!e` Remove every style in the current workbook except for Normal, Currency, Comma, Percent
     and Hyperlink

`!u` Remove every unused style (slower, because it needs to check which styles are unused)

`!n` Remove every hidden named range

### Sheet Functions

`sb` Toggle page breaks

`su` Unhide every sheet (including 'Very Hidden' ones)

`sz` Reset zoom level in the current sheet to 85% and toggles between Page Break and Normal views

`sa` Reset zoom level in every sheet to 85%

`sp` Attempt to unprotect the current password-protected sheet through brute force

### Edit Cells

`em` Moves every comment in the active sheet to their original positioning and sets their
     width to autofit contents

`e-` Flips the sign of currently selected cells

`eu` Toggles underline (none, normal, accounting)
