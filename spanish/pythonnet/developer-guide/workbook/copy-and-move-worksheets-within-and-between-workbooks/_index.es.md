---
title: Copiar y Mover Hojas de Cálculo Dentro y Entre Libros de Excel
type: docs
weight: 80
url: /es/python-net/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

A veces, necesitas varias hojas de cálculo con formato y entradas de datos comunes. Por ejemplo, si trabajas con presupuestos trimestrales, es posible que desees crear un libro con hojas que contengan los mismos encabezados de columna, encabezados de fila y fórmulas. Existe una manera de hacerlo: creando una hoja y luego copiándola tres veces.

Aspose.Cells para Python via .NET soporta copiar o mover hojas de trabajo dentro o entre libros de trabajo. Las hojas de trabajo, incluyendo datos, formatos, tablas, matrices, gráficos, imágenes y otros objetos, se copian con el mayor nivel de precisión posible.

{{% /alert %}}

## **Copiar y mover hojas de cálculo**

### **Copiando una Hoja de Cálculo dentro de un Libro**

Los pasos iniciales son los mismos para todos los ejemplos.

1. Crear dos libros con algunos datos en Microsoft Excel. Para este ejemplo, creamos dos nuevos libros en Microsoft Excel e introducimos algunos datos en las hojas de cálculo.

 - FirstWorkbook.xlsx (3 hojas de cálculo).
- SecondWorkbook.xlsx (1 hoja de cálculo).

1. Descargue e instale Aspose.Cells para Python via .NET:
   1. [Descargar Aspose.Cells para Python via .NET](https://downloads.aspose.com/cells/python-net).
   1. Instálelo en su equipo de desarrollo.
      Todos los componentes [Aspose](http://www.aspose.com/), cuando se instalan, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.
1. Cree un proyecto y agregue referencias:   
1. Copia la hoja de cálculo dentro de un libro de trabajo.
   El primer ejemplo copia la primera hoja de cálculo (Copia) dentro de FirstWorkbook.xlsx.

Al ejecutar el código, se copia la hoja llamada Copia dentro de FirstWorkbook.xlsx con el nombre Última Hoja.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheets.py" >}}

### **Moviendo una Hoja de Cálculo dentro de un Libro de Trabajo**

El siguiente código muestra cómo mover una hoja de cálculo desde una posición a otra en un libro de trabajo. Al ejecutar el código, se mueve la hoja llamada Mover del índice 1 al índice 2 en FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheets.py" >}}

### **Copiando una hoja de cálculo entre libros**

Al ejecutar el código, se copia la hoja llamada Copia en SecondWorkbook.xlsx con el nombre Hoja2.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.py" >}}

### **Moviendo una hoja de cálculo entre libros**

Al ejecutar el código se mueve la hoja llamada Mover de FirstWorkbook.xlsx a SecondWorkbook.xlsx con el nombre Hoja3.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.py" >}}
{{< app/cells/assistant language="python-net" >}}
