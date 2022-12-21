---
title: テンプレート ファイルからワークブックを読み込む際のデータの種類のフィルタリング
type: docs
weight: 680
url: /ja/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}} 

テンプレート ファイルからワークブックを作成するときに、読み込むデータの種類を指定したい場合があります。ロードされたデータをフィルタリングすると、特別な目的のためにパフォーマンスを向上させることができます。[LightCell API](/cells/ja/java/using-lightcells-api/) .をご利用ください[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions)この目的のためのプロパティ。

{{% /alert %}} 
## **テンプレート ファイルからワークブックを読み込む際のデータの種類のフィルタリング**
次のサンプル コードは、ワークブックを[テンプレートファイル](5472556.xlsx)指定されたリンクからダウンロードできます。

次のスクリーンショットは、[テンプレートファイル](5472556.xlsx)また、色が赤で背景が黄色のデータは読み込まれないことも説明しています。[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions)プロパティはに設定されています[LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE).

![todo:画像_代替_文章](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

次のスクリーンショットは、[PDF出力](5472554.pdf)指定されたリンクからダウンロードできます。ここでわかるように、赤色と黄色の背景のデータは存在しませんが、すべての形状が存在します。

![todo:画像_代替_文章](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
