---
title: Convert Worksheet to Image - Remove Whitespace around Data with C++
linktitle: Convert Worksheet to Image - Remove Whitespace around Data
type: docs
weight: 40
url: /cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Learn how to convert a worksheet to an image and remove whitespace around the data using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you need to present worksheet images in applications or web pages. For example, you might need to insert images into a Word document, a PDF file, a PowerPoint presentation, or some other document. Basically, you want to render a worksheet as an image so that it can be pasted into other applications. Aspose.Cells allows you to convert Microsoft Excel worksheets to images.

{{% /alert %}}

## **Remove Whitespace around Data**

The [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) API converts a worksheet to an image file with any specified attributes, for example, image format, paginated sheets, etc. Several image formats are supported, including BMP, GIF, JPG, TIFF, and EMF.

When you use the sheet-to-image feature, the output image has whitespace, that is, a border, around it by default. You can remove this by setting the top, bottom, left, and right page setup margins for the source worksheet to 0 and specify [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) attributes accordingly.

The following code snippet removes the whitespace around the data in the output image.

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
