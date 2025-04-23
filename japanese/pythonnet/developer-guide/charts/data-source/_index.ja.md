---
title: チャートのデータソースを設定
description: Aspose.Cells for Python via .NET がサポートするさまざまなデータソースについて学びます。ガイドでは、利用可能なさまざまな種類のデータソースと、それらからデータを接続・取得してワークシートに反映させる方法を紹介します。
keywords: Aspose.Cells for Python via .NET、チャート作成、データフォーマット、ラベル、色、フォント、外観、操作性。
linktitle: データソース
type: docs
weight: 10
url: /ja/python-net/data-formatting-in-charts/
---

以前のトピックで、チャートのデータソースを設定する方法の多くの例を提供しましたが、このトピックではチャートに設定できるデータの種類について詳細を提供します。

## **チャートデータの設定**

Aspose.Cells for Python via .NET を使用してチャートのデータラベルを管理する際に扱う2つのタイプのデータがあります：

- チャートデータ。
- カテゴリデータ。

### **チャートデータ**

チャートデータは、チャートを作成するためのデータソースとして使用するデータです。 [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)オブジェクトの[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/add)メソッドを呼び出すことで、セルの範囲（チャートデータを含む）を追加できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsData-1.py" >}}

### **カテゴリデータ**

カテゴリデータは、チャートデータのラベリングに使用され、[**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)の[**category_data**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/category_data)プロパティを使用して追加できます。以下に使用例を示します。上記のコードを実行すると、ワークシートに列グラフが追加されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingCategoryData-1.py" >}}

## **高度なトピック**
- [行や範囲をコピーする際に、チャートのデータソースを宛先ワークシートに変更する](/cells/ja/python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [動的なチャートを作成する](/cells/ja/python-net/create-dynamic-charts/)
- [Chart.SetChartDataRangeメソッドを使用した簡単なチャート設定方法](/cells/ja/python-net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [チャートシリーズのX値とY値のタイプを検索する](/cells/ja/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/)
