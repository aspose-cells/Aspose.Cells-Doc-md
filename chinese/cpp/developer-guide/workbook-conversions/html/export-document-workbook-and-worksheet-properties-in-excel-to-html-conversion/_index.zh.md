---
title: 使用C++导出Excel的文档工作簿和工作表属性到HTML
linktitle: 导出Excel中的文档工作簿和工作表属性到HTML
type: docs
weight: 50
url: /zh/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: 学习如何在将Excel文件转换为HTML时导出或避免导出文档、工作簿和工作表属性，使用编号Aspose.Cells for C++。
---

## **可能的使用场景**

当使用Microsoft Excel或Aspose.Cells导出Excel为HTML时，它还会导出各种类型的文档、工作簿和工作表属性，如下截图所示。可以通过将[**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportdocumentproperties/)、[**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/)和[**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/)设置为**false**来避免导出这些属性。这些属性的默认值是**true**。下图显示了导出HTML中这些属性的样子。

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **将Excel中的文档、工作簿和工作表属性导出为HTML**

下方示例代码加载【示例Excel文件】(61767776.xlsx)，并将其转换为HTML，未导出文档、工作簿及工作表属性，输出的HTML文件为(61767779.zip)。

## **示例代码**

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleExportDocumentWorkbookAndWorksheetPropertiesInHTML.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html";

    // Load the sample Excel file
    Workbook workbook(inputFilePath);

    // Specify Html Save Options
    HtmlSaveOptions options;

    // We do not want to export document, workbook and worksheet properties
    options.SetExportDocumentProperties(false);
    options.SetExportWorkbookProperties(false);
    options.SetExportWorksheetProperties(false);

    // Export the Excel file to Html with Html Save Options
    workbook.Save(outputFilePath, options);

    std::cout << "Excel file exported to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
