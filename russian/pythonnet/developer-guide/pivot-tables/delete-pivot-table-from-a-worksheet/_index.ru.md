---
title: Удалить сводную таблицу из листа
type: docs
weight: 60
url: /ru/python-net/delete-pivot-table-from-a-worksheet/
description: Код Python via .NET для удаления сводной таблицы из электронных таблиц Excel
keywords: Aspose.Cells для Python Excel, библиотека Excel Python, Python via .NET удалить сводную таблицу из электронной таблицы, Python via .NET удалить сводную таблицу из Excel, как удалить сводную таблицу с использованием Python via .NET, удалить сводную таблицу с использованием Python via .NET, удалить сводную таблицу из Excel с использованием Python via .NET, Python via .NET удалить сводную таблицу, Python via .NET удалить сводную таблицу, удалить сводную таблицу, удалить сводную таблицу, как удалить сводную таблицу
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET предоставляет возможность удалить или удалить сводную таблицу из электронной таблицы. Вы можете удалить сводную таблицу, используя объект сводной таблицы или позицию сводной таблицы. Пожалуйста, используйте метод [**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) для удаления сводной таблицы с использованием объекта сводной таблицы и метод [**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool) для удаления объекта сводной таблицы по его позиции в коллекции сводных таблиц.

{{% /alert %}}

## **Как удалить сводную таблицу из электронной таблицы с использованием библиотеки Aspose.Cells для Excel Python**

В следующем примере кода удаляются две сводные таблицы с листа. Сначала удаляется сводная таблица, используя метод [**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/), а затем удаляется сводная таблица, используя метод [**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}
{{< app/cells/assistant language="python-net" >}}
