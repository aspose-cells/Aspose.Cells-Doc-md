---
title: Insertar o Eliminar Filas en una Hoja de Cálculo de Excel
type: docs
weight: 20
url: /es/python-net/insert-or-delete-rows-in-an-excel-worksheet/
description: Este artículo proporciona el código Python para insertar y eliminar filas en la hoja de cálculo de Excel con la biblioteca Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel Python, insertar o eliminar filas en una hoja de cálculo de Excel con Python, insertar o eliminar filas en Excel con Python, insertar filas en Excel con Python, eliminar filas en Excel con Python, insertar o eliminar filas en una hoja de cálculo de Excel con Python, insertar o eliminar filas en Excel con Python, insertar filas en Excel con Python, eliminar filas en Excel con Python
---

{{% alert color="primary" %}}

Al crear una hoja de cálculo nueva, o trabajar con una hoja de cálculo existente, es posible que necesite agregar filas o columnas adicionales para alojar datos. En otros momentos, es posible que necesite eliminar filas o columnas de posiciones específicas en la hoja de cálculo.

{{% /alert %}}

Aspose.Cells para Python via .NET ofrece dos métodos para insertar y eliminar filas: [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) y [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/). Estos métodos están optimizados para el rendimiento y realizan el trabajo muy rápidamente.

Para insertar o eliminar un número de filas, recomendamos que siempre use los métodos [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) y [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/) en lugar de usar los métodos [**Cells.insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row) o [**delete_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_row) en un bucle.

Aspose.Cells para Python via .NET funciona de la misma manera que lo hace Microsoft Excel. Cuando se agregan filas o columnas, el contenido de la hoja de cálculo se desplaza hacia abajo y hacia la derecha. Cuando se eliminan filas o columnas, el contenido de la hoja de cálculo se desplaza hacia arriba o hacia la izquierda. Cualquier referencia en otras hojas de cálculo y celdas se actualiza cuando se agregan o eliminan filas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertDeleteRows-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
