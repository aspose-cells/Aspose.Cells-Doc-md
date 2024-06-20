---
title: Acceder y modificar el valor de la celda
type: docs
weight: 20
url: /es/net/aspose-cells-gridweb/access-and-modify-cell-value/
keywords: GridWeb,valor de la celda,modificar,valor
description: Este artículo presenta cómo obtener y modificar el valor de la celda en GridWeb.
---

{{% alert color="primary" %}} 

[Acceder a las celdas de la hoja de cálculo](/cells/es/net/aspose-cells-gridweb/access-worksheet-cells/) discute el acceso a las celdas. Este tema amplía esa discusión para mostrar cómo acceder y modificar los valores de las celdas utilizando la API de Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Acceder y modificar el valor de una celda**
### **Valores de cadena**
Antes de acceder y modificar el valor de una celda, es necesario saber cómo acceder a las celdas. Para obtener detalles sobre los diferentes enfoques para acceder a las celdas, consulte [Acceder a las celdas de la hoja de cálculo](/cells/es/net/aspose-cells-gridweb/access-worksheet-cells/).

Cada celda tiene una propiedad llamada StringValue. Una vez que se accede a una celda, los desarrolladores pueden usar la propiedad StringValue para acceder al valor de cadena de las celdas. Para modificar los valores de las celdas, se proporciona un método especial PutValue, que se puede usar para actualizar el valor de cadena de la celda.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **Todos los tipos de valores**
El método PutValue del objeto de una celda tiene 8 sobrecargas disponibles que se pueden usar para modificar cualquier tipo de valor (booleano, entero, doble, DateTime y cadena) en una celda.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



También hay una versión sobrecargada del método PutValue que puede tomar cualquier tipo de valor en formato de cadena y convertirlo automáticamente a un tipo de datos adecuado. Para lograrlo, pase el valor booleano true a otro parámetro del método PutValue como se muestra a continuación en el ejemplo.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
