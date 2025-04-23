---
title: Copiar y mover hojas de cálculo
type: docs
weight: 10
url: /es/go-cpp/copying-and-moving-worksheets/
---

{{% alert color="primary" %}}

A veces, necesitas varias hojas de cálculo con formato y datos comunes. Por ejemplo, si trabajas con presupuestos trimestrales, es posible que desees crear un libro de trabajo con hojas que contengan los mismos encabezados de columna, encabezados de fila y fórmulas. Existe una forma de hacer esto: creando una hoja y luego copiándola.

Aspose.Cells admite la copia y movimiento de hojas de cálculo dentro o entre libros de trabajo. Una hoja de cálculo, completa con datos, formato, tablas, matrices, gráficos, imágenes y otros objetos, se copian con el más alto grado de precisión.

{{% /alert %}}

## **Mover o Copiar Hojas usando Microsoft Excel**

Los siguientes son los pasos involucrados en copiar y mover hojas de cálculo dentro o entre libros de trabajo en Microsoft Excel.

1. Para mover o copiar hojas a otro libro de trabajo, abre el libro de trabajo que recibirá las hojas.
1. Cambia al libro de trabajo que contiene las hojas que deseas mover o copiar, y luego selecciona las hojas.
1. En el menú **Editar**, haga clic en **Mover o copiar hoja**.
1. En el cuadro de diálogo **Hacia el libro**, haga clic en el libro que recibirá las hojas.
1. Para mover o copiar las hojas seleccionadas a un nuevo libro de trabajo, haga clic en **Nuevo libro**.
1. En el cuadro **Antes de la hoja**, haga clic en la hoja antes de la cual desea insertar las hojas movidas o copiadas.
1. Para copiar las hojas en lugar de moverlas, seleccione la casilla **Crear una copia**.

### **Copiar hojas de cálculo dentro de un libro con Aspose.Cells**

Aspose.Cells proporciona un método sobrecargado [AddCopy()](https://reference.aspose.com/cells/go-cpp/worksheetcollection/addcopy_string/) que se usa para agregar una hoja de cálculo a la colección y copiar datos de una hoja existente. Una versión del método toma el índice de la hoja de origen como parámetro. La otra versión toma el nombre de la hoja de origen. El siguiente ejemplo muestra cómo copiar una hoja de cálculo existente dentro de un libro de trabajo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyWorksheetsWithinWorkbook.go" >}}

### **Mover Hojas de Cálculo dentro de un Libro de Trabajo**

Aspose.Cells proporciona un método [MoveTo()](https://reference.aspose.com/cells/go-cpp/worksheet/moveto/) que se usa para mover una hoja de cálculo a otra ubicación en la misma hoja de cálculo. El método toma el índice de la hoja de destino como parámetro. El siguiente ejemplo muestra cómo mover una hoja de cálculo a otra ubicación dentro del libro de trabajo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MoveWorksheetsWithinWorkbook.go" >}}
