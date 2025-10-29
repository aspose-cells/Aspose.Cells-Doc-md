---
title: 使用C++剪切并粘贴范围
linktitle: 剪切和粘贴范围
type: docs
weight: 130
url: /zh/cpp/cut-and-paste-cells/
description: 学习如何使用Aspose.Cells for C++在工作表内剪切和粘贴单元格。
---

## **剪切和粘贴单元格**

Aspose.Cells允许你通过使用[**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/)方法和[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合中的[**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/)方法在工作表中剪切粘贴单元格，参数如下：

- [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)：要剪切的单元格范围。
- 行索引：要插入单元格的行索引。
- 列索引：要插入单元格的列索引。
- [**ShiftType**](https://reference.aspose.com/cells/cpp/aspose.cells/shifttype/)：列的移动方向。

以下示例展示了如何在工作表中剪切和粘贴单元格。

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(0, 2).SetValue(1);
    worksheet.GetCells().Get(1, 2).SetValue(2);
    worksheet.GetCells().Get(2, 2).SetValue(3);
    worksheet.GetCells().Get(2, 3).SetValue(4);

    Range namedRange = worksheet.GetCells().CreateRange(0, 2, 3, 1);
    namedRange.SetName(u"NamedRange");

    Range cut = worksheet.GetCells().CreateRange(u"C:C");

    worksheet.GetCells().InsertCutCells(cut, 0, 1, ShiftType::Right);

    workbook.Save(outDir + u"CutAndPasteCells.xlsx");

    std::cout << "Cells cut and pasted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
