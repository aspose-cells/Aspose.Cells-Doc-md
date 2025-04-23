---
title: C++でのグラフの外観設定
linktitle: チャートの形式
description: Aspose.Cells for C++でグラフの外観を設定する方法を学びます。レイアウト、色、フォント、エフェクトのカスタマイズ方法を紹介し、望ましいビジュアルスタイルを実現し、ワークシートを向上させます。
keywords: Aspose.Cells for C++、グラフ作成、グラフの外観、レイアウト、色、フォント、エフェクト、ワークシート
type: docs
weight: 20
url: /ja/cpp/setting-chart-appearance/
---

## **グラフの外観設定**
チャートの作成方法では、Aspose.Cellsが提供するチャートの種類やオブジェクトについて簡単に紹介し、それらの作成方法について説明しました。この記事では、プロパティを設定してチャートの外観をカスタマイズする方法について説明します。

- チャートエリアの設定。
- チャートラインの設定。
- テーマの適用。
- チャートと軸のタイトルの設定。
- グリッド線の操作。

### **チャートエリアの設定**
チャートには異なる種類のエリアがあり、Aspose.Cellsは各エリアの外観を変更する柔軟性を提供します。開発者は、前景色、背景色、塗りつぶし形式などの異なる書式設定をエリアに適用して、その外観を変更できます。

以下の例では、チャートの異なる種類のエリアに異なる書式設定を適用しました。

- プロットエリア
- チャートエリア
- SeriesCollectionエリア
- SeriesCollection内の単一のポイントのエリア

以下のコードスニペットは、チャートエリアを設定する方法を示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

### **チャートラインの設定**
開発者はまた、[SeriesCollection](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)の線やデータマーカーに様々なスタイルを適用できます。以下のコードスニペットは、Aspose.Cells APIを使用してグラフの線を設定する例です。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Applying a dotted line style on the lines of a SeriesCollection
    chart.GetNSeries().Get(0).GetBorder().SetStyle(LineType::Dot);

    // Applying a triangular marker style on the data markers of a SeriesCollection
    chart.GetNSeries().Get(0).GetMarker().SetMarkerStyle(ChartMarkerType::Triangle);

    // Setting the weight of all lines in a SeriesCollection to medium
    chart.GetNSeries().Get(1).GetBorder().SetWeight(WeightType::MediumLine);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Microsoft Excel 2007/2010のテーマをチャートに適用**
開発者はまた、Microsoft Excelのテーマやカラーを[SeriesCollection](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)や他のグラフオブジェクトに適用できます。以下の例で示します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Instantiate the workbook to open the file that contains a chart
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(1);

    // Get the first chart in the sheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Specify the FillFormat's type to Solid Fill of the first series
    chart.GetNSeries().Get(0).GetArea().GetFillFormat().SetFillType(FillType::Solid);

    // Get the CellsColor of SolidFill
    CellsColor cc = chart.GetNSeries().Get(0).GetArea().GetFillFormat().GetSolidFill().GetCellsColor();

    // Create a theme in Accent style
    cc.SetThemeColor(ThemeColor(ThemeColorType::Accent6, 0.6));

    // Apply the theme to the series
    chart.GetNSeries().Get(0).GetArea().GetFillFormat().GetSolidFill().SetCellsColor(cc);

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Chart theme applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **チャートや軸のタイトルの設定**
Microsoft Excelを使用して、WYSIWYG環境でチャートおよびその軸のタイトルを設定できます。Aspose.Cellsも、開発者が実行時にチャートとその軸のタイトルを設定できるようにします。すべてのチャートとそれらの軸には、[Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/) プロパティが含まれており、これを使用してタイトルを設定できます。例を以下に示します。

次のコードスニペットは、チャートや軸にタイトルを設定する方法を示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Setting the title of category axis of the chart
    chart.GetCategoryAxis().GetTitle().SetText(u"Category");

    // Setting the title of value axis of the chart
    chart.GetValueAxis().GetTitle().SetText(u"Value");

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **主な目盛りの操作**
主な目盛りの外観をカスタマイズできます。目盛りを非表示にしたり表示したり、その色やその他の設定を定義できます。以下では、目盛りを非表示にする方法と色を変更する方法を説明します。

#### **メジャーグリッドラインの非表示**
開発者は、[Line](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/line/) オブジェクトの [IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/line/isvisible/) プロパティを**true**または**false**に設定して、主要な格子線の表示/非表示を制御できます。

次のコードスニペットは、メジャーグリッド線を非表示にする方法を示しています。メジャーグリッド線を非表示にした後、ワークシートに列のチャートが追加され、グリッド線がありません。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Hiding the major gridlines of Category Axis
    chart.GetCategoryAxis().GetMajorGridLines().SetIsVisible(false);

    // Hiding the major gridlines of Value Axis
    chart.GetValueAxis().GetMajorGridLines().SetIsVisible(false);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **メジャーグリッドラインの設定変更**
開発者は、メジャーグリッド線の可視性だけでなく、色などの他のプロパティも制御できます。

次のコードスニペットは、メジャーグリッド線の色を変更する方法を示しています。メジャーグリッド線の色を設定した後、ワークシートに変更されたグリッド線を持つ列チャートが追加されます。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Setting the color of Category Axis' major gridlines to silver
    chart.GetCategoryAxis().GetMajorGridLines().SetColor(Color::Silver());

    // Setting the color of Value Axis' major gridlines to red
    chart.GetValueAxis().GetMajorGridLines().SetColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created and formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**
- [チャートシリーズの値の形式コードを設定する](/cells/ja/cpp/set-the-values-format-code-of-chart-series/)
- [グラフの背景に画像を設定する](/cells/ja/cpp/set-picture-as-background-fill-in-the-chart/)
