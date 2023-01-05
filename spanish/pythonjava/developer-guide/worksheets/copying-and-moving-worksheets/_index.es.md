---
title: Copiar y mover hojas de trabajo
type: docs
weight: 20
url: /es/python-java/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

A veces, necesita varias hojas de trabajo con formato y datos comunes. Por ejemplo, si trabaja con presupuestos trimestrales, es posible que desee crear un libro de trabajo con hojas que contengan los mismos encabezados de columna, encabezados de fila y fórmulas. Hay una manera de hacer esto: creando una hoja y luego copiándola.

Aspose.Cells admite copiar y mover hojas de trabajo dentro o entre libros de trabajo. Las hojas de trabajo, completas con datos, formato, tablas, matrices, gráficos, imágenes y otros objetos, se copian con el mayor grado de precisión.

{{% /alert %}} 
## **Mover o copiar hojas usando Microsoft Excel**
Los siguientes son los pasos necesarios para copiar y mover hojas de trabajo dentro o entre libros de trabajo.

1. Abra el libro de trabajo que recibirá las hojas.
1. Cambie al libro de trabajo que contiene las hojas que desea mover o copiar y luego seleccione las hojas.
1. Sobre el**Editar**menú, haga clic**Mover o copiar hoja**.
1. En el cuadro Para reservar, haga clic en el libro de trabajo para recibir las hojas.
1. Para mover o copiar las hojas seleccionadas a un nuevo libro, haga clic en**Nuevo libro**.
1. En el**antes de la hoja**cuadro, haga clic en la hoja antes de la cual desea insertar las hojas movidas o copiadas.
1. Para copiar las hojas en lugar de moverlas, seleccione la**crear una copia**caja.
### **Copiar hojas de trabajo dentro de un libro de trabajo**
Aspose.Cells proporciona una sobrecarga[WorksheetCollection.addCopy()](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#addCopy\(int\)) método que se utiliza para copiar una hoja de cálculo existente. Una versión del método toma el índice de la hoja de cálculo de origen como parámetro. La otra versión toma el nombre de la hoja de trabajo de origen.

El siguiente ejemplo muestra cómo copiar una hoja de trabajo existente dentro de un libro de trabajo.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWithinWorkbook.py" >}}
### **Copiar hojas de trabajo entre libros de trabajo**
Aspose.Cells proporciona el[Hoja de trabajo.copia()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#copy\(com.aspose.cells.Worksheet\)) método utilizado para copiar hojas de cálculo a otros libros. El método toma el objeto de la hoja de cálculo de origen como parámetro.

El siguiente ejemplo muestra cómo copiar una hoja de trabajo de un libro de trabajo a otro libro de trabajo.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWorksheetsBetweenWorkbooks.py" >}}
### **Mover hojas de trabajo dentro del libro de trabajo**
Aspose.Cells proporciona el[Hoja de trabajo.moveTo()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#moveTo\(int\)) método utilizado para mover una hoja de trabajo a otra ubicación en la misma hoja de cálculo.

El siguiente ejemplo muestra cómo mover una hoja de trabajo a otra ubicación dentro del libro de trabajo.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-MoveWorksheet.py" >}}
