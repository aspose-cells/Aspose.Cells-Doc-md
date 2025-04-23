---
title: ChartGlobalizationSettingsクラスを使用して、チャートコンポーネントの異なる言語を設定する方法 
description: Aspose.Cells for .NETでChartGlobalizationSettingsクラスを使用して、チャートコンポーネントの異なる言語を設定する方法を学びます。当社のガイドは、チャート要素、ラベル、凡例を異なる言語にローカライズして、データを適切な文化的な方法で表示する方法を理解するのに役立ちます。
keywords: Aspose.Cells for .NET、チャート作成、チャートのグローバリゼーション、言語、ローカライゼーション、ChartGlobalizationSettings、要素、ラベル、凡例
type: docs
weight: 2200
url: /ja/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **可能な使用シナリオ**

Aspose.CellsのAPIは、ユーザーがチャートコンポーネントを異なる言語に設定したい場合に取り扱うために、[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)クラスを公開しています。スプレッドシート内の小計のカスタムラベル。 

## **ChartGlobalizationSettingsクラスの紹介**

[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)クラスは現在、異なる言語に翻訳するためのカスタムクラスでオーバーライドできる8つのメソッドを提供します。例えば、AxisTitle名、AxisUnit名、ChartTitle名など。
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/)：軸タイトルの名前を取得します。
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/)：軸単位の名前を取得します。
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/)：チャートタイトルの名前を取得します。
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/)：凡例の減少の名前を取得します。
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/)：凡例の増加の名前を取得します。
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/)：凡例の合計の名前を取得します。
1. [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/)：チャートの「その他」ラベルの名前を取得します。
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/)：チャート内の系列の名前を取得します。

### **カスタム言語の翻訳**
以下、次のデータを元にウォーターフォールチャートを作成します。チャートコンポーネントの名前は、チャート内で英語で表示されます。チャートタイトル、凡例の増減名、合計名、および軸タイトルのトルコ語表示方法を示すためにトルコ語の例を使用します。

![todo:image_alt_text](sample.png)

## **サンプルコード**
次のサンプルコードは、[サンプルExcelファイル](waterfall.xlsx)を読み込みます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

## サンプルコードによって生成された出力

これは上記のサンプルコードのコンソール出力です。

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
