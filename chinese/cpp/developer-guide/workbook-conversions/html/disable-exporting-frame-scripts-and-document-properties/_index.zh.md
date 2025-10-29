---
title: 使用C++禁用导出帧脚本和文档属性
type: docs
weight: 310
url: /zh/cpp/disable-exporting-frame-scripts-and-document-properties/
description: 使用Aspose.Cells和C++禁用导出帧脚本与文档属性。
---

{{% alert color="primary" %}}

Aspose.Cells在将工作簿转换为HTML时，会导出框架脚本和文档属性。Aspose.Cells for C++的8.6.0版本引入了一个选项，可以选择性禁用框架脚本和文档属性的导出。请使用HtmlSaveOptions.ExportFrameScriptsAndProperties属性禁用导出。

{{% /alert %}}

## **禁用导出框架脚本和文档属性**

以下示例代码允许您禁用导出框架脚本和文档属性。一旦您将工作簿转换为HTML，输出文件将不包含任何框架脚本和文档属性。

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

    // Open the required workbook to convert
    U16String inputFilePath = srcDir + u"Sample1.xlsx";
    Workbook workbook(inputFilePath);

    // Disable exporting frame scripts and document properties
    HtmlSaveOptions options;
    options.SetExportFrameScriptsAndProperties(false);

    // Save workbook as HTML
    workbook.Save(outDir + u"output.out.html", options);

    std::cout << "Workbook saved successfully as HTML!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
