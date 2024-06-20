---
title: 画像またはImageOrPrintOptionsを使用してワークシートおよびブックを画像にレンダリング
type: docs
weight: 220
url: /ja/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---

{{% alert color="primary" %}}

この文書は、ワークシートまたはブックを画像ファイルに変換し、画像や印刷オプションを適用する方法について詳細な理解を提供するように設計されています。解像度、TIFF圧縮、画像形式、ページ品質などのオプションの設定がサポートされています。

{{% /alert %}}

## **概要**

時々、ワークシートを図解的に表示する必要があります。ワークシートの画像をアプリケーションやWebページに挿入する必要があります。画像をWord文書、PDFファイル、PowerPointプレゼンテーションに挿入したり、他のシナリオで使用する必要があります。別の場所で使用するためにワークシートを画像としてレンダリングしたいと思うだけです。Aspose.CellsはExcelファイルのワークシートを画像に変換することをサポートしています。また、Aspose.Cellsは画像形式、解像度（縦と横の両方）、画像品質、およびその他の画像および印刷オプションを設定することをサポートしています。

APIには、例えば[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)、[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)などの貴重なクラスがいくつかあります。

[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)クラスは、ワークシートのイメージをレンダリングするタスクを処理し、[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)クラスはワークブックのイメージを処理します。両前述のクラスには、ワークシートまたはワークブックをイメージファイルに直接変換する*toImage*メソッドのオーバーロードされたバージョンがいくつかあり、指定した属性やオプションでイメージファイルを保存できます。BMP、PNG、GIFF、JPEG、TIFF、EMFなどのさまざまな画像形式がサポートされています。

### **ワークシートを画像に変換**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **変換オプション**

特定のページを画像に保存することが可能です。次のコードは、ワークブック内の最初と2番目のワークシートをJPG画像に変換します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

またはワークブックをサイクルして、それぞれのワークシートを別々の画像にレンダリングすることができます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **ワークブックを画像に変換**

完全なワークブックを画像形式にレンダリングするためには、上記の方法を使用するか、単純に[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)クラスを使用し、[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)のインスタンスと[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)のオブジェクトを受け入れるようにします。

ホールワークブックを複数のフレームまたはページでTIFF画像単体で保存することができます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## 関連記事

- [ワークシートを異なる画像形式に変換する](/cells/ja/java/converting-worksheet-to-different-image-formats/)
- [viewBox属性を使用してチャートをSVGにエクスポート](/cells/ja/java/export-chart-to-svg-with-viewbox-attribute/)
- [希望の幅と高さでワークシートまたはチャートを画像にエクスポート](/cells/ja/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [ワークシートを画像に変換し、ページごとに画像をワークシートに変換する](/cells/ja/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
