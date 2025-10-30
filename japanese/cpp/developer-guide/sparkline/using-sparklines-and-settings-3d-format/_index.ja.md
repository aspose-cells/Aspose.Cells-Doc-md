---
title: C++を使ったスパークラインと3Dフォーマットの設定
linktitle: スパークラインと設定3Dフォーマットの使用
type: docs
weight: 40
url: /ja/cpp/using-sparklines-and-settings-3d-format/
description: Aspose.Cellsを使用してExcelファイル内のスパークラインの使い方や3Dフォーマットの適用方法を学びます。
---

## **スパークラインの使用**
Microsoft Excel 2010では、これまで以上に情報をさまざまな方法で分析できます。新しいデータ分析および可視化ツールを使用して重要なデータトレンドを追跡および強調することができます。スパークラインは、表内に配置してデータとグラフを同時に表示できるミニチャートです。スパークラインを適切に使用すると、データ分析が迅速かつ的確になります。また、情報のシンプルな表示を提供し、多くの複雑なチャートでワークシートが過度に混雑するのを避けることもできます。

Aspose.Cellsは、スプレッドシート内のスパークラインを操作するためのAPIを提供しています。
### **Microsoft Excelでのスパークライン**
Microsoft Excel 2010にスパークラインを挿入するには:

1. スパークラインが表示されるセルを選択します。視覚的にわかりやすくするため、データの横のセルを選択します。
1. リボンの**挿入**を選択し、**スパークライン**グループで**列**を選択します。
1. ワークシートに含まれるソースデータのセル範囲を選択または入力します。チャートが表示されます。

スパークラインは、例えばソフトボールリーグの勝敗記録などのトレンドを見るのに役立ちます。スパークラインは、リーグ内の各チームのシーズン全体を要約することさえできます。
### **Aspose.Cellsを使用したスパークライン**
開発者は、Aspose.CellsのAPIを使用してスパークラインを作成、削除、読み取りが可能です。スパークラインを管理するクラスは[Aspose.Cells.Charts](https://reference.aspose.com/cells/cpp/aspose.cells.charts/)名前空間に含まれているため、これらの機能を使う前にこの名前空間をインポートしてください。

指定されたデータ範囲にカスタムグラフィックスを追加することで、開発者は選択したセル領域に異なる種類の小さなチャートを追加する自由があります。

以下の例は、スパークライン機能を示しています。この例では次のことを示しています:

1. 簡単なテンプレートファイルを開きます。
1. ワークシートのスパークライン情報を読み取ります。
1.指定されたデータ範囲に新しいスパークラインをセル領域に追加します。
1. Excelファイルをディスクに保存します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    Workbook book(inputFilePath);
    Worksheet sheet = book.GetWorksheets().Get(0);

    SparklineGroupCollection sparklineGroups = sheet.GetSparklineGroups();
    for (int i = 0; i < sparklineGroups.GetCount(); ++i)
    {
        SparklineGroup g = sparklineGroups.Get(i);
        std::cout << "sparkline group: type:" << static_cast<int>(g.GetType()) << ", sparkline items count:" << g.GetSparklines().GetCount() << std::endl;
        for (int j = 0; j < g.GetSparklines().GetCount(); ++j)
        {
            Sparkline s = g.GetSparklines().Get(j);
            std::cout << "sparkline: row:" << s.GetRow() << ", col:" << s.GetColumn() << ", dataRange:" << s.GetDataRange().ToUtf8() << std::endl;
        }
    }

    CellArea ca;
    ca.StartColumn = 4;
    ca.EndColumn = 4;
    ca.StartRow = 1;
    ca.EndRow = 7;

    int idx = sheet.GetSparklineGroups().Add(SparklineType::Column, u"Sheet1!B2:D8", false, ca);
    SparklineGroup group = sheet.GetSparklineGroups().Get(idx);

    CellsColor clr = book.CreateCellsColor();
    clr.SetColor(Color::Orange());
    group.SetSeriesColor(clr);

    book.Save(outDir + u"Book1.out.xlsx");
    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **3Dフォーマットの設定**
シナリオに応じた結果を得るために、3Dチャートスタイルが必要な場合があります。Aspose.Cellsでは、Microsoft Excel 2007の3Dフォーマットを適用するための関連するAPIを提供しています。

Microsoft Excel 2007の3Dフォーマットを適用する方法を示す完全な例が以下に示されています。例のコードを実行すると、ワークシートに3D効果のある列グラフが追加されます。

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook book;

    // Add a Data Worksheet
    Worksheet dataSheet = book.GetWorksheets().Add(u"DataSheet");

    // Add Chart Worksheet
    Worksheet sheet = book.GetWorksheets().Add(u"MyChart");

    // Put some values into the cells in the data worksheet
    dataSheet.GetCells().Get(u"B1").PutValue(1);
    dataSheet.GetCells().Get(u"B2").PutValue(2);
    dataSheet.GetCells().Get(u"B3").PutValue(3);
    dataSheet.GetCells().Get(u"A1").PutValue(u"A");
    dataSheet.GetCells().Get(u"A2").PutValue(u"B");
    dataSheet.GetCells().Get(u"A3").PutValue(u"C");

    // Define the Chart Collection
    ChartCollection charts = sheet.GetCharts();

    // Add a Column chart to the Chart Worksheet
    int chartSheetIdx = charts.Add(ChartType::Column, 5, 0, 25, 15);

    // Get the newly added Chart
    Chart chart = book.GetWorksheets().Get(2).GetCharts().Get(0);

    // Set the background/foreground color for PlotArea/ChartArea
    chart.GetPlotArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetChartArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetChartArea().GetArea().SetForegroundColor(Color::White());

    // Hide the Legend
    chart.SetShowLegend(false);

    // Add Data Series for the Chart
    chart.GetNSeries().Add(u"DataSheet!B1:B3", true);

    // Specify the Category Data
    chart.GetNSeries().SetCategoryData(u"DataSheet!A1:A3");

    // Get the Data Series
    Series ser = chart.GetNSeries().Get(0);

    // Apply the 3-D formatting
    ShapePropertyCollection spPr = ser.GetShapeProperties();
    Format3D fmt3d = spPr.GetFormat3D();

    // Specify Bevel with its height/width
    Bevel bevel = fmt3d.GetTopBevel();
    bevel.SetType(BevelPresetType::Circle);
    bevel.SetHeight(2);
    bevel.SetWidth(5);

    // Specify Surface material type
    fmt3d.SetSurfaceMaterialType(PresetMaterialType::WarmMatte);

    // Specify surface lighting type
    fmt3d.SetSurfaceLightingType(LightRigType::ThreePoint);

    // Specify lighting angle
    fmt3d.SetLightingAngle(20);

    // Specify Series background/foreground and line color
    ser.GetArea().SetBackgroundColor(Color::Maroon());
    ser.GetArea().SetForegroundColor(Color::Maroon());
    ser.GetBorder().SetColor(Color::Maroon());

    // Save the Excel file
    book.Save(outDir + u"3d_format.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
