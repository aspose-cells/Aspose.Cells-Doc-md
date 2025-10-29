---
title: 导出数据棒、颜色刻度和图标集条件格式时的Excel转HTML，支持C++
linktitle: 导出条件格式为HTML
type: docs
weight: 30
url: /zh/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
description: 学习在使用 Aspose.Cells for C++ 将Excel文件转换为HTML时，导出数据条、颜色刻度和图标集条件格式。
---

{{% alert color="primary" %}} 

你可以在转换Excel文件为HTML时导出数据棒、颜色刻度和图标集条件格式。此特性能被Microsoft Excel部分支持，但Aspose.Cells for C++支持完整导出。

{{% /alert %}} 

## **在Excel转HTML时导出数据棒、颜色刻度和图标集条件格式**
下方截图显示了带有数据条、颜色刻度和图标集条件格式的【示例Excel文件】(5115558.xlsx)。你可以通过提供的链接下载【示例Excel文件】(5115558.xlsx)。

![todo:image_alt_text](conversion_1.png)

下方截图显示了Aspose.Cells输出的HTML文件，展示了数据条、颜色刻度和图标集条件格式。如你所见，它与【示例Excel文件】(5115558.xlsx)完全一致。

![todo:image_alt_text](conversion_2.png)

### **示例代码**
以下示例代码将示例Excel文件转换为HTML，这只是一次普通的【Excel转HTML转换】(/cells/zh/cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml)。

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
    U16String filePath = srcDir + u"sample.xlsx";

    // Load your sample excel file in a workbook object
    Workbook wb(filePath);

    // Save it in HTML format
    wb.Save(outDir + u"ConvertingToHTMLFiles_out.html", SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
