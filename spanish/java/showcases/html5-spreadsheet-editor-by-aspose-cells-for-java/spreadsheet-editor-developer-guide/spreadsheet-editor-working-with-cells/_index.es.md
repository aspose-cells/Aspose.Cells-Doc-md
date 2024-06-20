---
title: Editor de hojas de cálculo Trabajar con celdas
type: docs
weight: 40
url: /es/java/spreadsheet-editor-working-with-cells/
---

**Tabla de contenidos**

- [Seleccionar una Celda](#SpreadsheetEditor-WorkingwithCells-SelectingaCell) 
  - Callback de selección de celda
- [Eliminar una Celda](#SpreadsheetEditor-WorkingwithCells-DeleteaCell) 
  - WorksheetView.removeCellShiftUp
  - WorksheetView.removeCellShiftLeft
- [Borrar una celda](#SpreadsheetEditor-WorkingwithCells-ClearaCell) 
  - WorksheetView.clearCurrentCellFormatting
  - WorksheetView.clearCurrentCellContents
  - WorksheetView.clearCurrentCell
### **Seleccionar una Celda**
Usa el puntero de tu ratón para señalar una celda. Haz clic en una celda para seleccionarla. La celda seleccionada se resalta con un rectángulo en negrita.

**¿Cómo funciona?**

Cuando el usuario hace clic en una celda, el evento es manejado por una función de devolución de llamada de JavaScript que está adjunta al componente Primefaces.
#### **Callback de selección de celda**
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
### **Eliminar una Celda**
Para eliminar una celda:

1. Haz clic en la celda que deseas eliminar.
1. Cambie a la pestaña **Formato**.
1. Haz clic en el botón **Eliminar celda**.
1. Elija el botón **Mover celdas hacia arriba** o **Mover celdas a la izquierda**.

El editor eliminará la celda seleccionada. Las celdas adyacentes se desplazarán automáticamente ya sea horizontal o verticalmente para ajustar el espacio.

**¿Cómo funciona?**

Los botones **Mover celdas hacia arriba** y **Mover celdas a la izquierda** son manejados por el bean de backend JSF **WorksheetView**. El código fuente de los métodos respectivos es el siguiente:
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
### **Borrar una celda**
Para borrar una celda:

1. Haga clic en una celda que desee borrar.
1. Cambie a la pestaña **Formato**.
1. Haga clic en el botón **Borrar celda**.
1. Elija la opción **Formatos**, **Contenidos** o **Ambos**.

El editor borrará la celda seleccionada.

**¿Cómo funciona?**

Los **Formatos**, **Contenidos** y **Ambos** son manejados por el bean de backend JSF **WorksheetView**. El código fuente de los métodos respectivos es el siguiente:
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
