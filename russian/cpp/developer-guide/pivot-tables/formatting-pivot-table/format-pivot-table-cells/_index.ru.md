---
title: Форматирование ячеек сводной таблицы с помощью C++
linktitle: Форматирование ячеек сводной таблицы
type: docs
weight: 30
url: /ru/cpp/format-pivot-table-cells/
description: Узнайте, как форматировать ячейки сводной таблицы с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Иногда вам нужно форматировать ячейки сводной таблицы. Например, вы хотите применить цвет фона к ячейкам сводной таблицы. Aspose.Cells предоставляет два метода [**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) и [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/), которые можно использовать для этой цели.

[**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) применяет стиль ко всей сводной таблице, а [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) — к отдельной ячейке сводной таблицы.

{{% /alert %}}

Следующий пример кода загружает [образец файла Excel](pivot_format.xlsx), содержащий две сводные таблицы, и выполняет операции форматирования всей сводной таблицы и отдельных ячеек в сводной таблице.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook(u"pivot_format.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(u"Sheet1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(1);

    Style style = workbook.CreateStyle();
    style.SetPattern(BackgroundType::Solid);
    style.SetBackgroundColor(Color::LightBlue());
    pivotTable.FormatAll(style);

    style = workbook.CreateStyle();
    style.SetPattern(BackgroundType::Solid);
    style.SetBackgroundColor(Color::Yellow());

    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(0);
    pivotTable2.Format(16, 5, style);

    workbook.Save(u"out.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Связанные статьи

- [Форматирование сводной таблицы](/cells/ru/cpp/formatting-pivot-table/)
- [Работа с форматами отображения данных DataField в сводной таблице](/cells/ru/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
