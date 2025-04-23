---
title: ワークシートを画像に変換し、ページごとにワークシートを画像に変換
type: docs
weight: 210
url: /ja/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

このドキュメントは、開発者に、ワークシートを画像ファイルに変換する方法と、複数のページを持つワークシートを1ページごとに画像ファイルに変換する方法についての詳細な理解を提供するように設計されています。

時々、ワークシートを画像として表示する必要があります。例えば、アプリケーションやWebページで使用するために画像を挿入したい場合があります。画像をWord文書、PDFファイル、PowerPointプレゼンテーションに挿入する必要があったり、他のシナリオで使用する必要があったりします。単純に言えば、ワークシートを画像としてレンダリングしたいのです。 Aspose.Cells API は、Microsoft Excelファイルのワークシートを画像に変換することをサポートしています。また、Aspose.Cells は、ワークブックを複数のイメージファイルに変換することもサポートしています。

{{% /alert %}}

## **Aspose.Cellsを使用してワークシートを画像ファイルに変換する方法**

この記事では、Aspose.Cells for Java APIを使用してワークシートをイメージに変換する方法について説明します。APIは、[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)、[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)など、いくつかの貴重なクラスを提供しています。[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) クラスは、ワークシートを描画し、そのワークシートのイメージを生成するための[**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage-int-java.io.OutputStream-)メソッドをオーバーロードされたものを提供しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **結果**

上記のコードを実行した後、Sheet1というワークシートがSheetImage.jpgという画像ファイルに変換されます。

**生成されたJPG**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **Aspose.Cellsを使用して、ワークシートを画像ファイルにページごとに変換する**

この例では、Aspose.Cellsを使用して、複数のページを持つテンプレートワークブックからワークシートを1つの画像ファイルに変換する方法を示します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **結果**

上記のコードを実行した後、Sheet1というワークシートが1ページごとに1つのイメージファイル（Sheet 1 Page 1.TiffおよびSheet 1 Page 2.Tiff）に変換されます。

**生成されたイメージファイル（Sheet 1 Page 1.Tiff）**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**生成されたイメージファイル（Sheet 1 Page 2.Tiff）**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

この記事では、Aspose.Cellsを使用してワークシートをイメージファイルに変換し、複数のページを持つワークシートを1ページごとに1つのイメージファイルに変換する方法について説明します。Aspose.Cellsは他のコンポーネントよりも柔軟性があり、優れた速度、効率性、信頼性を提供しています。結果からも分かるように、Aspose.Cellsは長年にわたる研究、設計、慎重なチューニングの成果を享受しています。

{{% /alert %}}

## 関連記事

- [ワークシートを異なる画像形式に変換する](/cells/ja/java/converting-worksheet-to-different-image-formats/)
- [希望の幅と高さでワークシートまたはチャートを画像にエクスポート](/cells/ja/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
{{< app/cells/assistant language="java" >}}
