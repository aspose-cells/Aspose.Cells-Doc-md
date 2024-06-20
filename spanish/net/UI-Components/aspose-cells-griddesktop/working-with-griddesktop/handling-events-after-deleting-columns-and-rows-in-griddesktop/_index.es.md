---
title: Manejo de Eventos después de Eliminar Columnas y Filas en GridDesktop
type: docs
weight: 80
url: /es/net/aspose-cells-griddesktop/handle-events-after-delete-columns-and-rows-in-griddesktop/
keywords: GridDesktop,eventos,eliminar fila,eliminar columna
description: Este artículo introduce los eventos después de eliminar filas/columnas en GridDesktop.
---

## **Escenarios de uso posibles**
Aspose.Cells para GridDesktop ha agregado dos nuevos eventos, es decir, AfterDeleteColumns y AfterDeleteRows como se muestra en la siguiente captura de pantalla. Estos eventos se activan cuando elimina columnas y filas respectivamente.

![todo:image_alt_text](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **Manejo de Eventos después de Eliminar Columnas y Filas en GridDesktop**
El siguiente código de muestra explica cómo hacer uso de los eventos AfterDeleteColumns y AfterDeleteRows. Cada vez que se eliminan columnas o filas, se llamará a la función dada y mostrará un cuadro de mensaje que muestra el índice de la columna o fila eliminada.
## **Código de muestra**
{{< highlight java >}}

 private void gridDesktop1_AfterDeleteColumnsAndRows(object sender, Aspose.Cells.GridDesktop.WorksheetEventArgs args)

{

    if(args.SheetEvents == Aspose.Cells.GridDesktop.WorksheetEvents.ColumnDeleted)

    {

        MessageBox.Show("Deleted Column Index: " + args.Index);

    }

    if (args.SheetEvents == Aspose.Cells.GridDesktop.WorksheetEvents.RowDeleted)

    {

        MessageBox.Show("Deleted Row Index: " + args.Index);

    }

}

{{< /highlight >}}
