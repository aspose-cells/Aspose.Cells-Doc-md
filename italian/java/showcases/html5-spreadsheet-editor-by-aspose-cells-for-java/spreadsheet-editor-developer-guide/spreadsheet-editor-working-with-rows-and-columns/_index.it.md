---
title: Editor di fogli di calcolo - Utilizzo di righe e colonne
type: docs
weight: 30
url: /it/java/spreadsheet-editor-working-with-rows-and-columns/
---
**Sommario**

- [Aggiungi una riga](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaRow) 
 - WorksheetView.addRowAbove
 - WorksheetView.addRowBelow
- [Aggiungi una colonna](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaColumn) 
 - WorksheetView.addColumnBefore
 - WorksheetView.addColumnAfter
- [Elimina una riga](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaRow) 
 - WorksheetView.deleteRow
- [Elimina una colonna](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaColumn) 
 - WorksheetView.deleteColumn
- [Larghezza colonna e altezza riga](#SpreadsheetEditor-WorkingwithRowsandColumns-ColumnWidthandRowHeight) 
 - WorksheetView.setCurrentRowHeight
 - WorksheetView.setCurrentColumnWidth
- [Inserisci uno Cell](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
 - WorksheetView.addCellShiftRight
 - WorksheetView.addCellShiftDown
### **Aggiungi una riga**
Per aggiungere una nuova riga:

1. Fare clic su una cella in cui si desidera aggiungere una riga.
1.  Passa a**Scheda Formato**.
1.  Clic**Aggiungi riga sopra** per aggiungere una riga sopra la cella selezionata.
1.  Clic**Aggiungi riga sotto** per aggiungere una riga sotto la cella selezionata.

L'editor aggiungerà una nuova riga nella posizione selezionata.

![cose da fare:immagine_alt_testo](jjsornm.png)

**Come funziona?**

 Il**Aggiungi riga sopra** e**Aggiungi riga sotto** sono gestiti dal bean backend JSF**Foglio di lavoroVisualizza**. Il codice sorgente dei rispettivi metodi è il seguente:
#### **WorksheetView.addRowAbove**
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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

1. Fare clic su una cella in cui si desidera aggiungere una colonna.
1.  Passa a**Scheda Formato**.
1.  Clic**Aggiungi colonna prima**per aggiungere una colonna prima della cella selezionata.
1.  Clic**Aggiungi colonna dopo** per aggiungere una colonna dopo la cella selezionata.

L'editor aggiungerà una nuova colonna nella posizione selezionata.

![cose da fare:immagine_alt_testo](jjsornm.png)

**Come funziona?**

 Il**Aggiungi colonna prima** e**Aggiungi colonna dopo** sono gestiti dal bean backend JSF**Foglio di lavoroVisualizza**. Il codice sorgente dei rispettivi metodi è il seguente:
#### **WorksheetView.addColumnBefore**
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
### **Elimina una riga**
Per eliminare una riga:

1. Fare clic su una cella nella riga che si desidera eliminare.
1.  Passa a**Scheda Formato**.
1.  Clic**Elimina riga** pulsante.

L'editor eliminerà la riga che include la cella selezionata.

![cose da fare:immagine_alt_testo](jjsornm.png)

**Come funziona?**

 Il**Elimina riga** Il pulsante è gestito dal bean backend JSF**Foglio di lavoroVisualizza** utilizzando il metodo**WorksheetView.deleteRow**:
#### **WorksheetView.deleteRow**
{{< highlight "java" >}}

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
### **Elimina una colonna**
Per eliminare una colonna:

1. Fare clic su una cella nella colonna che si desidera eliminare.
1.  Passa a**Scheda Formato**.
1.  Clic**Elimina colonna** pulsante.

L'editor eliminerà la colonna che include la cella selezionata.

![cose da fare:immagine_alt_testo](jjsornm.png)

**Come funziona?**

 Il**Elimina colonna** Il pulsante è gestito dal bean backend JSF**Foglio di lavoroVisualizza** utilizzando il metodo**WorksheetView.deleteColumn**:
#### **WorksheetView.deleteColumn**
{{< highlight "java" >}}

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
### **Larghezza colonna e altezza riga**
Per modificare la larghezza di una colonna:

1. Fare clic su qualsiasi cella all'interno della colonna.
1.  Passa a**Scheda Formato**.
1.  Clic**Larghezza della colonna** pulsante per aprire**Larghezza della colonna**dialogo.
1. Immettere un nuovo valore nella finestra di dialogo.
1.  Clic**Chiudere**.

L'editor cambierà la larghezza della colonna.

**Come modificare l'altezza della riga?**

Per modificare l'altezza di una riga:

1. Fare clic su qualsiasi cella all'interno della riga.
1.  Passa a**Scheda Formato**.
1.  Clic**Altezza della riga** pulsante per aprire**Altezza della riga**dialogo.
1. Immettere un nuovo valore nella finestra di dialogo.
1.  Clic**Chiudere**.

L'editor cambierà l'altezza della riga.

**Come funziona?**

 Quando l'utente invia il valore di larghezza e altezza, questi valori vengono gestiti lato server da**setCurrentRowHeight** e**setCurrentColumnWidth** metodi del bean backend JSF**Foglio di lavoroVisualizza**.
#### **WorksheetView.setCurrentRowHeight**
{{< highlight "java" >}}

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
{{< highlight "java" >}}

     public void setCurrentColumnWidth(int width) {

        if (!isLoaded()) {

            return;

        }

        getAsposeWorksheet().getCells().setColumnWidthPixel(currentColumnId, width);

        reloadColumnWidth(currentColumnId);

        RequestContext.getCurrentInstance().update("sheet");

    }

{{< /highlight >}}
### **Inserisci uno Cell**
Per aggiungere una nuova cella:

1. Fare clic su una cella in cui si desidera nuovo.
1.  Passa a**Inserisci scheda**.
1.  Clic**Cell** pulsante.
1.  Scegliere**Maiusc Cells Destra** o**Maiusc Cells Giù** pulsante.

L'editor aggiungerà una nuova cella nella posizione selezionata. Le celle adiacenti verranno automaticamente spostate orizzontalmente o verticalmente per creare spazio per quella nuova.

**Come funziona?**

 Il**Maiusc Cells Destra** e**Maiusc Cells Giù** sono gestiti dal bean backend JSF**Foglio di lavoroVisualizza**. Il codice sorgente dei rispettivi metodi è il seguente:
#### **WorksheetView.addCellShiftRight**
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
