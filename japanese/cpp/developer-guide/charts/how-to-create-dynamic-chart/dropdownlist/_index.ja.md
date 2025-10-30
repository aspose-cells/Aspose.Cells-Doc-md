---
title: C++でドロップダウンリストを使った動的チャート作成方法
linktitle: ドロップダウンリストを使った動的チャートの作成
description: Aspose.Cells for C++を使用して、ドロップダウンリスト選択に基づいて更新される動的チャートを作成する方法を学びます。ステップバイステップのガイドでは、柔軟なデータ可視化のためにチャートにドロップダウンリストを統合する方法を示します。
keywords: Aspose.Cells for C++、動的チャート、ドロップダウンリスト、データ可視化、統合、柔軟な可視化。
type: docs
weight: 76
url: /ja/cpp/create-dynamic-chart-with-dropdownlist/
---

## **可能な使用シナリオ**
Excelでのドロップダウンリストを使用した動的チャートは、選択したデータに基づいてダイナミックに更新されるインタラクティブなチャートをユーザーが作成できる強力なツールです。この機能は、複数のデータセットを分析したり、さまざまなシナリオを比較したりする必要がある状況で特に有用です。

ドロップダウンリストを使用した動的チャートの一般的な応用例は、財務分析です。たとえば、企業には異なる年や部門の複数の財務データがあるかもしれません。ドロップダウンリストを使用することで、ユーザーは分析したい特定のデータセットを選択し、チャートは自動的に対応する情報を表示します。これにより、簡単に比較し、トレンドやパターンを特定できます。

もう1つの応用例は、営業とマーケティングです。企業には異なる製品や地域の販売データがあるかもしれません。ドロップダウンリストを使用した動的チャートでは、ユーザーはドロップダウンリストから特定の製品や地域を選択し、チャートは選択したオプションの販売実績を動的に表示します。これにより、トップのパフォーマンスエリアや製品を特定し、データに基づいた意思決定が行えます。

要するに、Excelでのドロップダウンリストを使用した動的チャートは、データを柔軟にインタラクティブに可視化および分析する手段を提供します。複数のデータセットを比較したり、さまざまなシナリオを探ったりする必要がある状況で価値があり、財務分析、営業とマーケティングなど様々な応用に使える多目的なツールです。

## **Aspose Cellsを使ってドロップダウンリスト付きの動的チャートを作成**
次の段落では、Aspose.Cellsを使用してドロップダウンリスト付きの動的チャートを作成する方法を示します。例のコードと、このコードで作成したExcelファイルを紹介します。

## **サンプルコード**
次のサンプルコードでは、[ドロップダウンリストファイル](DynamicChartWithDropdownlist.xlsx)を生成します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A3").PutValue(u"Tea");
    sheet.GetCells().Get(u"A4").PutValue(u"Coffee");
    sheet.GetCells().Get(u"A5").PutValue(u"Sugar");

    // In this example, we will add 12 months of data
    sheet.GetCells().Get(u"B2").PutValue(u"Jan");
    sheet.GetCells().Get(u"C2").PutValue(u"Feb");
    sheet.GetCells().Get(u"D2").PutValue(u"Mar");
    sheet.GetCells().Get(u"E2").PutValue(u"Apr");
    sheet.GetCells().Get(u"F2").PutValue(u"May");
    sheet.GetCells().Get(u"G2").PutValue(u"Jun");
    sheet.GetCells().Get(u"H2").PutValue(u"Jul");
    sheet.GetCells().Get(u"I2").PutValue(u"Aug");
    sheet.GetCells().Get(u"J2").PutValue(u"Sep");
    sheet.GetCells().Get(u"K2").PutValue(u"Oct");
    sheet.GetCells().Get(u"L2").PutValue(u"Nov");
    sheet.GetCells().Get(u"M2").PutValue(u"Dec");

    int allMonths = 12;
    int iCount = 3;
    for (int i = 0; i < iCount; i++)
    {
        for (int j = 0; j < allMonths; j++)
        {
            int _row = i + 2;
            int _column = j + 1;
            sheet.GetCells().Get(_row, _column).PutValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
        }
    }

    // This is the Dropdownlist for Dynamic Data
    CellArea ca = CellArea::CreateCellArea(9, 0, 9, 0);
    int _index = sheet.GetValidations().Add(ca);
    Validation _va = sheet.GetValidations().Get(_index);
    _va.SetType(ValidationType::List);
    _va.SetInCellDropDown(true);
    _va.SetFormula1(u"=$B$2:$M$2");

    sheet.GetCells().Get(u"A9").PutValue(u"Current Month");
    sheet.GetCells().Get(u"A10").PutValue(u"Jan");

    Style _style = sheet.GetCells().Get(u"A10").GetStyle();
    _style.GetFont().SetIsBold(true);
    _style.SetPattern(BackgroundType::Solid);
    _style.SetForegroundColor(Color::Yellow());
    sheet.GetCells().Get(u"A10").SetStyle(_style);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtMonthData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtXLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=Sheet1!$A$3:$A$5");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 8, 2, 20, 8);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"month", true);
    chart.GetNSeries().Get(0).SetName(u"=Sheet1!$A$10");
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtMonthData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtXLabels");

    // Save the workbook as an Excel file.
    workbook.Save(u"DynamicChartWithDropdownlist.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **メモ**
生成されたファイルでは、チャートは選択した月のデータを動的にカウントします。これはサンプルコードでの「OFFSET」式の使用によって行われます。

```cpp
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

セル「Sheet1!$A$10」のドロップダウンリストの値を変更してみると、チャートが動的に変化することがわかります。これで、Aspose.Cellsを使用して動的なチャートをドロップダウンリストで作成しました。
{{< app/cells/assistant language="cpp" >}}
