---
title: Image
type: docs
weight: 300
url: /ja/python-net/convert-excel-to-image/
description: Aspose.Cells for Python via .NET API を使用して、チャートを Image に変換します。
keywords: Python Convert Chart to Image, Export Chart to Image in Python via NET, Python Save Chart to Image.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET を使用すると、ワークブックからワークシートをエクスポートし、別の形式に変換できます。この記事では、ワークシートをさまざまな形式に変換する方法について説明します。

{{% /alert %}}

## ワークブックを TIFF に変換しています

Excel ファイルには、複数のページを持つ複数のシートを含めることができます。[ワークブックレンダリング](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender)Excel を複数ページの TIFF に変換できます。また、TIFF の複数のオプションを制御できます。[圧縮](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/), [色深度](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/)、 解決（[水平解像度](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/), [垂直解像度](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)).

次のコード スニペットは、Excel を複数ページのある TIFF に変換する方法を示しています。の[ソース Excel ファイル](workbook-to-tiff-with-mulitiple-pages.xlsx)そして[生成された TIFF 画像](workbook-to-tiff-with-mulitiple-pages.tiff)参考までに添付します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

##  **ワークシートをImageに変換中**

ワークシートには、分析するデータが含まれています。たとえば、ワークシートにはパラメータ、合計、パーセンテージ、例外、計算を含めることができます。

開発者は、ワークシートを画像として表示する必要がある場合があります。たとえば、アプリケーションまたは Web ページでワークシートの画像を使用する必要がある場合があります。 Microsoft Word 文書、PDF ファイル、PowerPoint プレゼンテーション、またはその他の文書タイプに画像を挿入することができます。簡単に言うと、ワークシートを画像としてレンダリングして、他の場所で使用できるようにしたいと考えます。

Aspose.Cells for Python via .NET は、Excel ワークシートの画像への変換をサポートしています。この機能を使用するには、**[aspose.cells.rendering](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/)**名前空間をプログラムまたはプロジェクトに追加します。これには、レンダリングと印刷のためのいくつかの貴重なクラスがあります。たとえば、 *[シートレンダリング](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**, *[画像または印刷オプション](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/)**, *[ワークブックレンダリング](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/)**、 その他。

の**[SheetRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**クラスは画像としてレンダリングするワークシートを表します。オーバーロードされたメソッドがあります。 *[to_image](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str)**、ワークシートをさまざまな属性またはオプションを持つ画像ファイルに変換できます。 System.Drawing.Bitmap オブジェクトを返し、画像ファイルをディスクまたはストリームに保存できます。いくつかの画像形式がサポートされています (例: BMP、PNG、GIF、JPG、JPEG、TIFF、EMF)。

次のコード スニペットは、Excel ファイル内のワークシートを画像ファイルに変換する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

現在、ワークシートを画像に変換するための API は 3D バブル チャートをサポートしていません。

{{% /alert %}}

##  **ワークシートをSVGに変換中**

SVG はスケーラブル ベクター グラフィックスの略です。 SVG は、2 次元ベクトル グラフィックスの XML 標準に基づいた仕様です。これは、World Wide Web Consortium (W3C) によって 1999 年から開発が進められているオープン標準です。

Aspose.Cells for Python via .NET は、バージョン 7.1.0 以降、ワークシートを SVG 画像に変換できるようになりました。次のコード スニペットは、Excel ファイル内のワークシートを SVG 画像ファイルに変換する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

##  **アドバンストトピック**
- [Excel グラフを Image に変換する](/cells/ja/python-net/convert-an-excel-chart-to-image/)
- [グラフを SVG 形式の Image に変換する](/cells/ja/python-net/converting-chart-to-image-in-svg-format/)
- [viewBox 属性を使用してチャートを SVG にエクスポート](/cells/ja/python-net/export-chart-to-svg-with-viewbox-attribute/)
