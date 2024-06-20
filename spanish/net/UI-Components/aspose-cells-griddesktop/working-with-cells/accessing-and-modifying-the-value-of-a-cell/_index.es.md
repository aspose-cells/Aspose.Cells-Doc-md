---
title: Accediendo y Modificando el Valor de una Celda
type: docs
weight: 20
url: /es/net/aspose-cells-griddesktop/accessing-and-modifying-the-value-of-a-cell/
keywords: GridDesktop,cell,modify cell,get cell,modify cell value,get cell value
description: Este artículo introduce cómo obtener y modificar el valor de la celda en GridDesktop.
---

{{% alert color="primary" %}} 

En nuestro tema anterior, hemos discutido sobre cómo acceder a las celdas de una hoja de cálculo. En este tema, simplemente ampliaremos ese tema para mostrar a los desarrolladores cómo pueden acceder y modificar los valores de las celdas usando la API de Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **Acceder y Modificar el Valor de la Celda usando Aspose.Cells.GridDesktop**
Antes de acceder y modificar el valor de una celda, debemos saber cómo acceder a las celdas. Hay tres enfoques para acceder a las celdas de una hoja de cálculo. Para obtener más detalles sobre estos tres enfoques, por favor [Acceder a las Celdas en una Hoja de Cálculo.](/cells/es/net/accessing-cells-in-a-worksheet/)

Cada celda tiene una propiedad llamada Valor. Entonces, una vez que se accede a una celda, los desarrolladores pueden acceder y modificar el contenido de la propiedad Valor para acceder y cambiar el valor de una celda.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**IMPORTANTE:** Utilizar la propiedad Valor de una celda para modificar su valor es un buen enfoque para establecer el valor de una o unas pocas celdas. Si necesita establecer los valores de muchas celdas, entonces el rendimiento de este enfoque no sería bueno. Por lo tanto, para establecer los valores de muchas celdas, debería usar el método **SetCellValue** de la celda para mejorar el rendimiento de sus aplicaciones. A continuación se muestra una versión modificada del fragmento de código anterior usando el método **SetCellValue**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
