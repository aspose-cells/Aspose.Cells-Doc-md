---
title: Copiar y mover hojas de cálculo
type: docs
weight: 10
url: /es/net/copying-and-moving-worksheets/
description: Este artículo incluye código de muestra y describe cómo copiar y mover hojas de cálculo programáticamente tanto dentro de un libro de trabajo de Excel como entre libros de trabajo de Excel utilizando la API de C# o la Biblioteca .NET.
keywords: copiar hoja de cálculo c#, mover hoja de cálculo c#
---

{{% alert color="primary" %}}

A veces, necesitas varias hojas de cálculo con formato y datos comunes. Por ejemplo, si trabajas con presupuestos trimestrales, es posible que desees crear un libro de trabajo con hojas que contengan los mismos encabezados de columna, encabezados de fila y fórmulas. Existe una forma de hacer esto: creando una hoja y luego copiándola.

Aspose.Cells admite la copia y el movimiento de hojas de cálculo dentro o entre libros de trabajo. Las hojas de cálculo, completas con datos, formato, tablas, matrices, gráficos, imágenes y otros objetos, se copian con el mayor grado de precisión.

{{% /alert %}}

## **Mover o Copiar Hojas usando Microsoft Excel**

A continuación se detallan los pasos necesarios para copiar y mover hojas de cálculo dentro o entre libros de trabajo en Microsoft Excel.

1. Para mover o copiar hojas a otro libro de trabajo, abre el libro de trabajo que recibirá las hojas.
1. Cambia al libro de trabajo que contiene las hojas que deseas mover o copiar, y luego selecciona las hojas.
1. En el menú **Editar**, haga clic en **Mover o copiar hoja**.
1. En el cuadro de diálogo **Hacia el libro**, haga clic en el libro que recibirá las hojas.
1. Para mover o copiar las hojas seleccionadas a un nuevo libro de trabajo, haga clic en **Nuevo libro**.
1. En el cuadro **Antes de la hoja**, haga clic en la hoja antes de la cual desea insertar las hojas movidas o copiadas.
1. Para copiar las hojas en lugar de moverlas, seleccione la casilla **Crear una copia**.

### **Copiar hojas de cálculo dentro de un libro con Aspose.Cells**

Aspose.Cells proporciona un método sobrecargado, [**Aspose.Cells.WorksheetCollection.AddCopy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/addcopy/index), que se utiliza para agregar una hoja de cálculo a la colección y copiar datos de una hoja de cálculo existente. Una versión del método toma el índice de la hoja de cálculo fuente como parámetro. La otra versión toma el nombre de la hoja de cálculo fuente.

El siguiente ejemplo muestra cómo copiar una hoja de trabajo existente dentro de un libro.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWithinWorkbook-1.cs" >}}

### **Copiar Hojas de Cálculo entre Libros de Trabajo**

Aspose.Cells proporciona un método, [**Aspose.Cells.Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index) utilizado para copiar datos y formato de una hoja de cálculo de origen a otra hoja de cálculo dentro o entre libros de trabajo. El método toma el objeto de hoja de cálculo de origen como parámetro.

El siguiente ejemplo muestra cómo copiar una hoja de cálculo de un libro a otro libro.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.cs" >}}

El siguiente ejemplo muestra cómo copiar una hoja de cálculo de un libro a otro.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.cs" >}}

### **Mover Hojas de Cálculo dentro de un Libro de Trabajo**

Aspose.Cells proporciona un método [**Aspose.Cells.Worksheet.MoveTo()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/moveto) que se utiliza para mover una hoja de cálculo a otra ubicación en la misma hoja de cálculo. El método toma el índice de hoja de cálculo de destino como parámetro.

El siguiente ejemplo muestra cómo mover una hoja de cálculo a otra ubicación dentro del libro.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-MoveWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
