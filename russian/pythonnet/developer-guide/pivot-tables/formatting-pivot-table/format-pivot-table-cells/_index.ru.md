---
title: Форматирование ячеек сводной таблицы
type: docs
weight: 30
url: /ru/python-net/format-pivot-table-cells/
description: Как форматировать ячейки сводной таблицы с помощью Aspose.Cells для Python via .NET.
keywords: Форматирование ячеек сводной таблицы.
---

{{% alert color="primary" %}}

Иногда вам может потребоваться форматировать ячейки сводной таблицы. Например, вы хотите применить цвет фона к ячейкам сводной таблицы. Aspose.Cells для Python via .NET предоставляет два метода [**PivotTable.format_all(style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) и [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/), которые можно использовать для этой цели.

[**PivotTable.format_all(style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) применяет стиль ко всей сводной таблице, в то время как [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/) применяет стиль к одной ячейке сводной таблицы.

{{% /alert %}}
Следующий образец кода загружает [образец файла Excel](pivot_format.xlsx), который содержит две сводные таблицы, и выполняет операцию форматирования всей сводной таблицы и форматирования отдельных ячеек в сводной таблице.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormatPivotTableCells-1.py" >}}

## Связанные статьи

- [Форматирование сводной таблицы](/cells/ru/python-net/formatting-pivot-table/)
- [Работа с форматами отображения данных DataField в сводной таблице](/cells/ru/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
{{< app/cells/assistant language="python-net" >}}
