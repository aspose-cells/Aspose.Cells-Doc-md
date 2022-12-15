---
title: 电子表格编辑器 - 使用行和列
type: docs
weight: 30
url: /zh/java/spreadsheet-editor-working-with-rows-and-columns/
---
**目录**

- [添加一行](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaRow) 
 WorksheetView.addRowAbove
 - WorksheetView.addRowBelow
- [添加列](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaColumn) 
 WorksheetView.addColumnBefore
 - WorksheetView.addColumnAfter
- [删除一行](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaRow) 
 WorksheetView.deleteRow
- [删除列](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaColumn) 
 - WorksheetView.deleteColumn
- [列宽和行高](#SpreadsheetEditor-WorkingwithRowsandColumns-ColumnWidthandRowHeight) 
 工作表视图.setCurrentRowHeight
 - 工作表视图.setCurrentColumnWidth
- [插入一个 Cell](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
 - 工作表视图.addCellShiftRight
 - WorksheetView.addCellShiftDown
### **添加一行**
添加新行：

1. 单击要添加行的单元格。
1. 切换到**格式选项卡**.
1. 点击**在上面添加行**在所选单元格上方添加一行。
1. 点击**在下方添加行**在所选单元格下方添加一行。

编辑器将在所选位置添加一个新行。

![待办事项：图像_替代_文本](jjsornm.png)

**这个怎么运作？**

这**在上面添加行**和**在下方添加行**由 JSF 后端 bean 处理**工作表视图**.各个方法的源码如下：
#### **工作表视图.addRowAbove**
{{< highlight "java" >}}

     public void addRowAbove() {

        try {

            getAsposeWorksheet().getCells().insertRows(currentRowId, 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not add row", cx.getMessage());

            return;

        }

        purge();

        reloadRowHeight(currentRowId);

    }

{{< /highlight >}}

#### **工作表视图.addRowBelow**
{{< highlight "java" >}}

     public void addRowBelow() {

        if (getCurrentRowId() < 0) {

            msg.sendMessage("No cell selected", null);

            return;

        }

        int newRowId = currentRowId + 1;

        try {

            getAsposeWorksheet().getCells().insertRows(newRowId, 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not add row", cx.getMessage());

            return;

        }

        purge();

        reloadRowHeight(newRowId);

    }

{{< /highlight >}}
### **添加列**
要添加新列：

1. 单击要添加列的单元格。
1. 切换到**格式选项卡**.
1. 点击**在前面添加列**在所选单元格之前添加一列。
1. 点击**在之后添加列**在所选单元格后添加一列。

编辑器将在所选位置添加一个新列。

![待办事项：图像_替代_文本](jjsornm.png)

**这个怎么运作？**

这**在前面添加列**和**在之后添加列**由 JSF 后端 bean 处理**工作表视图**.各个方法的源码如下：
#### **工作表视图.addColumnBefore**
{{< highlight "java" >}}

     public void addColumnBefore() {

        try {

            getAsposeWorksheet().getCells().insertColumns(getCurrentColumnId(), 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not add column", cx.getMessage());

            return;

        }

        reloadColumnWidth(currentColumnId);

        purge();

    }

{{< /highlight >}}

#### **WorksheetView.addColumnAfter**
{{< highlight "java" >}}

     public void addColumnAfter() {

        int newColumnId = currentColumnId + 1;

        try {

            getAsposeWorksheet().getCells().insertColumns(newColumnId, 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not add column", cx.getMessage());

            return;

        }

        reloadColumnWidth(newColumnId);

        purge();

    }

{{< /highlight >}}
### **删除一行**
要删除一行：

1. 单击要删除的行中的单元格。
1. 切换到**格式选项卡**.
1. 点击**删除行**按钮。

编辑器将删除包含所选单元格的行。

![待办事项：图像_替代_文本](jjsornm.png)

**这个怎么运作？**

这**删除行**按钮由 JSF 后端 bean 处理**工作表视图**使用方法**工作表视图.deleteRow**:
#### **工作表视图.deleteRow**
{{< highlight "java" >}}

     public void deleteRow() {

        try {

            getAsposeWorksheet().getCells().deleteRows(currentRowId, 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not delete row", cx.getMessage());

            return;

        }

        cells.getRows(workbook.getCurrent()).remove(currentRowId);

        getRowHeight().remove(currentRowId);

        purge();

    }

{{< /highlight >}}
### **删除列**
要删除列：

1. 单击要删除的列中的单元格。
1. 切换到**格式选项卡**.
1. 点击**删除列**按钮。

编辑器将删除包含所选单元格的列。

![待办事项：图像_替代_文本](jjsornm.png)

**这个怎么运作？**

这**删除列**按钮由 JSF 后端 bean 处理**工作表视图**使用方法**工作表视图.deleteColumn**:
#### **工作表视图.deleteColumn**
{{< highlight "java" >}}

     public void deleteColumn() {

        try {

            getAsposeWorksheet().getCells().deleteColumns(currentColumnId, 1, true);

        } catch (com.aspose.cells.CellsException cx) {

            msg.sendMessage("Could not delete column", cx.getMessage());

            return;

        }

        cells.getColumns(workbook.getCurrent()).remove(currentColumnId);

        getRowHeight().remove(currentColumnId);

        purge();

    }

{{< /highlight >}}
### **列宽和行高**
要更改列的宽度：

1. 单击列内的任何单元格。
1. 切换到**格式选项卡**.
1. 点击**列宽**打开按钮**列宽**对话。
1. 在对话框中输入新值。
1. 点击**关**.

编辑器将更改列的宽度。

**如何改变行高？**

要更改行的高度：

1. 单击行内的任何单元格。
1. 切换到**格式选项卡**.
1. 点击**行高**打开按钮**行高**对话。
1. 在对话框中输入新值。
1. 点击**关**.

编辑器将更改行的高度。

**这个怎么运作？**

当用户提交宽度和高度的值时，这些值在服务器端由**设置当前行高**和**设置当前列宽**JSF后端bean的方法**工作表视图**.
#### **工作表视图.setCurrentRowHeight**
{{< highlight "java" >}}

     public void setCurrentRowHeight(int height) {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().setRowHeightPixel(currentRowId, height);

        reloadRowHeight(currentRowId);

        RequestContext.getCurrentInstance().update("sheet");

    }

{{< /highlight >}}

#### **工作表视图.setCurrentColumnWidth**
{{< highlight "java" >}}

     public void setCurrentColumnWidth(int width) {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().setColumnWidthPixel(currentColumnId, width);

        reloadColumnWidth(currentColumnId);

        RequestContext.getCurrentInstance().update("sheet");

    }

{{< /highlight >}}
### **插入一个 Cell**
添加新单元格：

1. 单击要新建的单元格。
1. 切换到**插入标签**.
1. 点击**Cell**按钮。
1. 选择**右移 Cells**或者**向下移动 Cells**按钮。

编辑器将在所选位置添加一个新单元格。相邻的单元格将自动水平或垂直移动以为新单元格留出空间。

**这个怎么运作？**

这**右移 Cells**和**向下移动 Cells**由 JSF 后端 bean 处理**工作表视图**.各个方法的源码如下：
#### **工作表视图.addCellShiftRight**
{{< highlight "java" >}}

     public void addCellShiftRight() {

        if (!isLoaded()) {

            return;

        }

        com.aspose.cells.CellArea a = new com.aspose.cells.CellArea();

        a.StartColumn = a.EndColumn = currentColumnId;

        a.StartRow = a.EndRow = currentRowId;

        getAsposeWorksheet().getCells().insertRange(a, com.aspose.cells.ShiftType.RIGHT);

        purge();

    }

{{< /highlight >}}

#### **工作表视图.addCellShiftDown**
{{< highlight "java" >}}

     public void addCellShiftDown() {

        if (!isLoaded()) {

            return;

        }

        com.aspose.cells.CellArea a = new com.aspose.cells.CellArea();

        a.StartColumn = a.EndColumn = currentColumnId;

        a.StartRow = a.EndRow = currentRowId;

        getAsposeWorksheet().getCells().insertRange(a, com.aspose.cells.ShiftType.DOWN);

        purge();

    }

{{< /highlight >}}
