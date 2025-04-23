---
title: C++を使用してChartGlobalizationSettingsクラスを使い、チャートコンポーネントの異なる言語を設定する方法
linktitle: ChartGlobalizationSettingsクラスの使用
description: Aspose.Cells for C++でChartGlobalizationSettingsクラスの使い方を学び、チャートコンポーネントの異なる言語設定を行います。ガイドは、チャートの要素、ラベル、凡例を異なる言語にローカライズする方法を理解し、データを文化的に適切な方法で提示できるよう支援します。
keywords: Aspose.Cells for C++、チャート作成、チャートグローバリゼーション、言語、ローカリゼーション、ChartGlobalizationSettings、要素、ラベル、凡例。
type: docs
weight: 2200
url: /ja/cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **可能な使用シナリオ**

Aspose.CellsのAPIは、ユーザーがチャートコンポーネントを異なる言語に設定したい場合に取り扱うために、[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/)クラスを公開しています。スプレッドシート内の小計のカスタムラベル。 

## **ChartGlobalizationSettingsクラスの紹介**

[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/)クラスは、現在、カスタムクラスでオーバーライドできる次の8つのメソッドを提供しています。これにより、軸タイトル名、軸単位名、チャイトル名などを異なる言語に翻訳できます。

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/)：軸タイトルの名前を取得します。
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/)：軸単位の名前を取得します。
1. [**GetChartTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/)：チャートタイトルの名前を取得します。
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/)：凡例の減少の名前を取得します。
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/)：凡例の増加の名前を取得します。
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/)：凡例の合計の名前を取得します。
1. [**GetOtherName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getothername/)：チャートの「その他」ラベルの名前を取得します。
1. [**GetSeriesName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getseriesname/)：チャート内の系列の名前を取得します。

### **カスタム言語の翻訳**
以下、次のデータを元にウォーターフォールチャートを作成します。チャートコンポーネントの名前は、チャート内で英語で表示されます。チャートタイトル、凡例の増減名、合計名、および軸タイトルのトルコ語表示方法を示すためにトルコ語の例を使用します。

![todo:image_alt_text](sample.png)

## **サンプルコード**
次のサンプルコードは、[サンプルExcelファイル](waterfall.xlsx)を読み込みます。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

class TurkeyChartGlobalizationSettings : public ChartGlobalizationSettings
{
public:
    TurkeyChartGlobalizationSettings() : ChartGlobalizationSettings() {}

    U16String GetChartTitleName() override
    {
        return u"Grafik Başlığı"; // Chart Title
    }

    U16String GetLegendIncreaseName() override
    {
        return u"Artış"; // Increase
    }

    U16String GetLegendDecreaseName() override
    {
        return u"Düşüş"; // Decrease
    }

    U16String GetLegendTotalName() override
    {
        return u"Toplam"; // Total
    }

    U16String GetAxisTitleName() override
    {
        return u"Eksen Başlığı"; // Axis Title
    }
};

void ChartGlobalizationSettingsTest()
{
    // Create an instance of existing Workbook
    U16String pathName = u"input.xlsx";
    Workbook workbook(pathName);

    // Set custom chartGlobalizationSettings, here is TurkeyChartGlobalizationSettings
    TurkeyChartGlobalizationSettings* globalizationSettings = new TurkeyChartGlobalizationSettings();
    workbook.GetSettings().GetGlobalizationSettings()->SetChartSettings(globalizationSettings);

    // Get the worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Load the chart from source worksheet
    ChartCollection chartCollection = worksheet.GetCharts();
    Chart chart = chartCollection.Get(0);

    // Chart Calculate
    chart.Calculate();

    // Get the chart title
    Title title = chart.GetTitle();

    // Output the name of the Chart title
    std::cout << "\nWorkbook chart title: " << title.GetText().ToUtf8() << std::endl;

    // Get the legend labels
    Vector<U16String> legendEntriesLabels = chart.GetLegend().GetLegendLabels();

    // Output the name of the Legend
    for (int i = 0; i < legendEntriesLabels.GetLength(); i++)
    {
        std::cout << "\nWorkbook chart legend: " << legendEntriesLabels[i].ToUtf8() << std::endl;
    }

    // Output the name of the Axis title
    Title categoryAxisTitle = chart.GetCategoryAxis().GetTitle();
    std::cout << "\nWorkbook category axis title: " << categoryAxisTitle.GetText().ToUtf8() << std::endl;

    delete globalizationSettings;
}

int main()
{
    Aspose::Cells::Startup();
    ChartGlobalizationSettingsTest();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## サンプルコードによって生成された出力

これは上記のサンプルコードのコンソール出力です。

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
