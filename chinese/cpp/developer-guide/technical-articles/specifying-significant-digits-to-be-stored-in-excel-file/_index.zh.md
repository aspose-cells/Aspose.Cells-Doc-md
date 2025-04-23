---
title: 用C++在Excel文件中指定存储的有效数字
linktitle: 指定有效数字
type: docs
weight: 30
url: /zh/cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: 学习如何使用Aspose.Cells与C++在Excel文件中指定存储的有效数字。
---

## **可能的使用场景**

默认情况下，Aspose.Cells在Excel文件中存储双精度数值时保留17位有效数字，不同于MS-Excel只存储15位有效数字。你可以使用[**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/)属性将Aspose.Cells的默认行为从17位改为15位。

## **指定要在Excel文件中存储的有效数字**

以下示例代码在将双精度值存储到Excel文件时强制使用15位有效数字。请检查[输出Excel文件](22774105.xlsx)，将其扩展名改为.zip并解压，即可见文件只存储了15位有效数字。下方截图说明[**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/)属性对输出文件的影响。

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **示例代码**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // By default, Aspose.Cells stores 17 significant digits unlike
    // MS-Excel which stores only 15 significant digits
    CellsHelper::SetSignificantDigits(15);

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell c = worksheet.GetCells().Get(u"A1");

    // Put double value, only 15 significant digits as specified by
    // CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
    c.PutValue(1234567890.123451711);

    // Save the workbook
    workbook.Save(outDir + u"out_SignificantDigits.xlsx");

    std::cout << "Workbook saved successfully with significant digits set to 15!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
