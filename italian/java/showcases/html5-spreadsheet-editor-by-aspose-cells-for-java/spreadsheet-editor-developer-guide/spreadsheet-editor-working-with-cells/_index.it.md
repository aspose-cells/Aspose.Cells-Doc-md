---
title: Editor del Foglio di Calcolo  Lavorare con le Celle
type: docs
weight: 40
url: /it/java/spreadsheet-editor-working-with-cells/
---

**Tabella dei contenuti**

- [Selezione di una cella](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
  - Richiamata di selezione della cella
- [Elimina una cella](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
  - WorksheetView.removeCellShiftUp
  - WorksheetView.removeCellShiftLeft
- [Cancella una cella](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
  - WorksheetView.clearCurrentCellFormatting
  - WorksheetView.clearCurrentCellContents
  - WorksheetView.clearCurrentCell
### **Selezione di una cella**
Usa il puntatore del mouse per puntare a una cella. Clicca su una cella per selezionarla. La cella selezionata è evidenziata da un rettangolo in grassetto.

**Come funziona?**

Quando l'utente clicca su una cella, l'evento è gestito da una funzione di callback JavaScript che è allegata al componente Primefaces.
#### **Callback selezione cella**
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
### **Elimina una cella**
Per eliminare una cella:

1. Fai clic su una cella che desideri eliminare.
1. Passare alla scheda **Formato**.
1. Fai clic sul pulsante **Elimina cella**.
1. Scegli il pulsante **Sposta celle in su** o **Sposta celle a sinistra**.

L'editor eliminerà la cella selezionata. Le celle adiacenti verranno spostate automaticamente sia orizzontalmente che verticalmente per adattare lo spazio.

**Come funziona?**

I pulsanti **Sposta celle in su** e **Sposta celle a sinistra** sono gestiti dal bean backend JSF **WorksheetView**. Il codice sorgente dei rispettivi metodi è il seguente:
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
### **Cancella una cella**
Per cancellare una cella:

1. Fai clic su una cella che desideri cancellare.
1. Passare alla scheda **Formato**.
1. Fare clic sul pulsante **Cancella cella**.
1. Scegliere l'opzione **Formati**, **Contenuti** o **Entrambi**.

L'editor cancellerà la cella selezionata.

**Come funziona?**

I **Formati**, i **Contenuti** e **Entrambi** sono gestiti dal bean backend JSF **WorksheetView**. Il codice sorgente dei metodi rispettivi è il seguente:
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
