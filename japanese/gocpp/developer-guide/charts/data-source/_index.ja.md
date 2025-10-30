---
title: Golang を使った C++ によるチャートのデータソース設定
linktitle: データソース
type: docs
weight: 10
url: /ja/go-cpp/data-formatting-in-charts/
description: Aspose.Cells for C++がサポートするさまざまなデータソースについて学びます。ガイドは、利用可能なデータソースの種類と、それらに接続してデータを取得し、ワークシートを埋める方法を案内します。
keywords: Aspose.Cells for C++、チャート作成、データフォーマット、ラベル、色、フォント、外観、使いやすさ。
---

これまでのトピックでは、データソースを設定する方法の多くの例を示してきました。このトピックでは、チャートに設定できるデータの種類について詳しく説明します。

## **チャートデータの設定**

Aspose.Cellsを使用してチャートを作成する際に扱うデータには、次の2種類があります：

- チャートデータ。
- カテゴリデータ。

### **チャートデータ**

チャートデータは、チャートを作成するためのデータソースとして使用するデータです。 [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/)オブジェクトの[**Add**](https://reference.aspose.com/cells/go-cpp/seriescollection/add/)メソッドを呼び出すことで、セルの範囲（チャートデータを含む）を追加できます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource.go" >}}
### **カテゴリデータ**

カテゴリデータは、チャートデータのラベリングに使用され、[**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/)の[**GetCategoryData()**](https://reference.aspose.com/cells/go-cpp/seriescollection/getcategorydata/)プロパティを使用して追加できます。以下に使用例を示します。上記のコードを実行すると、ワークシートに列グラフが追加されます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource-1.go" >}}
## ** 高度なトピック**
- [行や範囲をコピーする際に、チャートのデータソースを宛先ワークシートに変更する](/cells/ja/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [動的なチャートを作成する](/cells/ja/cpp/create-dynamic-charts/)
- [Chart.SetChartDataRangeメソッドを使用した簡単なチャート設定方法](/cells/ja/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [チャートシリーズのX値とY値のタイプを検索する](/cells/ja/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
