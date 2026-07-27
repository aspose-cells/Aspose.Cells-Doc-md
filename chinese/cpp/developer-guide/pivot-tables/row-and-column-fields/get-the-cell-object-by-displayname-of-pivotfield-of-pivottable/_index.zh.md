---
title: 通过数据透视表的 PivotField 的显示名称获取单元格对象（C++）
linktitle: 通过数据透视表的 PivotField 的显示名称获取单元格对象
type: docs
weight: 70
url: /zh/cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: 学习如何通过数据透视字段的显示名称检索单元格对象并应用格式，使用 Aspose.Cells for C++。
---

{{% alert color="primary" %}}

Aspose.Cells 提供了 [**PivotTable::GetCellByDisplayName()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getcellbydisplayname/) 方法，可以通过数据透视字段的显示名称访问单元格对象。此方法在需要突出显示或格式化数据透视表标题时非常有用。本文详细介绍了如何通过数据字段的显示名称检索单元格对象，然后进行格式化。

{{% /alert %}}

## **用 C++ 通过数据透视表的 PivotField 的显示名称获取单元格对象**

以下代码访问工作表的第一个数据透视表，并根据数据透视表的第二个数据字段的显示名称检索单元格。然后，将单元格的填充颜色设为浅蓝色，字体颜色设为黑色。以下为执行前后数据透视表的效果截图。

|**透视表 - 在之前**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"source.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    Cell cell = pivotTable.GetCellByDisplayName(pivotTable.GetDataFields().Get(0).GetDisplayName());

    Style style = cell.GetStyle();
    style.SetForegroundColor(Color::LightBlue());
    style.GetFont().SetColor(Color::Black());

    pivotTable.Format(cell.GetRow(), cell.GetColumn(), style);
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Pivot table formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

|**透视表 - 在之后**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
{{< app/cells/assistant language="cpp" >}}
