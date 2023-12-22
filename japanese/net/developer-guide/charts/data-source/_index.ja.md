---
title: グラフのデータソースを設定する
description: Aspose.Cells for .NET でサポートされているさまざまなデータ ソースについて説明します。このガイドでは、利用可能なさまざまな種類のデータ ソースについて説明し、それらのデータ ソースに接続してデータを取得してワークシートにデータを入力する方法を説明します。
keywords: Aspose.Cells for .NET, charting, data formatting, labels, colors, fonts, appearance, usability.
linktitle: 情報元
type: docs
weight: 10
url: /ja/net/data-formatting-in-charts/
---
これまでのトピックでは、グラフのデータ ソースを設定する方法を示す多くの例をすでに提供しましたが、このトピックでは、グラフに設定できるデータの種類についてさらに詳しく説明します。

##  **チャートデータの設定**

Aspose.Cells を使用してグラフを操作するときに処理するデータは次の 2 種類があります。

- チャートデータ。
- カテゴリデータ。

###  **チャートデータ**

チャート データは、チャートを作成するためのデータ ソースとして使用するデータです。を呼び出すことで、セル範囲 (グラフ データを含む) を追加できます。[**シリーズコレクション**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)オブジェクトの[**追加**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

###  **カテゴリデータ**

カテゴリ データはグラフ データのラベル付けに使用され、次のデータに追加できます。[**シリーズコレクション**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)それを使用して[**カテゴリデータ**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)財産。グラフとカテゴリ データの使用を示す完全な例を以下に示します。上記のコード例を実行すると、以下に示すように縦棒グラフがワークシートに追加されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

##  **アドバンストトピック**
- [行または範囲のコピー中にグラフのデータ ソースを宛先ワークシートに変更する](/cells/ja/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [動的なチャートの作成](/cells/ja/net/create-dynamic-charts/)
- [Chart.SetChartDataRangeメソッドを使用した簡単なチャート設定方法](/cells/ja/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [チャート系列のポイントの X 値と Y 値のタイプを検索する](/cells/ja/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
