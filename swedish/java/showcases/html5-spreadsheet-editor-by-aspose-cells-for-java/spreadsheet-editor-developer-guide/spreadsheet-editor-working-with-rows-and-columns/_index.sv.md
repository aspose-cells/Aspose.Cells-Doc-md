---
title: Kalkylarksredigerare - Arbeta med rader och kolumner
type: docs
weight: 30
url: /sv/java/spreadsheet-editor-working-with-rows-and-columns/
---
**Innehållsförteckning**

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
- [Sätt in ett Cell](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
 - WorksheetView.addCellShiftRight
 - WorksheetView.addCellShiftDown
### **Lägg till en rad**
Så här lägger du till en ny rad:

1. Klicka på en cell där du vill lägga till en rad.
1.  Byta till**Fliken Format**.
1.  Klick**Lägg till rad ovan** för att lägga till en rad ovanför den markerade cellen.
1.  Klick**Lägg till rad nedan** för att lägga till en rad under den markerade cellen.

Redaktören lägger till en ny rad på den valda platsen.

![todo:image_alt_text](jjsornm.png)

**Hur det fungerar?**

 De**Lägg till rad ovan** och**Lägg till rad nedan** hanteras av JSF backend bean**Arbetsbladsvy**Källkoden för respektive metoder är följande:
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
### **Lägg till en kolumn**
Så här lägger du till en ny kolumn:

1. Klicka på en cell där du vill lägga till en kolumn.
1.  Byta till**Fliken Format**.
1.  Klick**Lägg till kolumn före** för att lägga till en kolumn före den markerade cellen.
1.  Klick**Lägg till kolumn efter** för att lägga till en kolumn efter den markerade cellen.

Redaktören lägger till en ny kolumn på den valda platsen.

![todo:image_alt_text](jjsornm.png)

**Hur det fungerar?**

 De**Lägg till kolumn före** och**Lägg till kolumn efter** hanteras av JSF backend bean**Arbetsbladsvy**Källkoden för respektive metoder är följande:
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
### **Ta bort en rad**
Så här tar du bort en rad:

1. Klicka på en cell i raden du vill ta bort.
1.  Byta till**Fliken Format**.
1.  Klick**Ta bort rad** knapp.

Redaktören tar bort raden som innehåller den markerade cellen.

![todo:image_alt_text](jjsornm.png)

**Hur det fungerar?**

 De**Ta bort rad** knappen hanteras av JSF backend bean**Arbetsbladsvy** använder metoden**WorksheetView.deleteRow**:
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
### **Ta bort en kolumn**
Så här tar du bort en kolumn:

1. Klicka på en cell i kolumnen du vill ta bort.
1.  Byta till**Fliken Format**.
1.  Klick**Ta bort kolumn** knapp.

Redaktören tar bort kolumnen som innehåller den markerade cellen.

![todo:image_alt_text](jjsornm.png)

**Hur det fungerar?**

 De**Ta bort kolumn** knappen hanteras av JSF backend bean**Arbetsbladsvy** använder metoden**WorksheetView.deleteColumn**:
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
### **Kolumnbredd och radhöjd**
Så här ändrar du bredden på en kolumn:

1. Klicka på valfri cell i kolumnen.
1.  Byta till**Fliken Format**.
1.  Klick**Kolumnbredd** knappen för att öppna**Kolumnbredd** dialog.
1. Ange ett nytt värde i dialogrutan.
1.  Klick**Stänga**.

Redaktören ändrar spaltens bredd.

**Hur ändrar man radhöjd?**

Så här ändrar du höjden på en rad:

1. Klicka på valfri cell inuti raden.
1.  Byta till**Fliken Format**.
1.  Klick**Radhöjd** knappen för att öppna**Radhöjd** dialog.
1. Ange ett nytt värde i dialogrutan.
1.  Klick**Stänga**.

Redaktören kommer att ändra höjden på raden.

**Hur det fungerar?**

 När användaren skickar in värdet för bredd och höjd, hanteras dessa värden på serversidan av**setCurrentRowHeight** och**setCurrentColumnWidth** metoder för JSF backend bean**Arbetsbladsvy**.
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
### **Sätt in ett Cell**
Så här lägger du till en ny cell:

1. Klicka på en cell där du vill ny.
1.  Byta till**Infoga flik**.
1.  Klick**Cell** knapp.
1.  Välja**Skift Cells Höger** eller**Skift Cells Ner** knapp.

Redaktören lägger till en ny cell på den valda platsen. De intilliggande cellerna kommer automatiskt att flyttas antingen horisontellt eller vertikalt för att skapa utrymme för den nya.

**Hur det fungerar?**

 De**Skift Cells Höger** och**Skift Cells Ner** hanteras av JSF backend bean**Arbetsbladsvy**Källkoden för respektive metoder är följande:
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
