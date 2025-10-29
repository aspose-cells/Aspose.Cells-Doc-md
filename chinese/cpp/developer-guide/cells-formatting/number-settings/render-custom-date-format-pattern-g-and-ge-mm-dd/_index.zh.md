---
title: 使用C++渲染自定义日期格式g和ge mm dd
description: Aspose.Cells是一个支持使用自定义日期格式 g 和 ge 渲染日期的C++库。本文将描述如何使用Aspose.Cells库渲染自定义日期格式，以便用户可以控制日期的显示方式。
keywords: Aspose.Cells，C++库，电子表格，自定义日期格式，渲染， g 模式， ge 模式，控制显示
type: docs
weight: 160
url: /zh/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/
---

{{% alert color="primary" %}}

Aspose.Cells现在能够呈现类似于g、ge.mm.dd等自定义日期格式模式。请查看附加的源Excel文件(5112361.xlsx)和Aspose.Cells转换的PDF(5112360.pdf)作为参考。

{{% /alert %}}

下面的示例代码将转换包含类似于g和ge.mm.dd的自定义格式模式的源Excel文件(5112361.xlsx)成为输出PDF(5112360.pdf)。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from an existing Excel file
    U16String inputFilePath = srcDir + u"SourceFile.xlsx";
    Workbook workbook(inputFilePath);

    // Save the Excel file as PDF
    workbook.Save(outDir + u"CustomDateFormat_out.pdf");

    std::cout << "File saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
