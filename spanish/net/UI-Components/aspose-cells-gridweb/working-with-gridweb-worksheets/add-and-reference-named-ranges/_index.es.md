---
title: Agregar y hacer referencia a rangos con nombre
type: docs
weight: 120
url: /es/net/add-and-reference-named-ranges/
---
{{% alert color="primary" %}} 

 Normalmente, las etiquetas de columna y fila se utilizan para hacer referencia de forma única a las celdas. Pero puede crear nombres descriptivos para representar celdas, rangos de celdas, fórmulas o valores constantes. La palabra**Nombre**puede hacer referencia a una cadena de caracteres que representa una celda, un rango de celdas, una fórmula o un valor constante. Por ejemplo, use nombres fáciles de entender, como Productos, para hacer referencia a rangos difíciles de entender, como Ventas!C20:C30. Las etiquetas se pueden usar en fórmulas que se refieren a datos en la misma hoja de trabajo; si desea representar un rango en otra hoja de trabajo, puede usar un nombre.**Rangos con nombre** es una de las características más poderosas de Microsoft Excel. Los usuarios pueden asignar un nombre a un rango y usar ese nombre en fórmulas. Aspose.Cells. GridWeb admite esta función.

{{% /alert %}} 
## **Agregar/Hacer referencia a rangos con nombre en fórmulas**
El control GridWeb proporciona dos clases (GridName y GridNameCollection) para trabajar con rangos con nombre. El siguiente fragmento de código lo ayudará a comprender cómo crear el rango con nombre y acceder a él en las fórmulas.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessNamedRanges.aspx-AddNamedRange.cs" >}}
