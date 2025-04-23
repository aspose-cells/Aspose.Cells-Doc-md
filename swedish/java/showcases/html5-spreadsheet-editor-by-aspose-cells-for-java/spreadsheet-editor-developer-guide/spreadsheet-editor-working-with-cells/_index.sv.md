---
title: Kalkylbladsredigerare  Arbeta med celler
type: docs
weight: 40
url: /sv/java/spreadsheet-editor-working-with-cells/
---

Innehållsförteckning

- [Välja en cell](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
  - Cellvalsanrop
- [Ta bort en cell](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
  - WorksheetView.removeCellShiftUp
  - WorksheetView.removeCellShiftLeft
- [Rensa en cell](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
  - WorksheetView.clearCurrentCellFormatting
  - WorksheetView.clearCurrentCellContents
  - WorksheetView.clearCurrentCell
### **Välja en cell**
Använd muspekaren för att peka på en cell. Klicka på en cell för att välja den. Den valda cellen markeras med en fet rektangel.

**Hur fungerar det?**

När användaren klickar på en cell hanteras händelsen av JavaScripts återuppringningsfunktion som är knuten till Primefaces-komponenten.
#### **Cellvalsanrop**
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
### **Ta bort en cell**
För att ta bort en cell:

1. Klicka på en cell du vill ta bort.
1. Byt till **Formatflik**.
1. Klicka på **Ta bort cell** knappen.
1. Välj **Skifta celler upp** eller **Skifta celler vänster** knappen.

Redigeraren kommer att ta bort den valda cellen. De intilliggande cellerna kommer automatiskt att flyttas antingen horisontellt eller vertikalt för att anpassa utrymmet.

**Hur fungerar det?**

**Skifta celler upp** och **Skifta celler vänster** hanteras av JSF backend bean **WorksheetView**. Källkoden för respektive metoder är följande:
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
### **Rensa en cell**
För att rensa en cell:

1. Klicka på en cell du vill rensa.
1. Byt till **Formatflik**.
1. Klicka på **Rensa cell** knappen.
1. Välj **Format**, **Innehåll** eller **Båda** alternativet.

Redigeraren kommer att rensa den valda cellen.

**Hur fungerar det?**

**Format**, **Innehåll** och **Båda** hanteras av JSF backend bean **WorksheetView**. Källkoden för respektive metoder är följande:
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
