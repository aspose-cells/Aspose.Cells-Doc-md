---
title:  ChartGlobalizationSettings クラスを使用してグラフ コンポーネントに異なる言語を設定する
description: Aspose.Cells for .NET の ChartGlobalizationSettings クラスを使用して、グラフ コンポーネントにさまざまな言語を設定する方法を学習します。このガイドは、グラフの要素、ラベル、凡例をさまざまな言語にローカライズする方法を理解し、文化的に適切な方法でデータを表示できるようにするのに役立ちます。
keywords: Aspose.Cells for .NET, charting, chart globalization, languages, localization, ChartGlobalizationSettings, elements, labels, legends.
type: docs
weight: 2200
url: /ja/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---
##  **考えられる使用シナリオ**

 Aspose.Cells API により、[**チャートグローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)ユーザーがチャートコンポーネントを別の言語に設定したいシナリオに対処するためにクラスを追加します。スプレッドシートの小計のカスタム ラベル。

##  **ChartGlobalizationSettings クラスの概要**

の[**チャートグローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)クラスは現在、次の 8 つのメソッドを提供しており、カスタム クラスでオーバーライドして、AxisTitle 名、AxisUnit 名、ChartTitle 名などを別の言語に翻訳できます。
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): 軸のタイトル名を取得します。
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/)：軸ユニット名を取得します。
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): チャートのタイトルの名前を取得します。
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): レジェンドの減少の名前を取得します。
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): レジェンドの増加名を取得します。
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): 凡例の合計の名前を取得します。
1. [**他の名前を取得する**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/)チャートの「その他」ラベルの名前を取得します。
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): チャート内のシリーズの名前を取得します。

###  **カスタム言語翻訳**
ここでは、以下のデータをもとにウォーターフォールチャートを作成していきます。チャートコンポーネントの名前はチャート内に英語で表示されます。トルコ語の例を使用して、グラフのタイトル、凡例の増減名、合計名、軸タイトルをトルコ語で表示する方法を示します。

![todo:image_alt_text](sample.png)

##  **サンプルコード**
次のサンプルコードは、[サンプル Excel ファイル](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

## サンプルコードによって生成される出力

これは、上記のサンプル コードのコンソール出力です。

{{< highlight "java" >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
