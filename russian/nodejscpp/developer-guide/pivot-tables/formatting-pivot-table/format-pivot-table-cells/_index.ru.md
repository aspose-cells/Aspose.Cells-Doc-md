---
title: Форматирование ячеек сводной таблицы
type: docs
weight: 30
url: /ru/nodejs-cpp/format-pivot-table-cells/
description: Как форматировать ячейки сводной таблицы с помощью Aspose.Cells for Node.js via C++.
keywords: Форматирование ячеек сводной таблицы.
---

{{% alert color="primary" %}}

 Иногда нужно форматировать ячейки сводной таблицы. Например, применить цвет фона к ячейкам сводной таблицы. Aspose.Cells for Node.js via C++ предоставляет два метода [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) и [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-), которые можно использовать для этой цели.

[**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) применяет стиль ко всей сводной таблице, в то время как [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-) применяет стиль к одной ячейке сводной таблицы.

{{% /alert %}}
Следующий образец кода загружает [образец файла Excel](pivot_format.xlsx), который содержит две сводные таблицы, и выполняет операцию форматирования всей сводной таблицы и форматирования отдельных ячеек в сводной таблице.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FormatPivotTableCells-1.js" >}}

## Связанные статьи

- [Форматирование сводной таблицы](/cells/ru/nodejs-cpp/formatting-pivot-table/)
- [Работа с форматами отображения данных DataField в сводной таблице](/cells/ru/nodejs-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
