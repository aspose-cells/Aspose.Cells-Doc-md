---
title: 电子表编辑器-行和列操作
type: docs
weight: 30
url: /zh/java/spreadsheet-editor-working-with-rows-and-columns/
---

**目录**

- [添加行](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaRow) 
  - WorksheetView.addRowAbove
  - WorksheetView.addRowBelow
- [添加列](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaColumn) 
  - WorksheetView.addColumnBefore
  - WorksheetView.addColumnAfter
- [删除一行](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaRow) 
  - WorksheetView.deleteRow
- [删除列](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaColumn) 
  - WorksheetView.deleteColumn
- [列宽度和行高度](#SpreadsheetEditor-WorkingwithRowsandColumns-ColumnWidthandRowHeight) 
  - WorksheetView.setCurrentRowHeight
  - WorksheetView.setCurrentColumnWidth
- [插入单元格](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
  - WorksheetView.addCellShiftRight
  - WorksheetView.addCellShiftDown
### **添加行**
要添加新行:

1. 单击要添加行的单元格。
1. 切换到**格式**选项卡.
1. 单击 **在上方添加行** 以在所选单元格上方添加行。
1. 单击 **在下方添加行** 以在所选单元格下方添加行。

编辑器将在选择的位置添加新行。

![todo:image_alt_text](jjsornm.png)

**它是如何工作的？**

**在上方添加行** 和 **在下方添加行** 由JSF后端bean **WorksheetView** 处理。相应方法的源代码如下:
#### **WorksheetView.addRowAbove**
{{< highlight java >}}

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

#### **WorksheetView.addRowBelow**
{{< highlight java >}}

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
要添加新列:

1. 单击要添加列的单元格。
1. 切换到**格式**选项卡.
1. 单击 **在之前添加列** 以在所选单元格之前添加列。
1. 单击 **在之后添加列** 以在所选单元格之后添加列。

编辑器将在选择的位置添加新列。

![todo:image_alt_text](jjsornm.png)

**它是如何工作的？**

**Add Column Before**和**Add Column After**由JSF后端bean**WorksheetView**处理。相应方法的源代码如下所示：
#### **WorksheetView.addColumnBefore**
{{< highlight java >}}

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
{{< highlight java >}}

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

1. 单击要删除行的单元格。
1. 切换到**格式**选项卡.
1. 单击**删除行**按钮。

编辑器将删除包含选定单元格的行。

![todo:image_alt_text](jjsornm.png)

**它是如何工作的？**

**删除列**按钮由JSF后端bean **WorksheetView**使用方法**WorksheetView.deleteRow**处理：
#### **WorksheetView.deleteRow**
{{< highlight java >}}

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
1. 切换到**格式**选项卡.
1. 单击**删除列**按钮。

编辑器将删除包含选定单元格的列。

![todo:image_alt_text](jjsornm.png)

**它是如何工作的？**

**删除列**按钮由JSF后端bean **WorksheetView**使用方法 **WorksheetView.deleteColumn**处理：
#### **WorksheetView.deleteColumn**
{{< highlight java >}}

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
### **列宽度和行高度**
要更改列的宽度：

1. 单击列内的任何单元格。
1. 切换到**格式**选项卡.
1. 单击**列宽度**按钮以打开**列宽度**对话框。
1. 在对话框中输入新值.
1. 单击**关闭**。

编辑器将更改列的宽度。

**如何更改行高？**

更改行高度:

1. 单击行内的任意单元格.
1. 切换到**格式**选项卡.
1. 单击**行高**按钮以打开**行高**对话框.
1. 在对话框中输入新值.
1. 单击**关闭**。

编辑器将更改行的高度.

**它是如何工作的？**

当用户提交宽度和高度的值时, 这些值由JSF后端bean **WorksheetView**的**setCurrentRowHeight**和**setCurrentColumnWidth**方法处理.
#### **WorksheetView.setCurrentRowHeight**
{{< highlight java >}}

     public void setCurrentRowHeight(int height) {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().setRowHeightPixel(currentRowId, height);

        reloadRowHeight(currentRowId);

        RequestContext.getCurrentInstance().update("sheet");

    }

{{< /highlight >}}

#### **WorksheetView.setCurrentColumnWidth**
{{< highlight java >}}

     public void setCurrentColumnWidth(int width) {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().setColumnWidthPixel(currentColumnId, width);

        reloadColumnWidth(currentColumnId);

        RequestContext.getCurrentInstance().update("sheet");

    }

{{< /highlight >}}
### **插入单元格**
添加新单元格:

1. 单击您想要新单元格的地方的单元格.
1. 切换到**插入**选项卡.
1. 单击**单元格**按钮.
1. 选择**右移单元格**或**向下移动单元格**按钮.

编辑器将在所选位置添加新单元格。 相邻的单元格将自动转移，以横向或纵向创建空间.

**它是如何工作的？**

**右移单元格**和**向下移动单元格**由JSF后端bean **WorksheetView**处理。 相应方法的源代码如下:
#### **WorksheetView.addCellShiftRight**
{{< highlight java >}}

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

#### **WorksheetView.addCellShiftDown**
{{< highlight java >}}

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
