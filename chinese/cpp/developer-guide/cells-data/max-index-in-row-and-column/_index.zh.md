---
title: 用 C++ 获取行中的最大列索引和列中的最大行索引
linktitle: 获取行中最大列索引和列中最大行索引
type: docs
weight: 600
url: /zh/cpp/get-max-index-in-row-and-column/
description: 了解如何通过Aspose.Cells for C++ API获取行中的最大列索引和列中的最大行索引。
keywords: 获取行中最大列索引，获取列中最大行索引，获取行中最大数据列索引，获取列中最大数据行索引。
---

## **可能的使用场景**
当只需要操作某些行或列的数据范围时，需知道数据范围的起止范围。Aspose.Cells提供此功能。要获取某行的最大列索引，你可以使用[Row.GetLastCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/)和[Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)属性，然后用[Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)属性获取最大列索引和最大含数据列索引。而获得一列的最大行索引和最大数据行索引，则需在该列创建范围，遍历范围找到最后一个单元格，最后用[Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)属性获取行号。

Aspose.Cells 提供以下属性和方法，帮助您实现目标。
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)

## **使用 Aspose.Cells 获取行中的最大列索引和列中的最大行索引**
此示例演示如何：

1. 加载[示例文件](sample.xlsx)。
1. 获取需要获取最大列索引和最大数据列索引的行。
1. 获取[Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)属性。
1. 根据列创建一个范围。
1. 获取迭代器并遍历范围。
1. 获取[Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)属性。

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String filePath = srcDir + u"sample.xlsx";

    Workbook workbook(filePath);
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    Row row = cells.CheckRow(1);
    if (row)
    {
        std::cout << "Max column index in row: " << row.GetLastCell().GetColumn() << std::endl;
        std::cout << "Max data column index in row: " << row.GetLastDataCell().GetColumn() << std::endl;
    }

    Range columnRange = cells.CreateRange(1, 1, true);
    auto colIter = columnRange.GetEnumerator();

    int maxRow = 0;
    int maxDataRow = 0;

    while (colIter.MoveNext())
    {
        Cell currCell = colIter.GetCurrent();
        if (!currCell.GetStringValue().IsEmpty())
        {
            maxDataRow = currCell.GetRow();
        }
        if (!currCell.GetStringValue().IsEmpty() || currCell.GetHasCustomStyle())
        {
            maxRow = currCell.GetRow();
        }
    }

    std::cout << "Max row index in Column: " << maxRow << std::endl;
    std::cout << "Max data row index in Column: " << maxDataRow << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
