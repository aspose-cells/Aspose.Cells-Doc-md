---
title: Cambiar el tamaño de filas y columnas
type: docs
weight: 30
url: /es/net/resize-rows-and-columns/
---
{{% alert color="primary" %}} 

A veces, los valores de celda son más anchos que la celda en la que se encuentran o se encuentran en varias líneas. Dichos valores no son completamente visibles para los usuarios a menos que cambien la altura y el ancho de las filas y columnas. Aspose.Cells. GridWeb es totalmente compatible con la configuración de la altura de las filas y el ancho de las columnas. En este tema se describen estas características en detalle con la ayuda de ejemplos.

{{% /alert %}} 
## **Trabajar con alturas de fila y ancho de columna**
### **Configuración de la altura de fila**
Para establecer la altura de una fila:

1. Agregue el control Aspose.Cells.GridWeb a su formulario web.
1. Acceda a la colección Cells de la hoja de trabajo.
1. Establezca la altura de todas las celdas en cualquier fila especificada.

{{% alert color="primary" %}} 

El método SetRowHeight y SetColumnWidth de la colección Cells también tiene variantes disponibles para establecer medidas de altura de fila y ancho de columna en pulgadas y píxeles.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetRowHeight.cs" >}}
### **Configuración del ancho de columna**
Para establecer el ancho de una columna:

1. Agregue el control Aspose.Cells.GridWeb a su formulario web.
1. Acceda a la colección Cells de la hoja de trabajo.
1. Establezca el ancho de todas las celdas en cualquier columna especificada.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetColumnWidth.cs" >}}
