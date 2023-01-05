---
title: グラフのデータ ラベルのテキストの折り返しを無効にする
type: docs
weight: 60
url: /ja/java/disable-text-wrapping-for-data-labels-of-the-chart/
---
{{% alert color="primary" %}}

Microsoft Excel 2013 では、ユーザーはグラフのデータ ラベル内のテキストをラップまたはアンラップできます。デフォルトでは、データ ラベルのテキストは折り返されます。

{{% /alert %}}

Aspose.Cells は[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)方法。に設定**真実**また**間違い**データ ラベルのテキスト ラッピングをそれぞれ有効または無効にします。

同様に、[**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)メソッドを使用して、データ ラベルが既にラップされているかどうかを確認します。

このスクリーンショットは、データ ラベルのテキストが折り返されたグラフを含むサンプル Microsoft Excel ファイルを示しています。ご覧のとおり、**テキストを図形で折り返す**Microsoft Excel 2013 の Format Datalabels パネルの ALIGNMENT セクションの ALIGNMENT オプション。

**データ ラベルのラッピング**

![todo:画像_代替_文章](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

次のサンプル コードは、Aspose.Cells を使用してサンプル Microsoft Excel ファイルを読み込み、[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)方法。コードが実行されると、チャートは次のようになります。以前にラップされたテキストがアンラップされます。

**1 行だけにデータ ラベルを表示する**

![todo:画像_代替_文章](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
