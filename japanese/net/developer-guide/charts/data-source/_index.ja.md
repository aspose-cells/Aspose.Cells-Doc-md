---
title: チャートのデータソースを設定
description: Aspose.Cells for .NETでサポートされているさまざまなデータソースについて学びます。このガイドでは、利用可能なさまざまなデータソースの種類と、それらのデータソースに接続してデータを取得し、ワークシートを作成するための方法を紹介します。
keywords: Aspose.Cells for .NET、チャート作成、データの書式設定、ラベル、色、フォント、外観、使いやすさ。
linktitle: データソース
type: docs
weight: 10
url: /ja/net/data-formatting-in-charts/
---

以前のトピックで、チャートのデータソースを設定する方法の多くの例を提供しましたが、このトピックではチャートに設定できるデータの種類について詳細を提供します。

## **チャートデータの設定**

Aspose.Cellsを使用してチャートを作成する際に扱うデータには、次の2種類があります：

- チャートデータ。
- カテゴリデータ。

### **チャートデータ**

チャートデータは、チャートを作成するためのデータソースとして使用するデータです。 [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)オブジェクトの[**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)メソッドを呼び出すことで、セルの範囲（チャートデータを含む）を追加できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **カテゴリデータ**

カテゴリデータは、チャートデータのラベリングに使用され、[**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)の[**CategoryData**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)プロパティを使用して追加できます。以下に使用例を示します。上記のコードを実行すると、ワークシートに列グラフが追加されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **高度なトピック**
- [行や範囲をコピーする際に、チャートのデータソースを宛先ワークシートに変更する](/cells/ja/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [動的なチャートを作成する](/cells/ja/net/create-dynamic-charts/)
- [Chart.SetChartDataRangeメソッドを使用した簡単なチャート設定方法](/cells/ja/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [チャートシリーズのX値とY値のタイプを検索する](/cells/ja/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
{{< app/cells/assistant language="csharp" >}}
