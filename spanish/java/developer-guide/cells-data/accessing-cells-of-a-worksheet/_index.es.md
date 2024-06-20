---
title: Acceso a las Celdas de una Hoja de Cálculo
type: docs
weight: 10
url: /es/java/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

Sabemos que todas las hojas de cálculo pueden contener datos que básicamente se almacenan en celdas (con las que está compuesta una hoja de cálculo). Una celda es una parte básica de una hoja de cálculo que se utiliza para construir toda la hoja de cálculo como una secuencia de filas y columnas. Antes de intentar acceder a los datos de una hoja de cálculo, necesitaríamos acceder a sus celdas. Por lo tanto, en este tema, discutiremos algunos enfoques básicos para acceder a las celdas de la hoja de cálculo en tiempo de ejecución utilizando Aspose.Cells.

{{% /alert %}} 
## **Accediendo a las celdas**
Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una colección [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) proporciona una colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) que representa todas las celdas de la hoja de cálculo.

Podemos usar la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) para acceder a las celdas en una hoja de cálculo. Aspose.Cells proporciona diferentes enfoques básicos para acceder a las celdas:

1. [Usar el nombre de la celda](/cells/es/java/acceso-a-las-celdas-de-una-hoja-de-cálculo/).
1. [Usar el índice de fila y columna](/cells/es/java/acceso-a-las-celdas-de-una-hoja-de-cálculo/).
### **Usando el nombre de la celda**
Los desarrolladores pueden acceder a cualquier celda específica pasando su nombre de celda a la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) de la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).

Si crea una hoja de cálculo en blanco al principio, el recuento de la colección de [Celdas](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) es cero. Cuando utiliza este enfoque para acceder a una celda, verificará si esta celda existe en la colección o no. Si es así, devuelve el objeto de celda en la colección; de lo contrario, crea un nuevo objeto [Celda](https://reference.aspose.com/cells/java/com.aspose.cells/Cell), agrega el objeto a la colección de [Celdas](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) y luego devuelve el objeto. Este enfoque es la forma más sencilla de acceder a la celda si está familiarizado con Microsoft Excel, pero es más lento que otros enfoques.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **Usando el índice de fila y columna de la celda**
Los desarrolladores pueden acceder a una celda específica pasando los índices de su fila y columna a la colección de [Celdas](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) de la clase [Hoja de Cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).

Este enfoque funciona de la misma manera que el primer enfoque.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **Artículos relacionados**
{{% alert color="primary" %}} 

- [Rangos nombrados](/cells/es/java/named-ranges/)

{{% /alert %}} 
## **Acceso al rango de visualización máxima de la hoja de cálculo**
Aspose.Cells permite a los desarrolladores acceder al rango de visualización máximo de una hoja de cálculo. El rango de visualización máximo - el rango de celdas entre la primera y la última celda con contenido - es útil cuando necesitas copiar, seleccionar o mostrar todo el contenido de una hoja de cálculo en una imagen.

Puede acceder al rango de visualización máxima de una hoja de cálculo utilizando [Worksheet.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange).

En la figura siguiente, el rango de visualización máxima de la hoja de cálculo seleccionada es A1:G15.

**Mostrando el rango de visualización máxima de esta hoja de cálculo** 

![todo:image_alt_text](accessing-cells-of-a-worksheet_1.png)

El siguiente código de ejemplo ilustra cómo acceder a la propiedad [MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange). El código genera la siguiente salida.

{{< highlight java >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
