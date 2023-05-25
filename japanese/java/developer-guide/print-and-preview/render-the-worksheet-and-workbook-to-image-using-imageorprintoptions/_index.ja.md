---
title: ImageOrPrintOptions を使用してワークシートとワークブックを画像にレンダリングする
type: docs
weight: 220
url: /ja/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---
{{% alert color="primary" %}}

このドキュメントは、ワークシートまたはワークブックを画像ファイルに変換し、さまざまな画像とその画像の印刷オプション、解像度、TIFF 圧縮、画像形式、ページ品質などのオプションを適用する方法を詳細に理解できるように設計されています。

{{% /alert %}}

##  **概要**

場合によっては、ワークシートを図で表現することが必要になる場合があります。ワークシートの画像をアプリケーションまたは Web ページに表示する必要はありません。画像を Word 文書、PDF ファイル、PowerPoint プレゼンテーションに挿入したり、他のシナリオで使用したりする必要がある場合があります。ワークシートを画像としてレンダリングして、他の場所で使用できるようにしたいだけです。 Aspose.Cells は、Excel ファイルのワークシートの画像への変換をサポートしています。また、Aspose.Cells は、画像形式、解像度 (垂直方向と水平方向の両方)、画質、その他の画像および印刷オプションなどのさまざまなオプションの設定をサポートしています。

API は、いくつかの貴重なクラスを提供します。たとえば、[**シートレンダリング**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**画像または印刷オプション**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**ワークブックレンダリング**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)、など。

の[**シートレンダリング**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)クラスはワークシートの画像をレンダリングするタスクを処理しますが、[**ワークブックレンダリング**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)ワークブックに対しても同じことを行います。前述の両方のクラスには、いくつかのオーバーロードされたバージョンがあります。*画像へ*ワークシートまたはワークブックを、必要な属性またはオプションで指定された画像ファイルに直接変換できるメソッド。画像ファイルをディスク/ストリームに保存できます。サポートされている画像形式はいくつかあります (例: BMP、PNG、GIF、JPEG、TIFF、EMF など)。

###  **ワークシートを画像に変換**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

##  **変換オプション**

特定のページを画像として保存することが可能です。次のコードは、ワークブック内の最初と 2 番目のワークシートを JPG 画像に変換します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

または、ワークブックを循環して、その中の各ワークシートを個別の画像にレンダリングすることもできます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

##  **ワークブックを画像に変換:**

完全なワークブックを画像形式でレンダリングするには、上記の方法を使用するか、単に[**ワークブックレンダリング**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)のインスタンスを受け入れるクラス[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)の対象物でもあります[**画像または印刷オプション**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

ワークブック全体を複数のフレームまたはページを含む 1 つの TIFF 画像に保存できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## 関連記事

- [ワークシートを別の画像形式に変換する](/cells/ja/java/converting-worksheet-to-different-image-formats/)
- [viewBox 属性を使用してチャートを SVG にエクスポート](/cells/ja/java/export-chart-to-svg-with-viewbox-attribute/)
- [ワークシートまたはチャートを希望の幅と高さで画像にエクスポート](/cells/ja/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [ページごとにワークシートを画像に変換し、ワークシートを画像に変換する](/cells/ja/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
