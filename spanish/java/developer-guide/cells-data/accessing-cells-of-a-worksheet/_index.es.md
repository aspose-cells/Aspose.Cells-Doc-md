---
title: Acceso a Cells de una hoja de trabajo
type: docs
weight: 10
url: /es/java/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Sabemos que todas las hojas de cálculo pueden contener datos que básicamente se almacenan en celdas (con las que se compone una hoja de cálculo). Una celda es una parte básica de una hoja de trabajo que se utiliza para construir la hoja de trabajo completa como una secuencia de filas y columnas. Antes de intentar acceder a los datos de una hoja de trabajo, necesitaríamos acceder a sus celdas. Entonces, en este tema, discutiremos algunos enfoques básicos para acceder a las celdas de la hoja de trabajo en tiempo de ejecución usando Aspose.Cells.

{{% /alert %}} 
## **Accediendo al Cells**
 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Excel Microsoft. Él[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) clase. Él[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la clase proporciona un[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)colección que representa todas las celdas de la hoja de trabajo.

 Podemos usar el[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)colección para acceder a las celdas de una hoja de trabajo. Aspose.Cells proporciona diferentes enfoques básicos para acceder a las celdas:

1. [Usando el nombre de la celda](/cells/es/java/accessing-cells-of-a-worksheet/).
1. [Usando el índice de fila y columna](/cells/es/java/accessing-cells-of-a-worksheet/).
### **Usando Cell Nombre**
 Los desarrolladores pueden acceder a cualquier celda específica pasando su nombre de celda al[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) colección de la[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)clase.

 Si crea una hoja de cálculo en blanco al principio, el recuento de[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)la recaudación es cero. Cuando utiliza este enfoque para acceder a una celda, verificará si esta celda existe en la colección o no. En caso afirmativo, devuelve el objeto de celda en la colección; de lo contrario, crea una nueva[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) objeto, añade el objeto al[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)colección y luego devuelve el objeto. Este enfoque es la forma más fácil de acceder a la celda si está familiarizado con Microsoft Excel, pero es más lento que otros enfoques.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **Uso del índice de filas y columnas del Cell**
 Los desarrolladores pueden acceder a cualquier celda específica pasando los índices de su fila y columna al[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) colección de la[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)clase.

Este enfoque funciona de la misma manera que el primer enfoque.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **Artículos relacionados**
{{% alert color="primary" %}} 

- [Rangos con nombre](/cells/es/java/named-ranges/)

{{% /alert %}} 
## **Acceso al rango máximo de visualización de la hoja de trabajo**
Aspose.Cells permite a los desarrolladores acceder al rango máximo de visualización de una hoja de trabajo. El rango de visualización máximo, el rango de celdas entre la primera y la última celda con contenido, es útil cuando necesita copiar, seleccionar o mostrar todo el contenido de una hoja de trabajo en una imagen.

 Puede acceder al rango máximo de visualización de una hoja de trabajo usando[Hoja de trabajo.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange).

En la siguiente figura, el rango máximo de visualización de la hoja de cálculo seleccionada es A1:G15.

**Mostrando el rango máximo de visualización de esta hoja de cálculo** 

![todo:imagen_alternativa_texto](accessing-cells-of-a-worksheet_1.png)

 El siguiente código de ejemplo ilustra cómo acceder a la[MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange)propiedad. El código genera el siguiente resultado.

{{< highlight "java" >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
