---
title: Editor de hojas de cálculo  Trabajando con Filas y Columnas
type: docs
weight: 30
url: /es/java/spreadsheet-editor-working-with-rows-and-columns/
---

**Tabla de contenidos**

- [Agregar una fila](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaRow) 
  - WorksheetView.addRowAbove
  - WorksheetView.addRowBelow
- [Agregar una columna](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaColumn) 
  - WorksheetView.addColumnBefore
  - WorksheetView.addColumnAfter
- [Eliminar una fila](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaRow) 
  - WorksheetView.deleteRow
- [Eliminar una columna](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaColumn) 
  - WorksheetView.deleteColumn
- [Ancho de columna y altura de fila](#SpreadsheetEditor-WorkingwithRowsandColumns-ColumnWidthandRowHeight) 
  - WorksheetView.setCurrentRowHeight
  - WorksheetView.setCurrentColumnWidth
- [Insertar una celda](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
  - WorksheetView.addCellShiftRight
  - WorksheetView.addCellShiftDown
### **Agregar una fila**
Para agregar una nueva fila:

1. Haz clic en una celda donde desees agregar una fila.
1. Cambie a la pestaña **Formato**.
1. Haz clic en **Agregar fila arriba** para agregar una fila encima de la celda seleccionada.
1. Haz clic en **Agregar fila abajo** para agregar una fila debajo de la celda seleccionada.

El editor agregará una nueva fila en la ubicación seleccionada.

![todo:image_alt_text](jjsornm.png)

**¿Cómo funciona?**

El **Agregar fila arriba** y **Agregar fila abajo** están manejados por el bean de backend JSF **WorksheetView**. El código fuente de los métodos respectivos es el siguiente:
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
### **Agregar una columna**
Para agregar una nueva columna:

1. Haga clic en una celda donde desee agregar una columna.
1. Cambie a la pestaña **Formato**.
1. Haga clic en **Agregar columna antes** para agregar una columna antes de la celda seleccionada.
1. Haga clic en **Agregar columna después** para agregar una columna después de la celda seleccionada.

El editor agregará una nueva columna en la ubicación seleccionada.

![todo:image_alt_text](jjsornm.png)

**¿Cómo funciona?**

El **Agregar columna antes** y **Agregar columna después** están manejados por el bean de backend JSF **WorksheetView**. El código fuente de los métodos respectivos es el siguiente:
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
### **Eliminar una fila**
Para eliminar una fila:

1. Haga clic en una celda en la fila que desea eliminar.
1. Cambie a la pestaña **Formato**.
1. Haz clic en el botón **Eliminar fila**.

El editor eliminará la fila que incluye la celda seleccionada.

![todo:image_alt_text](jjsornm.png)

**¿Cómo funciona?**

El botón **Eliminar fila** es manejado por el bean de backend JSF **WorksheetView** utilizando el método **WorksheetView.deleteRow**:
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
### **Eliminar una columna**
Para eliminar una columna:

1. Haz clic en una celda en la columna que deseas eliminar.
1. Cambie a la pestaña **Formato**.
1. Haz clic en el botón **Eliminar columna**.

El editor eliminará la columna que incluye la celda seleccionada.

![todo:image_alt_text](jjsornm.png)

**¿Cómo funciona?**

El botón **Eliminar columna** es manejado por el bean de backend JSF **WorksheetView** utilizando el método **WorksheetView.deleteColumn**:
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
### **Ancho de columna y altura de fila**
Para cambiar el ancho de una columna:

1. Haz clic en cualquier celda dentro de la columna.
1. Cambie a la pestaña **Formato**.
1. Haz clic en el botón **Ancho de columna** para abrir el diálogo **Ancho de columna**.
1. Ingrese un nuevo valor en el cuadro de diálogo.
1. Haga clic en **Cerrar**.

El editor cambiará el ancho de la columna.

**¿Cómo cambiar la altura de la fila?**

Para cambiar la altura de una fila:

1. Haga clic en cualquier celda dentro de la fila.
1. Cambie a la pestaña **Formato**.
1. Haga clic en el botón **Altura de fila** para abrir el cuadro de diálogo **Altura de fila**.
1. Ingrese un nuevo valor en el cuadro de diálogo.
1. Haga clic en **Cerrar**.

El editor cambiará la altura de la fila.

**¿Cómo funciona?**

Cuando el usuario envía el valor de ancho y altura, estos valores son manejados en el lado del servidor por los métodos **setCurrentRowHeight** y **setCurrentColumnWidth** del bean backend JSF **WorksheetView**.
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
### **Insertar una celda**
Para agregar una nueva celda:

1. Haga clic en una celda donde desee la nueva.
1. Cambie a la pestaña **Insertar**.
1. Haga clic en el botón **Celda**.
1. Elija el botón **Desplazar celdas a la derecha** o **Desplazar celdas hacia abajo**.

El editor agregará una nueva celda en la ubicación seleccionada. Las celdas adyacentes se desplazarán automáticamente horizontalmente o verticalmente para crear espacio para la nueva.

**¿Cómo funciona?**

El **Desplazar celdas a la derecha** y **Desplazar celdas hacia abajo** son manejados por el bean de backend de JSF **WorksheetView**. El código fuente de los métodos respectivos es el siguiente:
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
