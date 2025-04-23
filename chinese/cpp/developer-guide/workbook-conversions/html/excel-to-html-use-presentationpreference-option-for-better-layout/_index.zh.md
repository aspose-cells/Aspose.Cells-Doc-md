---
title: Excel转HTML  使用PresentationPreference选项实现更佳布局，支持C++
linktitle: 将Excel转换为HTML  使用PresentationPreference选项以获得更好的布局
type: docs
weight: 220
url: /zh/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
description: 学习在使用C++保存Excel为HTML时实现更佳布局的方法。
---

{{% alert color="primary" %}} 

Aspose.Cells为需要在将Microsoft Excel文件保存为HTML或MHT格式时获得更好布局的开发人员提供了有用的HtmlSaveOptions.PresentationPreference属性。该属性的默认值为false。我们建议将此属性设置为true，以获得更有吸引力的Excel报告呈现。

{{% /alert %}} 

请参阅下面的示例代码，演示了如何使用幻灯片首选项渲染来自Excel报告的HTML文件。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Instantiate the Workbook and load an Excel file
    Workbook workbook(inputFilePath);

    // Create HtmlSaveOptions object
    HtmlSaveOptions options;

    // Set the Presentation preference option
    options.SetPresentationPreference(true);

    // Save the Excel file to HTML with specified option
    U16String outputFilePath = srcDir + u"outPresentationlayout1.out.html";
    workbook.Save(outputFilePath, options);

    std::cout << "Excel file saved as HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
