---
title: Copiar y mover hojas de trabajo dentro y entre libros de trabajo
type: docs
weight: 20
url: /es/java/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

A veces, necesita varias hojas de trabajo con formato y entrada de datos comunes. Por ejemplo, si trabaja con presupuestos trimestrales, es posible que desee crear un libro de trabajo con hojas que contengan los mismos encabezados de columna, encabezados de fila y fórmulas. Hay una manera de hacer esto: creando una hoja y luego copiándola tres veces.

Aspose.Cells admite copiar o mover hojas de trabajo dentro o entre libros de trabajo. Las hojas de trabajo que incluyen datos, formato, tablas, matrices, gráficos, imágenes y otros objetos se copian con el mayor grado de precisión.

{{% /alert %}}

## **Copiar y mover hojas de trabajo**

Este artículo explica cómo usar Aspose.Cells para:

- [Copiar una hoja de trabajo dentro de un libro de trabajo](/cells/es/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook).
- [Mover una hoja de trabajo dentro de un libro de trabajo](/cells/es/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook).
- [Copiar una hoja de cálculo entre libros](/cells/es/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks).
- [Mover una hoja de cálculo entre libros](/cells/es/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks).

### **Copiar una hoja de trabajo dentro de un libro de trabajo**

Los pasos iniciales son los mismos para todos los ejemplos.

1. Cree dos libros de trabajo con algunos datos en Microsoft Excel. A los efectos de este ejemplo, creamos dos nuevos libros de trabajo en Microsoft Excel e ingresamos algunos datos en las hojas de trabajo.

- FirstWorkbook.xls (3 hojas de trabajo)
- SecondWorkbook.xls (1 hoja de trabajo).

  **FirstWorkbook.xls**

![todo:imagen_alternativa_texto](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![todo:imagen_alternativa_texto](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. Descargar e instalar Aspose.Cells:
   1. [Descargar Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
 1. Descomprímalo en su computadora de desarrollo.
 Todos[Aspose](http://www.aspose.com/) Los componentes, cuando están instalados, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inyecta marcas de agua en los documentos producidos.
1. Crear un proyecto:
 1. Cree un proyecto usando un editor Java como Eclipse o cree un programa simple usando un editor de texto.
1. Agregue una ruta de clase:
1. Extraiga Aspose.Cells.jar y dom4j_1.6.1.jar de Aspose.Cells.zip.
 1. Establezca el classpath del proyecto en Eclipse:
 1. Seleccione su proyecto en Eclipse y haga clic en los menús**Proyecto** , después**Propiedades**.
 1. Seleccione**Java Ruta de construcción** en el lado izquierdo del cuadro de diálogo, luego seleccione la pestaña Bibliotecas,
 1. Haga clic en**Agregar JAR** o**Agregar JAR externos** para seleccionar Aspose.Cells.jar y dom4j_1.6.1.jar y agregarlos a las rutas de compilación.

{{% alert color="primary" %}}

O puede configurar el classpath en tiempo de ejecución en un indicador de DOS en Windows.
Por ejemplo:

{{< highlight "java" >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. Copie la hoja de trabajo dentro de un libro de trabajo:
 continuación se muestra el código utilizado por para realizar la tarea. Copia la hoja de trabajo Copiar dentro de FirstWorkbook.xls.

Al ejecutar el código, se mueve la hoja de trabajo denominada Copia dentro de FirstWorkbook.xls con el nuevo nombre Última hoja.

**Archivo de salida**

![todo:imagen_alternativa_texto](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **Mover una hoja de trabajo dentro de un libro de trabajo**

A continuación se muestra el código utilizado para realizar la tarea.

Ejecutar el código mueve la hoja de cálculo Mover del índice 1 al índice 2 en FirstWorkbook.xls.

**Archivo de salida**

![todo:imagen_alternativa_texto](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **Copiar una hoja de trabajo entre libros de trabajo**

Al ejecutar el código, se copia la hoja de cálculo Copiar en SecondWorkbook.xls con el nuevo nombre Hoja2.

**Archivo de salida**

![todo:imagen_alternativa_texto](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **Mover una hoja de trabajo entre libros de trabajo**

Ejecutar el código mueve la hoja de trabajo de movimiento de FirstWorkbook.xls a SecondWorkbook.xls con el nuevo nombre Sheet3.

**Salida FirstWorkbook.xls**

![todo:imagen_alternativa_texto](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**Salida SecondWorkbook.xls**

![todo:imagen_alternativa_texto](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **Conclusión**

{{% alert color="primary" %}}

Este artículo explica cómo copiar y mover hojas de trabajo dentro y entre libros de trabajo usando Aspose.Cells.

 Aspose.Cells se ha beneficiado de años de investigación, diseño y ajuste cuidadoso. Agradecemos sus consultas, comentarios y sugerencias en[Aspose.Cells Foro](https://forum.aspose.com/c/cells/9). Garantizamos una pronta respuesta.

{{% /alert %}}
