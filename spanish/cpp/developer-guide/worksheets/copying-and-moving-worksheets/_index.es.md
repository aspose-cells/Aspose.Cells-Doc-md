---
title: Copiar y mover hojas de trabajo
type: docs
weight: 10
url: /es/cpp/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

A veces, necesita varias hojas de trabajo con formato y datos comunes. Por ejemplo, si trabaja con presupuestos trimestrales, es posible que desee crear un libro de trabajo con hojas que contengan los mismos encabezados de columna, encabezados de fila y fórmulas. Hay una manera de hacer esto: creando una hoja y luego copiándola.

Aspose.Cells admite copiar y mover hojas de trabajo dentro o entre libros de trabajo. Una hoja de trabajo, completa con datos, formato, tablas, matrices, gráficos, imágenes y otros objetos, se copian con el más alto grado de precisión.

{{% /alert %}} 
## **Mover o copiar hojas usando Microsoft Excel**
Los siguientes son los pasos necesarios para copiar y mover hojas de trabajo dentro o entre libros de trabajo en Microsoft Excel.

1. Para mover o copiar hojas a otro libro, abra el libro que recibirá las hojas.
1. Cambie al libro de trabajo que contiene las hojas que desea mover o copiar y luego seleccione las hojas.
1.  Sobre el**Editar** menú, haga clic**Mover o copiar hoja**.
1.  En el**Reservar** cuadro de diálogo, haga clic en el libro de trabajo para recibir las hojas.
1.  Para mover o copiar las hojas seleccionadas a un nuevo libro, haga clic en**Nuevo libro**.
1.  En el**antes de la hoja** cuadro, haga clic en la hoja antes de la cual desea insertar las hojas movidas o copiadas.
1.  Para copiar las hojas en lugar de moverlas, seleccione la**crear una copia** caja.
### **Copie hojas de trabajo dentro de un libro de trabajo con Aspose.Cells**
 Aspose.Cells proporciona un método sobrecargado[AgregarCopia()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa1e73c54ea19bb7aa0f9f197c2baa5ba)que se utiliza para agregar una hoja de trabajo a la colección y copiar datos de una hoja de trabajo existente. Una versión del método toma el índice de la hoja de cálculo de origen como parámetro. La otra versión toma el nombre de la hoja de trabajo de origen. El siguiente ejemplo muestra cómo copiar una hoja de trabajo existente dentro de un libro de trabajo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook.cpp" >}}
### **Mover hojas de trabajo dentro del libro de trabajo**
 Aspose.Cells proporciona un método[Mover a()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a240bf1d3d52ea8c8bfd54ffa320921b7)que se utiliza para mover una hoja de trabajo a otra ubicación en la misma hoja de cálculo. El método toma el índice de la hoja de cálculo de destino como parámetro. El siguiente ejemplo muestra cómo mover una hoja de trabajo a otra ubicación dentro del libro de trabajo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook.cpp" >}}
