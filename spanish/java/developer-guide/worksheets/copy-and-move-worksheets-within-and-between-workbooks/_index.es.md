---
title: Copiar y Mover Hojas de Cálculo Dentro y Entre Libros de Excel
type: docs
weight: 20
url: /es/java/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

A veces, necesitas varias hojas de cálculo con formato y entradas de datos comunes. Por ejemplo, si trabajas con presupuestos trimestrales, es posible que desees crear un libro con hojas que contengan los mismos encabezados de columna, encabezados de fila y fórmulas. Existe una manera de hacerlo: creando una hoja y luego copiándola tres veces.

Aspose.Cells admite la copia o el movimiento de hojas de cálculo dentro o entre libros de Excel. Las hojas de cálculo, incluidos datos, formato, tablas, matrices, gráficos, imágenes y otros objetos, se copian con el más alto grado de precisión.

{{% /alert %}}

## **Copiar y mover hojas de cálculo**

Este artículo explica cómo utilizar Aspose.Cells para:

- [Copiar una hoja de cálculo dentro de un libro](/cells/es/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook).
- [Mover una hoja de cálculo dentro de un libro](/cells/es/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook).
- [Copiar una hoja de cálculo entre libros](/cells/es/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks).
- [Mover una hoja de cálculo entre libros](/cells/es/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks).

### **Copiando una Hoja de Cálculo dentro de un Libro**

Los pasos iniciales son los mismos para todos los ejemplos.

1. Crear dos libros con algunos datos en Microsoft Excel. Para este ejemplo, creamos dos nuevos libros en Microsoft Excel e introducimos algunos datos en las hojas de cálculo.

- FirstWorkbook.xls (3 hojas de cálculo)
- SecondWorkbook.xls (1 hoja de cálculo)

  **FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. Descargue e instale Aspose.Cells:
   1. [Descargar Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
   1. Descomprímelo en tu computadora de desarrollo.
      Todos los componentes [Aspose](http://www.aspose.com/), cuando se instalan, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.
1. Cree un proyecto:
   1. Crear un proyecto usando un editor de Java como Eclipse o crear un programa simple usando un editor de texto.
1. Agregar una ruta de clase:
   1. Extrae Aspose.Cells.jar y dom4j_1.6.1.jar de Aspose.Cells.zip.
   1. Configura la ruta de clase del proyecto en Eclipse:
      1. Selecciona tu proyecto en Eclipse y haz clic en los menús **Proyecto**, luego **Propiedades**.
      1. Selecciona **Ruta de compilación de Java** en el lado izquierdo del cuadro de diálogo, luego selecciona la pestaña de Bibliotecas.
      1. Haz clic en **Agregar JARs** o **Agregar JARs Externos** para seleccionar Aspose.Cells.jar y dom4j_1.6.1.jar y añádelos a las rutas de compilación.

{{% alert color="primary" %}}

O puedes configurar la ruta de clases en tiempo de ejecución en un símbolo del sistema en Windows.
Por ejemplo:

{{< highlight java >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. Copiar hoja de cálculo dentro de un libro:
   A continuación se muestra el código utilizado para realizar la tarea. Copia la hoja de cálculo Copiar dentro de PrimerLibro.xls.

Ejecutar el código mueve la hoja de cálculo denominada Copiar dentro de PrimerLibro.xls con el nuevo nombre Última Hoja.

Archivo de salida

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **Moviendo una hoja de cálculo dentro de un libro**

A continuación se muestra el código utilizado para realizar la tarea.

Ejecutar el código mueve la hoja de cálculo Mover desde el índice 1 al índice 2 en PrimerLibro.xls.

Archivo de salida

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **Copiando una hoja de cálculo entre libros**

Ejecutar el código copia la hoja de cálculo Copiar a SegundoLibro.xls con el nuevo nombre Hoja2.

Archivo de salida

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **Moviendo una hoja de cálculo entre libros**

Ejecutar el código mueve la hoja de cálculo mover de PrimerLibro.xls a SegundoLibro.xls con el nuevo nombre Hoja3.

**Salida PrimerLibro.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**Salida SegundoLibro.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **Conclusión**

{{% alert color="primary" %}}

Este artículo explica cómo copiar y mover hojas de cálculo dentro y entre libros de trabajo utilizando Aspose.Cells.

Aspose.Cells ha se ha beneficiado de años de investigación, diseño y ajuste cuidadoso. Agradecemos sus consultas, comentarios y sugerencias en el [Foro de Aspose.Cells](https://forum.aspose.com/c/cells/9). Garantizamos una respuesta rápida.

{{% /alert %}}
