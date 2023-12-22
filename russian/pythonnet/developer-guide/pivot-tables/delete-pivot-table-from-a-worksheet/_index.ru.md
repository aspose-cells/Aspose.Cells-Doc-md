---
title: Удалить сводную таблицу с листа
type: docs
weight: 60
url: /ru/python-net/delete-pivot-table-from-a-worksheet/
description: Python via .NET код для удаления сводной таблицы для листов Excel
keywords: Python via .NET remove pivot table from worksheet, Python via .NET remove pivot table from excel, how to delete pivot table with Python via .NET, delete pivot table with Python via .NET, delete pivot table from excel with Python via .NET, Python via .NET delete pivot table, Python via .NET remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET предоставляет функцию удаления или удаления сводной таблицы с рабочего листа. Вы можете удалить сводную таблицу, используя объект сводной таблицы или позицию сводной таблицы. Пожалуйста, используйте[**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) метод удаления сводной таблицы с использованием объекта сводной таблицы и[**Worksheet.pivot_tables.remove_at(index, Keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)метод для удаления объекта сводной таблицы, используя его позицию внутри коллекции сводных таблиц.

{{% /alert %}}

 Следующий пример кода удаляет две сводные таблицы с листа. Сначала он удаляет сводную таблицу, используя[**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) метод, а затем удаляет сводную таблицу, используя[**Worksheet.pivot_tables.remove_at(index, Keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool) метод

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}
