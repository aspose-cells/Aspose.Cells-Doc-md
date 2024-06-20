---
title: Agregar y Referenciar Rangos Nombrados
type: docs
weight: 120
url: /es/net/aspose-cells-gridweb/add-and-reference-named-ranges/
keywords: GridWeb,GridName,Names
description: Este artículo presenta cómo trabajar con rangos nombrados en GridWeb. 
---

{{% alert color="primary" %}} 

Normalmente, las etiquetas de columnas y filas se utilizan para referirse de manera única a celdas. Pero puedes crear nombres descriptivos para representar celdas, rangos de celdas, fórmulas o valores constantes. La palabra **Nombre** puede referirse a una cadena de caracteres que representa una celda, rango de celdas, fórmula o valor constante. Por ejemplo, utiliza nombres fáciles de entender, como 'Productos', para referirse a rangos difíciles de entender, como 'Ventas!C20:C30'. Las etiquetas se pueden utilizar en fórmulas que hacen referencia a datos en la misma hoja de cálculo; si deseas representar un rango en otra hoja de cálculo, puedes usar un nombre. Los **Rangos Nombrados** es una de las características más poderosas de Microsoft Excel. Los usuarios pueden asignar un nombre a un rango y utilizar ese nombre en fórmulas. Aspose.Cells.GridWeb admite esta característica.

{{% /alert %}} 
## **Agregar/Hacer referencia a los rangos con nombre en las fórmulas**
El control GridWeb proporciona dos clases (GridName y GridNameCollection) para trabajar con rangos nombrados. El siguiente fragmento de código te ayudará a entender cómo crear el Rango Nombrado y acceder a él en las fórmulas.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessNamedRanges.aspx-AddNamedRange.cs" >}}
