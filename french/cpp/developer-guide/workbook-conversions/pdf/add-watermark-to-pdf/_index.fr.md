---
title: Ajouter un filigrane au PDF avec C++
linktitle: Ajouter un filigrane au PDF
type: docs
weight: 9
url: /fr/cpp/add-watermark-to-pdf/
description: Apprenez comment ajouter des filigranes texte et image aux fichiers PDF lors du rendu en utilisant Aspose.Cells avec C++.
---

Lors de la conversion d'un fichier Excel en PDF, vous pouvez avoir besoin d'ajouter un filigrane au fichier PDF. Les exemples ci-dessous montrent comment ajouter des filigranes texte et image au PDF lors du rendu.

## **Ajouter un filigrane de texte au PDF**

Vous pouvez facilement ajouter un filigrane de texte au PDF en spécifiant le texte et la police correspondante. Vous pouvez également définir l'alignement, le décalage, la rotation, l'opacité, le premier plan / l'arrière-plan, et la mise à l'échelle de la page dans [RenderingWatermark](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/renderingwatermark/).

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

## **Ajouter un filigrane graphique au PDF**

Vous pouvez ajouter un filigrane d'image au PDF simplement en spécifiant les octets de l'image. Vous pouvez également définir l'alignement, le décalage, la rotation, l'opacité, le premier plan / l'arrière-plan, et la mise à l'échelle de la page dans [RenderingWatermark](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/renderingwatermark/).

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
