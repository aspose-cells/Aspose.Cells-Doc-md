---
title: シートのセル範囲を画像にエクスポート（C++）
linktitle: セル範囲を画像にエクスポート
type: docs
weight: 60
url: /ja/cpp/export-range-of-cells-in-a-worksheet-to-image/
description: Aspose.Cells を使用して特定のセル範囲を画像にエクスポートする方法（C++）
---

## **可能な使用シナリオ**

Aspose.Cellsを使用してワークシートのイメージを作成できます。ただし、ワークシート内のセルの範囲をイメージにエクスポートする必要がある場合があります。この記事では、これをどのように行うかについて説明します。

## **ワークシートのセルの範囲をイメージにエクスポート**

範囲のイメージを取得するには、印刷範囲を所定の範囲に設定し、すべての余白を0に設定し、さらに[**ImageOrPrintOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getonepagepersheet/) を **true**に設定します。次のコードは、範囲D8:G16のイメージを取得します。下のスクリーンショットは、コードで使用される[サンプルExcelファイル](47153160.xlsx)のイメージです。任意のExcelファイルでコードを試すことができます。

## **サンプルExcelファイルのスクリーンショットとそのエクスポートされたイメージ**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

コードを実行すると、範囲D8:G16のイメージが作成されます。

**![todo:image_alt_text](Output-Image.png)**

## **サンプルコード**

```cpp
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

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleExportRangeOfCellsInWorksheetToImage.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area with the desired range
    worksheet.GetPageSetup().SetPrintArea(u"D8:G16");

    // Set all margins to 0
    worksheet.GetPageSetup().SetLeftMargin(0);
    worksheet.GetPageSetup().SetRightMargin(0);
    worksheet.GetPageSetup().SetTopMargin(0);
    worksheet.GetPageSetup().SetBottomMargin(0);

    // Set OnePagePerSheet option as true
    ImageOrPrintOptions options;
    options.SetOnePagePerSheet(true);
    options.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);

    // Take the image of the worksheet
    SheetRender sr(worksheet, options);
    sr.ToImage(0, outDir + u"outputExportRangeOfCellsInWorksheetToImage.jpg");

    std::cout << "Worksheet image exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
