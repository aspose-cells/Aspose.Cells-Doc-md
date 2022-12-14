---
title: Tabelleneditor - Arbeiten mit Zeilen und Spalten
type: docs
weight: 30
url: /de/java/spreadsheet-editor-working-with-rows-and-columns/
---
**Inhaltsverzeichnis**

- [Zeile hinzufügen](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaRow) 
 - WorksheetView.addRowAbove
 - WorksheetView.addRowBelow
- [Spalte hinzufügen](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaColumn) 
 - WorksheetView.addColumnBefore
 - WorksheetView.addColumnAfter
- [Löschen Sie eine Zeile](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaRow) 
 - WorksheetView.deleteRow
- [Löschen Sie eine Spalte](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaColumn) 
 - WorksheetView.deleteColumn
- [Spaltenbreite und Zeilenhöhe](#SpreadsheetEditor-WorkingwithRowsandColumns-ColumnWidthandRowHeight) 
 - WorksheetView.setCurrentRowHeight
 - WorksheetView.setCurrentColumnWidth
- [Geben Sie eine Cell ein](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
 - WorksheetView.addCellShiftRight
 - WorksheetView.addCellShiftDown
### **Zeile hinzufügen**
So fügen Sie eine neue Zeile hinzu:

1. Klicken Sie auf eine Zelle, in der Sie eine Zeile hinzufügen möchten.
1.  Wechseln zu**Registerkarte „Format“.**.
1.  Klicken**Zeile oben hinzufügen** , um eine Zeile über der ausgewählten Zelle hinzuzufügen.
1.  Klicken**Zeile unten hinzufügen** , um eine Zeile unter der ausgewählten Zelle hinzuzufügen.

Der Editor fügt an der ausgewählten Stelle eine neue Zeile hinzu.

![todo: Bild_alt_Text](jjsornm.png)

**Wie es funktioniert?**

 Das**Zeile oben hinzufügen** und**Zeile unten hinzufügen** werden von der JSF-Backend-Bean verarbeitet**Arbeitsblattansicht**. Der Quellcode der jeweiligen Methoden sieht wie folgt aus:
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
### **Spalte hinzufügen**
So fügen Sie eine neue Spalte hinzu:

1. Klicken Sie auf eine Zelle, in der Sie eine Spalte hinzufügen möchten.
1.  Wechseln zu**Registerkarte „Format“.**.
1.  Klicken**Spalte davor hinzufügen** um eine Spalte vor der ausgewählten Zelle hinzuzufügen.
1.  Klicken**Spalte danach hinzufügen** , um eine Spalte nach der ausgewählten Zelle hinzuzufügen.

Der Editor fügt an der ausgewählten Stelle eine neue Spalte hinzu.

![todo: Bild_alt_Text](jjsornm.png)

**Wie es funktioniert?**

 Das**Spalte davor hinzufügen** und**Spalte danach hinzufügen** werden von der JSF-Backend-Bean verarbeitet**Arbeitsblattansicht**. Der Quellcode der jeweiligen Methoden sieht wie folgt aus:
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
### **Löschen Sie eine Zeile**
So löschen Sie eine Zeile:

1. Klicken Sie auf eine Zelle in der Zeile, die Sie löschen möchten.
1.  Wechseln zu**Registerkarte „Format“.**.
1.  Klicken**Zeile löschen** Taste.

Der Editor löscht die Zeile, die die ausgewählte Zelle enthält.

![todo: Bild_alt_Text](jjsornm.png)

**Wie es funktioniert?**

 Das**Zeile löschen** Die Schaltfläche wird von der JSF-Backend-Bean verarbeitet**Arbeitsblattansicht** Methode verwenden**WorksheetView.deleteRow**:
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
### **Löschen Sie eine Spalte**
So löschen Sie eine Spalte:

1. Klicken Sie auf eine Zelle in der Spalte, die Sie löschen möchten.
1.  Wechseln zu**Registerkarte „Format“.**.
1.  Klicken**Spalte löschen** Taste.

Der Editor löscht die Spalte, die die ausgewählte Zelle enthält.

![todo: Bild_alt_Text](jjsornm.png)

**Wie es funktioniert?**

 Das**Spalte löschen** Die Schaltfläche wird von der JSF-Backend-Bean verarbeitet**Arbeitsblattansicht** Methode verwenden**WorksheetView.deleteColumn**:
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
### **Spaltenbreite und Zeilenhöhe**
So ändern Sie die Breite einer Spalte:

1. Klicken Sie auf eine beliebige Zelle innerhalb der Spalte.
1.  Wechseln zu**Registerkarte „Format“.**.
1.  Klicken**Spaltenbreite** Taste zum Öffnen**Spaltenbreite**Dialog.
1. Geben Sie im Dialogfeld einen neuen Wert ein.
1.  Klicken**Nah dran**.

Der Editor ändert die Spaltenbreite.

**Wie ändert man die Zeilenhöhe?**

So ändern Sie die Höhe einer Zeile:

1. Klicken Sie auf eine beliebige Zelle innerhalb der Zeile.
1.  Wechseln zu**Registerkarte „Format“.**.
1.  Klicken**Zeilenhöhe** Taste zum Öffnen**Zeilenhöhe**Dialog.
1. Geben Sie im Dialogfeld einen neuen Wert ein.
1.  Klicken**Nah dran**.

Der Editor ändert die Zeilenhöhe.

**Wie es funktioniert?**

 Wenn der Benutzer den Wert für Breite und Höhe übermittelt, werden diese Werte serverseitig verarbeitet von**setCurrentRowHeight** und**setCurrentColumnWidth** Methoden der JSF-Backend-Bean**Arbeitsblattansicht**.
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
### **Geben Sie eine Cell ein**
So fügen Sie eine neue Zelle hinzu:

1. Klicken Sie auf eine Zelle, in die Sie neu möchten.
1.  Wechseln zu**Registerkarte einfügen**.
1.  Klicken**Cell** Taste.
1.  Wählen**Verschiebung Cells Rechts** oder**Schicht Cells Runter** Taste.

Der Editor fügt an der ausgewählten Stelle eine neue Zelle hinzu. Die angrenzenden Zellen werden automatisch entweder horizontal oder vertikal verschoben, um Platz für die neue zu schaffen.

**Wie es funktioniert?**

 Das**Verschiebung Cells Rechts** und**Schicht Cells Runter** werden von der JSF-Backend-Bean verarbeitet**Arbeitsblattansicht**. Der Quellcode der jeweiligen Methoden sieht wie folgt aus:
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
