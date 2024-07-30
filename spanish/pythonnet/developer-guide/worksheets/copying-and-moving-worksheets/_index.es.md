---
title: Copiar y mover hojas de cálculo
type: docs
weight: 10
url: /es/python-net/copying-and-moving-worksheets/
description: Este artículo incluye código de muestra y describe cómo copiar y mover hojas de cálculo programáticamente tanto dentro de un libro de Excel como entre libros de Excel utilizando la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, copiar hoja de cálculo en Python, mover hoja de cálculo en Python, copiar hojas de cálculo entre libros de trabajo en Python, mover hojas de cálculo dentro de un libro en Python, copiar hojas de cálculo entre libros de trabajo en Python, copiar hojas de cálculo dentro de un libro en Python.
---

{{% alert color="primary" %}}

A veces, necesitas varias hojas de cálculo con formato y datos comunes. Por ejemplo, si trabajas con presupuestos trimestrales, es posible que desees crear un libro de trabajo con hojas que contengan los mismos encabezados de columna, encabezados de fila y fórmulas. Existe una forma de hacer esto: creando una hoja y luego copiándola.

Aspose.Cells para Python via .NET admite la copia y el movimiento de hojas de cálculo dentro o entre libros de Excel. Las hojas de cálculo, completas con datos, formato, tablas, matrices, gráficos, imágenes y otros objetos, se copian con el más alto grado de precisión.

{{% /alert %}}

## **Cómo mover o copiar hojas utilizando Microsoft Excel**

A continuación se detallan los pasos necesarios para copiar y mover hojas de cálculo dentro o entre libros de trabajo en Microsoft Excel.

1. Para mover o copiar hojas a otro libro de trabajo, abre el libro de trabajo que recibirá las hojas.
1. Cambia al libro de trabajo que contiene las hojas que deseas mover o copiar, y luego selecciona las hojas.
1. En el menú **Editar**, haga clic en **Mover o copiar hoja**.
1. En el cuadro de diálogo **Hacia el libro**, haga clic en el libro que recibirá las hojas.
1. Para mover o copiar las hojas seleccionadas a un nuevo libro de trabajo, haga clic en **Nuevo libro**.
1. En el cuadro **Antes de la hoja**, haga clic en la hoja antes de la cual desea insertar las hojas movidas o copiadas.
1. Para copiar las hojas en lugar de moverlas, seleccione la casilla **Crear una copia**.

## **Cómo copiar hojas dentro de un libro con la Biblioteca de Python Excel de Aspose.Cells**

Aspose.Cells for Python via .NET proporciona un método sobrecargado, [**Aspose.Cells.WorksheetCollection.add_copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add_copy/#str), que se utiliza para agregar una hoja a la colección y copiar datos de una hoja existente. Una versión del método toma el índice de la hoja de origen como parámetro. La otra versión toma el nombre de la hoja de origen.

El siguiente ejemplo muestra cómo copiar una hoja de trabajo existente dentro de un libro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWithinWorkbook-1.py" >}}

## **Cómo copiar hojas entre libros**

Aspose.Cells for Python via .NET proporciona un método, [**Aspose.Cells.Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy/#aspose.cells.Worksheet) utilizado para copiar datos y formato de una hoja de origen a otra hoja dentro o entre libros. El método toma como parámetro el objeto de la hoja de origen.

El siguiente ejemplo muestra cómo copiar una hoja de cálculo de un libro a otro libro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.py" >}}

El siguiente ejemplo muestra cómo copiar una hoja de cálculo de un libro a otro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.py" >}}

## **Cómo mover hojas dentro de un libro**

Aspose.Cells for Python via .NET proporciona un método [**Aspose.Cells.Worksheet.move_to()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/move_to/#int) que se utiliza para mover una hoja a otra ubicación en la misma hoja de cálculo. El método toma el índice de la hoja de destino como parámetro.

El siguiente ejemplo muestra cómo mover una hoja de cálculo a otra ubicación dentro del libro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-MoveWorksheet-1.py" >}}
