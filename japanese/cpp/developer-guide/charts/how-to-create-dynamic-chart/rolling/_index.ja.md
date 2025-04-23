---
title: C++を使った動的ローリングチャートの作成方法
linktitle: 動的ローリングチャートの作成方法
description: Aspose.Cells for C++を使用して動的ローリングチャートを作成する方法を学びます。滑らかなデータ遷移とローリング平均を実装し、連続した更新表示を行う方法を示します。
keywords: Aspose.Cells for C++、動的ローリングチャート、データ遷移、滑らかな平均値、連続表示、更新された視覚化。
type: docs
weight: 74
url: /ja/cpp/create-dynamic-rolling-chart/
---

## **可能な使用シナリオ**
動的ローリングチャートとは、データポイントが常にシフトして更新されるグラフィカルな表現を指します。このタイプのチャートは継続的に自動更新され、新しいデータポイントが追加されると古いデータポイントは破棄されます。

動的ローリングチャートは、リアルタイムやストリーミングデータのトレンドやパターンを可視化するために一般的に使用されます。株式市場の分析、気象モニタリング、またはライブパフォーマンスの追跡など、時間的な側面や時間の経過に伴う変化が重要なシナリオで特に有用です。

これらのチャートは通常、アニメーションや自動スクロールのメカニズムを使用して、常に最新の情報が表示されるようにしています。ローリングウィンドウの長さは、過去の1時間、1日、または1週間など、特定の時間期間を表示するようにカスタマイズできます。

要約すると、動的なローリングチャートは、古いデータを破棄しながら最新のデータポイントを表示する連続的に更新されるグラフ表現であり、ユーザーがリアルタイムのトレンドやパターンを観察することができます。

## **Aspose Cellsを使用して動的なローリングチャートを作成する**
次の段落では、Aspose.Cellsを使用して動的なローリングチャートを作成する方法を示します。例のコードと、このコードで作成されたExcelファイルも表示します。

## **サンプルコード**
次のサンプルコードは[DynamicRollingChart.xlsx]を生成します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Your local test path
    U16String LocalPath = u"";

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A1").PutValue(u"Month");
    sheet.GetCells().Get(u"A2").PutValue(1);
    sheet.GetCells().Get(u"A3").PutValue(2);
    sheet.GetCells().Get(u"A4").PutValue(3);
    sheet.GetCells().Get(u"A5").PutValue(4);
    sheet.GetCells().Get(u"A6").PutValue(5);
    sheet.GetCells().Get(u"A7").PutValue(6);
    sheet.GetCells().Get(u"A8").PutValue(7);

    sheet.GetCells().Get(u"B1").PutValue(u"Sales");
    sheet.GetCells().Get(u"B2").PutValue(50);
    sheet.GetCells().Get(u"B3").PutValue(45);
    sheet.GetCells().Get(u"B4").PutValue(55);
    sheet.GetCells().Get(u"B5").PutValue(60);
    sheet.GetCells().Get(u"B6").PutValue(55);
    sheet.GetCells().Get(u"B7").PutValue(65);
    sheet.GetCells().Get(u"B8").PutValue(70);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 10, 3, 25, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtLabels");

    // Save the workbook as an Excel file.
    workbook.Save(LocalPath + u"DynamicRollingChart.xlsx");

    std::cout << "Dynamic rolling chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **メモ**
生成されたファイルでは、列Aと列Bにデータを追加できます。これに対し、チャートは最新の5つのデータセットを動的にカウントします。これは、例のコードの「OFFSET」式を使用して行います。

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

数式の中の数値「-5」を「-10」に変更してみると、動的チャートは最新の10つのデータセットをカウントします。これでAspose.Cellsを使用して動的なローリングチャートを作成しました。
