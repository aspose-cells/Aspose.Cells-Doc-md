---
title: 使用C++查找具有特定样式的单元格
linktitle: 查找具有特定样式的单元格
type: docs
weight: 190
url: /zh/cpp/find-cells-with-specific-style/
description: 学习如何使用Aspose.Cells for C++ API查找或搜索具有特定样式的单元格。
keywords: 查找应用了特定样式的单元格，搜索应用了特定样式的单元格
---

{{% alert color="primary" %}}

有时，您需要查找应用了特定样式的单元格。您可以使用 Aspose.Cells 查找所有具有相同样式的单元格。 Aspose.Cells 提供了 [**FindOptions.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/getstyle/) 属性，您可以使用它来指定要搜索具有样式的单元格。

{{% /alert %}}

此示例中的代码查找所有具有与A1单元格相同样式的单元格。在代码执行后，所有具有与A1相同样式的单元格将包含文本“找到”。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"TestBook.xlsx";

    Workbook workbook(filePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    FindOptions options;
    options.SetStyle(style);

    Cell nextCell;

    do
    {
        nextCell = worksheet.GetCells().Find(U16String(), nextCell, options);
        if (nextCell.GetRow() == -1)
            break;
        nextCell.PutValue(u"Found");
    } while (true);

    U16String outputPath = outDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
