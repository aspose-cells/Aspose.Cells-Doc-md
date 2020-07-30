---
title : "Spreadsheet Editor - Working with Functions" 
description : "" 
weight : 16878 
toc : false
type: docs
url: /java/showcases/html5spreadsheet/developerguide/spreadsheet+editor+-+working+with+functions/
---

# Aspose.Cells for Java : Spreadsheet Editor - Working with Functions


**Table of Contents**


*   [Formula Bar](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar)
    *   saveFormulaBarContents
*   [Insert a Function](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)


### Formula Bar

The formula bar is a text box on top of the sheet area. It displays the formula of current cell as well as allows the user to edit it.

**How it works?**

When a cell is selected the formula bar is synchronized with the cell and the formula is displayed. The user is allowed to edit. When the user edit and press enter key, the JavaScript function **saveFormulaBarContents** is executed

#### saveFormulaBarContents

{{< code lang="cs" >}}
function saveFormulaBarContents() {
    var newContents = PF('formulaBar').jq.val();
    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);
    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;
}
{{< /code >}}

### Insert a Function

To insert a function or formula:

1.  Click a cell to select it.
2.  Click **Insert Function** button on top.
3.  Follow the instructions on the **Insert Function** dialog.

