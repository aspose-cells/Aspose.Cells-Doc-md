---
title: チャートでのデータの書式設定
linktitle: データソース
type: docs
weight: 50
url: /ja/java/data-formatting-in-charts/
---

{{% alert color="primary" %}}

以前のトピックで、チャートのデータソースを設定する方法の多くの例を提供しましたが、このトピックではチャートに設定できるデータの種類について詳細を提供します。

{{% /alert %}}

## **チャートデータの設定**

Aspose.Cellsを使用してチャートを作成する際に扱うデータには、次の2種類があります：

- [チャートデータ](/cells/ja/java/data-formatting-in-charts/#chart-data)
- [カテゴリデータ](/cells/ja/java/data-formatting-in-charts/#category-data)

### **チャートデータ**

チャートデータとは、チャートを作成するためのデータソースとして使用されるデータです。[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)オブジェクトの[**Add**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add(java.lang.Object))メソッドを呼び出すことで、チャートデータを含むセルの範囲を追加できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **カテゴリデータ**

カテゴリデータは、チャートデータにラベル付けするために使用され、[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)の[**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData)メソッドを使用して追加できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**カラムチャートとチャート＆カテゴリデータ** 

![todo:image_alt_text](data-formatting-in-charts_1.png)

## **高度なトピック**
- [動的なチャートを作成する](/cells/ja/java/create-dynamic-charts/)
- [Chart.setChartDataRangeメソッドを使用したチャートセットアップの簡単な方法](/cells/ja/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [チャートシリーズのX値とY値のタイプを検索する](/cells/ja/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [チャートシリーズの値の形式コードを設定する](/cells/ja/java/set-the-values-format-code-of-chart-series/)
