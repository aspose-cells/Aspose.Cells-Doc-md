---
title: Editor de hojas de cálculo - Trabajando con Cells
type: docs
weight: 40
url: /es/java/spreadsheet-editor-working-with-cells/
---
**Tabla de contenido**

- [Seleccionando un Cell](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
 - Cell devolución de llamada de selección
- [Eliminar un Cell](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
 - WorksheetView.removeCellShiftUp
 - WorksheetView.removeCellShiftLeft
- [Borrar un Cell](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
 - WorksheetView.clearCurrentCellFormatting
 - WorksheetView.clearCurrentCellContents
 - WorksheetView.clearCurrentCell
### **Seleccionando un Cell**
Use el puntero del mouse para señalar una celda. Haga clic en una celda para seleccionarla. La celda seleccionada se resalta con un rectángulo en negrita.

**¿Cómo funciona?**

Cuando el usuario hace clic en una celda, el evento es manejado por la función de devolución de llamada de JavaScript que se adjunta al componente Primefaces.
#### **Cell devolución de llamada de selección**
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
### **Eliminar un Cell**
Para eliminar una celda:

1. Haz clic en una celda que quieras eliminar.
1.  Cambiar a**Pestaña Formato**.
1.  Hacer clic**Eliminar Cell** botón.
1.  Elegir**Turno Cells Arriba** o**Turno Cells Izquierda** botón.

El editor eliminará la celda seleccionada. Las celdas adyacentes se desplazarán automáticamente ya sea horizontal o verticalmente para ajustar el espacio.

**¿Cómo funciona?**

 los**Turno Cells Arriba** y**Turno Cells Izquierda** son manejados por JSF backend bean**Vista de hoja de trabajo**. El código fuente de los respectivos métodos es el siguiente:
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
### **Borrar un Cell**
Para borrar una celda:

1. Haz clic en una celda que quieras borrar.
1.  Cambiar a**Pestaña Formato**.
1.  Hacer clic**Claro Cell** botón.
1.  Elegir**Formatos**, **Contenido** o**Ambas cosas** opción.

El editor borrará la celda seleccionada.

**¿Cómo funciona?**

 los**Formatos**, **Contenido** y**Ambas cosas** son manejados por JSF backend bean**Vista de hoja de trabajo**. El código fuente de los respectivos métodos es el siguiente:
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
