---
title: グラフのデータ ソースを設定する
linktitle: 情報元
type: docs
weight: 10
url: /ja/net/data-formatting-in-charts/
---
前のトピックでは、グラフのデータ ソースを設定する方法を示すために既に多くの例を提供しましたが、このトピックでは、グラフに設定できるデータの種類についてさらに詳しく説明します。

## **チャートデータの設定**

次のように、Aspose.Cells を使用してグラフを操作する際に扱うデータには、次の 2 種類があります。

- グラフ データ。
- カテゴリ データ。

### **チャートデータ**

チャート データは、チャートを作成するためのデータ ソースとして使用するデータです。を呼び出して、セル範囲 (グラフ データを含む) を追加できます。[**シリーズコレクション**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)オブジェクトの[**追加**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **カテゴリーデータ**

カテゴリ データは、グラフ データのラベル付けに使用され、追加できます。[**シリーズコレクション**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)その使用によって[**カテゴリデータ**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)財産。チャートとカテゴリ データの使用方法を示す完全な例を以下に示します。上記のコード例を実行すると、以下に示すように縦棒グラフがワークシートに追加されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **先行トピック**
- [行または範囲のコピー中にチャートのデータ ソースを宛先ワークシートに変更する](/cells/ja/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [ダイナミック チャートの作成](/cells/ja/net/create-dynamic-charts/)
- [Chart.SetChartDataRange メソッドを使用したチャート設定の簡単な方法](/cells/ja/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [チャート シリーズのポイントの X 値と Y 値のタイプを見つける](/cells/ja/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
