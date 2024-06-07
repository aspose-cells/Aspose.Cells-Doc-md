---
title: 电子表格编辑器 - 使用单元格
type: docs
weight: 40
url: /zh/java/spreadsheet-editor-working-with-cells/
---

**目录**

- [选择单元格](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
  - 选择单元格回调
- [删除单元格](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
  - WorksheetView.removeCellShiftUp
  - WorksheetView.removeCellShiftLeft
- [清除单元格](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
  - WorksheetView.clearCurrentCellFormatting
  - WorksheetView.clearCurrentCellContents
  - WorksheetView.clearCurrentCell
### **选择单元格**
使用鼠标指针指向一个单元格。单击一个单元格来选中它。所选单元格会用粗体矩形进行突出显示。

**它是如何工作的？**

当用户点击一个单元格时，事件由附加到 Primefaces 组件的 JavaScript 回调函数处理。
#### **选择单元格回调**
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
执行以下操作以删除单元格：

1. 点击要删除的单元格。
1. 切换到**格式**选项卡.
1. 点击**删除单元格**按钮。
1. 选择**向上移动单元格**或**向左移动单元格**按钮。

编辑器将删除所选的单元格。相邻的单元格将自动水平或垂直移动以调整空间。

**它是如何工作的？**

**向上移动单元格**和**向左移动单元格**由JSF后端Bean **WorksheetView** 处理。方法的源代码如下：
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

1. 点击要清除的单元格。
1. 切换到**格式**选项卡.
1. 点击**清除单元格**按钮。
1. 选择**格式**、**内容**或**两者都清除**选项。

编辑器将清除所选的单元格。

**它是如何工作的？**

**格式**、**内容**和**两者都清除**由JSF后端Bean **WorksheetView** 处理。方法的源代码如下：
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
