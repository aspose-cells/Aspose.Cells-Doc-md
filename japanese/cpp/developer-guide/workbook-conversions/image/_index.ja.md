---
title: Excelを画像に変換（C++使用）
linktitle: Excelを画像に変換
type: docs
weight: 300
url: /ja/cpp/convert-excel-to-image/
description: Aspose.Cells for C++を使用して、ExcelのワークシートをTIFFやSVGフォーマットを含む画像に変換する方法を学びましょう。
---

{{% alert color="primary" %}}

Aspose.Cellsでは、ワークブックからワークシートをエクスポートし、異なる形式に変換することができます。この記事ではワークシートを異なる形式に変換する方法について説明します。

{{% /alert %}}

## ワークブックをTIFF形式に変換

Excelファイルには複数のシートとページが含まれる場合があります。[**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/)を使用してExcelを複数ページのTIFFに変換できます。また、[圧縮](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/)、[GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/)、解像度（[GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/)、[GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)）などの複数のオプションを制御できます。

次のコードスニペットは、Excelを複数ページのTIFFに変換する方法を示しています。[元のExcelファイル](workbook-to-tiff-with-mulitiple-pages.xlsx)と[生成されたTIFF画像](workbook-to-tiff-with-mulitiple-pages.tiff)を参照できます。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main() {
    Aspose::Cells::Startup();

    // Load the workbook
    Workbook wb(u"workbook-to-tiff-with-mulitiple-pages.xlsx");

    // Create image options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Tiff);

    // Set resolution to 200 DPI
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetVerticalResolution(200);

    // Set TIFF compression to LZW
    imgOptions.SetTiffCompression(TiffCompression::CompressionLZW);

    // Render the workbook to TIFF
    WorkbookRender workbookRender(wb, imgOptions);
    workbookRender.ToImage(u"workbook-to-tiff-with-mulitiple-pages.tiff");

    std::cout << "Workbook rendered to TIFF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **ワークシートをイメージに変換**

ワークシートには分析したいデータが含まれています。 例えば、ワークシートにはパラメータ、合計、パーセンテージ、例外、計算などが含まれることがあります。

開発者として、ワークシートを画像として表示する必要があるかもしれません。 たとえば、ワークシートの画像をアプリケーションやWebページで使用する必要があるかもしれません。 Microsoft Word文書、PDFファイル、PowerPointプレゼンテーション、またはその他のドキュメントタイプに画像を挿入したいかもしれません。 要するに、ワークシートを他の場所で使用できるように画像として描画したいのです。

Aspose.CellsはExcelのワークシートを画像に変換することをサポートします。この機能を使用するには、プログラムまたはプロジェクトに[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/)名前空間をインポートしてください。レンダリングや印刷に役立つクラスがいくつかあります。例として [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)、[**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/)などです。

[**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)クラスは画像としてレンダリングするワークシートを表します。オーバーロードされたメソッド [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) は、異なる属性またはオプションを持つワークシートを画像ファイルに変換できます。これはSystem.Drawing.Bitmapオブジェクトを返し、画像ファイルをディスクまたはストリームに保存できます。サポートされている画像フォーマットには BMP、PNG、GIF、JPG、JPEG、TIFF、EMF があります。

次のコードスニペットは、Excelファイルのワークシートを画像ファイルに変換する方法を示しています。

```cpp
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::wstring numStr = std::to_wstring(j + 1);
        U16String numU16Str(reinterpret_cast<const char16_t*>(numStr.c_str()));
        U16String outputPath = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + numU16Str + U16String(u".tif");
        sr.ToImage(j, outputPath);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

現在、ワークシートを画像に変換するAPIは3Dバブルチャートをサポートしていません。

{{% /alert %}}

## **ワークシートをSVGに変換**

SVGはScalable Vector Graphicsの略です。 SVGは、二次元ベクトルグラフィックのためのXML標準に基づいた仕様です。 1999年以来、World Wide Web Consortium（W3C）によって開発されてきたオープンな標準です。

Aspose.Cells for C++ はバージョン 7.1.0 以降、ワークシートをSVG画像に変換できるようになりました。以下のコードスニペットは、Excelファイル内のワークシートをSVG画像ファイルに変換する方法を示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a workbook
    Workbook workbook;

    // Put sample text in the first cell of first worksheet in the newly created workbook
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET1");

    // Add second worksheet in the workbook
    workbook.GetWorksheets().Add(SheetType::Worksheet);

    // Set text in first cell of the second sheet
    workbook.GetWorksheets().Get(1).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET2");

    // Set currently active sheet index to 1 i.e. Sheet2
    workbook.GetWorksheets().SetActiveSheetIndex(1);

    // Save workbook to SVG. It shall render the active sheet only to SVG
    workbook.Save(outDir + u"ConvertWorksheetToSVG_out.svg");

    std::cout << "Worksheet converted to SVG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**
- [Excelのチャートを画像に変換](/cells/ja/cpp/convert-an-excel-chart-to-image/)
- [SVG形式でチャートを画像に変換](/cells/ja/cpp/converting-chart-to-image-in-svg-format/)
- [viewBox属性を使用してチャートをSVGにエクスポート](/cells/ja/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [ExcelからTIFFへの変換の進行状況を追跡](/cells/ja/cpp/track-conversion-progress-of-excel-to-tiff/)
