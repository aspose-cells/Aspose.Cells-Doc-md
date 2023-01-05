---
title: チャートでのデータの書式設定
linktitle: 情報元
type: docs
weight: 50
url: /ja/java/data-formatting-in-charts/
---
{{% alert color="primary" %}}

前のトピックでは、グラフのデータ ソースを設定する方法を示すために既に多くの例を提供しましたが、このトピックでは、グラフに設定できるデータの種類についてさらに詳しく説明します。

{{% /alert %}}

## **チャートデータの設定**

次のように、Aspose.Cells を使用してグラフを操作する際に扱うデータには、次の 2 種類があります。

- [チャートデータ](/cells/ja/java/data-formatting-in-charts/#chart-data).
- [カテゴリーデータ](/cells/ja/java/data-formatting-in-charts/#category-data).

### **チャートデータ**

チャート データは、チャートを作成するためのデータ ソースとして使用するデータです。を呼び出して、セル範囲 (グラフ データを含む) を追加できます。[**シリーズコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)オブジェクトの[**追加**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add(java.lang.Object)） 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **カテゴリーデータ**

カテゴリ データは、グラフ データのラベル付けに使用され、追加できます。[**シリーズコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)その使用によって[**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData)方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**グラフとカテゴリ データを含む縦棒グラフ** 

![todo:画像_代替_文章](data-formatting-in-charts_1.png)

## **先行トピック**
- [ダイナミック チャートの作成](/cells/ja/java/create-dynamic-charts/)
- [Chart.setChartDataRange メソッドを使用したチャート設定の簡単な方法](/cells/ja/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [チャート シリーズのポイントの X 値と Y 値のタイプを見つける](/cells/ja/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [チャート シリーズの値のフォーマット コードを設定する](/cells/ja/java/set-the-values-format-code-of-chart-series/)
