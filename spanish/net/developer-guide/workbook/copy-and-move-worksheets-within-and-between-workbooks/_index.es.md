---
title: Copiar y mover hojas de trabajo dentro y entre libros de trabajo
type: docs
weight: 80
url: /es/net/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

A veces, necesita varias hojas de trabajo con formato y entrada de datos comunes. Por ejemplo, si trabaja con presupuestos trimestrales, es posible que desee crear un libro de trabajo con hojas que contengan los mismos encabezados de columna, encabezados de fila y fórmulas. Hay una manera de hacer esto: creando una hoja y luego copiándola tres veces.

Aspose.Cells admite copiar o mover hojas de trabajo dentro o entre libros de trabajo. Las hojas de trabajo que incluyen datos, formato, tablas, matrices, gráficos, imágenes y otros objetos se copian con el mayor grado de precisión.

{{% /alert %}}

## **Copiar y mover hojas de trabajo**

### **Copiar una hoja de trabajo dentro de un libro de trabajo**

Los pasos iniciales son los mismos para todos los ejemplos.

1. Cree dos libros de trabajo con algunos datos en Microsoft Excel. A los efectos de este ejemplo, creamos dos nuevos libros de trabajo en Microsoft Excel e ingresamos algunos datos en las hojas de trabajo.

- FirstWorkbook.xlsx (3 hojas de trabajo).
- SecondWorkbook.xlsx (1 hoja de trabajo).

1. Descargar e instalar Aspose.Cells:
   1. [Descargar Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
 1. Instálelo en su computadora de desarrollo.
 Todos[Aspose](http://www.aspose.com/) Los componentes, cuando están instalados, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inyecta marcas de agua en los documentos producidos.
1. Crear un proyecto:
 1. Inicie Visual Studio.Net.
 1. Cree una nueva aplicación de consola.
1. Añadir referencias:
 1. Agregue una referencia a Aspose.Cells al proyecto.
 Por ejemplo, agregue una referencia a ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Copie la hoja de trabajo dentro de un libro de trabajo
 El primer ejemplo copia la primera hoja de trabajo (Copiar) dentro de FirstWorkbook.xlsx.

Al ejecutar el código, la hoja de cálculo denominada Copiar se copia dentro de FirstWorkbook.xlsx con el nombre Última hoja.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheets.cs" >}}

### **Mover una hoja de trabajo dentro de un libro de trabajo**

El siguiente código muestra cómo mover una hoja de cálculo de una posición en un libro de trabajo a otra. Al ejecutar el código, se mueve la hoja de trabajo llamada Mover del índice 1 al índice 2 en FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheets.cs" >}}

### **Copiar una hoja de trabajo entre libros de trabajo**

Al ejecutar el código, se copia la hoja de trabajo denominada Copiar en SecondWorkbook.xlsx con el nombre Hoja2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.cs" >}}

### **Mover una hoja de trabajo entre libros de trabajo**

Al ejecutar el código, se mueve la hoja de trabajo llamada Move from FirstWorkbook.xlsx a SecondWorkbook.xlsx con el nombre Sheet3.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.cs" >}}
