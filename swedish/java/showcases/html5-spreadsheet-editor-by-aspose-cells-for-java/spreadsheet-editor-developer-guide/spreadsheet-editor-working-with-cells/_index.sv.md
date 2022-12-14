---
title: Kalkylarksredigerare - Arbeta med Cells
type: docs
weight: 40
url: /sv/java/spreadsheet-editor-working-with-cells/
---
**Innehållsförteckning**

- [Välj en Cell](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
 - Cell valåteruppringning
- [Ta bort ett Cell](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
 - WorksheetView.removeCellShiftUp
 - WorksheetView.removeCellShiftLeft
- [Rensa en Cell](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
 - WorksheetView.clearCurrentCellFormatting
 - WorksheetView.clearCurrentCellContents
 - WorksheetView.clearCurrentCell
### **Välj en Cell**
Använd muspekaren för att peka på en cell. Klicka på en cell för att markera den. Den markerade cellen är markerad med en fet rektangel.

**Hur det fungerar?**

När användaren klickar på en cell hanteras händelsen av JavaScript-återuppringningsfunktionen som är kopplad till Primefaces-komponenten.
#### **Cell val återuppringning**
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
### **Ta bort ett Cell**
Så här tar du bort en cell:

1. Klicka på en cell du vill ta bort.
1.  Byta till**Fliken Format**.
1.  Klick**Radera Cell** knapp.
1.  Välja**Skift Cells Upp** eller**Skift Cells Vänster** knapp.

Redaktören tar bort den markerade cellen. De intilliggande cellerna kommer automatiskt att flyttas antingen horisontellt eller vertikalt för att justera utrymmet.

**Hur det fungerar?**

 De**Skift Cells Upp** och**Skift Cells Vänster** hanteras av JSF backend bean**Arbetsbladsvy**Källkoden för respektive metoder är följande:
#### **WorksheetView.removeCellShiftUp**
{{< highlight "java" >}}

     public void removeCellShiftUp() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().deleteRange(currentRowId, currentColumnId, currentRowId, currentColumnId, com.aspose.cells.ShiftType.UP);

        purge();

    }

{{< /highlight >}}

#### **WorksheetView.removeCellShiftLeft**
{{< highlight "java" >}}

     public void removeCellShiftLeft() {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().deleteRange(currentRowId, currentColumnId, currentRowId, currentColumnId, com.aspose.cells.ShiftType.LEFT);

        purge();

    }

{{< /highlight >}}
### **Rensa en Cell**
Så här rensar du en cell:

1. Klicka på en cell du vill rensa.
1.  Byta till**Fliken Format**.
1.  Klick**Rensa Cell** knapp.
1.  Välja**Format**, **Innehåll** eller**Både** alternativ.

Redaktören rensar den markerade cellen.

**Hur det fungerar?**

 De**Format**, **Innehåll** och**Både** hanteras av JSF backend bean**Arbetsbladsvy**Källkoden för respektive metoder är följande:
#### **WorksheetView.clearCurrentCellFormatting**
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

#### **WorksheetView.clearCurrentCellContents**
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

#### **WorksheetView.clearCurrentCell**
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
