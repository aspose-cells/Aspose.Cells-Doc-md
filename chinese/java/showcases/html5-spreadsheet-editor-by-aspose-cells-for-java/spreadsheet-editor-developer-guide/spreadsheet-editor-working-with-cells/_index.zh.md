---
title: 电子表格编辑器  与单元格一起工作
type: docs
weight: 40
url: /zh/java/spreadsheet-editor-working-with-cells/
---

**目录**

- [选择单元格](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
  - 单元格选择回调
- [删除单元格](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
  - WorksheetView.removeCellShiftUp
  - WorksheetView.removeCellShiftLeft
- [清除单元格](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
  - WorksheetView.clearCurrentCellFormatting
  - WorksheetView.clearCurrentCellContents
  - WorksheetView.clearCurrentCell
### **选择单元格**
使用鼠标指针指向单元格。单击单元格以选择它。所选择的单元格将以粗体矩形进行突显。

**它是如何工作的？**

当用户单击单元格时，事件将由附加到Primefaces组件的JavaScript回调函数处理。
#### **单元格选择回调**
{{< highlight java >}}

                     var columnId = $(this).find('.ui-cell-editor-input input').attr('data-columnid');

                    var rowId = $(this).find('.ui-cell-editor-input input').attr('data-rowid');

                    var clientId = $(this).find('.ui-cell-editor').attr('id');

                    PF('currentColumnIdValue').jq.val(columnId);

                    PF('currentRowIdValue').jq.val(rowId);

                    PF('currentCellClientIdValue').jq.val(clientId);

                    if ($(this).find('.ui-cell-editor-output div').hasClass('b')) {

                        PF('boldOptionButton').check();

                    } else {

                        PF('boldOptionButton').uncheck();

                    }

                    if ($(this).find('.ui-cell-editor-output div').hasClass('i')) {

                        PF('italicOptionButton').check();

                    } else {

                        PF('italicOptionButton').uncheck();

                    }

                    if ($(this).find('.ui-cell-editor-output div').hasClass('u')) {

                        PF('underlineOptionButton').check();

                    } else {

                        PF('underlineOptionButton').uncheck();

                    }

                    PF('fontOptionSelector').selectValue($(this).find('.ui-cell-editor-output div').css('font-family').slice(1, -1));

                    PF('fontSizeOptionSelector').selectValue($(this).find('.ui-cell-editor-output div')[0].style.fontSize.replace('pt', ''));

                    ['al', 'ac', 'ar', 'aj'].forEach(function(v) {

                        if ($(this).find('.ui-cell-editor-output div').hasClass(v)) {

                            // TODO: save the value to PF('alignOptionSelector');

                        }

                    });

                    PF('currentColumnWidthValue').jq.val($(this).width());

                    PF('currentRowHeightValue').jq.val($(this).height());

                    $($this.selectedCell).removeClass('sheet-selected-cell');

                    $(this).addClass('sheet-selected-cell');

                    $this.selectedCell = this;

{{< /highlight >}}
### **删除单元格**
要删除单元格：

1. 单击要删除的单元格。
1. 切换到 **格式** 选项卡。
1. 单击**删除单元格**按钮。
1. 选择**将单元格上移**或**将单元格左移**按钮。

编辑器将删除所选单元格。相邻的单元格将自动水平或垂直移动以调整间距。

**它是如何工作的？**

**将单元格上移**和**将单元格左移**由JSF后端bean **WorksheetView** 处理。相应方法的源代码如下：
#### **WorksheetView.removeCellShiftUp**
{{< highlight java >}}

     public void removeCellShiftUp() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().deleteRange(currentRowId, currentColumnId, currentRowId, currentColumnId, com.aspose.cells.ShiftType.UP);

        purge();

    }

{{< /highlight >}}

#### **WorksheetView.removeCellShiftLeft**
{{< highlight java >}}

     public void removeCellShiftLeft() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().deleteRange(currentRowId, currentColumnId, currentRowId, currentColumnId, com.aspose.cells.ShiftType.LEFT);

        purge();

    }

{{< /highlight >}}
### **清除单元格**
要清除单元格：

1. 单击要清除的单元格。
1. 切换到 **格式** 选项卡。
1. 点击 **清除单元格** 按钮。
1. 选择 **格式**、**内容** 或 **全部** 选项。

编辑器将清除所选单元格。

**它是如何工作的？**

**格式**、**内容** 和 **全部** 由JSF后端bean **WorksheetView** 处理。相应方法的源代码如下：
#### **WorksheetView.clearCurrentCellFormatting**
{{< highlight java >}}

     public void clearCurrentCellFormatting() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().clearFormats(currentRowId, currentColumnId, currentRowId, currentColumnId);

        reloadCell(currentColumnId, currentRowId);

        RequestContext.getCurrentInstance().update(currentCellClientId);

    }

{{< /highlight >}}

#### **WorksheetView.clearCurrentCellContents**
{{< highlight java >}}

     public void clearCurrentCellContents() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().clearContents(currentRowId, currentColumnId, currentRowId, currentColumnId);

        reloadCell(currentColumnId, currentRowId);

        RequestContext.getCurrentInstance().update(currentCellClientId);

    }

{{< /highlight >}}

#### **WorksheetView.clearCurrentCell**
{{< highlight java >}}

     public void clearCurrentCell() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().clearRange(currentRowId, currentColumnId, currentRowId, currentColumnId);

        reloadCell(currentColumnId, currentRowId);

        RequestContext.getCurrentInstance().update(currentCellClientId);

    }

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
