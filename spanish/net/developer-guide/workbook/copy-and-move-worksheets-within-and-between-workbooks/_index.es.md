---
title: Copiar y Mover Hojas de Cálculo Dentro y Entre Libros de Excel
type: docs
weight: 80
url: /es/net/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

A veces, necesitas varias hojas de cálculo con formato y entradas de datos comunes. Por ejemplo, si trabajas con presupuestos trimestrales, es posible que desees crear un libro con hojas que contengan los mismos encabezados de columna, encabezados de fila y fórmulas. Existe una manera de hacerlo: creando una hoja y luego copiándola tres veces.

Aspose.Cells admite la copia o el movimiento de hojas de cálculo dentro o entre libros de Excel. Las hojas de cálculo, incluidos datos, formato, tablas, matrices, gráficos, imágenes y otros objetos, se copian con el más alto grado de precisión.

{{% /alert %}}

## **Copiar y mover hojas de cálculo**

### **Copiando una Hoja de Cálculo dentro de un Libro**

Los pasos iniciales son los mismos para todos los ejemplos.

1. Crear dos libros con algunos datos en Microsoft Excel. Para este ejemplo, creamos dos nuevos libros en Microsoft Excel e introducimos algunos datos en las hojas de cálculo.

 - FirstWorkbook.xlsx (3 hojas de cálculo).
- SecondWorkbook.xlsx (1 hoja de cálculo).

1. Descargue e instale Aspose.Cells:
   1. [Descargar Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
   1. Instálelo en su equipo de desarrollo.
      Todos los componentes [Aspose](http://www.aspose.com/), cuando se instalan, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.
1. Cree un proyecto:
   1. Inicia Visual Studio.Net.
   1. Cree una nueva aplicación de consola.
1. Agregue referencias:
   1. Agrega una referencia a Aspose.Cells al proyecto.
      Por ejemplo, agrega una referencia a ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Copia la hoja de cálculo dentro de un libro de trabajo.
   El primer ejemplo copia la primera hoja de cálculo (Copia) dentro de FirstWorkbook.xlsx.

Al ejecutar el código, se copia la hoja llamada Copia dentro de FirstWorkbook.xlsx con el nombre Última Hoja.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheets.cs" >}}

### **Moviendo una Hoja de Cálculo dentro de un Libro de Trabajo**

El siguiente código muestra cómo mover una hoja de cálculo desde una posición a otra en un libro de trabajo. Al ejecutar el código, se mueve la hoja llamada Mover del índice 1 al índice 2 en FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheets.cs" >}}

### **Copiando una hoja de cálculo entre libros**

Al ejecutar el código, se copia la hoja llamada Copia en SecondWorkbook.xlsx con el nombre Hoja2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.cs" >}}

### **Moviendo una hoja de cálculo entre libros**

Al ejecutar el código se mueve la hoja llamada Mover de FirstWorkbook.xlsx a SecondWorkbook.xlsx con el nombre Hoja3.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.cs" >}}
