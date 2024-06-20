---
title: Copiar y mover hojas de cálculo
type: docs
weight: 20
url: /es/python-java/copying-and-moving-worksheets/
---

{{% alert color="primary" %}} 

A veces, necesitas varias hojas de cálculo con formato y datos comunes. Por ejemplo, si trabajas con presupuestos trimestrales, es posible que desees crear un libro de trabajo con hojas que contengan los mismos encabezados de columna, encabezados de fila y fórmulas. Existe una forma de hacer esto: creando una hoja y luego copiándola.

Aspose.Cells admite copiar y mover hojas de cálculo dentro o entre libros. Las hojas de cálculo, completas con datos, formatos, tablas, matrices, gráficos, imágenes y otros objetos, se copian con el mayor grado de precisión.

{{% /alert %}} 
## **Mover o Copiar Hojas usando Microsoft Excel**
Los siguientes son los pasos involucrados en copiar y mover hojas de cálculo dentro o entre libros.

1. Abra el libro que recibirá las hojas.
1. Cambia al libro de trabajo que contiene las hojas que deseas mover o copiar, y luego selecciona las hojas.
3. En el menú **Editar**, haga clic en **Mover o copiar hoja**.
1. En el cuadro Libro, haga clic en el libro que recibirá las hojas.
5. Para mover o copiar las hojas seleccionadas a un nuevo libro, haga clic en **nuevo libro**.
6. En el cuadro **Antes de la hoja**, haga clic en la hoja antes de la cual desea insertar las hojas movidas o copiadas.
7. Para copiar las hojas en lugar de moverlas, seleccione la casilla de verificación **Crear una copia**.
### **Copiar Hojas de Cálculo dentro de un Libro de Trabajo**
Aspose.Cells proporciona un método sobrecargado [WorksheetCollection.addCopy()](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#addCopy\(int\)) que se utiliza para copiar una hoja de cálculo existente. Una versión del método toma el índice de la hoja de cálculo fuente como parámetro. La otra versión toma el nombre de la hoja de cálculo fuente.

El siguiente ejemplo muestra cómo copiar una hoja de trabajo existente dentro de un libro.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWithinWorkbook.py" >}}
### **Copiar Hojas de Cálculo entre Libros de Trabajo**
Aspose.Cells proporciona el método [Worksheet.copy()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#copy\(com.aspose.cells.Worksheet\)) utilizado para copiar hojas de cálculo a otros libros. El método toma el objeto de hoja de cálculo fuente como parámetro.

El siguiente ejemplo muestra cómo copiar una hoja de cálculo de un libro a otro libro.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWorksheetsBetweenWorkbooks.py" >}}
### **Mover Hojas de Cálculo dentro de un Libro de Trabajo**
Aspose.Cells proporciona el método [Worksheet.moveTo()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#moveTo\(int\)) utilizado para mover una hoja de cálculo a otra ubicación en la misma hoja de cálculo.

El siguiente ejemplo muestra cómo mover una hoja de cálculo a otra ubicación dentro del libro.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-MoveWorksheet.py" >}}
