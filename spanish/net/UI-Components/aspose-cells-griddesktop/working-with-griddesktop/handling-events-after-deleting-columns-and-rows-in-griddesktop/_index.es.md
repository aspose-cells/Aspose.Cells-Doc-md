---
title: Manejo de eventos después de eliminar columnas y filas en GridDesktop
type: docs
weight: 80
url: /es/net/handling-events-after-deleting-columns-and-rows-in-griddesktop/
---
## **Posibles escenarios de uso**
Aspose.Cells para GridDesktop ha agregado dos nuevos eventos, es decir, AfterDeleteColumns y AfterDeleteRows, como se muestra en la siguiente captura de pantalla. Estos eventos se activan cuando elimina columnas y filas respectivamente.

![todo:imagen_alternativa_texto](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **Manejo de eventos después de eliminar columnas y filas en GridDesktop**
El siguiente código de ejemplo explica cómo utilizar los eventos AfterDeleteColumns y AfterDeleteRows. Cada vez que elimine algunas columnas o filas, se llamará a la función dada y se mostrará un cuadro de mensaje que muestra el índice de la columna o fila eliminada.
## **Código de muestra**
{{< highlight "java" >}}

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
