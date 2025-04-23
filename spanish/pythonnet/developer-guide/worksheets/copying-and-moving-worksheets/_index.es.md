---
title: Copiar y mover hojas de cálculo
type: docs
weight: 10
url: /es/python-net/copying-and-moving-worksheets/
description: Este artículo incluye código de ejemplo y describe cómo copiar y mover hojas de cálculo programáticamente tanto dentro de un libro de Excel como entre libros de Excel usando la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel en Python, copiar hoja de cálculo en Python, mover hoja de cálculo en Python, copiar hojas de cálculo entre libros, mover hojas de cálculo dentro de un libro, copiar hojas de cálculo entre libros, copiar hojas de cálculo dentro de un libro.
---

{{% alert color="primary" %}}

A veces, necesitas varias hojas de cálculo con formato y datos comunes. Por ejemplo, si trabajas con presupuestos trimestrales, es posible que desees crear un libro de trabajo con hojas que contengan los mismos encabezados de columna, encabezados de fila y fórmulas. Existe una forma de hacer esto: creando una hoja y luego copiándola.

Aspose.Cells para Python via .NET soporta copiar y mover hojas de cálculo dentro o entre libros de trabajo. Las hojas de cálculo, completas con datos, formato, tablas, matrices, gráficos, imágenes y otros objetos, se copian con el mayor grado de precisión.

{{% /alert %}}

## **Cómo mover o copiar hojas usando Microsoft Excel**

A continuación se detallan los pasos necesarios para copiar y mover hojas de cálculo dentro o entre libros de trabajo en Microsoft Excel.

1. Para mover o copiar hojas a otro libro de trabajo, abre el libro de trabajo que recibirá las hojas.
1. Cambia al libro de trabajo que contiene las hojas que deseas mover o copiar, y luego selecciona las hojas.
1. En el menú **Editar**, haga clic en **Mover o copiar hoja**.
1. En el cuadro de diálogo **Hacia el libro**, haga clic en el libro que recibirá las hojas.
1. Para mover o copiar las hojas seleccionadas a un nuevo libro de trabajo, haga clic en **Nuevo libro**.
1. En el cuadro **Antes de la hoja**, haga clic en la hoja antes de la cual desea insertar las hojas movidas o copiadas.
1. Para copiar las hojas en lugar de moverlas, seleccione la casilla **Crear una copia**.

## **Cómo copiar hojas dentro de un libro con Aspose.Cells para Python Excel Library**

Aspose.Cells para Python via .NET proporciona un método sobrecargado, [**Aspose.Cells.WorksheetCollection.add_copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add_copy/#str), que se usa para agregar una hoja de cálculo a la colección y copiar datos de una hoja de cálculo existente. Una versión del método toma el índice de la hoja fuente como parámetro. La otra versión toma el nombre de la hoja fuente.

El siguiente ejemplo muestra cómo copiar una hoja de trabajo existente dentro de un libro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWithinWorkbook-1.py" >}}

## **Cómo copiar hojas entre libros de trabajo**

Aspose.Cells para Python via .NET proporciona un método, [**Aspose.Cells.Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy/#aspose.cells.Worksheet), utilizado para copiar datos y formato de una hoja de cálculo fuente a otra dentro o entre libros de trabajo. El método toma el objeto hoja de cálculo fuente como parámetro.

El siguiente ejemplo muestra cómo copiar una hoja de cálculo de un libro a otro libro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.py" >}}

El siguiente ejemplo muestra cómo copiar una hoja de cálculo de un libro a otro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.py" >}}

## **Cómo mover hojas de cálculo dentro de un libro**

Aspose.Cells para Python via .NET proporciona un método [**Aspose.Cells.Worksheet.move_to()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/move_to/#int) que se usa para mover una hoja de cálculo a otra ubicación en la misma hoja de cálculo. El método toma el índice de la hoja de cálculo de destino como parámetro.

El siguiente ejemplo muestra cómo mover una hoja de cálculo a otra ubicación dentro del libro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-MoveWorksheet-1.py" >}}
