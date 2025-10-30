---
title: C++を使ったスライサーのレンダリング
type: docs
weight: 40
url: /ja/cpp/rendering-slicer/
description: Aspose.Cellsを使用してExcelファイル内のスライサーをレンダリングします。
---

## **可能な使用シナリオ**
Aspose.Cellsはスライサーのレンダリングをサポートしています。ワークシートを画像に変換したり、ワークブックをPDFまたはHTML形式で保存すると、スライサーが適切にレンダリングされます。
## **スライサーをレンダリングする**
以下のサンプルコードは既存のスライサーを含む[サンプルExcelファイル](67338479.xlsx)を読み込み、スライサーのみをカバーする印刷範囲を設定してシートを画像に変換します。生成された[出力画像](67338480.png)はレンダリングされたスライサーを示しています。ご覧のとおり、スライサーは適切にレンダリングされ、サンプルExcelファイルと同じ見た目になります。

![todo:image_alt_text](rendering-slicer_1)
## **サンプルコード**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleRenderingSlicer.xlsx");

    // Access first worksheet.
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Set the print area because we want to render slicer only.
    ws.GetPageSetup().SetPrintArea(u"B15:E25");

    // Specify image or print options, set one page per sheet and only area to true.
    ImageOrPrintOptions imgOpts;
    imgOpts.SetHorizontalResolution(200);
    imgOpts.SetVerticalResolution(200);
    imgOpts.SetImageType(ImageType::Png);
    imgOpts.SetOnePagePerSheet(true);
    imgOpts.SetOnlyArea(true);

    // Create sheet render object and render worksheet to image.
    SheetRender sr(ws, imgOpts);
    sr.ToImage(0, u"outputRenderingSlicer.png");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
