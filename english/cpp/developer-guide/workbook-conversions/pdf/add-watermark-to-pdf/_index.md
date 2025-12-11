---  
title: Add Watermark To PDF with C++  
linktitle: Add Watermark To PDF  
type: docs  
weight: 9  
url: /cpp/add-watermark-to-pdf/  
description: Learn how to add text and image watermarks to PDF files while rendering using Aspose.Cells with C++.  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

While converting an Excel file to PDF, you may have a requirement to add a watermark to the PDF file. The following examples show how to add text and image watermarks to PDF while rendering.  

## **Add text watermark to PDF**  

You can easily add a text watermark to a PDF by specifying the text and the corresponding font. Also, you can set alignment, offset, rotation, opacity, foreground/background, and scale to the page in [RenderingWatermark](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/renderingwatermark/).  

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Prepare a workbook with 3 pages.
    Workbook wb;
    wb.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"Page1");
    int index = wb.GetWorksheets().Add();
    wb.GetWorksheets().Get(index).GetCells().Get(u"A1").PutValue(u"Page2");
    index = wb.GetWorksheets().Add();
    wb.GetWorksheets().Get(index).GetCells().Get(u"A1").PutValue(u"Page3");
    wb.GetWorksheets().Get(index).GetPageSetup().SetPaperSize(PaperSizeType::PaperA3);

    // Create a font for watermark, and specify bold, italic, color.
    RenderingFont font(u"Calibri", 68);
    font.SetItalic(true);
    font.SetBold(true);
    font.SetColor(Color::Blue());

    // Create a watermark from text and the specified font.
    RenderingWatermark watermark(u"Watermark", font);

    // Specify horizontal and vertical alignment.
    watermark.SetHAlignment(TextAlignmentType::Center);
    watermark.SetVAlignment(TextAlignmentType::Center);

    // Specify rotation.
    watermark.SetRotation(30);

    // Specify opacity.
    watermark.SetOpacity(0.6f);

    // Specify the scale to the page (e.g., 100, 50) in percent.
    watermark.SetScaleToPagePercent(50);

    // Specify watermark for rendering to PDF.
    PdfSaveOptions options;
    options.SetWatermark(watermark);

    // Save the workbook with the watermark.
    wb.Save(u"output_text_watermark.pdf", options);

    std::cout << "Workbook saved with watermark successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  

## **Add image watermark to PDF**  

You can add an image watermark to a PDF simply by specifying the image bytes. Also, you can set alignment, offset, rotation, opacity, foreground/background, and scale to the page in [RenderingWatermark](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/renderingwatermark/).  

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook with 3 pages
    Workbook wb;
    wb.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"Page1");
    int index = wb.GetWorksheets().Add();
    wb.GetWorksheets().Get(index).GetCells().Get(u"A1").PutValue(u"Page2");
    index = wb.GetWorksheets().Add();
    wb.GetWorksheets().Get(index).GetCells().Get(u"A1").PutValue(u"Page3");
    wb.GetWorksheets().Get(index).GetPageSetup().SetPaperSize(PaperSizeType::PaperA3);

    // Create a watermark from image (prepare image bytes)
    Vector<uint8_t> imageBytes; // Assume image bytes are prepared
    RenderingWatermark watermark(imageBytes);

    // Specify offset for alignment
    watermark.SetOffsetX(100);
    watermark.SetOffsetY(200);

    // Specify rotation
    watermark.SetRotation(30);

    // Specify watermark as background
    watermark.SetIsBackground(true);

    // Specify opacity
    watermark.SetOpacity(0.6f);

    // Specify the scale to the page (e.g., 100, 50) in percent
    watermark.SetScaleToPagePercent(50);

    // Specify watermark for rendering to PDF
    PdfSaveOptions options;
    options.SetWatermark(watermark);

    // Save the workbook with the watermark
    wb.Save(u"output_image_watermark.pdf", options);

    std::cout << "Workbook saved with watermark successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
