---
title: Adición de fórmulas al Cells
type: docs
weight: 30
url: /es/net/adding-formulas-to-cells/
---
{{% alert color="primary" %}} 

Una celda no solo puede contener un valor simple como una cifra numérica o algún texto, sino que también podemos insertar una fórmula en una celda como su valor. Una fórmula se usa en una celda cuando el valor de una celda debe determinarse después de algunos cálculos. En este tema, discutiremos cómo podemos acceder y modificar una fórmula aplicada en una celda.

{{% /alert %}} 
## **Agregar fórmula a un Cell**
 Agregar una fórmula a una celda es como establecer el valor de una celda, como hemos discutido en nuestro tema anterior:[Acceso y modificación del valor de un Cell](/cells/es/net/accessing-and-modifying-the-value-of-a-cell/) excepto que en ese caso, solo agregamos valores simples a las celdas. Ahora, agregaremos fórmulas. Los desarrolladores pueden usar la propiedad Valor de una celda para acceder y modificar la fórmula o de otra manera**Establecer valor de celda** El método de la celda también se puede usar para agregar o modificar la fórmula en una celda.

**IMPORTANTE:** La diferencia básica entre usar la propiedad Valor o**Establecer valor de celda** método de una celda es que la propiedad Value invoca**Ejecutar todas las fórmulas** método de Grid automáticamente para volver a calcular los valores de todas las fórmulas donde, como en el caso de**Establecer valor de celda** los desarrolladores de métodos deben llamar**Ejecutar todas las fórmulas** método explícitamente después de agregar las fórmulas a las celdas. En realidad, cuando usamos**Establecer valor de celda** método de una celda, entonces este método establece el valor de la celda en**FormulaType** solamente y no calcular la fórmula. Además, llamando**Ejecutar todas las fórmulas**método cada vez que no es necesario. Si desea agregar muchas fórmulas en las celdas de una hoja de trabajo, puede llamar**Ejecutar todas las fórmulas** método sólo una vez al final.

 Se agrega una fórmula a una celda como un valor de cadena. Además, la estructura de la fórmula debe ser compatible con la estructura de la fórmula de MS Excel. Todas las fórmulas deben comenzar con un**Signo igual (=)**.

 En el ejemplo que se muestra a continuación, hemos agregado una fórmula para multiplicar los valores de dos celdas de la hoja de trabajo y almacenar el resultado en otra celda.**Ejecutar todas las fórmulas** El método también se invoca al final.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}



Ahora ejecuta la aplicación. Si hace doble clic en la celda donde se agregó la fórmula, notará que el valor será reemplazado por la fórmula que realmente está calculando el valor en el back-end.

{{% alert color="primary" %}} 

 Aspose.Cells.GridDesktop es compatible con la mayoría de las funciones de uso común de MS Excel. Para obtener más detalles sobre la lista de funciones admitidas, por favor[haga clic aquí.](/cells/es/net/list-of-supported-functions/)

{{% /alert %}}
