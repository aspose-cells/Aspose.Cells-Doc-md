---
title: Obtener el índice máximo de columna en una fila y el índice máximo de fila en una columna con Golang vía C++
linktitle: Obtener el índice de columna máximo en fila y el índice de fila máximo en columna
type: docs
weight: 600
url: /es/go-cpp/get-max-index-in-row-and-column/
description: Aprende cómo obtener el índice máximo de columna en una fila y el índice máximo de fila en una columna mediante la API Aspose.Cells for C++.
keywords: Obtener el índice de columna máximo en fila, obtener el índice de fila máximo en columna, obtener el índice de columna de datos máximo en fila, obtener el índice de fila de datos máximo en columna.
---

## **Escenarios de uso posibles**
Cuando solo necesitas manipular algunos datos en filas o columnas, debes conocer el rango de datos de filas y columnas. Aspose.Cells ofrece esta función. Para obtener el índice máximo de columna en una fila, puedes obtener las propiedades [Row.GetLastCell()](https://reference.aspose.com/cells/go-cpp/row/getlastcell/) y [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/), y luego usar la propiedad [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) para obtener el índice máximo de columna y el índice máximo de columna de datos. Pero para obtener el índice máximo de fila y el índice máximo de fila de datos en una columna, debes crear un rango en la columna, recorrer el rango para encontrar la última celda, y finalmente obtener el atributo [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) en la celda.

Aspose.Cells proporciona las siguientes propiedades y métodos para ayudarlo a alcanzar sus metas.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/go-cpp/cell/getrow/)

## **Obtener el índice de columna máximo en fila y el índice de fila máximo en columna usando Aspose.Cells**
Este ejemplo muestra cómo:

1. Cargar el [archivo de muestra](sample.xlsx).
1. Obtener la fila que necesita obtener el índice de columna máximo e índice de columna de datos máximo.
1. Obtener el atributo [Cell.GetColumn()](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/) en la celda.
1. Crear un rango basado en la columna.
1. Obtener el iterador y recorrer el rango.
1. Obtener el atributo [Cell.GetRow()](https://reference.aspose.com/cells/go-cpp/cell/getrow/) en la celda.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MaxIndexInRowAndColumn.go" >}}
