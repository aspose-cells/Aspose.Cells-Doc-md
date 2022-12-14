---
title: Acceso y Modificación del Valor de un Cell
type: docs
weight: 20
url: /es/net/accessing-and-modifying-the-value-of-a-cell/
---
{{% alert color="primary" %}} 

En nuestro tema anterior, hemos discutido sobre el acceso a las celdas de una hoja de trabajo. En este tema, simplemente ampliaremos ese tema para mostrar a los desarrolladores cómo pueden acceder y modificar los valores de las celdas usando API de Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **Acceda y modifique el valor Cell usando Aspose.Cells.GridDesktop**
 Antes de acceder y modificar el valor de una celda, debemos saber cómo acceder a las celdas. Hay tres enfoques para acceder a las celdas de una hoja de trabajo. Para más detalles sobre estos tres enfoques, por favor[Accediendo a Cells en una hoja de trabajo.](/cells/es/net/accessing-cells-in-a-worksheet/)

Cada celda tiene una propiedad llamada Valor. Entonces, una vez que se accede a una celda, los desarrolladores pueden acceder y modificar el contenido de la propiedad Valor para acceder y cambiar el valor de una celda.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**IMPORTANTE:**El uso de la propiedad Valor de una celda para modificar su valor es un buen enfoque para establecer el valor de una o varias celdas. Si necesita establecer los valores de muchas celdas, el rendimiento de este enfoque no sería bueno. Entonces, para establecer los valores de muchas celdas, debe usar**Establecer valor de celda** método de la celda para mejorar el rendimiento de sus aplicaciones. Una versión modificada del fragmento de código anterior usando**Establecer valor de celda** El método se muestra a continuación.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
