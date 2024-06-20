---
title: Obtener el índice de columna máximo en fila y el índice de fila máximo en columna
type: docs
weight: 600
url: /es/python-net/get-max-index-in-row-and-column/
description: Aprenda cómo obtener el índice de columna máximo en una fila y el índice de fila máximo en una columna a través de la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel para Python, Obtener índice de columna máximo en fila en Python, Obtener índice de fila máximo en columna en Python, Obtener índice de columna de datos máximo en fila en Python, Obtener índice de fila de datos máximo en columna en Python. 
---

## **Escenarios de uso posibles**
Cuando solo necesita manipular algunos datos en las filas o columnas, necesita conocer el rango de datos de las filas y columnas. Aspose.Cells para Python via .NET ofrece esta característica. Para obtener el índice de columna máximo en una fila, puede obtener las propiedades [Row.last_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/) y [Row.last_data_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/), y luego usar la propiedad [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) para obtener el índice de columna máximo e índice de columna de datos máximo. Pero para obtener el índice de fila máximo e índice de fila de datos máximo en una columna, necesita crear un rango en la columna, luego recorrer el rango para encontrar la última celda, y finalmente obtener el atributo [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/) en la celda.

Aspose.Cells para Python via .NET proporciona las siguientes propiedades y métodos para ayudarlo a alcanzar sus objetivos.
- [**Row.last_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/)
- [**Row.last_data_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/)
- [**Cell.column**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/)
- [**Cell.row**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/)

## **Obtener el índice de columna máximo en fila y el índice de fila máximo en columna usando la biblioteca de Excel de Python de Aspose.Cells**
Este ejemplo muestra cómo:

1. Cargar el [archivo de muestra](sample.xlsx).
1. Obtener la fila que necesita obtener el índice de columna máximo e índice de columna de datos máximo.
1. Obtener el atributo [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) en la celda.
1. Crear un rango basado en la columna.
1. Obtener el iterador y recorrer el rango.
1. Obtener el atributo [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/) en la celda.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Cells-max-index-of-row-and-column.py" >}}
