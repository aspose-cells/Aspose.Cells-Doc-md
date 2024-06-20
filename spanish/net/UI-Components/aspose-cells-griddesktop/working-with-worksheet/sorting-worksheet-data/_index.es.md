---
title: Ordenar Datos de Hoja de Cálculo
type: docs
weight: 80
url: /es/net/aspose-cells-griddesktop/sorting-worksheet-data/
keywords: GridDesktop,ordenar,ordenamiento,ordenar datos,ordenar datos
description: Este artículo presenta cómo ordenar datos en una hoja de cálculo en GridDesktop.
---

{{% alert color="primary" %}} 

Ordenar es una tarea rutinaria importante que usamos principalmente al procesar datos. En este tema, discutiremos con la ayuda de un ejemplo simple cómo podemos ordenar datos en una hoja de cálculo.

{{% /alert %}} 
## ** Ordenar Datos de Hoja de Cálculo**
Para ordenar datos en una hoja de cálculo utilizando la API de Aspose.Cells.GridDesktop, por favor sigue los siguientes pasos:

- En primer lugar, crea un objeto global de **CellRange** para que pueda ser accedido en cualquier lugar en el alcance de tu clase
- Cree un controlador de eventos para el evento **SelectedCellRangeChanged** de **GridDesktop**. El evento **SelectedCellRangeChanged** se activa cada vez que se cambia un rango de celdas seleccionado por un usuario. Por ejemplo, si un usuario selecciona celdas (que contienen datos para ser ordenados), cada vez que cambie su rango de selección, este evento se activará.
- El controlador de eventos proporciona el argumento **CellRangeEventArgs** que a su vez proporciona el rango actualizado de celdas (seleccionadas por el usuario) en forma de un objeto **CellRange**. Entonces, en este controlador de eventos, asignaremos este objeto **CellRange** (que contiene el rango actualizado de celdas) al objeto **CellRange** global para que también pueda ser utilizado en otra parte del código. Para asegurarnos de que no perdamos el rango de celdas, escribiremos el código del controlador de eventos dentro de una condición.
- Ahora podemos escribir algo de código para ordenar los datos de la hoja de cálculo. En primer lugar, accede a una hoja de cálculo deseada.
- Cree un objeto **SortRange** que mantendrá el rango de celdas cuyos datos se van a ordenar. En el constructor de **SortRange**, podemos especificar la hoja de cálculo, los índices de la fila y columna de inicio, el número de filas y columnas a ordenar, la orientación de la ordenación (como de arriba hacia abajo o de izquierda a derecha), etc.
- Ahora podemos llamar al método **Sort** del objeto **SortRange** para realizar la ordenación de datos. En el método **Sort**, podemos especificar el índice de la columna o fila a ordenar y el orden de la clasificación (que puede ser **Ascendente** o **Descendente** según sus requisitos).
- Finalmente, podemos llamar al método **Invalidate** de **GridDesktop** para volver a dibujar las celdas.

En el ejemplo dado a continuación, hemos demostrado cómo ordenar datos en una columna.

Cree un objeto global de CellRange y el evento **SelectedCellRangeChanged** de GridDesktop. Ahora escriba el código como se muestra a continuación:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}


Ahora escribimos el método para **Ascendente Sort**. Puede crear un botón para **Ascendente Sort** y escribir el siguiente código dentro de su evento **Click**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}


Finalmente, escribimos algo de código para lograr la funcionalidad de **Descendente Sort**. Cree un botón de **Descendente Sort** y escriba el siguiente código dentro de su evento **Click**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
