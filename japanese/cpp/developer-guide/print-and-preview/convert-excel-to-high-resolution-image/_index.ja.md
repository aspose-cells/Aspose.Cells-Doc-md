---
title: C++でExcelを高解像度画像に変換
linktitle: Excelを高解像度画像に変換する
type: docs
weight: 100
url: /ja/cpp/convert-excel-to-high-resolution-image/
description: Aspose.CellsをC++で使用してExcelファイルから高解像度画像を生成します。
---

高解像度スクリーンの普及により、デフォルトの96 DPIで生成された画像はしばしばぼやけて不鮮明に見えます。高解像度スクリーンでの鮮明さを保つためには、より高いDPIで画像を生成することが重要です。Aspose.Cellsは[**ImageOrPrintOptions.GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/)と[**ImageOrPrintOptions.GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)を設定できる機能を提供し、高品質な画像を作成して高解像度ディスプレイ上でも鮮明に見せることができます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load the Excel file
    Workbook workbook(u"input.xlsx");

    // Create an instance of ImageOrPrintOptions
    ImageOrPrintOptions options;
    options.SetHorizontalResolution(300); // Set horizontal resolution to 300 DPI
    options.SetVerticalResolution(300);   // Set vertical resolution to 300 DPI
    options.SetImageType(ImageType::Png); // Set the image type

    // Get the worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Create a SheetRender instance
    SheetRender render(sheet, options);

    // Generate and save the image
    render.ToImage(0, u"output.png");

    std::cout << "Image generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
