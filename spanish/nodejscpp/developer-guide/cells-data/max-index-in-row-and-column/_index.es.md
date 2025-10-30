---
title: Obtener el índice de columna máximo en fila y el índice de fila máximo en columna
type: docs
weight: 600
url: /es/nodejs-cpp/get-max-index-in-row-and-column/
description: Aprende cómo obtener el índice máximo de columna en fila y el índice máximo de fila en columna a través de la API Aspose.Cells for Node.js via C++.
keywords: Obtener el índice máximo de columna en fila vía C++ en Node.js, obtener el índice máximo de fila en columna vía C++ en Node.js, obtener el índice máximo de columna de datos en fila vía C++ en Node.js, obtener el índice máximo de fila de datos en columna vía C++ en Node.js.
---

## **Escenarios de uso posibles**
Cuando solo necesitas manipular algunos datos en filas o columnas, debes conocer el rango de datos de filas y columnas. Aspose.Cells for Node.js via C++ ofrece esta función. Para obtener el índice máximo de columna en una fila, puedes usar los métodos [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--) y [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--), y luego usar el método [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) para obtener el índice máximo de columna y el índice máximo de columna de datos. Pero para obtener el índice máximo de fila y el índice máximo de datos de fila en una columna, debes crear un rango en la columna, recorrerlo para encontrar la última celda y finalmente llamar al método [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) en la celda.

Aspose.Cells for Node.js via C++ proporciona las siguientes propiedades y métodos para ayudarte a lograr tus objetivos.
- [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--)
- [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--)
- [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--)
- [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--)

## **Obtener el índice máximo de columna en fila y el índice máximo de fila en columna**
Este ejemplo muestra cómo:

1. Cargar el [archivo de muestra](sample.xlsx).
1. Obtener la fila que necesita obtener el índice de columna máximo e índice de columna de datos máximo.
1. Llama al método [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) en la celda.
1. Crear un rango basado en la columna.
1. Obtener el iterador y recorrer el rango.
1. Llama al método [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) en la celda.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-max-index-in-row-and-column.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
