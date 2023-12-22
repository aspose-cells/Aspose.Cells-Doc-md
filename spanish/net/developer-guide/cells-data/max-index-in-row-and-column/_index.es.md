---
title: Obtenga el índice máximo de columna en la fila y el índice máximo de fila en la columna
type: docs
weight: 600
url: /es/net/get-max-index-in-row-and-column/
description: Aprenda cómo obtener el índice máximo de columna en la fila y el índice máximo de fila en la columna a través de Aspose.Cells for .NET API.
keywords: Get Max Column Index in Row, Get Max Row Index in Column, Get Max Data Column Index in Row, Get Max Data Row Index in Column. 
---
##  **Posibles escenarios de uso**
Cuando solo necesita manipular algunos datos en las filas o columnas, necesita conocer el rango de datos de las filas y columnas. Aspose.Cells ofrece esta característica. Para obtener el índice máximo de columna en una fila, puede obtener el[Fila.ÚltimaCelda](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) y[Fila.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/) propiedades y luego use el[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) propiedad para obtener el índice máximo de columna y el índice máximo de columna de datos. Pero para obtener el índice de fila máximo y el índice de datos de fila máximo en una columna, debe crear un rango en la columna, luego recorrer el rango para encontrar la última celda y finalmente obtener el[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) atributo en la celda.

Aspose.Cells proporciona las siguientes propiedades y métodos para ayudarle a alcanzar sus objetivos.
- [**Fila.ÚltimaCelda**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Fila.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

##  **Obtenga el índice máximo de columna en la fila y el índice máximo de fila en la columna usando Aspose.Cells**
Este ejemplo muestra cómo:

1.  Carga el[archivo de muestra](sample.xlsx).
1. Obtenga la fila que necesita obtener el índice de columna máximo y el índice de columna de datos máximo.
1.  Conseguir[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) atributo en la celda.
1. Cree un rango basado en la columna.
1. Obtenga iterador y recorrido transversal.
1.  Conseguir[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) atributo en la celda.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}