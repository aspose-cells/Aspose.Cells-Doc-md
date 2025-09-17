##Spreadsheet Editor - Working with Cells
**Table of Contents**
- [Selecting a Cell](#SpreadsheetEditor-WorkingwithCells-SelectingaCell)
- Cell selection callback
- [Delete a Cell](#SpreadsheetEditor-WorkingwithCells-DeleteaCell)
- WorksheetView.removeCellShiftUp
- WorksheetView.removeCellShiftLeft
- [Clear a Cell](#SpreadsheetEditor-WorkingwithCells-ClearaCell)
- WorksheetView.clearCurrentCellFormatting
- WorksheetView.clearCurrentCellContents
- WorksheetView.clearCurrentCell
### **Selecting a Cell**
Use your mouse pointer to point to a cell. Click a cell to select it. The selected cell is highlighted by a bold rectangle.
**How it works?**
When the user click a cell, the event is handled by JavaScript callback function which is attached to Primefaces component.
#### **Cell selection callback**
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
### **Delete a Cell**
To delete a cell:
1. Click on a cell you want to delete.
1. Switch to **Format tab**.
1. Click **Delete Cell** button.
1. Choose **Shift Cells Up** or **Shift Cells Left** button.
The editor will delete the selected cell. The adjacent cells will be automatically shifted either horizontally or vertically to adjust the space.
**How it works?**
The **Shift Cells Up** and **Shift Cells Left** are handled by JSF backend bean **WorksheetView**. The source code of the respective methods is as follows:
#### **WorksheetView.removeCellShiftUp**
public void removeCellShiftUp() {
if (!isLoaded()) {
return;
}
getAsposeWorksheet().getCells().deleteRange(currentRowId, currentColumnId, currentRowId, currentColumnId, com.aspose.cells.ShiftType.UP);
purge();
}
#### **WorksheetView.removeCellShiftLeft**
public void removeCellShiftLeft() {
if (!isLoaded()) {
return;
}
getAsposeWorksheet().getCells().deleteRange(currentRowId, currentColumnId, currentRowId, currentColumnId, com.aspose.cells.ShiftType.LEFT);
purge();
}
### **Clear a Cell**
To clear a cell:
1. Click on a cell you want to clear.
1. Switch to **Format tab**.
1. Click **Clear Cell** button.
1. Choose **Formats**, **Contents** or **Both** option.
The editor will clear the selected cell.
**How it works?**
The **Formats**, **Contents** and **Both** are handled by JSF backend bean **WorksheetView**. The source code of the respective methods is as follows:
#### **WorksheetView.clearCurrentCellFormatting**
public void clearCurrentCellFormatting() {
if (!isLoaded()) {
return;
}
getAsposeWorksheet().getCells().clearFormats(currentRowId, currentColumnId, currentRowId, currentColumnId);
reloadCell(currentColumnId, currentRowId);
RequestContext.getCurrentInstance().update(currentCellClientId);
}
#### **WorksheetView.clearCurrentCellContents**
public void clearCurrentCellContents() {
if (!isLoaded()) {
return;
}
getAsposeWorksheet().getCells().clearContents(currentRowId, currentColumnId, currentRowId, currentColumnId);
reloadCell(currentColumnId, currentRowId);
RequestContext.getCurrentInstance().update(currentCellClientId);
}
#### **WorksheetView.clearCurrentCell**
public void clearCurrentCell() {
if (!isLoaded()) {
return;
}
getAsposeWorksheet().getCells().clearRange(currentRowId, currentColumnId, currentRowId, currentColumnId);
reloadCell(currentColumnId, currentRowId);
RequestContext.getCurrentInstance().update(currentCellClientId);
}
