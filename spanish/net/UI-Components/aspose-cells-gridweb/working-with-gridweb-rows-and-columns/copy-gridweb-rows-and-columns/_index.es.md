---
title: Copiar filas y columnas de GridWeb
type: docs
weight: 80
url: /es/net/aspose-cells-gridweb/copy-gridweb-rows-and-columns/
keywords: GridWeb,copiar
description: Este artículo introduce cómo copiar filas y columnas en GridWeb.
---

{{% alert color="primary" %}} 

El componente Aspose.Cells.GridWeb ofrece la posibilidad de copiar filas y columnas mientras se utiliza la clase GridCells. Este artículo demuestra el uso de APIs expuestas por Aspose.Cells.GridWeb para copiar filas y columnas en la interfaz de GridWeb. 

Los métodos GridCells.CopyRow, GridCells.CopyColumn, GridCells.CopyRows y GridCells.CopyColumns copiarán el contenido, estilo y fórmulas de la fila y columna fuente al destino.

{{% /alert %}} 
## **Copiando filas y columnas**
Si aún no está familiarizado con el componente Aspose.Cells.GridWeb, le sugerimos firmemente que consulte la [Introducción a Aspose.Cells.GridWeb](https://docs.aspose.com/cells/net/aspose-cells-gridweb/browsers-capabilities/) y el artículo detallado sobre [Cómo agregar el componente Aspose.Cells.GridWeb en una aplicación WebForms](https://docs.aspose.com/cells/net/aspose-cells-gridweb/add-gridweb-to-web-form/).
### **Copiando una Sola Fila**
Para mantener el ejemplo simple, el artículo utiliza una hoja de cálculo existente con una fila y una fórmula simple que suma todos los valores en la fila. Así es como se muestra la hoja de cálculo en la interfaz de Aspose.Cells.GridWeb antes de copiar la fila.

![todo:image_alt_text](copy-gridweb-rows-and-columns_1.png)

El fragmento de código es simple como se muestra a continuación. Accede al objeto GridCells de la hoja de cálculo activa para hacer una copia de la primera fila a la fila siguiente.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


Así es como se ve Aspose.Cells.GridWeb después de la operación de copia de fila.

![todo:image_alt_text](copy-gridweb-rows-and-columns_2.png)
### **Copia de una sola columna**
El siguiente ejemplo utiliza una hoja de cálculo existente con una columna y una fórmula simple que suma todos los valores en la columna. Así es como se muestra la hoja de cálculo en la interfaz de Aspose.Cells.GridWeb antes de copiar la columna.

![todo:image_alt_text](copy-gridweb-rows-and-columns_3.png)

Similar al ejemplo anterior, el siguiente fragmento de código accede al objeto GridCells del pedido de hoja de cálculo activa para hacer una copia de la primera columna a la columna siguiente.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



Así es como se ve Aspose.Cells.GridWeb después de la operación de copia de columna.

![todo:image_alt_text](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

Puede utilizar los métodos GridCells.CopyRow y GridCells.CopyColumn en un bucle para copiar la fila y la columna fuente a varias filas y columnas, respectivamente.

{{% /alert %}} 
### **Copia de varias filas**
También es posible copiar múltiples filas a un nuevo destino mientras se utiliza el método GridCells.CopyRows, que toma un parámetro adicional de tipo entero para especificar el número de filas fuente que se copiarán.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



Así es como Aspose.Cells.GridWeb se ve antes y después de la operación de copia de columnas.

![todo:image_alt_text](copy-gridweb-rows-and-columns_5.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_6.png)
### **Copiar Múltiples Columnas**
La clase GridCells también proporciona el método CopyColumns, que toma un parámetro adicional de tipo entero para especificar el número de columnas fuente que se copiarán.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



Así es como Aspose.Cells.GridWeb se ve antes y después de la operación de copia de columnas.

![todo:image_alt_text](copy-gridweb-rows-and-columns_7.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_8.png)
