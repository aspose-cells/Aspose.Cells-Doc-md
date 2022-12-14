---
title: Uso de rangos con nombre
type: docs
weight: 110
url: /es/net/using-named-ranges/
---
{{% alert color="primary" %}} 

 Normalmente, utiliza las etiquetas de columnas y filas en una hoja de trabajo para hacer referencia a las celdas dentro de esas columnas y filas. Pero puede crear nombres descriptivos para representar celdas, rangos de celdas, fórmulas o valores constantes. La palabra**Nombre**puede hacer referencia a una cadena de caracteres que representa una celda, un rango de celdas, una fórmula o un valor constante. Por ejemplo, use nombres fáciles de entender, como Productos, para hacer referencia a rangos difíciles de entender, como Ventas!C20:C30 para representar una celda, un rango de celdas, una fórmula o un valor constante. Las etiquetas se pueden usar en fórmulas que se refieren a datos en la misma hoja de trabajo; si desea representar un rango en otra hoja de trabajo, puede usar un nombre.**Rangos con nombre** se encuentran entre las características más poderosas de Microsoft. Los usuarios pueden asignar un nombre a un rango con nombre para que este rango de celdas pueda ser referido con su nombre en las fórmulas.**Aspose.Cells.GridDesktop** admite esta función.

{{% /alert %}} 
## **Agregar/Hacer referencia a rangos con nombre en fórmulas**
El control GridDesktop admite la importación/exportación de rangos con nombre en los archivos de Excel, proporciona dos clases (**Nombre** y**NameCollection**) para trabajar con rangos con nombre.

El siguiente fragmento de código le ayudará a usarlos.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingNamedRanges-1.cs" >}}
