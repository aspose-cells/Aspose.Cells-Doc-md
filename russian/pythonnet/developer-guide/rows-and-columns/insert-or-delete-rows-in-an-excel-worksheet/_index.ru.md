---
title: Вставка или удаление строк в рабочем листе Excel
type: docs
weight: 20
url: /ru/python-net/insert-or-delete-rows-in-an-excel-worksheet/
description: В этой статье предоставлен код на Python для вставки и удаления строк в листе Excel с использованием библиотеки Aspose.Cells для Python via .NET.
keywords: Библиотека Python Excel, вставка или удаление строк в таблице Excel с помощью Python, вставка или удаление строк в Excel с помощью Python, вставка строк в Excel с помощью Python, удаление строк в Excel с помощью Python, вставка или удаление строк в таблице Excel с помощью Python, вставка или удаление строк в Excel с помощью Python, вставка строк в Excel с помощью Python, удаление строк в Excel с помощью Python
---

{{% alert color="primary" %}}

При создании нового рабочего листа или работы с существующим листом в Excel вам может понадобиться добавить дополнительные строки или столбцы для размещения данных. В других случаях может потребоваться удалить строки или столбцы из указанных позиций на листе.

{{% /alert %}}

Aspose.Cells для Python via .NET предлагает два метода для вставки и удаления строк: [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) и [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/). Эти методы оптимизированы для производительности и выполняют задачу очень быстро.

Для вставки или удаления нескольких строк рекомендуем всегда использовать методы [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) и [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/), вместо использования методов [**Cells.insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row) или [**delete_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_row) в цикле.

Aspose.Cells для Python via .NET работает так же, как делает Microsoft Excel. При добавлении строк или столбцов содержимое листа переносится вниз и вправо. При удалении строк или столбцов содержимое переносится вверх или влево. Любые ссылки в других листах и ячейках обновляются при добавлении или удалении строк.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertDeleteRows-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
