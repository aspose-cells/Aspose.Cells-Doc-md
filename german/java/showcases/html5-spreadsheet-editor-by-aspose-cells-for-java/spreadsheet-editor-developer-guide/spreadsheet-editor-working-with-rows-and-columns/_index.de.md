---
title: Tabellenkalkulations Editor  Arbeiten mit Zeilen und Spalten
type: docs
weight: 30
url: /de/java/spreadsheet-editor-working-with-rows-and-columns/
---

**Inhaltsverzeichnis**

- [Eine Zeile hinzufügen](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaRow) 
  - WorksheetView.addRowAbove
  - WorksheetView.addRowBelow
- [Eine Spalte hinzufügen](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaColumn) 
  - WorksheetView.addColumnBefore
  - WorksheetView.addColumnAfter
- [Eine Zeile löschen](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaRow) 
  - WorksheetView.deleteRow
- [Eine Spalte löschen](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaColumn) 
  - WorksheetView.deleteColumn
- [Spaltenbreite und Zeilenhöhe](#SpreadsheetEditor-WorkingwithRowsandColumns-ColumnWidthandRowHeight) 
  - WorksheetView.setCurrentRowHeight
  - WorksheetView.setCurrentColumnWidth
- [Eine Zelle einfügen](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
  - WorksheetView.addCellShiftRight
  - WorksheetView.addCellShiftDown
### **Eine Zeile hinzufügen**
Um eine neue Zeile hinzuzufügen:

1. Klicken Sie auf eine Zelle, an der Sie eine Zeile hinzufügen möchten.
1. Wechseln Sie zum **Format-Tab**.
1. Klicken Sie auf **Zeile oben hinzufügen**, um eine Zeile über der ausgewählten Zelle hinzuzufügen.
1. Klicken Sie auf **Zeile unten hinzufügen**, um eine Zeile unter der ausgewählten Zelle hinzuzufügen.

Der Editor fügt an der ausgewählten Stelle eine neue Zeile hinzu.

![todo:image_alt_text](jjsornm.png)

**Wie funktioniert es?**

Das **Hinzufügen einer Zeile oben** und **Hinzufügen einer Zeile unten** wird vom JSF-Backend-Bean **WorksheetView** verarbeitet. Der Quellcode der entsprechenden Methoden lautet wie folgt:
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
### **Eine Spalte hinzufügen**
Um eine neue Spalte hinzuzufügen:

1. Klicken Sie auf die Zelle, in der Sie eine Spalte hinzufügen möchten.
1. Wechseln Sie zum **Format-Tab**.
1. Klicken Sie auf **Spalte davor hinzufügen**, um eine Spalte vor der ausgewählten Zelle hinzuzufügen.
1. Klicken Sie auf **Spalte danach hinzufügen**, um eine Spalte nach der ausgewählten Zelle hinzuzufügen.

Der Editor fügt eine neue Spalte an der ausgewählten Position hinzu.

![todo:image_alt_text](jjsornm.png)

**Wie funktioniert es?**

Das **Spalte davor hinzufügen** und **Spalte danach hinzufügen** werden vom JSF-Backend-Bean **WorksheetView** verwaltet. Der Quellcode der entsprechenden Methoden lautet wie folgt:
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
### **Eine Zeile löschen**
Um eine Zeile zu löschen:

1. Klicken Sie auf eine Zelle in der Zeile, die Sie löschen möchten.
1. Wechseln Sie zum **Format-Tab**.
1. Klicken Sie auf die Schaltfläche **Zeile löschen**.

Der Editor wird die Zeile löschen, die die ausgewählte Zelle enthält.

![todo:image_alt_text](jjsornm.png)

**Wie funktioniert es?**

Die **Zeile löschen**-Schaltfläche wird vom JSF-Backend-Bean **WorksheetView** mit der Methode **WorksheetView.deleteRow** verwendet:
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
### **Eine Spalte löschen**
Um eine Spalte zu löschen:

1. Klicken Sie auf eine Zelle in der Spalte, die Sie löschen möchten.
1. Wechseln Sie zum **Format-Tab**.
1. Klicken Sie auf die Schaltfläche **Spalte löschen**.

Der Editor löscht die Spalte, die die ausgewählte Zelle enthält.

![todo:image_alt_text](jjsornm.png)

**Wie funktioniert es?**

Die Schaltfläche **Spalte löschen** wird vom JSF-Backend-Bean **WorksheetView** mit der Methode **WorksheetView.deleteColumn** behandelt:
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
### **Spaltenbreite und Zeilenhöhe**
Um die Breite einer Spalte zu ändern:

1. Klicken Sie auf eine Zelle in der Spalte.
1. Wechseln Sie zum **Format-Tab**.
1. Klicken Sie auf die Schaltfläche **Spaltenbreite**, um den **Spaltenbreite**-Dialog zu öffnen.
1. Geben Sie einen neuen Wert im Dialogfeld ein.
1. Klicken Sie auf **Schließen**.

Der Editor ändert die Breite der Spalte.

**Wie ändert man die Zeilenhöhe?**

Um die Höhe einer Zeile zu ändern:

1. Klicken Sie auf eine Zelle in der Zeile.
1. Wechseln Sie zum **Format-Tab**.
1. Klicken Sie auf die Schaltfläche **Zeilenhöhe**, um den **Zeilenhöhe**-Dialog zu öffnen.
1. Geben Sie einen neuen Wert im Dialogfeld ein.
1. Klicken Sie auf **Schließen**.

Der Editor wird die Höhe der Zeile ändern.

**Wie funktioniert es?**

Wenn der Benutzer den Wert von Breite und Höhe eingibt, werden diese Werte auf der Serverseite von den Methoden **setCurrentRowHeight** und **setCurrentColumnWidth** des JSF-Backend-Beans **WorksheetView** verarbeitet.
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
### **Eine Zelle einfügen**
Um eine neue Zelle hinzuzufügen:

1. Klicken Sie auf eine Zelle, in der Sie eine neue möchten.
1. Wechseln Sie zu **Einfügen**Registerkarte.
1. Klicken Sie auf die Schaltfläche **Zelle**.
1. Wählen Sie die Schaltfläche **Zellen rechts verschieben** oder **Zellen nach unten verschieben**.

Der Editor fügt eine neue Zelle an der ausgewählten Position hinzu. Die benachbarten Zellen werden automatisch horizontal oder vertikal verschoben, um Platz für die neue zu schaffen.

**Wie funktioniert es?**

Das Verschieben von Zellen rechts und das Verschieben von Zellen nach unten werden vom JSF-Backend-Bean **WorksheetView** gehandhabt. Der Quellcode der entsprechenden Methoden lautet wie folgt:
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
