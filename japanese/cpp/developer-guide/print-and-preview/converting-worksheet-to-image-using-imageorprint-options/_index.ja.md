---
title: C++を使用した ImageOrPrint Options でシートを画像に変換
linktitle: シートを画像に変換
type: docs
weight: 90
url: /ja/cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Aspose.Cells を使用してシートを画像に変換し、解像度、TIFF 圧縮、画像フォーマット、ページ品質などのさまざまな画像および印刷オプションを適用する方法を学びます。
---

{{% alert color="primary" %}}

このドキュメントは、シートを画像ファイルに変換し、解像度、TIFF圧縮、画像フォーマット、ページ品質など、画像のさまざまなオプションを適用する方法について詳細な理解を提供することを目的としています。

{{% /alert %}}

## **ワークシートをイメージとして保存する - 異なるアプローチ**

時には、ワークシートを画像として提示する必要があります。アプリケーションやウェブページでシートの画像を表示したり、Word文書、PDFファイル、PowerPointプレゼンテーションに挿入したり、その他のシナリオで使用したりできます。簡単に言えば、シートを画像としてレンダリングし、他の場所で使用したいのです。Aspose.Cells は、Excelファイル内のシートを画像に変換することをサポートしています。さらに、画像フォーマット、解像度（縦横両方）、画質、その他の画像および印刷オプションを設定することも可能です。

Office Automation を検討するかもしれませんが、これには独自の欠点があります。セキュリティ、安定性、拡張性、速度、価格、機能など、いくつかの理由や問題があります。要するに、多くの理由がありますが、最も重要なのは、Microsoft 自体がソフトウェアソリューションによる Office automation を強く推奨していないことです。

この記事では、Visual Studio でコンソールアプリケーションを作成し、少ないコード行で Aspose.Cells API を使用してシートを画像に変換する方法を示します。

プログラム/プロジェクトに [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) 名前空間を含める必要があります。これには [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)、[**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) などいくつかの有用なクラスがあります。

[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) クラスは、シートの画像をレンダリングするためのシートを表します。このクラスには、所望の属性やオプションでシートを画像ファイルに直接変換できるオーバーロードされた [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) メソッドがあります。ビットマップオブジェクトを返すことができ、画像ファイルをディスクまたはストリームに保存できます。BMP、PNG、GIF、JPEG、TIFF、EMF など、多くの画像フォーマットをサポートしています。

## **Aspose.Cells を使用したシートの画像への変換（ImageOrPrint オプション利用）**

### **Microsoft Excel でテンプレートワークブックを作成する**

MS Excel で新しいブックを作成し、最初のシートにいくつかのデータを追加しました。次に、テンプレートファイルのシート「Sheet1」を画像ファイル「SheetImage.tiff」に変換し、水平方向と垂直方向の解像度、Tiff圧縮などのさまざまな画像オプションを適用します。

### **Aspose.Cellsをダウンロードしてインストールする**

まず、[ダウンロード](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++ を行ってください。開発コンピュータにインストールします。すべての [Aspose](http://www.aspose.com/) コンポーネントは、インストール時に評価モードで動作します。評価モードには時間制限はなく、生成されたドキュメントに水印だけが挿入されます。

### **プロジェクトを作成する**

Visual Studio を起動し、新しいコンソールアプリケーションを作成します。この例は C++ コンソールアプリケーションを示します。

### **参照の追加**

このプロジェクトは Aspose.Cells を使用します。そのため、プロジェクトに Aspose.Cells コンポーネントへの参照を追加する必要があります。例として、`...\Program Files\Aspose\Aspose.Cells for C++\Bin\Aspose.Cells.lib` への参照を追加してください。

### **シートを画像ファイルに変換**

```c++
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

    Workbook book(srcDir + u"sampleWorksheetToAnImage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(300);
    options.SetVerticalResolution(300);
    options.SetTiffCompression(TiffCompression::CompressionLZW);
    options.SetImageType(ImageType::Tiff);
    options.SetPrintingPage(PrintingPageType::Default);

    SheetRender sr(sheet, options);

    int pageIndex = 3;
    int pageNumber = pageIndex + 1;
    std::wstring pageStr = std::to_wstring(pageNumber);
    U16String pageNumberStr(reinterpret_cast<const char16_t*>(pageStr.c_str()));
    U16String outputPath = outDir + U16String(u"outputWorksheetToAnImage_") + pageNumberStr + U16String(u".tiff");
    sr.ToImage(pageIndex, outputPath);

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **変換オプション**

特定のページを画像として保存することも可能です。以下のコードは、ワークブック内の最初と2番目のシートを JPG 画像に変換します。

```c++
#include <iostream>
#include <fstream>
#include <sstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"sampleSpecificPagesToImages.xlsx";
    Workbook workbook(inputPath);

    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);

    SheetRender sr(worksheet, imgOptions);

    int32_t pageIndex = 3;

    Vector<uint8_t> imageData = sr.ToImage(pageIndex);

    std::wstringstream ws;
    ws << (pageIndex + 1);
    U16String pageNumStr(reinterpret_cast<const char16_t*>(ws.str().c_str()));

    U16String outputPath = outDir + u"outputSpecificPagesToImage_" + pageNumStr + u".jpg";
    std::ofstream outputFile(outputPath.ToUtf8(), std::ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Page rendered successfully to: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **WorkbookRender を使用した画像変換**

TIFF画像は複数のフレームを含むことができます。ワークブック全体を複数のフレームまたはページを持つ単一のTIFF画像に保存できます。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook wb(srcDir + u"sampleUseWorkbookRenderForImageConversion.xlsx");

    // Set image options
    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Tiff);

    // Render workbook to image
    WorkbookRender wr(wb, opts);
    wr.ToImage(outDir + u"outputUseWorkbookRenderForImageConversion.tiff");

    std::cout << "Workbook rendered to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
