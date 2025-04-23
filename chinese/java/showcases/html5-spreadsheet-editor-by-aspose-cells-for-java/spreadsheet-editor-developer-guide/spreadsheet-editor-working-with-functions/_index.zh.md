---
title: 电子表格编辑器  使用函数
type: docs
weight: 60
url: /zh/java/spreadsheet-editor-working-with-functions/
---

**目录**

- [公式栏](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
  - saveFormulaBarContents
- [插入函数](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **公式栏**
公式栏是工作表区域顶部的文本框。它显示当前单元格的公式，并允许用户编辑它。

**它是如何工作的？**

当选定单元格时，公式栏会与单元格同步，并显示公式。用户可以进行编辑。用户进行编辑并按下回车键时，将执行JavaScript函数 **saveFormulaBarContents**。
#### **saveFormulaBarContents**
{{< highlight java >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **插入函数**
要插入函数或公式：

1. 单击单元格以选择它。
1. 在顶部单击**插入函数**按钮。
1. 按照**插入函数**对话框中的说明操作。
{{< app/cells/assistant language="java" >}}
