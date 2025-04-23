---
title: 画像
type: docs
weight: 300
url: /ja/net/convert-excel-to-image/
---


{{% alert color="primary" %}}

Aspose.Cellsでは、ワークブックからワークシートをエクスポートし、異なる形式に変換することができます。この記事ではワークシートを異なる形式に変換する方法について説明します。

{{% /alert %}}

## ワークブックをTIFF形式に変換

Excelファイルには複数のシートと複数のページが含まれる場合があります。 [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)を使用してExcelを複数ページのTIFFに変換できます。また、[圧縮](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression)、[カラーの深度](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth)、解像度([水平解像度](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution)、[垂直解像度](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution))などのTIFFの複数のオプションを制御することができます。

次のコードスニペットは、Excelを複数ページのTIFFに変換する方法を示しています。[元のExcelファイル](workbook-to-tiff-with-mulitiple-pages.xlsx)と[生成されたTIFF画像](workbook-to-tiff-with-mulitiple-pages.tiff)を参照できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **ワークシートをイメージに変換**

ワークシートには分析したいデータが含まれています。 例えば、ワークシートにはパラメータ、合計、パーセンテージ、例外、計算などが含まれることがあります。

開発者として、ワークシートを画像として表示する必要があるかもしれません。 たとえば、ワークシートの画像をアプリケーションやWebページで使用する必要があるかもしれません。 Microsoft Word文書、PDFファイル、PowerPointプレゼンテーション、またはその他のドキュメントタイプに画像を挿入したいかもしれません。 要するに、ワークシートを他の場所で使用できるように画像として描画したいのです。

Aspose.CellsはExcelワークシートを画像に変換する機能をサポートしています。この機能を使用するには、プログラムやプロジェクトに[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)名前空間をインポートする必要があります。レンダリングや印刷に関連する貴重なクラスがいくつかあり、たとえば[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)、[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)などがあります。

[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)クラスは画像としてレンダリングするワークシートを表します。[**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)というオーバーロードされたメソッドを使用して、異なる属性やオプションを持つ画像ファイルにワークシートを変換できます。それはSystem.Drawing.Bitmap オブジェクトを返し、画像ファイルをディスクやストリームに保存できます。BMP、PNG、GIF、JPG、JPEG、TIFF、EMFなど、いくつかの画像形式がサポートされています。

次のコードスニペットは、Excelファイルのワークシートを画像ファイルに変換する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

現在、ワークシートを画像に変換するAPIは3Dバブルチャートをサポートしていません。

{{% /alert %}}

## **ワークシートをSVGに変換**

SVGはScalable Vector Graphicsの略です。 SVGは、二次元ベクトルグラフィックのためのXML標準に基づいた仕様です。 1999年以来、World Wide Web Consortium（W3C）によって開発されてきたオープンな標準です。

Aspose.Cells for .NETはバージョン7.1.0以降からワークブック内のワークシートをSVG画像に変換することができます。次のコードスニペットは、Excelファイル内のワークシートをSVG画像ファイルに変換する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **高度なトピック**
- [Excelのチャートを画像に変換](/cells/ja/net/convert-an-excel-chart-to-image/)
- [SVG形式でチャートを画像に変換](/cells/ja/net/converting-chart-to-image-in-svg-format/)
- [viewBox属性を使用してチャートをSVGにエクスポート](/cells/ja/net/export-chart-to-svg-with-viewbox-attribute/)
- [ExcelからTIFFへの変換の進行状況を追跡](/cells/ja/net/track-conversion-progress-of-excel-to-tiff/)
{{< app/cells/assistant language="csharp" >}}
