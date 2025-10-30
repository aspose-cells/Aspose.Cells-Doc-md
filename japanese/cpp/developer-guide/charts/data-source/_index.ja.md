---
title: C++でのチャートのデータソース設定
linktitle: データソース
type: docs
weight: 10
url: /ja/cpp/data-formatting-in-charts/
description: Aspose.Cells for C++がサポートするさまざまなデータソースについて学びます。ガイドは、利用可能なデータソースの種類と、それらに接続してデータを取得し、ワークシートを埋める方法を案内します。
keywords: Aspose.Cells for C++、チャート作成、データフォーマット、ラベル、色、フォント、外観、使いやすさ。
---

これまでのトピックでは、データソースを設定する方法の多くの例を示してきました。このトピックでは、チャートに設定できるデータの種類について詳しく説明します。

## **チャートデータの設定**

Aspose.Cellsを使用してチャートを作成する際に扱うデータには、次の2種類があります：

- チャートデータ。
- カテゴリデータ。

### **チャートデータ**

チャートデータは、チャートを作成するためのデータソースとして使用するデータです。 [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)オブジェクトの[**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/add/)メソッドを呼び出すことで、セルの範囲（チャートデータを含む）を追加できます。

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Excel object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(300);
    worksheet.GetCells().Get(u"B1").PutValue(160);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Adding sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **カテゴリデータ**

カテゴリデータは、チャートデータのラベリングに使用され、[**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)の[**GetCategoryData()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/getcategorydata/)プロパティを使用して追加できます。以下に使用例を示します。上記のコードを実行すると、ワークシートに列グラフが追加されます。

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(10);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(200);
    worksheet.GetCells().Get(u"B1").PutValue(120);
    worksheet.GetCells().Get(u"B2").PutValue(320);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Add sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Set the data source for the category data of SeriesCollection
    chart.GetNSeries().SetCategoryData(u"C1:C4");

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## ** 高度なトピック**
- [行や範囲をコピーする際に、チャートのデータソースを宛先ワークシートに変更する](/cells/ja/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [動的なチャートを作成する](/cells/ja/cpp/create-dynamic-charts/)
- [Chart.SetChartDataRangeメソッドを使用した簡単なチャート設定方法](/cells/ja/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [チャートシリーズのX値とY値のタイプを検索する](/cells/ja/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
{{< app/cells/assistant language="cpp" >}}
