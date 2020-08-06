---
title: Spreadsheet Editor - Working with Functions
type: docs
weight: 60
url: /java/spreadsheet-editor-working-with-functions/
---

**Table of Contents**

- [Formula Bar](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
  - saveFormulaBarContents
- [Insert a Function](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **Formula Bar**
The formula bar is a text box on top of the sheet area. It displays the formula of current cell as well as allows the user to edit it.

**How it works?**

When a cell is selected the formula bar is synchronized with the cell and the formula is displayed. The user is allowed to edit. When the user edit and press enter key, the JavaScript function **saveFormulaBarContents** is executed
#### **saveFormulaBarContents**
{{< highlight java >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **Insert a Function**
To insert a function or formula:

1. Click a cell to select it.
1. Click **Insert Function** button on top.
1. Follow the instructions on the **Insert Function** dialog.
