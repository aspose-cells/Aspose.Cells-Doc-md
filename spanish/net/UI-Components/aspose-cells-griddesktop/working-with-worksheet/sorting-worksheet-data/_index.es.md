---
title: Clasificación de datos de la hoja de trabajo
type: docs
weight: 80
url: /es/net/sorting-worksheet-data/
---
{{% alert color="primary" %}} 

La clasificación es una tarea rutinaria importante que utilizamos principalmente al procesar datos. En este tema, discutiremos con la ayuda de un ejemplo simple cómo podemos ordenar los datos en una hoja de trabajo.

{{% /alert %}} 
## **Clasificación de datos de la hoja de trabajo**
Para ordenar datos en una hoja de trabajo utilizando API de Aspose.Cells.GridDesktop, siga los pasos a continuación:

-  En primer lugar, cree un objeto global de**rango de celdas** para que se pueda acceder a ella desde cualquier lugar del ámbito de su clase
-  Crear un controlador de eventos para**SelectedCellRangeChanged** evento de**GridEscritorio**. **SelectedCellRangeChanged** El evento se activa cada vez que se cambia un rango de celdas seleccionado por un usuario. Por ejemplo, si un usuario selecciona celdas (que contienen datos para ordenar), cada vez que cambie su rango de selección, se activará este evento.
-  El controlador de eventos proporciona**CellRangeEventArgs** argumento que proporciona además el rango de actualización de celdas (seleccionado por el usuario) en forma de un**rango de celdas** objeto. Entonces, en este controlador de eventos, asignaremos este**rango de celdas** objeto (que contiene rango actualizado de celdas) al global**rango de celdas**objeto para que también se pueda usar en otra parte del código. Para asegurarnos de no perder el rango de celdas, escribiremos el código del controlador de eventos dentro de una condición
- Ahora podemos escribir algo de código para ordenar los datos de la hoja de trabajo. En primer lugar, acceda a la hoja de trabajo deseada
-  Crear un**ordenarrango** objeto que mantendrá el rango de celdas cuyos datos se van a ordenar. En**ordenarrango** constructor, podemos especificar la hoja de trabajo, los índices de la fila y la columna de inicio, el número de filas y columnas para ordenar, la orientación de la clasificación (como de arriba a abajo o de izquierda a derecha), etc.
-  Ahora podemos llamar**Tipo** método de**ordenarrango** objeto para realizar la clasificación de datos. En**Tipo** método, podemos especificar el índice de la columna o fila a ordenar y el orden de clasificación (que puede ser**ascendente** o**Descendente** según sus requisitos)
-  Finalmente, podemos llamar**Invalidar** método de**GridEscritorio** para redibujar celdas.

En el ejemplo que se muestra a continuación, hemos demostrado cómo ordenar los datos en una columna.

 Cree un objeto global de CellRange y**SelectedCellRangeChanged**evento de GridDesktop. Ahora escriba el código como se indica a continuación:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}


 Ahora escribimos el método para**orden ascendente** . Puede crear un botón para**orden ascendente** y escriba debajo del código dentro de su**Hacer clic** Evento.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}


 Finalmente, escribimos algo de código para lograr**orden descendente** funcionalidad. Crear un**orden descendente** botón y escriba debajo del código dentro de su**Hacer clic** Evento.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
