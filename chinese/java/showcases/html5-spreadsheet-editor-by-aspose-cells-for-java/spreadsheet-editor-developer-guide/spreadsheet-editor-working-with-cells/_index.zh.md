---
title: 电子表格编辑器 - 使用 Cells
type: docs
weight: 40
url: /zh/java/spreadsheet-editor-working-with-cells/
---
**目录**

- [选择一个 Cell](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
 - Cell 选择回调
- [删除一个 Cell](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
 - WorksheetView.removeCellShiftUp
 - WorksheetView.removeCellShiftLeft
- [清除一个 Cell](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
 WorksheetView.clearCurrentCellFormatting
 - WorksheetView.clearCurrentCellContents
 - 工作表视图.clearCurrentCell
### **选择一个 Cell**
使用鼠标指针指向一个单元格。单击一个单元格以将其选中。所选单元格以粗体矩形突出显示。

**怎么运行的？**

当用户单击一个单元格时，该事件由附加到 Primefaces 组件的 JavaScript 回调函数处理。
#### **Cell选择回调**
{{< highlight "java" >}}

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
### **删除一个 Cell**
要删除一个单元格：

1. 单击要删除的单元格。
1. 切换到**格式选项卡**.
1. 点击**删除 Cell**按钮。
1. 选择**上移 Cells**要么**左移 Cells**按钮。

编辑器将删除选定的单元格。相邻的单元格将自动水平或垂直移动以调整空间。

**怎么运行的？**

这**上移 Cells**和**左移 Cells**由 JSF 后端 bean 处理**工作表视图**.各个方法的源码如下：
#### **工作表视图.removeCellShiftUp**
{{< highlight "java" >}}

     public void removeCellShiftUp() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().deleteRange(currentRowId, currentColumnId, currentRowId, currentColumnId, com.aspose.cells.ShiftType.UP);

        purge();

    }

{{< /highlight >}}

#### **工作表视图.removeCellShiftLeft**
{{< highlight "java" >}}

     public void removeCellShiftLeft() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().deleteRange(currentRowId, currentColumnId, currentRowId, currentColumnId, com.aspose.cells.ShiftType.LEFT);

        purge();

    }

{{< /highlight >}}
### **清除一个 Cell**
要清除单元格：

1. 单击要清除的单元格。
1. 切换到**格式选项卡**.
1. 点击**清除 Cell**按钮。
1. 选择**格式**, **内容**要么**两个都**选项。

编辑器将清除选定的单元格。

**怎么运行的？**

这**格式**, **内容**和**两个都**由 JSF 后端 bean 处理**工作表视图**.各个方法的源码如下：
#### **工作表视图.clearCurrentCellFormatting**
{{< highlight "java" >}}

     public void clearCurrentCellFormatting() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().clearFormats(currentRowId, currentColumnId, currentRowId, currentColumnId);

        reloadCell(currentColumnId, currentRowId);

        RequestContext.getCurrentInstance().update(currentCellClientId);

    }

{{< /highlight >}}

#### **工作表视图.clearCurrentCellContents**
{{< highlight "java" >}}

     public void clearCurrentCellContents() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().clearContents(currentRowId, currentColumnId, currentRowId, currentColumnId);

        reloadCell(currentColumnId, currentRowId);

        RequestContext.getCurrentInstance().update(currentCellClientId);

    }

{{< /highlight >}}

#### **工作表视图.clearCurrentCell**
{{< highlight "java" >}}

     public void clearCurrentCell() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().clearRange(currentRowId, currentColumnId, currentRowId, currentColumnId);

        reloadCell(currentColumnId, currentRowId);

        RequestContext.getCurrentInstance().update(currentCellClientId);

    }

{{< /highlight >}}
