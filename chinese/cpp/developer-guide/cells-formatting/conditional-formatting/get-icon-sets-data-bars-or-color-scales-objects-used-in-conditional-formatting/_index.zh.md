---
title: 获取条件格式中使用的图标集、数据条或颜色比例对象（适用于C++）
linktitle: 获取图标集、数据条或颜色刻度对象
description: Aspose.Cells for C++ 是一个用于操作电子表格文件的库。它支持在条件格式中使用图标集、数据条和颜色刻度对象以显示电子表格中的数据。本文介绍如何使用 Aspose.Cells 库获取这些对象的数据。
keywords: Aspose.Cells, 条件格式, 图标集, 数据条, 颜色刻度, 电子表格
type: docs
weight: 10
url: /zh/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}} 

有时，你需要检索单元格或一组单元格中的条件格式所用的图标集，并基于它创建一个图像文件。你可能需要读取条件格式中使用的数据条或颜色刻度。Aspose.Cells for C++ 支持此功能。

{{% /alert %}} 

以下示例代码显示如何读取用于条件格式的图标集。通过 Aspose.Cells 简单的 API，图标集的图像数据将被保存为图像。

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell cell = sheet.GetCells().Get(u"A1");

    // Get the conditional formatting result object
    ConditionalFormattingResult cfr = cell.GetConditionalFormattingResult();

    // Get the icon set
    ConditionalFormattingIcon icon = cfr.GetConditionalFormattingIcon();

    // Get the image data from the icon
    Vector<uint8_t> imageData = icon.GetImageData();

    // Create the image file based on the icon's image data
    ofstream outputFile((outDir + u"imgIcon.out.jpg").ToUtf8(), ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Icon image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
