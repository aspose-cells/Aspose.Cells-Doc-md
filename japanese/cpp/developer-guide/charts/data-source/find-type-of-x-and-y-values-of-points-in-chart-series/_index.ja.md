---
title: C++でチャートシリーズのX値とY値の種類を見つける方法
linktitle: チャートシリーズのポイントのXおよびY値のタイプを検索する
description: Aspose.Cells for C++を使用して、チャートシリーズポイントのX値とY値の種類を判定する方法を学びます。ガイドでは、さまざまなデータ値のタイプと、それらにアクセスし操作する方法を説明します。
keywords: Aspose.Cells for C++, チャート作成, X値, Y値, データタイプ, アクセス, 操作, チャート系列。
type: docs
weight: 150
url: /ja/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **可能な使用シナリオ**
時には、シリーズ内のチャートポイントのX値とY値のタイプを知りたい場合があります。Aspose.Cellsは `ChartPoint::get_XValueType` と `ChartPoint::get_YValueType` メソッドを提供しており、これらを利用できます。ただし、これらのプロパティを使用する前に `Chart::Calculate()` を呼び出す必要がある点に注意してください。

## **チャートシリーズのX値とY値のタイプを検索する**
次のサンプルコードは、[サンプルExcelファイル](64716905.xlsx)をロードし、最初のワークシートの最初のチャートにアクセスします。次に、`Chart::Calculate()` を呼び出し、最初のチャートポイントのX値とY値の種類を判定してコンソールに出力します。参考のため、以下の出力例を参照してください。

## **サンプルコード**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load sample Excel file containing chart
    Workbook wb(srcDir + u"sampleFindTypeOfXandYValuesOfPointsInChartSeries.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = ws.GetCharts().Get(0);

    // Calculate chart data
    ch.Calculate();

    // Access first chart point in the first series
    ChartPoint pnt = ch.GetNSeries().Get(0).GetPoints().Get(0);

    // Print the types of X and Y values of chart point
    std::cout << "X Value Type: " << static_cast<int>(pnt.GetXValueType()) << std::endl;
    std::cout << "Y Value Type: " << static_cast<int>(pnt.GetYValueType()) << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **コンソール出力**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
