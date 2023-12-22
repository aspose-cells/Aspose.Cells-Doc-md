---
title: Copiar y mover hojas de trabajo
type: docs
weight: 10
url: /es/cpp/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

A veces, necesita varias hojas de trabajo con datos y formatos comunes. Por ejemplo, si trabaja con presupuestos trimestrales, es posible que desee crear un libro con hojas que contengan los mismos encabezados de columna, encabezados de fila y fórmulas. Hay una manera de hacer esto: creando una hoja y luego copiándola.

Aspose.Cells admite copiar y mover hojas de trabajo dentro o entre libros. Una hoja de trabajo, completa con datos, formato, tablas, matrices, gráficos, imágenes y otros objetos, se copia con el más alto grado de precisión.

{{% /alert %}} 
##  **Mover o copiar hojas usando Microsoft Excel**
Los siguientes son los pasos necesarios para copiar y mover hojas de trabajo dentro o entre libros en Microsoft Excel.

1. Para mover o copiar hojas a otro libro, abra el libro que recibirá las hojas.
1. Cambie al libro que contiene las hojas que desea mover o copiar y luego seleccione las hojas.
1.  Sobre el**Editar** menú, haga clic en *Mover o copiar hoja**.
1. En el**Reservar** cuadro de diálogo, haga clic en el libro para recibir las hojas.
1. Para mover o copiar las hojas seleccionadas a un nuevo libro, haga clic en *Nuevo libro**.
1. En el**Antes de la hoja** , haga clic en la hoja delante de la cual desea insertar las hojas movidas o copiadas.
1.  Para copiar las hojas en lugar de moverlas, seleccione el**crear una copia** caja.
###  **Copie hojas de trabajo dentro de un libro de trabajo con Aspose.Cells**
 Aspose.Cells proporciona un método sobrecargado[AddCopy()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/addcopy/)que se utiliza para agregar una hoja de trabajo a la colección y copiar datos de una hoja de trabajo existente. Una versión del método toma el índice de la hoja de trabajo fuente como parámetro. La otra versión toma el nombre de la hoja de trabajo fuente. El siguiente ejemplo muestra cómo copiar una hoja de trabajo existente dentro de un libro de trabajo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook-new.cpp" >}}
###  **Mover hojas de trabajo dentro del libro de trabajo**
 Aspose.Cells proporciona un método[MoveTo()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/moveto/)que se utiliza para mover una hoja de cálculo a otra ubicación en la misma hoja de cálculo. El método toma el índice de la hoja de trabajo de destino como parámetro. El siguiente ejemplo muestra cómo mover una hoja de trabajo a otra ubicación dentro del libro.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook-new.cpp" >}}
