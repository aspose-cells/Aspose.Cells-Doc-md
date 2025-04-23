---
title: 用 C++ 格式化数据透视表单元格
linktitle: 格式化数据透视表单元格
type: docs
weight: 30
url: /zh/cpp/format-pivot-table-cells/
description: 了解如何使用Aspose.Cells与C++格式化数据透视表单元格。
---

{{% alert color="primary" %}}

有时，您可能希望格式化数据透视表单元格。例如，您可能希望对数据透视表单元格应用背景颜色。Aspose.Cells提供了两种方法[**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/)和[**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/)，您可以用于此目的。

[**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) 将样式应用于整个数据透视表，而 [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) 将样式应用于数据透视表的单个单元格。

{{% /alert %}}

以下示例代码加载包含两个数据透视表的[示例Excel文件](pivot_format.xlsx)，实现对整个数据透视表的格式化和对数据透视表中单个单元格的格式化操作。

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

## 相关文章

- [格式化数据透视表](/cells/zh/cpp/formatting-pivot-table/)
- [在数据透视表的DataField中使用数据显示格式](/cells/zh/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
