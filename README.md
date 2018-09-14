## Install

1. Copy Terra.xlam in this folder to a local folder in your computer (like 'My Documents')
2. Open Excel and press `Alt`, `T`, `I`
3. Click on 'Browse'
4. Find the add-in *in your local folder* and install it


## Usage
- Excel Workbook macros can be easily accessed by pressing / twice, followed by a hotkey
- Additional macros are available when a chart is selected


## Available hotkeys in this version

### Workbook Hotkeys

c   Toggle circularity on / off. Assumes there's a cell called "Circ" with a number
    1 or 0 in it. Fails silently otherwise

w   Autofits multiple columns to the minimum width needed for all of them to show their
    contents. Due to Excel's idiosyncrassies you might (rarely) need to run this command
    multiple times

k   Toggle cell fill through colors in current Theme, setting foreground font color to
    white / black depending on brightness of fill color

a   If the current selected range is within a delimited workbook page, select the entire
    page
  
b   Toggle page breaks on / off

u   Unhide every sheet in Workbook (including 'Very Hidden' sheets)

!e  Delete every style in the current workbook except for Normal, Currency, Comma and
    Percent
   
!u  Delete every unused style (slower)

!f  Delete unused number formats (slow -- please wait for it to finish)

m   Moves every comment in the active sheet to their original positioning and sets their
    width to autofit contents

y   Sets zoom to 80% and toggles between Page Break and Normal Views
