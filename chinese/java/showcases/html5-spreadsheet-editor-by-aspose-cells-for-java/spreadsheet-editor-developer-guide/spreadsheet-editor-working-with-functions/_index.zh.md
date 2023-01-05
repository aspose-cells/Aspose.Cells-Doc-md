---
title: 电子表格编辑器 - 使用函数
type: docs
weight: 60
url: /zh/java/spreadsheet-editor-working-with-functions/
---
**目录**

- [公式栏](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
 保存公式栏内容
- [插入函数](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **公式栏**
公式栏是工作表区域顶部的文本框。它显示当前单元格的公式并允许用户对其进行编辑。

**怎么运行的？**

选择单元格后，编辑栏将与单元格同步并显示公式。允许用户编辑。当用户编辑并按下回车键时，JavaScript 函数**保存公式栏内容**被执行
#### **保存公式栏内容**
{{< highlight "java" >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **插入函数**
要插入函数或公式：

1. 单击一个单元格以将其选中。
1. 点击**插入函数**按钮在上面。
1. 按照说明进行操作**插入函数**对话。
