---
title: Copiar y mover hojas de cálculo
type: docs
weight: 20
url: /es/java/copying-and-moving-worksheets/
---

{{% alert color="primary" %}}

A veces, necesitas varias hojas de cálculo con formato y datos comunes. Por ejemplo, si trabajas con presupuestos trimestrales, es posible que desees crear un libro de trabajo con hojas que contengan los mismos encabezados de columna, encabezados de fila y fórmulas. Existe una forma de hacer esto: creando una hoja y luego copiándola.

Aspose.Cells admite la copia y el movimiento de hojas de cálculo dentro o entre libros de trabajo. Las hojas de cálculo, completas con datos, formato, tablas, matrices, gráficos, imágenes y otros objetos, se copian con el mayor grado de precisión.

{{% /alert %}}

## **Mover o Copiar Hojas usando Microsoft Excel**

A continuación se presentan los pasos involucrados para copiar y mover hojas de trabajo dentro o entre libros.

1. Para mover o copiar hojas a otro libro de trabajo, abre el libro de trabajo que recibirá las hojas.
1. Cambia al libro de trabajo que contiene las hojas que deseas mover o copiar, y luego selecciona las hojas.
1. En el menú **Editar**, haga clic en **Mover o copiar hoja**.
1. En el cuadro Libro, haga clic en el libro que recibirá las hojas.
1. Para mover o copiar las hojas seleccionadas a un nuevo libro, haga clic en **nuevo libro**.
1. En el cuadro **Antes de la hoja**, haga clic en la hoja antes de la cual desea insertar las hojas movidas o copiadas.
1. Para copiar las hojas en lugar de moverlas, seleccione la casilla **Crear una copia**.

## **Copiar Hojas de Cálculo dentro de un Libro de Trabajo**

Aspose.Cells proporciona un método sobrecargado, [**WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#addCopy(int)), que se utiliza para agregar una hoja de cálculo a la colección y copiar datos de una hoja de cálculo existente. Una versión del método toma el índice de la hoja de cálculo fuente como parámetro. La otra versión toma el nombre de la hoja de cálculo fuente.

El siguiente ejemplo muestra cómo copiar una hoja de trabajo existente dentro de un libro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWithinWorkbook-CopyWithinWorkbook.java" >}}

## **Copiar Hojas de Cálculo entre Libros de Trabajo**

Aspose.Cells proporciona un método, [**Worksheet.copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)), utilizado para copiar datos y formato de una hoja de cálculo de origen a otra hoja de cálculo dentro o entre los libros de trabajo. El método toma el objeto de la hoja de cálculo de origen como parámetro.

El siguiente ejemplo muestra cómo copiar una hoja de cálculo de un libro a otro libro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetsBetweenWorkbooks-CopyWorksheetsBetweenWorkbooks.java" >}}

El siguiente ejemplo muestra cómo copiar una hoja de cálculo de un libro a otro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetFromWorkbookToOther-CopyWorksheetFromWorkbookToOther.java" >}}

## **Mover Hojas de Cálculo dentro de un Libro de Trabajo**

Aspose.Cells proporciona un método, [**Worksheet.moveTo()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#moveTo(int)), utilizado para mover una hoja de cálculo a otra ubicación en la misma hoja de cálculo.

El siguiente ejemplo muestra cómo mover una hoja de cálculo a otra ubicación dentro del libro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-MoveWorksheet-MoveWorksheet.java" >}}
