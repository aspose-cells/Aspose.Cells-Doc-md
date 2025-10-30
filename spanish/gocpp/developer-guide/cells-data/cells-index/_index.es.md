---
title: Obtener el índice de celdas con Golang mediante C++
linktitle: Obtener el índice de celdas
type: docs
weight: 600
url: /es/go-cpp/get-cells-index/
description: Aprender cómo obtener el índice de fila o columna por el nombre de fila, columna o celdas. Convertir el nombre de la celda a índice de fila y columna basado en cero usando Aspose.Cells con Golang mediante C++.
keywords: Obtener el índice de fila y columna por el nombre de la celda, Obtener el índice de columna por el nombre de la columna, Obtener el índice de fila por el nombre de la fila, Obtener el índice por el nombre de la celda.
---

{{% alert color="primary" %}}
 La vista predeterminada de Excel es referencia estilo A1, donde cada columna se define como A, B, C.... y las celdas se nombran como A1, B2, C3... y así sucesivamente.
Es posible que quieras saber en qué fila y columna se encuentra esta celda.

{{% /alert %}}

## **Escenarios de uso posibles**

Cuando solo necesitas manipular datos específicos en la hoja de cálculo por índice de fila y columna, necesitas conocer los índices de fila y columna de esa celda específica.
 Aspose.Cells ofrece esta función para obtener el índice de fila y columna por el nombre de la fila, columna y celda.
 Aspose.Cells proporciona las siguientes propiedades y métodos para ayudarte a lograr tus objetivos:

- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/rownametoindex/)

 Nota: La indexación comienza en cero en Aspose.Cells for C++, pero el ID de la fila es uno en MS Excel.

## **Obtener Índices de Celdas usando Aspose.Cells**

Este ejemplo muestra cómo:

1. Crear un libro de trabajo y agregar algunos datos.
1. Encontrar la celda específica en la primera hoja de trabajo.
1. Obtener el índice de fila e índice de columna por el nombre de la celda.
1. Obtener el índice de columna por el nombre de la columna.
1. Obtener el índice de fila por el nombre de la fila.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsIndex.go" >}}
