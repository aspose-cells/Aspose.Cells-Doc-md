---
title: ImageOrPrintOptions を使用してワークシートとワークブックをイメージにレンダリングする
type: docs
weight: 220
url: /ja/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---
{{% alert color="primary" %}}

このドキュメントは、ワークシートまたはワークブックを画像ファイルに変換し、画像にさまざまな画像および印刷オプション、解像度、TIFF 圧縮、画像形式、およびページ品質などのオプションを適用する方法を詳細に理解できるように設計されています。

{{% /alert %}}

## **概要**

場合によっては、ワークシートを絵で表したものとして提示する必要がある場合があります。ワークシート イメージをアプリケーションまたは Web ページに表示する必要があります。画像を Word 文書、PDF ファイル、PowerPoint プレゼンテーションに挿入したり、他のシナリオで使用したりする必要がある場合があります。他の場所で使用できるように、ワークシートを画像としてレンダリングしたいだけです。 Aspose.Cells は、Excel ファイルのワークシートを画像に変換することをサポートしています。また、Aspose.Cells は、画像形式、解像度 (縦と横の両方)、画質、その他の画像および印刷オプションなど、さまざまなオプションの設定をサポートしています。

API は、いくつかの価値のあるクラスを提供します。たとえば、[**シートレンダリング**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)など

の[**シートレンダリング**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)クラスは、ワークシートの画像をレンダリングするタスクを処理しますが、[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)ワークブックに対しても同じことを行います。前述の両方のクラスには、いくつかのオーバーロードされたバージョンの*toImage*ワークシートまたはワークブックを、目的の属性またはオプションで指定された画像ファイルに直接変換できるメソッド。画像ファイルをディスク/ストリームに保存できます。 BMP、PNG、GIFF、JPEG、TIFF、EMF など、いくつかの画像フォーマットがサポートされています。

### **ワークシートを画像に変換**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **変換オプション**

特定のページを画像として保存することができます。次のコードは、ワークブックの 1 番目と 2 番目のワークシートを JPG 画像に変換します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

または、ワークブックを循環して、その中の各ワークシートを個別の画像にレンダリングできます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **ワークブックを画像に変換:**

ワークブック全体を画像形式にレンダリングするには、上記の方法を使用するか、単純に[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)のインスタンスを受け入れるクラス[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)の対象だけでなく、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

{{% alert color="primary" %}}

の[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)クラスは、ワークブックを TIFF 形式でのみ保存できます。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## 関連記事

- [ワークシートを別の画像形式に変換する](/cells/ja/java/converting-worksheet-to-different-image-formats/)
- [viewBox属性を使用してグラフをSVGにエクスポートします](/cells/ja/java/export-chart-to-svg-with-viewbox-attribute/)
- [ワークシートまたはチャートを目的の幅と高さの画像にエクスポート](/cells/ja/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [ワークシートから画像へ、ワークシートから画像へのページ単位での変換](/cells/ja/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
