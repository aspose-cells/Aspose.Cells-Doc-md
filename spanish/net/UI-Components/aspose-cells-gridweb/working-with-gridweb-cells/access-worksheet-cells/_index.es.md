---
title: Acceder a la hoja de trabajo Cells
type: docs
weight: 10
url: /es/net/access-worksheet-cells/
---
{{% alert color="primary" %}} 

Este tema trata sobre las celdas, analizando la característica más básica de Aspose.Cells.GridWeb: acceder a las celdas.

{{% /alert %}} 
## **Acceso a Cells en una hoja de trabajo**
Cada hoja de trabajo contiene una propiedad con el nombre de Cells que en realidad es una colección de objetos GridCell donde un objeto GridCell representa una celda en Aspose.Cells.GridWeb. Es posible acceder a cualquier celda usando Aspose.Cells.GridWeb. Hay dos métodos preferidos, cada uno de los cuales se analiza a continuación.


### **Usando Cell Nombre**
Todas las celdas tienen un nombre único. Por ejemplo, A1, A2, B1, B2, etc. Aspose.Cells. GridWeb permite a los desarrolladores acceder a cualquier celda deseada usando el nombre de la celda. Simplemente pase el nombre de la celda (como índice) a la colección Cells de GridWorksheet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


### **Uso de índices de fila y columna**
Una celda también se puede reconocer por su ubicación en términos de índices de fila y columna. Simplemente pase los índices de fila y columna de una celda a la colección Cells de GridWorksheet. Este enfoque es más rápido que el anterior.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}
