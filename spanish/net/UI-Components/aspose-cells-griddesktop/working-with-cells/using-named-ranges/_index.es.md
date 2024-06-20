---
title: Usar rangos con nombre
type: docs
weight: 110
url: /es/net/aspose-cells-griddesktop/use-named-ranges/
keywords: GridDesktop, rangos con nombre, nombres
description: Este artículo introduce los rangos con nombre en GridDesktop.
---

{{% alert color="primary" %}} 

Normalmente, se utilizan las etiquetas de las columnas y filas en una hoja de cálculo para hacer referencia a las celdas dentro de esas columnas y filas. Pero puedes crear nombres descriptivos para representar celdas, rangos de celdas, fórmulas o valores constantes. La palabra **Nombre** puede referirse a una cadena de caracteres que representa una celda, rango de celdas, fórmula o valor constante. Por ejemplo, utiliza nombres fáciles de entender, como Productos, para referirte a rangos difíciles de entender, como Ventas!C20:C30 para representar una celda, rango de celdas, fórmula o valor constante. Las etiquetas se pueden utilizar en fórmulas que hacen referencia a datos en la misma hoja de cálculo; si deseas representar un rango en otra hoja de cálculo, puedes usar un nombre. Los **Rangos con Nombre** están entre las características más potentes de Microsoft. Los usuarios pueden asignar un nombre a un rango con nombre para que este rango de celdas pueda ser referido con su nombre en las fórmulas. **Aspose.Cells.GridDesktop** sí admite esta característica.

{{% /alert %}} 
## **Agregar/Hacer referencia a los rangos con nombre en las fórmulas**
El control GridDesktop admite importar/exportar rangos con nombre en los archivos de Excel, proporciona dos clases (**Name** y **NameCollection**) para trabajar con rangos con nombre.

El siguiente fragmento de código te ayudará a saber cómo usarlos.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingNamedRanges-1.cs" >}}
