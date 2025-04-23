---
title: C++を使った動的スクロールチャートの作成方法
linktitle: 動的スクロールチャートの作成
description: Aspose.Cells for C++を使用して動的スクロールチャートを作成する方法を学びます。ステップバイステップのガイドで、滑らかなデータ遷移と自動スクロールによる連続表示を実現します。
keywords: Aspose.Cells for C++、動的スクロールチャート、データ遷移、滑らかなスクロール、連続表示、更新された視覚化。
type: docs
weight: 75
url: /ja/cpp/create-dynamic-scrolling-chart/
---

## **可能な使用シナリオ**
動的スクロールチャートは、時間の経過とともに変化するデータを表示するためのグラフ表現の一種です。リアルタイムのデータ表示を提供するよう設計されており、ユーザーが連続的な更新やトレンドを追跡できます。新しいデータが追加されると、チャートは自動的に更新され、最新の情報を表示します。

動的スクロールチャートは、ファイナンス、株式市場分析、気象追跡、ソーシャルメディア分析など、さまざまな産業で一般的に使用されます。リアルタイム情報に基づいた、データパターンの視覚化と分析をユーザーが行い、的確な意思決定を行うことができます。

これらのチャートは通常、インタラクティブであり、ユーザーがズームインまたはズームアウト、過去のデータをスクロール、時間間隔を調整することができます。通常、複数のデータシリーズをサポートし、異なるメトリクスおよび相関を包括的に表示します。

全体として、動的スクロールチャートは、時系列データのモニタリングと分析に貴重なツールであり、リアルタイムの意思決定を容易にし、データの可視化能力を向上させるものです。

## **Aspose Cellsを使った動的スクロールチャートの作成**
次の段落では、Aspose.Cellsを使った動的スクロールチャートの作成方法を示します。例のコードと、このコードで作成したExcelファイルを紹介します。

## **サンプルコード**
次のサンプルコードは[DynamicScrollingChart.xlsx]を生成します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String localPath(u"");

    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    sheet.GetCells().Get(u"A1").PutValue(u"Day");
    sheet.GetCells().Get(u"B1").PutValue(u"Sales");

    int allDays = 30;
    int showDays = 10;
    int currentDay = 1;

    Cells cells = sheet.GetCells();
    for (int i = 0; i < allDays; i++)
    {
        int row = i + 1;
        cells.Get(row, 0).PutValue(i + 1);
        cells.Get(row, 1).PutValue(50 * (i % 2) + 20 * (i % 3) + 10 * (i / 3));
    }

    sheet.GetCells().Get(u"G19").PutValue(u"Start Day");
    sheet.GetCells().Get(u"G20").PutValue(currentDay);
    sheet.GetCells().Get(u"H19").PutValue(u"Show Days");
    sheet.GetCells().Get(u"H20").PutValue(showDays);

    int index = sheets.GetNames().Add(u"Sheet1!ChtScrollData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    index = sheets.GetNames().Add(u"Sheet1!ChtScrollLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    ScrollBar bar = sheet.GetShapes().AddScrollBar(2, 0, 3, 0, 200, 30);
    bar.SetMin(0);
    bar.SetMax(allDays - showDays);
    bar.SetCurrentValue(currentDay);
    bar.SetLinkedCell(u"$G$20");

    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 2, 4, 15, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtScrollData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtScrollLabels");

    workbook.Save(localPath + u"DynamicScrollingChart.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **メモ**
生成されたファイルでは、スクロールバーを操作できます。このとき、チャートは最新の10つのデータセットを動的にカウントします。これは、例のコードの「OFFSET」式を使用して行います。

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

セル「Sheet1!$H$20」で数値「10」を「15」に変更してみると、動的チャートは最新の15つのデータセットをカウントします。これでAspose.Cellsを使用して動的スクロールチャートを作成しました。
