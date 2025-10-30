---
title: C++を使った位置、サイズ、デザイナーグラフの操作
linktitle: 位置、サイズ、およびデザインチャートを操作
description: Microsoft Excelでレイアウトと可視化のために、Aspose.Cells for C++を使用して位置、サイズ、デザイナーチャートを効果的に操作する方法について学びます。ガイドでは、これらのプロパティを調整する方法を示します。
keywords: Aspose.Cells for C++、位置、サイズ、デザイナーチャート、Microsoft Excel、レイアウト、可視化。
type: docs
weight: 45
url: /ja/cpp/manipulate-position-size-and-designer-chart/
---

## **チャートの位置とサイズ**
時々、新しいまたは既存のチャートの位置やサイズをワークシート内で変更したい場合があります。Aspose.Cellsはこれを実現するために [Chart.GetChartObject()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getchartobject/) プロパティを提供します。サブプロパティを使って、チャートのサイズを新しい **高さ** と **幅** で変更したり、新しい **X** と **Y** 座標で位置を再設定したりできます。

### **チャートの位置とサイズの制御**
チャートの位置（X、Y座標）またはサイズ（高さ、幅）を変更するには、これらのプロパティを使用します。

1. [Chart.GetX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getx/)
1. [Chart.GetY()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gety/)
1. [Chart.GetHeight()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getheight/)
1. [Chart.GetWidth()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getwidth/)

上記のAPIの使用方法を説明する以下の例は、最初のワークシートにチャートが含まれる既存のワークブックを読み込みます。そして、Aspose.Cellsを使用して、チャートのサイズを変更し、再配置します。

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
    U16String inputFilePath = srcDir + u"chart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"chart.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(1);

    // Load the chart from the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Resize the chart
    chart.GetChartObject().SetWidth(400);
    chart.GetChartObject().SetHeight(300);

    // Reposition the chart
    chart.GetChartObject().SetX(250);
    chart.GetChartObject().SetY(150);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Chart resized and repositioned successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **デザイナーチャートの操作**
デザイナーテンプレートファイルでチャートを操作したり変更する必要がある場合があります。Aspose.Cellsはデザイナーチャートのコンテンツと要素を完全にサポートしています。データ、チャートのコンテンツ、背景画像、およびフォーマットは正確に保持されます。

### **テンプレートファイル内のデザイナーチャートを操作する**
テンプレートファイル内のデザイナーチャートを操作するには、チャート関連のAPIを使用してください。たとえば、Worksheet.Chartsプロパティを使用して、テンプレートファイル内の既存のチャートコレクションを取得できます。

#### **チャートの作成**
次の例は、ピラミッドチャートの作成方法を示しています。このチャートを後で操作します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    int chartIndex = worksheet.GetCharts().Add(ChartType::Pyramid, 5, 0, 15, 5);
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    chart.GetNSeries().Add(u"A1:B3", true);

    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **チャートの操作**
次の例は、既存のチャートの操作方法を示しています。この例では、上記で作成したチャートを変更します。生成された出力では、1つのデータポイントの日付ラベルが 'United Kingdom, 30K' に設定されていることに注意してください。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"piechart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Open the existing file
    Workbook workbook(inputFilePath);

    // Get the designer chart in the second sheet
    Worksheet sheet = workbook.GetWorksheets().Get(1);
    Chart chart = sheet.GetCharts().Get(0);

    // Get the data labels in the data series of the third data point
    DataLabels datalabels = chart.GetNSeries().Get(0).GetPoints().Get(2).GetDataLabels();

    // Change the text of the label
    datalabels.SetText(u"Unided Kingdom, 400K ");

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Data label text updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **デザイナーテンプレート内の折れ線グラフの操作**
この例では、折れ線グラフを操作します。既存のチャートにいくつかのデータシリーズを追加し、それらの線の色を変更します。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the designer chart in the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Add the third data series to it
    chart.GetNSeries().Add(U16String(u"{60, 80, 10}"), true);

    // Add another data series (fourth) to it
    chart.GetNSeries().Add(U16String(u"{0.3, 0.7, 1.2}"), true);

    // Plot the fourth data series on the second axis
    chart.GetNSeries().Get(3).SetPlotOnSecondAxis(true);

    // Change the Border color of the second data series
    chart.GetNSeries().Get(1).GetBorder().SetColor(Color::Green());

    // Change the Border color of the third data series
    chart.GetNSeries().Get(2).GetBorder().SetColor(Color::Red());

    // Make the second value axis visible
    chart.GetSecondValueAxis().SetIsVisible(true);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Chart modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
