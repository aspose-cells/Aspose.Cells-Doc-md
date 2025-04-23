---
title: Editor del Foglio Elettronico  Lavorare con Righe e Colonne
type: docs
weight: 30
url: /it/java/spreadsheet-editor-working-with-rows-and-columns/
---

**Tabella dei contenuti**

- [Aggiungi una riga](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaRow) 
  - WorksheetView.addRowAbove
  - WorksheetView.addRowBelow
- [Aggiungi una colonna](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaColumn) 
  - WorksheetView.addColumnBefore
  - WorksheetView.addColumnAfter
- [Elimina una Riga](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaRow) 
  - WorksheetView.deleteRow
- [Eliminare una colonna](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaColumn) 
  - WorksheetView.deleteColumn
- [Larghezza della colonna e altezza della riga](#SpreadsheetEditor-WorkingwithRowsandColumns-ColumnWidthandRowHeight) 
  - WorksheetView.setCurrentRowHeight
  - WorksheetView.setCurrentColumnWidth
- [Inserisci una cella](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
  - WorksheetView.addCellShiftRight
  - WorksheetView.addCellShiftDown
### **Aggiungi una riga**
Per aggiungere una nuova riga:

1. Fare clic su una cella dove si desidera aggiungere una riga.
1. Passare alla scheda **Formato**.
1. Fare clic su **Aggiungi riga sopra** per aggiungere una riga sopra la cella selezionata.
1. Fare clic su **Aggiungi riga sotto** per aggiungere una riga sotto la cella selezionata.

L'editore aggiungerà una nuova riga nella posizione selezionata.

![todo:image_alt_text](jjsornm.png)

**Come funziona?**

Gli **Aggiungi riga sopra** e **Aggiungi riga sotto** sono gestiti dal bean backend JSF **WorksheetView**. Il codice sorgente dei rispettivi metodi è il seguente:
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
### **Aggiungi una colonna**
Per aggiungere una nuova colonna:

1. Fare clic su una cella dove si desidera aggiungere una colonna.
1. Passare alla scheda **Formato**.
1. Fare clic su **Aggiungi colonna prima** per aggiungere una colonna prima della cella selezionata.
1. Fare clic su **Aggiungi colonna dopo** per aggiungere una colonna dopo la cella selezionata.

L'editore aggiungerà una nuova colonna nella posizione selezionata.

![todo:image_alt_text](jjsornm.png)

**Come funziona?**

**Aggiungi Colonna Prima** e **Aggiungi Colonna Dopo** sono gestite dal bean di backend JSF **WorksheetView**. Il codice sorgente dei rispettivi metodi è il seguente:
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
### **Elimina una Riga**
Per eliminare una riga:

1. Fare clic su una cella nella riga che si desidera eliminare.
1. Passare alla scheda **Formato**.
1. Fare clic sul pulsante **Elimina Riga**.

L'editore eliminerà la riga che include la cella selezionata.

![todo:image_alt_text](jjsornm.png)

**Come funziona?**

Il pulsante **Elimina Riga** è gestito dal bean di backend JSF **WorksheetView** utilizzando il metodo **WorksheetView.deleteRow**:
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
### **Eliminare una colonna**
Per eliminare una colonna:

1. Fare clic su una cella nella colonna che si desidera eliminare.
1. Passare alla scheda **Formato**.
1. Fare clic sul pulsante **Elimina Colonna**.

L'editore eliminerà la colonna che include la cella selezionata.

![todo:image_alt_text](jjsornm.png)

**Come funziona?**

Il pulsante **Elimina colonna** è gestito dal bean backend JSF **WorksheetView** utilizzando il metodo **WorksheetView.deleteColumn**:
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
### **Larghezza della colonna e altezza della riga**
Per modificare la larghezza di una colonna:

1. Fare clic su qualsiasi cella all'interno della colonna.
1. Passare alla scheda **Formato**.
1. Fare clic sul pulsante **Larghezza colonna** per aprire il dialogo **Larghezza colonna**.
1. Inserire un nuovo valore nella casella di dialogo.
1. Fare clic su **Chiudi**.

L'editor cambierà la larghezza della colonna.

**Come cambiare l'altezza della riga?**

Per modificare l'altezza di una riga:

1. Fare clic su qualsiasi cella all'interno della riga.
1. Passare alla scheda **Formato**.
1. Fare clic sul pulsante **Altezza riga** per aprire il dialogo **Altezza riga**.
1. Inserire un nuovo valore nella casella di dialogo.
1. Fare clic su **Chiudi**.

L'editor cambierà l'altezza della riga.

**Come funziona?**

Quando l'utente invia il valore di larghezza e altezza, questi valori vengono gestiti sul lato server dai metodi **setCurrentRowHeight** e **setCurrentColumnWidth** del bean backend JSF **WorksheetView**.
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
### **Inserisci una cella**
Per aggiungere una nuova cella:

1. Fare clic su una cella dove si desidera quella nuova.
1. Passare alla scheda **Inserisci**.
1. Fare clic sul pulsante **Cella**.
1. Scegliere il pulsante **Spostare celle a destra** o **Spostare celle in basso**.

L'editor aggiungerà una nuova cella nella posizione selezionata. Le celle adiacenti verranno spostate automaticamente orizzontalmente o verticalmente per creare spazio per la nuova.

**Come funziona?**

Lo **Spostamento celle a destra** e **Spostamento celle in basso** sono gestiti dal bean JSF backend **WorksheetView**. Il codice sorgente dei rispettivi metodi è il seguente:
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
{{< app/cells/assistant language="java" >}}
