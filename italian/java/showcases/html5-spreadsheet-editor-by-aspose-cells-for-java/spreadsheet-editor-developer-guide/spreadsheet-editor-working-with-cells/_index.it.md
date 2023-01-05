---
title: Editor di fogli di calcolo - Lavorare con Cells
type: docs
weight: 40
url: /it/java/spreadsheet-editor-working-with-cells/
---
**Sommario**

- [Selezionando uno Cell](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
 - Cell selezione richiamata
- [Cancella un Cell](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
 - WorksheetView.removeCellShiftUp
 - WorksheetView.removeCellShiftLeft
- [Cancella un Cell](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
 WorksheetView.clearCurrentCellFormatting
 - WorksheetView.clearCurrentCellContents
 - WorksheetView.clearCurrentCell
### **Selezionando uno Cell**
Usa il puntatore del mouse per indicare una cella. Fare clic su una cella per selezionarla. La cella selezionata è evidenziata da un rettangolo in grassetto.

**Come funziona?**

Quando l'utente fa clic su una cella, l'evento viene gestito dalla funzione di callback JavaScript collegata al componente Primefaces.
#### **Cell selezione richiamata**
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
### **Cancella un Cell**
Per eliminare una cella:

1. Fare clic su una cella che si desidera eliminare.
1.  Passa a**Scheda Formato**.
1.  Clic**Cancella Cell** pulsante.
1.  Scegliere**Turno Cells Su** o**Maiusc Cells Sinistra** pulsante.

L'editor eliminerà la cella selezionata. Le celle adiacenti verranno automaticamente spostate orizzontalmente o verticalmente per regolare lo spazio.

**Come funziona?**

 Il**Turno Cells Su** e**Maiusc Cells Sinistra** sono gestiti dal bean backend JSF**Foglio di lavoroVisualizza**. Il codice sorgente dei rispettivi metodi è il seguente:
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
### **Cancella un Cell**
Per cancellare una cella:

1. Fare clic su una cella che si desidera cancellare.
1.  Passa a**Scheda Formato**.
1.  Clic**Chiaro Cell** pulsante.
1.  Scegliere**Formati**, **Contenuti** o**Tutti e due** opzione.

L'editor cancellerà la cella selezionata.

**Come funziona?**

 Il**Formati**, **Contenuti** e**Tutti e due** sono gestiti dal bean backend JSF**Foglio di lavoroVisualizza**. Il codice sorgente dei rispettivi metodi è il seguente:
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
