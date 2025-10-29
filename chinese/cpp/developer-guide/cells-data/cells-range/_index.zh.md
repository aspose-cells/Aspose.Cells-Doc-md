---
title: 获取单元格范围与C++
linktitle: 获取单元格范围
type: docs
weight: 600
url: /zh/cpp/get-cells-range/
description: 学习如何通过Aspose.Cells for C++ API获取单元格范围。
keywords: 获取单元格的最大显示范围，获取单元格的最大行数，获取单元格的最大数据行数，获取单元格的最大列数，获取单元格的最大数据列数。
---

## **可能的使用场景**
当您只需要操作工作表上的一些数据时，您需要知道整个工作表的数据范围。Aspose.Cells提供了这一功能。Aspose.Cells提供以下属性和方法来帮助您实现您的目标。
- [**Cells.GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/)
- [**Cells.GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxrow/)
- [**Cells.GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/)
- [**Cells.GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/)
- [**Cells.GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/)

## **使用Aspose.Cells获取单元格范围**
此示例演示如何：

1. 创建一个工作簿。
1. 在第一个工作表中的单元格中添加数据。
1. 获取单元格 [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    cell = cells.Get(u"E10");
    Style temp = workbook.CreateStyle();
    temp.GetFont().SetColor(Color::Red());
    cell.SetStyle(temp);

    Range range = cells.GetMaxDisplayRange();

    std::cout << cells.GetMaxRow() << std::endl;
    std::cout << cells.GetMaxDataRow() << std::endl;
    std::cout << cells.GetMaxColumn() << std::endl;
    std::cout << cells.GetMaxDataColumn() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
