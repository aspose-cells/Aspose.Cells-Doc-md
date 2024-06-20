---
title: Agregar fórmula a la celda
type: docs
weight: 30
url: /es/net/aspose-cells-griddesktop/adding-formula-to-cell/
keywords: GridDesktop, fórmula
description: Este artículo presenta cómo obtener o establecer una fórmula en la celda en la hoja de cálculo en GridDesktop.
---

{{% alert color="primary" %}} 

Una celda puede contener no solo un valor simple como una cifra numérica o algún texto, sino también una fórmula como su valor. Se utiliza una fórmula en una celda cuando el valor de la celda debe ser determinado después de algunos cálculos. En este tema, discutiremos cómo acceder y modificar una fórmula aplicada a una celda.

{{% /alert %}} 
## **Agregar fórmula a una celda**
Agregar una fórmula a una celda es similar a establecer el valor de una celda, como hemos discutido en nuestro tema anterior: [Acceder y Modificar el Valor de una Celda](/cells/es/net/accessing-and-modifying-the-value-of-a-cell/) excepto que en ese caso, solo agregamos valores simples a las celdas. Ahora, agregaremos fórmulas. Los desarrolladores pueden utilizar la propiedad Valor de una celda para acceder y modificar la fórmula o, de lo contrario, también se puede usar el método **SetCellValue** de la celda para agregar o modificar la fórmula en una celda.

**IMPORTANTE:** La diferencia básica entre usar la propiedad Valor o el método **SetCellValue** de una celda es que la propiedad Valor invoca el método **RunAllFormulas** de Grid automáticamente para recalcular los valores de todas las fórmulas, mientras que en el caso del método **SetCellValue**, los desarrolladores necesitan llamar explícitamente al método **RunAllFormulas** después de que se agreguen las fórmulas a las celdas. De hecho, cuando usamos el método **SetCellValue** de una celda, este método establece el valor de la celda solo a **TipoFórmula**, sin calcular la fórmula. Además, llamar al método **RunAllFormulas** no es necesario cada vez. Si desea agregar muchas fórmulas en las celdas de una hoja de cálculo, puede llamar al método **RunAllFormulas** solo una vez al final.

Se agrega una fórmula a una celda como un valor de cadena. Además, la estructura de la fórmula debe ser compatible con la estructura de fórmula de MS Excel. Todas las fórmulas deben comenzar con un **signo igual (=)**.

En el ejemplo dado a continuación, hemos agregado una fórmula para multiplicar los valores de dos celdas de la hoja de cálculo y almacenar el resultado en otra celda. También se invoca el método **RunAllFormulas** al final.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}



Ahora ejecute la aplicación. Si hace doble clic en la celda donde se agregó la fórmula, notará que el valor será reemplazado por la fórmula que en realidad está calculando el valor en el backend.

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop admite la mayoría de las funciones comúnmente utilizadas de MS Excel. Para obtener más detalles sobre la lista de funciones admitidas, por favor [haga clic aquí.](/cells/es/net/list-of-supported-functions/)

{{% /alert %}}
