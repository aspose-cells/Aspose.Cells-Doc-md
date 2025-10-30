---
title: GolangとC++経由でExcelを画像に変換
linktitle: Excelを画像に変換
type: docs
weight: 300
url: /ja/go-cpp/convert-excel-to-image/
description: Aspose.Cells for C++を使用して、ExcelのワークシートをTIFFやSVGフォーマットを含む画像に変換する方法を学びましょう。
---

{{% alert color="primary" %}}

Aspose.Cellsでは、ワークブックからワークシートをエクスポートし、異なる形式に変換することができます。この記事ではワークシートを異なる形式に変換する方法について説明します。

{{% /alert %}}

## ワークブックをTIFF形式に変換

Excelファイルには複数のシートとページが含まれる場合があります。[**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/)を使用してExcelを複数ページのTIFFに変換できます。また、[圧縮](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/)、[GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/)、解像度（[GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/)、[GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)）などの複数のオプションを制御できます。

次のコードスニペットは、Excelを複数ページのTIFFに変換する方法を示しています。[元のExcelファイル](workbook-to-tiff-with-mulitiple-pages.xlsx)と[生成されたTIFF画像](workbook-to-tiff-with-mulitiple-pages.tiff)を参照できます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image.go" >}}
## **ワークシートをイメージに変換**

ワークシートには分析したいデータが含まれています。 例えば、ワークシートにはパラメータ、合計、パーセンテージ、例外、計算などが含まれることがあります。

開発者として、ワークシートを画像として表示する必要があるかもしれません。 たとえば、ワークシートの画像をアプリケーションやWebページで使用する必要があるかもしれません。 Microsoft Word文書、PDFファイル、PowerPointプレゼンテーション、またはその他のドキュメントタイプに画像を挿入したいかもしれません。 要するに、ワークシートを他の場所で使用できるように画像として描画したいのです。

Aspose.CellsはExcelのワークシートを画像に変換することをサポートします。この機能を使用するには、プログラムまたはプロジェクトに[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/go-cpp/)名前空間をインポートしてください。レンダリングや印刷に役立つクラスがいくつかあります。例として [**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/)、[**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/)などです。

[**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/)クラスは画像としてレンダリングするワークシートを表します。オーバーロードされたメソッド [**ToImage**](https://reference.aspose.com/cells/go-cpp/sheetrender/toimage/) は、異なる属性またはオプションを持つワークシートを画像ファイルに変換できます。これはSystem.Drawing.Bitmapオブジェクトを返し、画像ファイルをディスクまたはストリームに保存できます。サポートされている画像フォーマットには BMP、PNG、GIF、JPG、JPEG、TIFF、EMF があります。

次のコードスニペットは、Excelファイルのワークシートを画像ファイルに変換する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-1.go" >}}
{{% alert color="primary" %}}

現在、ワークシートを画像に変換するAPIは3Dバブルチャートをサポートしていません。

{{% /alert %}}

## **ワークシートをSVGに変換**

SVGはScalable Vector Graphicsの略です。 SVGは、二次元ベクトルグラフィックのためのXML標準に基づいた仕様です。 1999年以来、World Wide Web Consortium（W3C）によって開発されてきたオープンな標準です。

Aspose.Cells for C++ はバージョン 7.1.0 以降、ワークシートをSVG画像に変換できるようになりました。以下のコードスニペットは、Excelファイル内のワークシートをSVG画像ファイルに変換する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-2.go" >}}
## **高度なトピック**
- [Excelのチャートを画像に変換](/cells/ja/cpp/convert-an-excel-chart-to-image/)
- [SVG形式でチャートを画像に変換](/cells/ja/cpp/converting-chart-to-image-in-svg-format/)
- [viewBox属性を使用してチャートをSVGにエクスポート](/cells/ja/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [ExcelからTIFFへの変換の進行状況を追跡](/cells/ja/cpp/track-conversion-progress-of-excel-to-tiff/)
