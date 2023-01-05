---
title: Acceder y modificar valores Cell
type: docs
weight: 20
url: /es/net/access-and-modify-cell-values/
---
{{% alert color="primary" %}} 

[Acceder a la hoja de trabajo Cells](/cells/es/net/access-worksheet-cells/) habló sobre el acceso a las celdas. Este tema amplía esa discusión para mostrar cómo acceder y modificar valores de celda usando Aspose.Cells.GridWeb API.

{{% /alert %}} 
## **Acceso y modificación del valor de Cell**
### **Valores de cadena**
 Antes de acceder y modificar el valor de una celda, debe saber cómo acceder a las celdas. Para obtener detalles sobre los diferentes enfoques para acceder a las celdas, consulte[Acceder a la hoja de trabajo Cells](/cells/es/net/access-worksheet-cells/).

Cada celda tiene una propiedad llamada StringValue. Una vez que se accede a una celda, los desarrolladores pueden usar la propiedad StringValue para acceder al valor de la cadena de celdas. Para modificar los valores de las celdas, se proporciona un método especial PutValue, que se puede usar para actualizar el valor de cadena de la celda.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **Todo tipo de valores**
El método PutValue del objeto de una celda tiene 8 sobrecargas disponibles que se pueden usar para modificar cualquier tipo de valor (Boolean, int, double, DateTime y string) en una celda.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



También existe una versión sobrecargada del método PutValue que puede tomar cualquier tipo de valor en formato de cadena y convertirlo automáticamente a un tipo de datos adecuado. Para que esto suceda, pase el valor booleano verdadero a otro parámetro del método PutValue como se muestra a continuación en el ejemplo.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
