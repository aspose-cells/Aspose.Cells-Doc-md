---
title: Copiar filas y columnas de GridWeb
type: docs
weight: 80
url: /es/net/copy-gridweb-rows-and-columns/
---
{{% alert color="primary" %}} 

 Aspose.Cells. El componente GridWeb ofrece los medios para copiar filas y columnas mientras usa la clase GridCells. Este artículo demuestra el uso de las API expuestas por Aspose.Cells.GridWeb para copiar filas y columnas en la interfaz de GridWeb.

Los métodos GridCells.CopyRow, GridCells.CopyColumn, GridCells.CopyRows y GridCells.CopyColumns copiarán el contenido, el estilo y las fórmulas de la fila y columna de origen al destino.

{{% /alert %}} 
## **Copiar filas y columnas**
 Si aún no está familiarizado con el componente Aspose.Cells.GridWeb, le recomendamos encarecidamente que consulte el[Introducción a Aspose.Cells.GridWeb](https://docs.aspose.com/cells/net/browsers-capabilities/) y artículo detallado sobre[Cómo agregar el componente Aspose.Cells.GridWeb en una aplicación WebForms](https://docs.aspose.com/cells/net/add-gridweb-to-web-form/).
### **Copiar una sola fila**
Para simplificar el ejemplo, el artículo utiliza una hoja de cálculo existente con una fila y una fórmula simple que suma todos los valores de la fila. Así es como se muestra la hoja de cálculo en la interfaz Aspose.Cells.GridWeb antes de copiar la fila.

![todo:imagen_alternativa_texto](copy-gridweb-rows-and-columns_1.png)

El fragmento de código es simple, como se demuestra a continuación. Accede al objeto GridCells del orden de la hoja de trabajo activa para hacer una copia de la primera fila a la fila siguiente.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


Así es como se ve Aspose.Cells.GridWeb después de la operación de copia de fila.

![todo:imagen_alternativa_texto](copy-gridweb-rows-and-columns_2.png)
### **Copiar una sola columna**
El siguiente ejemplo utiliza una hoja de cálculo existente con una columna y una fórmula simple que suma todos los valores de la columna. Así es como se muestra la hoja de cálculo en la interfaz Aspose.Cells.GridWeb antes de copiar la columna.

![todo:imagen_alternativa_texto](copy-gridweb-rows-and-columns_3.png)

Similar al ejemplo anterior, el siguiente fragmento de código accede al objeto GridCells del orden de la hoja de trabajo activa para hacer una copia de la primera columna a la columna subsiguiente.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



Así es como se ve Aspose.Cells.GridWeb después de la operación de copia de columna.

![todo:imagen_alternativa_texto](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

Puede usar los métodos GridCells.CopyRow y GridCells.CopyColumn en bucle para copiar la fila y la columna de origen en varias filas y columnas, respectivamente.

{{% /alert %}} 
### **Copiar varias filas**
También es posible copiar varias filas a un nuevo destino usando el método GridCells.CopyRows, que toma un parámetro adicional de tipo entero para especificar la cantidad de filas de origen que se copiarán.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



Así es como se ve Aspose.Cells.GridWeb antes y después de la operación de copiar filas.

![todo:imagen_alternativa_texto](copy-gridweb-rows-and-columns_5.png)

![todo:imagen_alternativa_texto](copy-gridweb-rows-and-columns_6.png)
### **Copiar varias columnas**
La clase GridCells también proporciona el método CopyColumns, que toma un parámetro adicional de tipo entero para especificar el número de columnas de origen que se copiarán.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



Así es como se ve Aspose.Cells.GridWeb antes y después de la operación de copiar filas.

![todo:imagen_alternativa_texto](copy-gridweb-rows-and-columns_7.png)

![todo:imagen_alternativa_texto](copy-gridweb-rows-and-columns_8.png)
