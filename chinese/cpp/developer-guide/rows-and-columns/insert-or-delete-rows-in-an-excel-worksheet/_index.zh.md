---
title: 在C++中插入或删除Excel工作表中的行
linktitle: 插入或删除行
type: docs
weight: 20
url: /zh/cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: 本文提供在Excel工作表中插入和删除行的C++代码。
keywords: 在Excel中用C++插入或删除行，插入或删除Excel中的行，插入行到Excel，删除Excel中的行，使用C++在Excel工作表中插入或删除行，使用C++在Excel中插入或删除行，使用C++在Excel中插入行，使用C++删除Excel中的行
---

{{% alert color="primary" %}}

在创建新工作表或处理现有工作表时，您可能需要添加额外的行或列以容纳数据。其他时候，您可能需要从工作表中指定位置删除行或列。

{{% /alert %}}

Aspose.Cells提供了两种插入和删除行的方法：[**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)和[**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)。这些方法经过了性能优化，非常快速地完成工作。

要插入或删除多行，我们建议始终使用[**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)和[**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)方法，而不是在循环中使用[**Cells.InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)或[**DeleteRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterow/)方法。

Aspose.Cells的工作方式与Microsoft Excel相同。当添加行或列时，工作表内容向下和向右移动。当删除行或列时，工作表内容向上或向左移动。添加或删除行时，其他工作表和单元格中的引用会得到更新。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_book1.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Insert 10 rows at row index 2 (insertion starts at 3rd row)
    sheet.GetCells().InsertRows(2, 10);

    // Delete 5 rows now. (8th row - 12th row)
    sheet.GetCells().DeleteRows(7, 5);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted and deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
