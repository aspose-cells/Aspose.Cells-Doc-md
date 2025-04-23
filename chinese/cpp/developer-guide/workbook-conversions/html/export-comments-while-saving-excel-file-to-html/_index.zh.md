--- 
title: 使用C++导出评论并保存Excel文件为HTML 
linktitle: 导出Excel文件为HTML时导出注释 
type: docs 
weight: 40 
url: /zh/cpp/export-comments-while-saving-excel-file-to/ 
description: 了解如何使用Aspose.Cells结合C++导出保存Excel文件到HTML时的评论。 
--- 

## **可能的使用场景**

将Excel保存为HTML时，评论不会被导出。但是，Aspose.Cells通过[**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/)属性提供此功能。如果将其设置为**true**，HTML中也会显示Excel文件中的评论。

## **在将 Excel 文件保存为 HTML 时导出批注**

下面的示例代码演示了[**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/)属性的用法。截图显示将其设置为**true**时，HTML的效果。请下载[示例Excel文件](50528260.xlsx)和[生成的HTML](5052826.txt)以供参考。

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleExportCommentsHTML.xlsx";
    Workbook workbook(inputFilePath);

    // Export comments - set IsExportComments property to true
    HtmlSaveOptions opts;
    opts.SetIsExportComments(true);

    // Save the Excel file to HTML
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outputDir + u"outputExportCommentsHTML.html", opts);

    std::cout << "Excel file exported to HTML with comments successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
