---
title: PDFにウォーターマークを追加する（C++版）
linktitle: PDFに透かしを追加する
type: docs
weight: 9
url: /ja/cpp/add-watermark-to-pdf/
description: Aspose.Cellsを使用してレンダリング中にPDFファイルにテキストと画像のウォーターマークを追加する方法を学びます（C++版）。
---

ExcelファイルをPDFに変換する際に、PDFにウォーターマークを追加したい場合があります。以下の例は、レンダリング時にPDFにテキストと画像のウォーターマークを追加する方法を示しています。

## **PDFにテキストのウォーターマークを追加**

テキストと対応するフォントを指定するだけで、簡単にPDFにテキストウォーターマークを追加できます。また、配置、オフセット、回転、不透明度、前景/背景、ページへのスケールを設定できます([RenderingWatermark](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/renderingwatermark/))。

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

## **PDFに画像透かしを追加する**

画像のバイトを指定するだけで、PDFに画像ウォーターマークを追加できます。また、配置、オフセット、回転、不透明度、前景/背景、ページへのスケールを設定できます([RenderingWatermark](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/renderingwatermark/))。

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
