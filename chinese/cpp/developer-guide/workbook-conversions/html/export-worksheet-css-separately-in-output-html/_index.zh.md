---
title: 在输出的HTML中单独导出工作表CSS
linktitle: 在输出 HTML 中单独导出工作表 CSS
type: docs
weight: 80
url: /zh/cpp/export-worksheet-css-separately-in-output/
description: 了解如何在将Excel文件转换为HTML时，将工作表的CSS单独导出，使用编号Aspose.Cells for C++。
---

## **可能的使用场景**

Aspose.Cells支持在转换Excel为HTML时单独导出工作表CSS。请使用[**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/)属性实现这个功能，并在保存Excel为HTML格式时将其设置为**true**。

## **在输出 HTML 中单独导出工作表 CSS**

下面的示例代码创建一个 Excel 文件，在单元格 **B5** 中添加一些红色文本，然后使用 [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/) 属性将其保存为 HTML 格式。请参考代码生成的[output HTML](60489766.zip)。您将在其中找到名为  **stylesheet.css** 的结果。

## **示例代码**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and put value inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This is some text.");

    // Set the style of the cell - font color is Red
    Style st = cell.GetStyle();
    st.GetFont().SetColor(Color::Red());
    cell.SetStyle(st);

    // Specify html save options - export worksheet css separately
    HtmlSaveOptions opts;
    opts.SetExportWorksheetCSSSeparately(true);

    // Save the workbook in html
    wb.Save(u"outputExportWorksheetCSSSeparately.html", opts);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **导出单个工作簿到HTML**

当带有多个工作表的工作簿转换为HTML时，Aspose.Cells会创建一个HTML文件以及一个包含CSS和多个HTML文件的文件夹。打开该HTML文件时，标签可见。对于单个工作表的工作簿，也需要实现相同的行为。当转换为HTML时，之前未为单个工作表工作簿创建单独的文件夹，只创建了一个HTML文件。此HTML文件在浏览器中打开时不会显示标签。MS Excel也会为单个工作表创建正确的文件夹和HTML，因此使用Aspose.Cells API实现了相同的行为。可以从以下链接下载样本文件以供下面示例代码使用：

[sampleSingleSheet.xlsx](79527937.xlsx)

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
    U16String inputFilePath = srcDir + u"sampleSingleSheet.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputSampleSingleSheet.htm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify HTML save options
    HtmlSaveOptions options;

    // Set optional settings
    options.SetEncoding(EncodingType::UTF8);
    options.SetExportImagesAsBase64(true);
    options.SetExportGridLines(true);
    options.SetExportSimilarBorderStyle(true);
    options.SetExportBogusRowData(true);
    options.SetExcludeUnusedStyles(true);
    options.SetExportHiddenWorksheet(true);

    // Save the workbook in HTML format with specified HTML save options
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
