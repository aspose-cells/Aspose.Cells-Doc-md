---
title: テンプレートファイルからワークブックをロードする際にデータの種類をフィルタリングする
type: docs
weight: 680
url: /ja/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}} 

時々、テンプレートファイルからワークブックを構築する際に、ロードされるデータの種類を指定したい場合があります。ロードされるデータをフィルタリングすることで、特定の目的に対してパフォーマンスが向上し、特に[LightCells APIs](/cells/ja/java/using-lightcells-api/)を使用する場合に便利です。この目的のために、[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) プロパティを使用してください。

{{% /alert %}} 
## **テンプレートファイルからワークブックをロードする際にデータの種類をフィルタリングする**
以下のサンプルコードは、[テンプレートファイル](5472556.xlsx) からワークブックをロードする際に、形状オブジェクトのみをロードします。指定されたリンクからダウンロードすることができます。

以下のスクリーンショットは、[テンプレートファイル](5472556.xlsx) の内容を示し、赤色のデータおよび黄色の背景色のデータは[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) プロパティが[LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE) に設定されているため、ロードされないことを説明しています。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

指定されたリンクからダウンロードできる[出力PDF](5472554.pdf) を示す以下のスクリーンショットです。ここでは、赤色および黄色の背景色のデータが存在しないことが確認できますが、すべての形状オブジェクトは存在します。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
