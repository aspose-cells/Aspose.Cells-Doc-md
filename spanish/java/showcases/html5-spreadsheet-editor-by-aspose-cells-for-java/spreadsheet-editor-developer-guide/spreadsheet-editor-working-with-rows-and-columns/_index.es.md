---
title: "Editor de hojas de cálculo: trabajar con filas y columnas"
type: docs
weight: 30
url: /es/java/spreadsheet-editor-working-with-rows-and-columns/
---
**Tabla de contenido**

- [Agregar una fila](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaRow) 
 - WorksheetView.addRowAbove
 - WorksheetView.addRowBelow
- [Agregar una columna](#SpreadsheetEditor-WorkingwithRowsandColumns-AddaColumn) 
 - WorksheetView.addColumnBefore
 - WorksheetView.addColumnDespués
- [Eliminar una fila](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaRow) 
 - WorksheetView.deleteRow
- [Eliminar una columna](#SpreadsheetEditor-WorkingwithRowsandColumns-DeleteaColumn) 
 - WorksheetView.deleteColumn
- [Ancho de columna y alto de fila](#SpreadsheetEditor-WorkingwithRowsandColumns-ColumnWidthandRowHeight) 
 - WorksheetView.setCurrentRowHeight
 - WorksheetView.setCurrentColumnWidth
- [Inserta un Cell](#SpreadsheetEditor-WorkingwithRowsandColumns-InsertaCell) 
 - WorksheetView.addCellShiftRight
 - WorksheetView.addCellShiftDown
### **Agregar una fila**
Para agregar una nueva fila:

1. Haga clic en una celda donde desea agregar una fila.
1.  Cambiar a**Pestaña Formato**.
1.  Hacer clic**Agregar fila arriba** para agregar una fila encima de la celda seleccionada.
1.  Hacer clic**Agregar fila a continuación** para agregar una fila debajo de la celda seleccionada.

El editor agregará una nueva fila en la ubicación seleccionada.

![todo:imagen_alternativa_texto](jjsornm.png)

**¿Cómo funciona?**

 los**Agregar fila arriba** y**Agregar fila a continuación** son manejados por JSF backend bean**Vista de hoja de trabajo**. El código fuente de los respectivos métodos es el siguiente:
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
### **Agregar una columna**
Para agregar una nueva columna:

1. Haga clic en una celda donde desea agregar una columna.
1.  Cambiar a**Pestaña Formato**.
1.  Hacer clic**Agregar columna antes**para agregar una columna antes de la celda seleccionada.
1.  Hacer clic**Añadir columna después** para agregar una columna después de la celda seleccionada.

El editor agregará una nueva columna en la ubicación seleccionada.

![todo:imagen_alternativa_texto](jjsornm.png)

**¿Cómo funciona?**

 los**Agregar columna antes** y**Añadir columna después** son manejados por JSF backend bean**Vista de hoja de trabajo**. El código fuente de los respectivos métodos es el siguiente:
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
### **Eliminar una fila**
Para eliminar una fila:

1. Haga clic en una celda de la fila que desea eliminar.
1.  Cambiar a**Pestaña Formato**.
1.  Hacer clic**Borrar fila** botón.

El editor eliminará la fila que incluye la celda seleccionada.

![todo:imagen_alternativa_texto](jjsornm.png)

**¿Cómo funciona?**

 los**Borrar fila** el botón es manejado por JSF backend bean**Vista de hoja de trabajo** utilizando el método**WorksheetView.deleteRow**:
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
### **Eliminar una columna**
Para eliminar una columna:

1. Haga clic en una celda de la columna que desea eliminar.
1.  Cambiar a**Pestaña Formato**.
1.  Hacer clic**Eliminar columna** botón.

El editor eliminará la columna que incluye la celda seleccionada.

![todo:imagen_alternativa_texto](jjsornm.png)

**¿Cómo funciona?**

 los**Eliminar columna** el botón es manejado por JSF backend bean**Vista de hoja de trabajo** utilizando el método**WorksheetView.deleteColumn**:
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
### **Ancho de columna y alto de fila**
Para cambiar el ancho de una columna:

1. Haga clic en cualquier celda dentro de la columna.
1.  Cambiar a**Pestaña Formato**.
1.  Hacer clic**Ancho de columna** botón para abrir**Ancho de columna**diálogo.
1. Introduzca un nuevo valor en el cuadro de diálogo.
1.  Hacer clic**Cerca**.

El editor cambiará el ancho de la columna.

**¿Cómo cambiar la altura de la fila?**

Para cambiar la altura de una fila:

1. Haga clic en cualquier celda dentro de la fila.
1.  Cambiar a**Pestaña Formato**.
1.  Hacer clic**Altura de la fila** botón para abrir**Altura de la fila**diálogo.
1. Introduzca un nuevo valor en el cuadro de diálogo.
1.  Hacer clic**Cerca**.

El editor cambiará la altura de la fila.

**¿Cómo funciona?**

 Cuando el usuario envía el valor de ancho y alto, estos valores son manejados en el lado del servidor por**establecerCurrentRowHeight** y**establecerAnchoDeColumnaActual** métodos de JSF backend bean**Vista de hoja de trabajo**.
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
### **Inserta un Cell**
Para agregar una nueva celda:

1. Haga clic en una celda en la que desee crear una nueva.
1.  Cambiar a**Insertar pestaña**.
1.  Hacer clic**Cell** botón.
1.  Elegir**Cambio Cells Derecha** o**Cambio Cells Abajo** botón.

El editor agregará una nueva celda en la ubicación seleccionada. Las celdas adyacentes se desplazarán automáticamente ya sea horizontal o verticalmente para crear espacio para la nueva.

**¿Cómo funciona?**

 los**Cambio Cells Derecha** y**Cambio Cells Abajo** son manejados por JSF backend bean**Vista de hoja de trabajo**. El código fuente de los respectivos métodos es el siguiente:
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
