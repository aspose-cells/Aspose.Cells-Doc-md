---
title: 支持使用 C++ 在命名范围公式中支持德语区域设置
linktitle: 支持在命名范围公式中使用德国区域设置
type: docs
weight: 60
url: /zh/cpp/support-for-german-locale-in-named-range-formulae/
description: 学习如何使用 Aspose.Cells 与 C++ 处理德语区域的命名范围公式。
---

英语公式写入命名区域。该Excel文件可以在配置为德语区域的环境中打开，然而，英文公式会被翻译成德语。以下示例展示了该功能，但需要在德语环境下安装Excel且系统区域也设为德语。

您可以从以下链接下载测试此功能的示例文件：

[sampleNamedRangeTest.xlsm](73990165.xlsm)

```c++
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

    // Define the name and formula for the named range
    const U16String name(u"HasFormula");
    const U16String value(u"=GET.CELL(48, INDIRECT(\"ZS\",FALSE))");

    // Load the source workbook
    Workbook wbSource(srcDir + u"sampleNamedRangeTest.xlsm");

    // Get the worksheet collection
    WorksheetCollection wsCol = wbSource.GetWorksheets();

    // Add a new named range and get its index
    int32_t nameIndex = wsCol.GetNames().Add(name);

    // Get the named range by index
    Name namedRange = wsCol.GetNames().Get(nameIndex);

    // Set the formula for the named range
    namedRange.SetRefersTo(value);

    // Save the workbook with the new named range
    wbSource.Save(outDir + u"sampleOutputNamedRangeTest.xlsm");

    std::cout << "Named range added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
