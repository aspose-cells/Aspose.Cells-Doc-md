---
title: チャートのデータラベルのテキスト折り返しを無効にする
type: docs
weight: 60
url: /ja/java/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013では、データラベルのテキストはデフォルトで折り返されます。

{{% /alert %}}

Aspose.Cellsは[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)メソッドを提供しています。データラベルのテキストの折り返しを有効または無効にするには、**True**または**False**に設定します。

同様に、[**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)メソッドを使用して、データラベルが既に折り返されているかどうかを調べることができます。

このスクリーンショットは、データラベルのテキストが折り返されているサンプルMicrosoft Excelファイルを示しています。Microsoft Excel 2013のフォーマットデータラベルパネルのALIGNMENTセクションで、**図形のテキストを折り返し**オプションをチェックまたはクリアできることがわかります。

データラベルの折り返し

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

次のサンプルコードは、Aspose.Cellsを使用してサンプルMicrosoft Excelファイルを読み込み、[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)メソッドを使用してデータラベルのテキストの折り返しを無効にします。コード実行後、チャートは以下のようになります。以前折り返されていたテキストが折り返されていません。

データラベルを1行に表示する

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
