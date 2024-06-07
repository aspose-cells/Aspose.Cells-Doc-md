---
title: 电子表编辑器-使用功能
type: docs
weight: 60
url: /zh/java/spreadsheet-editor-working-with-functions/
---

**目录**

- [公式栏](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
  - saveFormulaBarContents
- [插入函数](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **公式栏**
公式栏是位于工作表区域顶部的文本框。它显示当前单元格的公式，并允许用户对其进行编辑。

**它是如何工作的？**

当选择单元格时，公式栏会与单元格同步，显示公式。允许用户进行编辑。当用户编辑并按回车键时，将执行JavaScript函数**saveFormulaBarContents**
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

1. 点击一个单元格进行选择。
1. 点击顶部的**插入函数**按钮。
1. 按照**插入函数**对话框上的说明进行操作。
