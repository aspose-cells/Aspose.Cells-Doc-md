---
title: 使用C++在输出PDF中渲染Unicode补充字符
linktitle: 渲染 Unicode 辅助字符
type: docs
weight: 350
url: /zh/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: 了解如何使用 Aspose.Cells for C++ 在输出 PDF 中渲染 Unicode 辅助字符。
---

{{% alert color="primary" %}}

普通的Unicode字符长为2个字节，而Unicode补充字符长为4个字节。Aspose.Cells现在支持呈现这些4字节Unicode字符。

在Unicode字符标准中，补充字符是指分配的代码点范围从U+10000到U+10FFFF。换句话说，这些是大于U+FFFF的Unicode字符。

- 在UTF-8中，这些字符每个都是4个字节长。
- 在UTF-16中，这些字符需要2个代理对（16位单位）。

{{% /alert %}}

## 通过Aspose.Cells在输出PDF中渲染Unicode补充字符

以下屏幕截图显示了Aspose.Cells如何将[源Excel文件](5115563.xlsx)渲染成[输出PDF](5115564.pdf)。您可以看到，所有三个Unicode补充字符都与由Microsoft Excel执行的渲染完全相同。

![todo:image_alt_text](output.png)

## 示例代码

您可以使用此示例代码将[源Excel文件](5115563.xlsx)转换为[输出PDF](5115564.pdf)。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"unicode-supplementary-characters.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"RenderUnicodeInOutput_out.pdf";

    // Load the source excel file containing Unicode Supplementary characters
    Workbook wb(inputFilePath);

    // Save the workbook as PDF
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully with Unicode Supplementary characters!" << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
