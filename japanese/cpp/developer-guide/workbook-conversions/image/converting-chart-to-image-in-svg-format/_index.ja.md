---
title: SVG形式のチャート画像に変換するC++による方法
linktitle: SVG形式でチャートを画像に変換
type: docs
weight: 240
url: /ja/cpp/converting-chart-to-image-in-svg-format/
description: Aspose.Cellsを使用してチャートをSVG画像に変換する方法を学びます。
---

{{% alert color="primary" %}}

スケーラブル・ベクター・グラフィックス（SVG）は、二次元グラフィックス用のXMLベースのベクター画像形式であり、対話性やアニメーションもサポートしています。SVG仕様は、1999年以来世界広範囲のウェブ consortium（W3C） によって開発されたオープンスタンダードです。

SVG画像とその動作はXMLテキストファイルで定義されています。これにより、検索、索引付け、スクリプト作成、圧縮が可能です。SVG画像はXMLファイルとして任意のテキストエディタで作成および編集できますが、一般的には図形作成ソフトウェアで作成されます。

Aspose.CellsはチャートをBMP、JPEG、PNG、GIF、SVGなどさまざまな形式の画像に保存できます。この記事では、チャートをSVG形式に保存する方法を説明します。

{{% /alert %}}

次のサンプルコードは、Aspose.Cellsを使用してチャートをSVG形式の画像に変換する方法について説明しています。このコードは、ソースとなるMicrosoft Excelファイルを読み込み、次に最初のワークシートで見つかった最初のチャートをSVG形式で保存します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleChartBook.xlsx";

    // Create workbook object from source file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set image or print options
    ImageOrPrintOptions opts;
    opts.SetImageType(Aspose::Cells::Drawing::ImageType::Svg);

    // Save the chart to svg format
    chart.ToImage(outDir + u"Image_out.svg", opts);

    std::cout << "Chart saved to SVG format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
