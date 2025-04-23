---
title: チャートのデータラベルの形状をテキストに合わせるようにサイズ変更する
type: docs
weight: 190
url: /ja/java/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}

Excelアプリケーションは、チャートのデータラベルの**テキストに合わせたシェイプをリサイズ**するオプションを提供しています。これにより、テキストが内部に収まるようにシェイプのサイズを拡大できます。このオプションは、Excelインターフェースでチャートのデータラベルを選択し、右クリックして**フォーマットデータラベル**メニューを選択することでアクセスできます。**Size & Properties**タブで、**Alignment**を展開して**テキストに合わせてサイズ変更**オプションを表示します。

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_1.png)

{{% /alert %}}

## **テキストに合わせるようにチャートのデータラベルの形状をリサイズする**

Excelのデータラベルのサイズをテキストに合わせる機能を模倣するために、Aspose.Cells APIでは、ブール型[**DataLabels.ResizeShapeToFitText**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText)プロパティが公開されています。次のコード例は、[**DataLabels.ResizeShapeToFitText**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText)プロパティの簡単な使用シナリオを示しています。

コードを実行する前のチャートは次のように見えます。

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResizeChartDataLabelShapeToFitText-ResizeChartDataLabelShapeToFitText.java" >}}

コードを実行した後のチャートは次のように見えます。

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_3.png)
{{< app/cells/assistant language="java" >}}
