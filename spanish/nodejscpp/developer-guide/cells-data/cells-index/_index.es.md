---
title: Obtener el índice de celdas
type: docs
weight: 600
url: /es/nodejs-cpp/get-cells-index/
description: Aprende cómo obtener la fila o columna por el nombre de la fila, columna o celdas. Convierte el nombre de la celda a índice de fila y columna basado en cero.
keywords: Obtener el índice de fila y columna por el nombre de la celda, Obtener el índice de columna por el nombre de la columna, Obtener el índice de fila por el nombre de la fila, Obtener el índice por el nombre de la celda. 
---

{{% alert color="primary" %}}
La vista predeterminada de Excel es la referencia de estilo A1, cada columna se define como A, B, C..., y las celdas se nombran como A1, B2, C3... y así sucesivamente.
Es posible que desee saber en qué fila y columna se encuentra esta celda.

{{% /alert %}}


## **Escenarios de uso posibles**
Cuando solo necesita manipular un dato específico en la hoja de cálculo por índice de fila y columna, necesita saber los índices de fila y columna de esa celda específica. 
Aspose.Cells for Node.js via C++ ofrece esta función para obtener el índice de fila y columna por el nombre de la fila, columna y celda. 
Aspose.Cells for Node.js via C++ proporciona las siguientes propiedades y métodos para ayudarte a lograr tus objetivos.
- [**CellsHelper.cellNameToIndex(string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#cellNameToIndex-string-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowNameToIndex-string-)

Nota: La indexación en Aspose.Cells for Node.js via C++ empieza en cero, pero el ID de la fila comienza en uno en MS Excel.

## **Obtener índices de celdas usando Aspose.Cells for Node.js via C++**
Este ejemplo muestra cómo:

1. Crear un libro de trabajo y agregar algunos datos.
1. Encontrar la celda específica en la primera hoja de trabajo.
1. Obtener el índice de fila e índice de columna por el nombre de la celda.
1. Obtener el índice de columna por el nombre de la columna.
1. Obtener el índice de fila por el nombre de la fila.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-get-index.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
