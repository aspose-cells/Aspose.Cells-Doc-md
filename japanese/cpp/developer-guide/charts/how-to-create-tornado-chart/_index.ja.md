---
title: C++でトルネードチャートを作成する方法
linktitle: トルネードチャートを作成する
type: docs
weight: 73
url: /ja/cpp/create-tornado-chart/
description: API Aspose.Cells for C++を使用してトルネードチャートを作成する方法を学びましょう。
keywords: C++を使用してトルネードチャートを作成、トルネードチャートを追加、挿入する
---

## **紹介**
竜巻チャート、または竜巻ダイアグラムまたは竜巻グラフとしても知られるものは、Excelで感度分析によく使用されるデータの視覚化タイプです。これは、特定の結果や成果に対する変数変更の影響を理解するのに役立ちます。

## **Excelで竜巻チャートを作成する方法**
Excelで竜巻チャートを作成する方法は次の通りです：
1. データを選択し、挿入 --> グラフ --> 挿入列または棒グラフ --> 積み上げ棒グラフに移動し、そこをクリックします。
<br>
<img src="1.png" width=70% />
2. Y軸を変更：Y軸を右クリックします。軸の書式設定をクリックします。ラベルで、ラベル位置ドロップダウンをクリックして、Low項目を選択します。
<br>
<img src="2.png" width=70% />
3. 任意の棒を選択し、書式設定に移動します。適切なギャップ幅を設定します。
<br>
<img src="3.png" width=70% />
4. 竜巻チャートからマイナス記号（-）を削除しましょう。X軸を選択します。書式設定に移動し、軸オプションで数字をクリックします。カテゴリでカスタムを選択し、フォーマットコードに###0,###0を記入します。追加をクリックします。
<br>
<img src="4.png" width=70% />
5. y軸をクリックし、「軸のオプション」に移動します。軸のオプションで、「逆順のカテゴリ」を選択します。
<br>
<img src="5.png" width=70% />

## **Aspose.Cellsで竜巻チャートを追加する方法**
次のサンプルコードをご覧ください。[サンプルExcelファイル](sample.xlsx)を読み込み、いくつかのサンプルデータが含まれているとします。次に、初期データに基づいて積み上げ棒グラフを作成し、関連するプロパティを設定します。最後に、ワークブックを[出力XLSX形式](out.xlsx)に保存します。次のスクリーンショットは、出力ExcelファイルでAspose.Cellsによって作成された竜巻チャートを示しています。
<br>
<img src="6.png" width=70% />

### **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Get the chart collection from the worksheet
    ChartCollection charts = sheet.GetCharts();

    // Add a bar chart
    int index = charts.Add(ChartType::BarStacked, 8, 1, 24, 8);
    Chart chart = charts.Get(index);

    // Set data for the bar chart
    chart.SetChartDataRange(u"A1:C7", true);

    // Set properties for the bar chart
    chart.GetTitle().SetText(u"Tornado chart");
    chart.SetStyle(2);
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetPlotArea().GetBorder().SetColor(Color::White());
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set properties for the category axis
    chart.GetCategoryAxis().SetTickLabelPosition(TickLabelPositionType::Low);
    chart.GetCategoryAxis().SetIsPlotOrderReversed(true);

    // Set gap width
    chart.SetGapWidth(10);

    // Set properties for the value axis
    Axis valueAxis = chart.GetValueAxis();
    valueAxis.GetTickLabels().SetNumberFormat(u"#,##0;#,##0");

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
