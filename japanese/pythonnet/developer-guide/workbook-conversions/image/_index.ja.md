---
title: 画像
type: docs
weight: 300
url: /ja/python-net/convert-excel-to-image/
description: Aspose.Cells for Python via .NET APIを使用して、チャートを画像に変換する。
keywords: Pythonでチャートを画像に変換する、Python via NETでチャートを画像にエクスポートする、Pythonでチャートを保存する。
---


{{% alert color="primary" %}}

Aspose.Cells for Python via .NETにより、ワークブックからワークシートをエクスポートして異なる形式に変換することができます。この記事では、ワークシートを異なる形式に変換する方法について説明します。

{{% /alert %}}

## ワークブックをTIFF形式に変換

Excelファイルには複数のシートと複数のページが含まれる場合があります。 [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender)では、[Compression](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/)、[Color depth](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/)、Resolution([Horizontal resolution](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/)、[Vertical resolution](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)）など、TIFFのための複数のオプションを制御できます。

次のコードスニペットは、Excelを複数ページのTIFFに変換する方法を示しています。[元のExcelファイル](workbook-to-tiff-with-mulitiple-pages.xlsx)と[生成されたTIFF画像](workbook-to-tiff-with-mulitiple-pages.tiff)を参照できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

## **ワークシートをイメージに変換**

ワークシートには分析したいデータが含まれています。 例えば、ワークシートにはパラメータ、合計、パーセンテージ、例外、計算などが含まれることがあります。

開発者として、ワークシートを画像として表示する必要があるかもしれません。 たとえば、ワークシートの画像をアプリケーションやWebページで使用する必要があるかもしれません。 Microsoft Word文書、PDFファイル、PowerPointプレゼンテーション、またはその他のドキュメントタイプに画像を挿入したいかもしれません。 要するに、ワークシートを他の場所で使用できるように画像として描画したいのです。

Aspose.Cells for Python via .NETは、Excelワークシートを画像に変換することをサポートしています。この機能を使用するためには、プログラムまたはプロジェクトに[**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/)名前空間をインポートする必要があります。[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/)、[**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/)など、レンダリングや印刷のための貴重なクラスがいくつかあります。

[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)クラスは画像としてレンダリングするワークシートを表します。[**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str)というオーバーロードされたメソッドを使用して、異なる属性やオプションを持つ画像ファイルにワークシートを変換できます。それはSystem.Drawing.Bitmap オブジェクトを返し、画像ファイルをディスクやストリームに保存できます。BMP、PNG、GIF、JPG、JPEG、TIFF、EMFなど、いくつかの画像形式がサポートされています。

次のコードスニペットは、Excelファイルのワークシートを画像ファイルに変換する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

現在、ワークシートを画像に変換するAPIは3Dバブルチャートをサポートしていません。

{{% /alert %}}

## **ワークシートをSVGに変換**

SVGはScalable Vector Graphicsの略です。 SVGは、二次元ベクトルグラフィックのためのXML標準に基づいた仕様です。 1999年以来、World Wide Web Consortium（W3C）によって開発されてきたオープンな標準です。

Aspose.Cells for Python via .NETは、バージョン7.1.0からワークブック内のワークシートをSVG画像に変換できるようになりました。以下のコードスニペットは、Excelファイル内のワークシートをSVG画像ファイルに変換する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

## **高度なトピック**
- [Excelのチャートを画像に変換](/cells/ja/python-net/convert-an-excel-chart-to-image/)
- [SVG形式でチャートを画像に変換](/cells/ja/python-net/converting-chart-to-image-in-svg-format/)
- [viewBox属性を使用してチャートをSVGにエクスポート](/cells/ja/python-net/export-chart-to-svg-with-viewbox-attribute/)
{{< app/cells/assistant language="python-net" >}}
