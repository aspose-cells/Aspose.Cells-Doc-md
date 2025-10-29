---
title: 将工作表转换为图像——去除数据周围的空白区域，使用C++
linktitle: 将工作表转换为图像——去除数据周围的空白区域
type: docs
weight: 40
url: /zh/cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: 学习如何将工作表转换为图像并去除数据周围的空白区域，使用Aspose.Cells for C++。
---

{{% alert color="primary" %}}

有时，您需要在应用程序或网页中呈现工作表图像。例如，您可能需要将图像插入 Word 文档、PDF 文件、PowerPoint 演示文稿或其他文档中。基本上，您希望将工作表呈现为图像，以便将其粘贴到其他应用程序中。Aspose.Cells 允许您将 Microsoft Excel 工作表转换为图像。

{{% /alert %}}

## **删除数据周围的空白**

[**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) API 可将工作表转换为带有任何指定属性（例如图像格式、分页工作表等）的图像文件。支持多种图像格式，包括 BMP、GIF、JPG、TIFF 和 EMF。

在使用工作表转图片功能时，输出图像默认会有空白边框。可以通过将源工作表的顶部、底部、左侧和右侧页边距设置为0，并相应指定 [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) 属性来去除这些空白。

以下代码片段删除输出图像中的数据周围的空白。

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

    // Open the template file
    Workbook book(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Define LoadOptions and set LoadFilter
    LoadOptions options;
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All));

    // Specify your print area if you want
    // sheet.GetPageSetup().SetPrintArea(u"A1:H8");

    // To remove the white border around the image.
    sheet.GetPageSetup().SetLeftMargin(0);
    sheet.GetPageSetup().SetRightMargin(0);
    sheet.GetPageSetup().SetBottomMargin(0);
    sheet.GetPageSetup().SetTopMargin(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Emf);

    // Set only one page would be rendered for the image
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetPrintingPage(PrintingPageType::IgnoreBlank);

    // Create the SheetRender object based on the sheet with its
    // ImageOrPrintOptions attributes
    SheetRender sr(sheet, imgOptions);

    // Convert the image
    sr.ToImage(0, outDir + u"outputRemoveWhitespaceAroundData.emf");

    std::cout << "Image converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
