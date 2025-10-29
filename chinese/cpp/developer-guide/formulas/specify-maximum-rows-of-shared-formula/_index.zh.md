---
title: 用 C++ 指定共享公式的最大行数
linktitle: 指定共享公式的最大行数
type: docs
weight: 40
url: /zh/cpp/specify-maximum-rows-of-shared-formula/
description: 学习如何用 Aspose.Cells for C++ 在 Excel 文件中指定共享公式的最大行数。
---

## **可能的使用场景**

默认的共享公式最大行数是 64，也可以是任何数字，例如 1000。不同的行数会影响共享公式的性能。因此，Aspose.Cells 提供了 [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/) 属性，可以用来设置最大行数。如果共享公式的总行数超过此值，它会被拆分成多个共享公式，如下面的截图所示。

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **指定共享公式的最大行数**

以下示例代码演示了 [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/) 属性的用法。它将共享公式的最大行数设置为 5，并在单元格 D1 中设置 100 行的共享公式，并保存为 [输出 Excel 文件](61767856.xlsx)。如果你解压输出文件的内容并查看 *sheet1.xml*，会看到共享公式在每隔 5 行后就会拆分，如上图所示。

## **示例代码**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Set the max rows of shared formula to 5
    wb.GetSettings().SetMaxRowsOfSharedFormula(5);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell D1
    Cell cell = ws.GetCells().Get(u"D1");

    // Set the shared formula in 100 rows
    cell.SetSharedFormula(u"=Sum(A1:A2)", 100, 1);

    // Save the output Excel file
    wb.Save(u"outputSpecifyMaximumRowsOfSharedFormula.xlsx");

    std::cout << "Shared formula set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
