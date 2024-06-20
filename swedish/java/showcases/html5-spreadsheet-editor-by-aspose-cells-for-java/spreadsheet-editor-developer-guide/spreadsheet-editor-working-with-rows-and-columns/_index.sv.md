---
title: Kalkyleringsredigerare  Arbeta med rader och kolumner
type: docs
weight: 30
url: /sv/java/spreadsheet-editor-working-with-rows-and-columns/
---

Innehållsförteckning

- [Lägg till en rad](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaRow) 
  - WorksheetView.addRowAbove
  - WorksheetView.addRowBelow
- [Lägg till en kolumn](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaColumn) 
  - WorksheetView.addColumnBefore
  - WorksheetView.addColumnAfter
- [Ta bort en rad](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaRow) 
  - WorksheetView.deleteRow
- [Ta bort en kolumn](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaColumn) 
  - WorksheetView.deleteColumn
- [Kolumnbredd och radhöjd](#SpreadsheetEditor-WorkingwithRowsandColumns-ColumnWidthandRowHeight) 
  - WorksheetView.setCurrentRowHeight
  - WorksheetView.setCurrentColumnWidth
- [Infoga en cell](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
  - WorksheetView.addCellShiftRight
  - WorksheetView.addCellShiftDown
### **Lägg till en rad**
För att lägga till en ny rad:

1. Klicka på en cell där du vill lägga till en rad.
1. Byt till **Formatflik**.
1. Klicka på **Lägg till rad ovanför** för att lägga till en rad ovanför den markerade cellen.
1. Klicka på **Lägg till rad nedanför** för att lägga till en rad under den markerade cellen.

Redigeraren kommer att lägga till en ny rad på den markerade platsen.

![todo:image_alt_text](jjsornm.png)

**Hur fungerar det?**

**Lägg till rad ovanför** och **Lägg till rad nedanför** hanteras av JSF backend bean **WorksheetView**. Källkoden för respektive metod är följande:
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
### **Lägg till en kolumn**
För att lägga till en ny kolumn:

1. Klicka på en cell där du vill lägga till en kolumn.
1. Byt till **Formatflik**.
1. Klicka på **Lägg till kolumn före** för att lägga till en kolumn före den markerade cellen.
1. Klicka på **Lägg till kolumn efter** för att lägga till en kolumn efter den markerade cellen.

Redigeraren kommer att lägga till en ny kolumn på den markerade platsen.

![todo:image_alt_text](jjsornm.png)

**Hur fungerar det?**

**Lägg till kolumn före** and **Lägg till kolumn efter** hanteras av JSF backend bean **WorksheetView**. Källkoden för respektive metod är följande:
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
### **Ta bort en rad**
För att ta bort en rad:

1. Klicka på en cell i den rad du vill ta bort.
1. Byt till **Formatflik**.
1. Klicka på **Ta bort rad** knappen.

Editorn kommer att ta bort raden som inkluderar den valda cellen.

![todo:image_alt_text](jjsornm.png)

**Hur fungerar det?**

Knappen **Delete Row** hanteras av JSF backend bean **WorksheetView** med metoden **WorksheetView.deleteRow**:
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
### **Ta bort en kolumn**
För att ta bort en kolumn:

1. Klicka på en cell i kolumnen du vill ta bort.
1. Byt till **Formatflik**.
1. Klicka på **Ta bort kolumn** knappen.

Editorn kommer att ta bort kolumnen som inkluderar den valda cellen.

![todo:image_alt_text](jjsornm.png)

**Hur fungerar det?**

Knappen **Delete Column** hanteras av JSF backend bean **WorksheetView** med metoden **WorksheetView.deleteColumn**:
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
### **Kolumnbredd och radhöjd**
För att ändra bredd på en kolumn:

1. Klicka på valfri cell i kolumnen.
1. Byt till **Formatflik**.
1. Klicka på **Kolumnbredd** knappen för att öppna dialogrutan **Kolumnbredd**.
1. Mata in ett nytt värde i dialogrutan.
1. Klicka på **Stäng**.

Editorn kommer att ändra bredden på kolumnen.

**Hur ändrar man radhöjden?**

För att ändra höjden på en rad:

1. Klicka på valfri cell i raden.
1. Byt till **Formatflik**.
1. Klicka på **Radhöjd** knappen för att öppna dialogrutan **Radhöjd**.
1. Mata in ett nytt värde i dialogrutan.
1. Klicka på **Stäng**.

Redaktören kommer att ändra radens höjd.

**Hur fungerar det?**

När användaren skickar värdet på bredd och höjd, hanteras dessa värden på serverns sida av metoderna **setCurrentRowHeight** och **setCurrentColumnWidth** av JSF backend bean **WorksheetView**.
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
### **Infoga en cell**
För att lägga till en ny cell:

1. Klicka på en cell där du vill ha ny.
1. Byt till fliken **Infoga**.
1. Klicka på knappen **Cell**.
1. Välj knappen **Förskjut celler höger** eller **Förskjut celler ned**.

Redaktören kommer att lägga till en ny cell på den valda platsen. De intilliggande cellerna kommer att automatiskt förflyttas antingen horisontellt eller vertikalt för att skapa plats för den nya.

**Hur fungerar det?**

Förskjutning av celler höger och Förskjutning av celler ned hanteras av JSF backend bean **WorksheetView**. Källkoden för de respektive metoderna är följande:
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
