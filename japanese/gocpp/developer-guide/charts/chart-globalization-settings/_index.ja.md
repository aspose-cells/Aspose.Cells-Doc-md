---
title: Golang を使用した C++ による ChartGlobalizationSettings クラスを使ったチャートコンポーネントの異なる言語設定
linktitle: ChartGlobalizationSettingsクラスの使用
description: Aspose.Cells for C++でChartGlobalizationSettingsクラスの使い方を学び、チャートコンポーネントの異なる言語設定を行います。ガイドは、チャートの要素、ラベル、凡例を異なる言語にローカライズする方法を理解し、データを文化的に適切な方法で提示できるよう支援します。
keywords: Aspose.Cells for C++、チャート作成、チャートグローバリゼーション、言語、ローカリゼーション、ChartGlobalizationSettings、要素、ラベル、凡例。
type: docs
weight: 2200
url: /ja/go-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **可能な使用シナリオ**

Aspose.CellsのAPIは、ユーザーがチャートコンポーネントを異なる言語に設定したい場合に取り扱うために、[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/)クラスを公開しています。スプレッドシート内の小計のカスタムラベル。 

## **ChartGlobalizationSettingsクラスの紹介**

[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/)クラスは、現在、カスタムクラスでオーバーライドできる次の8つのメソッドを提供しています。これにより、軸タイトル名、軸単位名、チャイトル名などを異なる言語に翻訳できます。

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxistitlename/)：軸タイトルの名前を取得します。
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxisunitname/)：軸単位の名前を取得します。
1. [**GetChartTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getcharttitlename/)：チャートタイトルの名前を取得します。
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegenddecreasename/)：凡例の減少の名前を取得します。
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendincreasename/)：凡例の増加の名前を取得します。
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendtotalname/)：凡例の合計の名前を取得します。
1. [**GetOtherName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getothername/)：チャートの「その他」ラベルの名前を取得します。
1. [**GetSeriesName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getseriesname/)：チャート内の系列の名前を取得します。

### **カスタム言語の翻訳**
以下、次のデータを元にウォーターフォールチャートを作成します。チャートコンポーネントの名前は、チャート内で英語で表示されます。チャートタイトル、凡例の増減名、合計名、および軸タイトルのトルコ語表示方法を示すためにトルコ語の例を使用します。

![todo:image_alt_text](sample.png)

## **サンプルコード**
次のサンプルコードは、[サンプルExcelファイル](waterfall.xlsx)を読み込みます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartGlobalizationSettings.go" >}}
## サンプルコードによって生成された出力

これは上記のサンプルコードのコンソール出力です。

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
