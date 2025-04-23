---
title: إضافة علامة مائية إلى PDF باستخدام C++
linktitle: إضافة علامة مائية إلى ملف PDF
type: docs
weight: 9
url: /ar/cpp/add-watermark-to-pdf/
description: تعلم كيفية إضافة علامات مائية نصية وصورة إلى ملفات PDF أثناء التصيير باستخدام Aspose.Cells مع C++.
---

 أثناء تحويل ملف Excel إلى PDF، قد تكون لديك متطلبات لإضافة علامة مائية إلى ملف PDF. تظهر الأمثلة التالية كيفية إضافة علامات مائية نصية وصورة إلى PDF أثناء التصيير إلى PDF.

## **إضافة علامة مائية نصية إلى PDF**

يمكنك بسهولة إضافة علامة مائية نصية إلى PDF عن طريق تحديد النص والخط المقابل. أيضًا، يمكنك ضبط المحاذاة، الإزاحة، الدوران، الشفافية، الأمام والخلف، وتغيير مقياس الصفحة في [RenderingWatermark](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/renderingwatermark/).

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

    // Specify the scale to page (e.g., 100, 50) in percent.
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

## **إضافة علامة مائية صورة إلى PDF**

يمكنك إضافة علامة مائية صورة إلى PDF فقط عن طريق تحديد بايتات الصورة. أيضًا، يمكنك ضبط المحاذاة، الإزاحة، الدوران، الشفافية، الأمام والخلف، وتغيير مقياس الصفحة في [RenderingWatermark](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/renderingwatermark/).

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

    // Specify offset to alignment
    watermark.SetOffsetX(100);
    watermark.SetOffsetY(200);

    // Specify rotation
    watermark.SetRotation(30);

    // Specify watermark to background
    watermark.SetIsBackground(true);

    // Specify opacity
    watermark.SetOpacity(0.6f);

    // Specify the scale to page (e.g., 100, 50) in percent
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
