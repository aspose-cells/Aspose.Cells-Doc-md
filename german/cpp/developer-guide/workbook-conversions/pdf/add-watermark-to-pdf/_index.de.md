---
title: Wasserzeichen zu PDF mit C++ hinzufügen
linktitle: Wasserzeichen zu PDF hinzufügen
type: docs
weight: 9
url: /de/cpp/add-watermark-to-pdf/
description: Erfahren Sie, wie Sie Text und Bild Wasserzeichen beim Rendern von PDF Dateien mit Aspose.Cells und C++ hinzufügen.
---

Beim Konvertieren einer Excel-Datei zu PDF können Anforderungen bestehen, ein Wasserzeichen zum PDF hinzuzufügen. Die folgenden Beispiele zeigen, wie Text- und Bild-Wasserzeichen beim Rendern in PDF hinzugefügt werden.

## **Text-Wasserzeichen zu PDF hinzufügen**

Sie können ganz einfach ein Text-Wasserzeichen zu PDF hinzufügen, indem Sie den Text und die entsprechende Schriftart angeben. Außerdem können Sie Ausrichtung, Verschiebung, Drehung, Opazität, Vorder-/Hintergrund und Skalierung auf der Seite in [RenderingWatermark](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/renderingwatermark/) einstellen.

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

## **Bildwasserzeichen zur PDF hinzufügen**

Sie können ein Bild-Wasserzeichen zu PDF hinzufügen, indem Sie einfach die Bildbytes eines Bildes angeben. Außerdem können Sie Ausrichtung, Verschiebung, Drehung, Opazität, Vorder-/Hintergrund und Skalierung auf der Seite in [RenderingWatermark](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/renderingwatermark/) einstellen.

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
{{< app/cells/assistant language="cpp" >}}
