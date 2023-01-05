---
title: ワークシートから画像へ、ワークシートから画像へのページ単位での変換
type: docs
weight: 210
url: /ja/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

このドキュメントは、開発者がワークシートを画像ファイルに変換する方法と、複数ページのワークシートをページごとに画像ファイルに変換する方法を詳細に理解できるように設計されています。

たとえば、ワークシートをアプリケーションや Web ページで使用するために、ワークシートを画像として表示する必要がある場合があります。画像を Word 文書、PDF ファイル、PowerPoint プレゼンテーションに挿入したり、他のシナリオで使用したりする必要がある場合があります。単純に、ワークシートを画像としてレンダリングしたいだけです。 Aspose.Cells API は、Microsoft Excel ファイルのワークシートを画像に変換することをサポートします。また、Aspose.Cells は、ワークブックを複数の画像ファイル (ページごとに 1 つ) に変換することをサポートしています。

{{% /alert %}}

## **Aspose.Cells を使用してワークシートを画像ファイルに変換する**

この記事では、Aspose.Cells for Java API を使用してワークシートを画像に変換する方法を示します。 API は、次のようないくつかの価値のあるクラスを提供します。[**シートレンダリング**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) 、 等々。の[**シートレンダリング**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)クラスは、ワークシートの画像をレンダリングするためのワークシートを表し、オーバーロードされた[**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream)任意の属性またはオプション セットを使用して、ワークシートを画像ファイルに直接変換できるメソッド。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **結果**

上記のコードを実行すると、Sheet1 という名前のワークシートが画像ファイル SheetImage.jpg に変換されます。

**出力JPG**

![todo:画像_代替_文章](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **Aspose.Cells を使用してワークシートをページごとに画像ファイルに変換する**

この例では、Aspose.Cells を使用して、複数ページのテンプレート ワークブックからワークシートをページごとに 1 つのイメージ ファイルに変換する方法を示します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **結果**

上記のコードを実行すると、Sheet1 という名前のワークシートが 2 つの画像ファイル (1 ページに 1 つ) に変換されます。Sheet 1 Page 1.Tiff と Sheet 1 Page 2.Tiff です。

**生成された画像ファイル (Sheet 1 Page 1.Tiff)**

![todo:画像_代替_文章](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**生成された画像ファイル (Sheet 1 Page 2.Tiff)**

![todo:画像_代替_文章](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

この記事では、Aspose.Cells を使用して、ワークシートを画像ファイルに変換する方法と、複数ページのワークシートを複数の画像ファイル (1 ページに 1 つ) に変換する方法を示します。結果は、Aspose.Cells が何年にもわたる研究、設計、および慎重な調整の恩恵を受けていることを示しています。

{{% /alert %}}

## 関連記事

- [ワークシートを別の画像形式に変換する](/cells/ja/java/converting-worksheet-to-different-image-formats/)
- [ワークシートまたはチャートを目的の幅と高さの画像にエクスポート](/cells/ja/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
