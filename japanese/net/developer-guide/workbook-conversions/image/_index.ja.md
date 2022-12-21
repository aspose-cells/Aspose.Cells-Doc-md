---
title: 画像
type: docs
weight: 300
url: /ja/net/convert-excel-to-image/
---
{{% alert color="primary" %}}

Aspose.Cells を使用すると、ブックからワークシートをエクスポートして、別の形式に変換できます。この記事では、ワークシートを別の形式に変換する方法について説明します。

{{% /alert %}}

## ワークブックを TIFF に変換する

Excel ファイルには、複数のページを持つ複数のシートを含めることができます。[WorkbookRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) Excel を複数ページの TIFF に変換できます。また、TIFF の複数のオプションを制御することもできます。[圧縮](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression), [色深度](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth)、 解決（[水平解像度](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution), [垂直解像度](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)).

次のコード スニペットは、Excel を複数ページの TIFF に変換する方法を示しています。の[ソースの Excel ファイル](workbook-to-tiff-with-mulitiple-pages.xlsx)と[生成された TIFF イメージ](workbook-to-tiff-with-mulitiple-pages.tiff)ご参考までに添付します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **ワークシートを画像に変換する**

ワークシートには、分析するデータが含まれています。たとえば、ワークシートには、パラメーター、合計、パーセンテージ、例外、および計算を含めることができます。

開発者は、ワークシートを画像として表示する必要がある場合があります。たとえば、アプリケーションまたは Web ページでワークシートの画像を使用する必要がある場合があります。 Microsoft Word 文書、PDF ファイル、PowerPoint プレゼンテーション、またはその他の文書タイプに画像を挿入したい場合があります。簡単に言えば、別の場所で使用できるように、ワークシートを画像としてレンダリングする必要があります。

Aspose.Cells は、Excel ワークシートの画像への変換をサポートしています。この機能を使用するには、インポートする必要があります**[Aspose.Cells.Rendering](https://reference.aspose.com/cells/net/aspose.cells.rendering)**名前空間をプログラムまたはプロジェクトに追加します。たとえば、レンダリングと印刷に役立ついくつかのクラスがあります。**[SheetRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)**, **[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**, **[WorkbookRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)**、 その他。

の**[SheetRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)**クラスは、画像としてレンダリングするワークシートを表します。オーバーロードされたメソッドがあり、**[ToImage](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)**、さまざまな属性またはオプションを使用してワークシートを画像ファイルに変換できます。これは System.Drawing.Bitmap オブジェクトを返し、イメージ ファイルをディスクまたはストリームに保存できます。 BMP、PNG、GIF、JPG、JPEG、TIFF、EMF など、いくつかの画像形式がサポートされています。

次のコード スニペットは、Excel ファイルのワークシートを画像ファイルに変換する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

現在、ワークシートを画像に変換するための API は、3D バブル チャートをサポートしていません。

{{% /alert %}}

## **ワークシートを SVG に変換する**

SVG はスケーラブル ベクター グラフィックスの略です。 SVG は、2 次元ベクター グラフィックスの XML 標準に基づく仕様です。これは、1999 年から World Wide Web Consortium (W3C) によって開発されているオープン標準です。

Aspose.Cells for .NET は、バージョン 7.1.0 からワークシートを SVG 画像に変換できました。次のコード スニペットは、Excel ファイルのワークシートを SVG イメージ ファイルに変換する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **先行トピック**
- [Excel チャートを画像に変換する](/cells/ja/net/convert-an-excel-chart-to-image/)
- [チャートを SVG 形式の画像に変換する](/cells/ja/net/converting-chart-to-image-in-svg-format/)
- [viewBox 属性を使用してチャートを SVG にエクスポート](/cells/ja/net/export-chart-to-svg-with-viewbox-attribute/)
- [Excel から TIFF への変換の進行状況を追跡する](/cells/ja/net/track-conversion-progress-of-excel-to-tiff/)
