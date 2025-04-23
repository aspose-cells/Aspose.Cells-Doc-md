---
title: 防止在使用C++保存为HTML时导出隐藏的工作表内容
linktitle: 防止导出隐藏的工作表内容
type: docs
weight: 210
url: /zh/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: 学习如何在使用Aspose.Cells for C++将Excel工作簿保存为HTML时防止导出隐藏内容。
---

{{% alert color="primary" %}}

您可以将 Excel 工作簿保存为 HTML。但是，如果工作簿包含隐藏的工作表，则 Aspose.Cells 默认情况下会将隐藏的工作表内容导出到 HTML 输出的 (_files) 目录中，该目录包含诸如工作表、图像、tabstrip.htm、stylesheet.css 等文件。有时，以这种方式导出隐藏的工作表内容是不合适的。例如，如果隐藏的工作表包含不应导出到 _files 目录的图像。

{{% /alert %}}

Aspose.Cells提供[**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexporthiddenworksheet/) 属性。默认情况下，它设置为**true**并且将隐藏的工作表导出为HTML。如果将其设置为**false**，Aspose.Cells将不会导出隐藏的工作表内容。

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
    U16String inputFilePath = srcDir + u"WorkbookWithHiddenContent.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"HtmlWithoutHiddenContent_out.html";

    // Create workbook object
    Workbook workbook(inputFilePath);

    // Create HTML save options
    HtmlSaveOptions options;

    // Do not export hidden worksheet contents
    options.SetExportHiddenWorksheet(false);

    // Save the workbook
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully without hidden content!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
