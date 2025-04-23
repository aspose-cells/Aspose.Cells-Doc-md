---
title: C++を使ったリーダーライン付きの円グラフ作成
linktitle: 円グラフ
description: Microsoft Excelでリーダーライン付きの円グラフをAspose.Cells for C++を使って作成する方法を学びます。ガイドでは、データポイントを凡例に結びつけ、チャート全体の明確さを向上させるリーダーラインの追加方法を示します。
keywords: Aspose.Cells for C++、円グラフ、リーダーライン、Microsoft Excel、データ可視化、チャートのカスタマイズ。
type: docs
weight: 45
url: /ja/cpp/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

この記事では、Aspose.Cells for C++ APIを使用してゼロからリーダーライン付きの円グラフを作成する方法について説明します。Excelでは、「リーダーラインを表示」オプションがデフォルトで設定されているため、Excelで円グラフを作成するとリーダーラインが表示されます。ただし、Aspose.Cells APIを使って同様のグラフを作成する場合は、明示的に [**Series.GetHasLeaderLines()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/gethasleaderlines/) プロパティを設定する必要があります。

{{% /alert %}}

Aspose.Cells for C++ APIを使用してリーダーライン付きの円グラフを作成する方法を示すために、最初に新しい [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) を作成し、シリーズデータソースとして機能するデータを入力します。データを配置したら、[**Chart**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/) の [**ChartType.Pie**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) 型のチャートをコレクションに追加し、そのさまざまな側面を設定して目的のチャートビューを得ます。

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

    // Create an instance of Workbook in XLSX format
    Workbook workbook(FileFormatType::Xlsx);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add two columns of data
    worksheet.GetCells().Get(u"A1").PutValue(u"Retail");
    worksheet.GetCells().Get(u"A2").PutValue(u"Services");
    worksheet.GetCells().Get(u"A3").PutValue(u"Info & Communication");
    worksheet.GetCells().Get(u"A4").PutValue(u"Transport Equip");
    worksheet.GetCells().Get(u"A5").PutValue(u"Construction");
    worksheet.GetCells().Get(u"A6").PutValue(u"Other Products");
    worksheet.GetCells().Get(u"A7").PutValue(u"Wholesale");
    worksheet.GetCells().Get(u"A8").PutValue(u"Land Transport");
    worksheet.GetCells().Get(u"A9").PutValue(u"Air Transport");
    worksheet.GetCells().Get(u"A10").PutValue(u"Electric Appliances");
    worksheet.GetCells().Get(u"A11").PutValue(u"Securities");
    worksheet.GetCells().Get(u"A12").PutValue(u"Textiles & Apparel");
    worksheet.GetCells().Get(u"A13").PutValue(u"Machinery");
    worksheet.GetCells().Get(u"A14").PutValue(u"Metal Products");
    worksheet.GetCells().Get(u"A15").PutValue(u"Cash");
    worksheet.GetCells().Get(u"A16").PutValue(u"Banks");

    worksheet.GetCells().Get(u"B1").PutValue(10.4);
    worksheet.GetCells().Get(u"B2").PutValue(5.2);
    worksheet.GetCells().Get(u"B3").PutValue(6.4);
    worksheet.GetCells().Get(u"B4").PutValue(10.4);
    worksheet.GetCells().Get(u"B5").PutValue(7.9);
    worksheet.GetCells().Get(u"B6").PutValue(4.1);
    worksheet.GetCells().Get(u"B7").PutValue(3.5);
    worksheet.GetCells().Get(u"B8").PutValue(5.7);
    worksheet.GetCells().Get(u"B9").PutValue(3);
    worksheet.GetCells().Get(u"B10").PutValue(14.7);
    worksheet.GetCells().Get(u"B11").PutValue(3.6);
    worksheet.GetCells().Get(u"B12").PutValue(2.8);
    worksheet.GetCells().Get(u"B13").PutValue(7.8);
    worksheet.GetCells().Get(u"B14").PutValue(2.4);
    worksheet.GetCells().Get(u"B15").PutValue(1.8);
    worksheet.GetCells().Get(u"B16").PutValue(10.1);

    // Create a pie chart and add it to the collection of charts
    int id = worksheet.GetCharts().Add(ChartType::Pie, 3, 3, 23, 13);

    // Access newly created Chart instance
    Chart chart = worksheet.GetCharts().Get(id);

    // Set series data range
    chart.GetNSeries().Add(u"B1:B16", true);

    // Set category data range
    chart.GetNSeries().SetCategoryData(u"A1:A16");

    // Turn off legend
    chart.SetShowLegend(false);

    // Access data labels
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();

    // Turn on category names
    dataLabels.SetShowCategoryName(true);

    // Turn on percentage format
    dataLabels.SetShowPercentage(true);

    // Set position
    dataLabels.SetPosition(LabelPositionType::OutsideEnd);

    // Set separator
    dataLabels.SetSeparatorType(DataLabelsSeparatorType::Comma);

    // Save the workbook
    workbook.Save(outDir + u"PieChart_out.xlsx");

    std::cout << "Pie chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

これまでに円グラフを作成し、異なる側面を設定しました。これからは、チャートのリーダーラインをオンにします。リーダーラインを表示するには、データラベルを少し移動する必要があります。

次のコードは、リーダーラインをオンにし、チャートを更新し、それからデータラベルの位置を計算して適切に移動します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook in XLSX format
    Workbook workbook(FileFormatType::Xlsx);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add two columns of data
    worksheet.GetCells().Get(u"A1").PutValue(u"Retail");
    worksheet.GetCells().Get(u"A2").PutValue(u"Services");
    worksheet.GetCells().Get(u"A3").PutValue(u"Info & Communication");
    worksheet.GetCells().Get(u"A4").PutValue(u"Transport Equip");
    worksheet.GetCells().Get(u"A5").PutValue(u"Construction");
    worksheet.GetCells().Get(u"A6").PutValue(u"Other Products");
    worksheet.GetCells().Get(u"A7").PutValue(u"Wholesale");
    worksheet.GetCells().Get(u"A8").PutValue(u"Land Transport");
    worksheet.GetCells().Get(u"A9").PutValue(u"Air Transport");
    worksheet.GetCells().Get(u"A10").PutValue(u"Electric Appliances");
    worksheet.GetCells().Get(u"A11").PutValue(u"Securities");
    worksheet.GetCells().Get(u"A12").PutValue(u"Textiles & Apparel");
    worksheet.GetCells().Get(u"A13").PutValue(u"Machinery");
    worksheet.GetCells().Get(u"A14").PutValue(u"Metal Products");
    worksheet.GetCells().Get(u"A15").PutValue(u"Cash");
    worksheet.GetCells().Get(u"A16").PutValue(u"Banks");

    worksheet.GetCells().Get(u"B1").PutValue(10.4);
    worksheet.GetCells().Get(u"B2").PutValue(5.2);
    worksheet.GetCells().Get(u"B3").PutValue(6.4);
    worksheet.GetCells().Get(u"B4").PutValue(10.4);
    worksheet.GetCells().Get(u"B5").PutValue(7.9);
    worksheet.GetCells().Get(u"B6").PutValue(4.1);
    worksheet.GetCells().Get(u"B7").PutValue(3.5);
    worksheet.GetCells().Get(u"B8").PutValue(5.7);
    worksheet.GetCells().Get(u"B9").PutValue(3);
    worksheet.GetCells().Get(u"B10").PutValue(14.7);
    worksheet.GetCells().Get(u"B11").PutValue(3.6);
    worksheet.GetCells().Get(u"B12").PutValue(2.8);
    worksheet.GetCells().Get(u"B13").PutValue(7.8);
    worksheet.GetCells().Get(u"B14").PutValue(2.4);
    worksheet.GetCells().Get(u"B15").PutValue(1.8);
    worksheet.GetCells().Get(u"B16").PutValue(10.1);

    // Create a pie chart and add it to the collection of charts
    int id = worksheet.GetCharts().Add(ChartType::Pie, 3, 3, 23, 13);

    // Access newly created Chart instance
    Chart chart = worksheet.GetCharts().Get(id);

    // Set series data range
    chart.GetNSeries().Add(u"B1:B16", true);

    // Set category data range
    chart.GetNSeries().SetCategoryData(u"A1:A16");

    // Turn off legend
    chart.SetShowLegend(false);

    // Access data labels
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();

    // Turn on category names
    dataLabels.SetShowCategoryName(true);

    // Turn on percentage format
    dataLabels.SetShowPercentage(true);

    // Set position
    dataLabels.SetPosition(LabelPositionType::OutsideEnd);

    // Set separator
    dataLabels.SetSeparatorType(DataLabelsSeparatorType::Comma);

    // Turn on leader lines
    chart.GetNSeries().Get(0).SetHasLeaderLines(true);

    // Calculate chart
    chart.Calculate();

    // You need to move DataLabels a little leftward or rightward depending on their position to show leader lines
    int DELTA = 100;
    for (int i = 0; i < chart.GetNSeries().Get(0).GetPoints().GetCount(); i++)
    {
        int X = chart.GetNSeries().Get(0).GetPoints().Get(i).GetDataLabels().GetX();
        // If it is greater than 2000, then move the X position a little right otherwise move the X position a little left
        if (X > 2000)
            chart.GetNSeries().Get(0).GetPoints().Get(i).GetDataLabels().SetX(X + DELTA);
        else
            chart.GetNSeries().Get(0).GetPoints().Get(i).GetDataLabels().SetX(X - DELTA);
    }

    // Save the workbook
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
}
```

最後に、次のコードでチャートを画像形式で保存し、ワークブックをXLSX形式で保存します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook in XLSX format
    Workbook workbook(FileFormatType::Xlsx);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add two columns of data
    worksheet.GetCells().Get(u"A1").PutValue(u"Retail");
    worksheet.GetCells().Get(u"A2").PutValue(u"Services");
    worksheet.GetCells().Get(u"A3").PutValue(u"Info & Communication");
    worksheet.GetCells().Get(u"A4").PutValue(u"Transport Equip");
    worksheet.GetCells().Get(u"A5").PutValue(u"Construction");
    worksheet.GetCells().Get(u"A6").PutValue(u"Other Products");
    worksheet.GetCells().Get(u"A7").PutValue(u"Wholesale");
    worksheet.GetCells().Get(u"A8").PutValue(u"Land Transport");
    worksheet.GetCells().Get(u"A9").PutValue(u"Air Transport");
    worksheet.GetCells().Get(u"A10").PutValue(u"Electric Appliances");
    worksheet.GetCells().Get(u"A11").PutValue(u"Securities");
    worksheet.GetCells().Get(u"A12").PutValue(u"Textiles & Apparel");
    worksheet.GetCells().Get(u"A13").PutValue(u"Machinery");
    worksheet.GetCells().Get(u"A14").PutValue(u"Metal Products");
    worksheet.GetCells().Get(u"A15").PutValue(u"Cash");
    worksheet.GetCells().Get(u"A16").PutValue(u"Banks");

    worksheet.GetCells().Get(u"B1").PutValue(10.4);
    worksheet.GetCells().Get(u"B2").PutValue(5.2);
    worksheet.GetCells().Get(u"B3").PutValue(6.4);
    worksheet.GetCells().Get(u"B4").PutValue(10.4);
    worksheet.GetCells().Get(u"B5").PutValue(7.9);
    worksheet.GetCells().Get(u"B6").PutValue(4.1);
    worksheet.GetCells().Get(u"B7").PutValue(3.5);
    worksheet.GetCells().Get(u"B8").PutValue(5.7);
    worksheet.GetCells().Get(u"B9").PutValue(3);
    worksheet.GetCells().Get(u"B10").PutValue(14.7);
    worksheet.GetCells().Get(u"B11").PutValue(3.6);
    worksheet.GetCells().Get(u"B12").PutValue(2.8);
    worksheet.GetCells().Get(u"B13").PutValue(7.8);
    worksheet.GetCells().Get(u"B14").PutValue(2.4);
    worksheet.GetCells().Get(u"B15").PutValue(1.8);
    worksheet.GetCells().Get(u"B16").PutValue(10.1);

    // Create a pie chart and add it to the collection of charts
    int id = worksheet.GetCharts().Add(ChartType::Pie, 3, 3, 23, 13);

    // Access newly created Chart instance
    Chart chart = worksheet.GetCharts().Get(id);

    // Set series data range
    chart.GetNSeries().Add(u"B1:B16", true);

    // Set category data range
    chart.GetNSeries().SetCategoryData(u"A1:A16");

    // Turn off legend
    chart.SetShowLegend(false);

    // Access data labels
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();

    // Turn on category names
    dataLabels.SetShowCategoryName(true);

    // Turn on percentage format
    dataLabels.SetShowPercentage(true);

    // Set position
    dataLabels.SetPosition(LabelPositionType::OutsideEnd);

    // Set separator
    dataLabels.SetSeparatorType(DataLabelsSeparatorType::Comma);

    // In order to save the chart image, create an instance of ImageOrPrintOptions
    ImageOrPrintOptions anOption;

    // Set image format
    anOption.SetImageType(ImageType::Png);

    // Set resolution
    anOption.SetHorizontalResolution(200);
    anOption.SetVerticalResolution(200);

    // Render chart to image
    chart.ToImage(u"output_out.png", anOption);

    // Save the workbook to see chart inside the Excel
    workbook.Save(u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

|**作成された円グラフ**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **高度なトピック**
- [円グラフでのカスタムスライスまたはセクターの色](/cells/ja/cpp/custom-slice-or-sector-colors-in-pie-chart/)
- [パイオブパイチャートまたはバーオブパイチャートでデータポイントが第2パイまたは棒にあるかどうかを見つける](/cells/ja/cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## 関連記事

- [チャートの作成](/cells/ja/cpp/creating-charts/)
- [チャートのカスタマイズ](/cells/ja/cpp/customizing-charts/)
- [グラフのデータ整形](/cells/ja/cpp/data-formatting-in-charts/)
- [グラフの外観設定](/cells/ja/cpp/setting-chart-appearance/)
