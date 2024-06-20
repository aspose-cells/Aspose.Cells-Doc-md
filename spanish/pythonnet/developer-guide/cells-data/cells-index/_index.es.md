---
title: Obtener el índice de celdas
type: docs
weight: 600
url: /es/python-net/get-cells-index/
description: Aprende cómo obtener una fila o columna por el nombre de la fila a través de la API de Aspose.Cells para Python via .NET, columna o celdas. Convierte el nombre de la celda a un índice de fila y columna basado en cero a través de la API de Aspose.Cells para Python via .NET.
keywords: Python Excel, obtener el índice de fila y columna por el nombre de la celda usando Python, obtener el índice de columna por el nombre de la columna usando Python, obtener el índice de fila por el nombre de la fila usando Python, obtener el índice por el nombre de celda usando Python. 
---

{{% alert color="primary" %}}
La vista predeterminada de Excel es la referencia de estilo A1, cada columna se define como A, B, C..., y las celdas se nombran como A1, B2, C3... y así sucesivamente.
Es posible que desee saber en qué fila y columna se encuentra esta celda.

{{% /alert %}}


## **Escenarios de uso posibles**
Cuando solo necesita manipular un dato específico en la hoja de cálculo por índice de fila y columna, necesita saber los índices de fila y columna de esa celda específica. 
Aspose.Cells for Python via .NET ofrece esta función para obtener el índice de fila y columna por el nombre de la fila, columna y celda. 
Aspose.Cells para Python via .NET proporciona las siguientes propiedades y métodos para ayudarlo a alcanzar sus objetivos.
- [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any)
- [**CellsHelper.column_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_index_to_name/#int)
- [**CellsHelper.column_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_name_to_index/#str)
- [**CellsHelper.row_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_index_to_name/#int)
- [**CellsHelper.row_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_name_to_index/#str)

Nota: El indexado es basado en cero en Aspose.Cells for Python via .NET, pero el id de fila es basado en uno en MS Excel.

## **Obtener Índices de Celdas usando la Biblioteca de Excel Aspose.Cells para Python**
Este ejemplo muestra cómo:

1. Crear un libro de trabajo y agregar algunos datos.
1. Encontrar la celda específica en la primera hoja de trabajo.
1. Obtener el índice de fila e índice de columna por el nombre de la celda.
1. Obtener el índice de columna por el nombre de la columna.
1. Obtener el índice de fila por el nombre de la fila.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-get-index.py" >}}
