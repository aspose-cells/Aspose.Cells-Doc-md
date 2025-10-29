---
title: 使用Aspose.Cells和C++将文本转换为列
linktitle: 将文本转换为列
type: docs
weight: 30
url: /zh/cpp/convert-text-to-columns-using-aspose-cells/
description: 学习如何在Excel文件中使用Aspose.Cells for C++将文本转换为列。
---

## **可能的使用场景**

您可以使用Microsoft Excel将文本转换为列。此功能可从*数据*选项卡下的*数据工具*中获取。为了将一列的内容拆分为多个列，数据应包含特定的分隔符，例如逗号（或其他字符），Microsoft Excel根据其将单元格的内容拆分为多个单元格。Aspose.Cells还提供了通过[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/)方法实现此功能。

## **使用Aspose.Cells将文本转换为列**

以下示例代码说明了[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/)方法的用法。代码首先在第一个工作表的A列添加一些人名。姓氏和名字之间用空格字符隔开。然后对A列应用[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/)方法，并将其保存为输出Excel文件。如果你打开【输出Excel文件】(25395213.xlsx)，你将看到，名字在A列，姓氏在B列，如截图所示。

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

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

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add people name in column A. Fast name and Last name are separated by space.
    ws.GetCells().Get(u"A1").PutValue(u"John Teal");
    ws.GetCells().Get(u"A2").PutValue(u"Peter Graham");
    ws.GetCells().Get(u"A3").PutValue(u"Brady Cortez");
    ws.GetCells().Get(u"A4").PutValue(u"Mack Nick");
    ws.GetCells().Get(u"A5").PutValue(u"Hsu Lee");

    // Create text load options with space as separator
    TxtLoadOptions opts;
    opts.SetSeparator(u' ');

    // Split the column A into two columns using TextToColumns() method
    // Now column A will have first name and column B will have second name
    ws.GetCells().TextToColumns(0, 0, 5, opts);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputTextToColumns.xlsx");

    std::cout << "Text to columns conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
