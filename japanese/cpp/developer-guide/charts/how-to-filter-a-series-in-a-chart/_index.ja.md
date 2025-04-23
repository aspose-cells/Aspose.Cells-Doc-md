---
title: C++を使用したチャートデータのフィルタリングの3つの方法
linktitle: チャートデータのフィルタリングの3つの方法
description: Aspose.Cells for C++を使用してExcelでチャートにフィルターを適用する方法について学びましょう。包括的なガイドでは、チャートへのフィルター適用、チャート要素のカスタマイズ、データ分析ツールの活用について説明します。
keywords: Aspose.Cells for C++、Excelのチャートフィルター、データ分析、意思決定、ビジュアライゼーション。
type: docs
weight: 2210
url: /ja/cpp/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. チャートからシリーズをフィルタリングする**

### **Excelでチャートからシリーズをフィルタリングする手順**
Excelでは、特定の系列をフィルタリングして、その系列をチャートに表示しないようにすることができます。元のチャートは**図1**に示されています。ただし、**Testseries2**と**Testseries4**をフィルターアウトすると、チャートは**図2**のように表示されます。

Aspose.Cellsでも同様の操作が可能です。[サンプル](seriesFiltered.xlsx)ファイルのように、**Testseries2**と**Testseries4**を除外したい場合、次のコードを実行できます。さらに、2つのリストを管理します。1つはすべての選択された系列を格納する（[GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/)）、もう1つはフィルタリングされた系列を格納する（[GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/)）。

**注意**：コード中で、**chart->GetNSeries()->Get(0)->SetIsFiltered(true);**を設定すると、[GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/)の最初の系列が除外され、[GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/)の適切な位置に移動します。その後、前の**NSeries[1]**が新しい最初の項目になり、続く系列は1つずつ前にシフトします。これにより、**chart->GetNSeries()->Get(1)->SetIsFiltered(true);**を実行すると、元の3番目の系列が除外されます。この操作は混乱を招く場合があるため、コードの操作は後ろから前へとシリーズを削除する方法を推奨します。

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **サンプルコード**
次のサンプルコードは、[サンプルExcelファイル](seriesFiltered.xlsx)を読み込みます。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of existing Workbook
    Workbook workbook(u"seriesFiltered.xlsx");

    // Get filtered series list
    SeriesCollection nSeriesFiltered = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetFilteredNSeries();

    // Get selected series list
    SeriesCollection nSeries = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetNSeries();

    // Should be 0
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 6
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Process from the end to the beginning
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Save the workbook
    workbook.Save(u"seriesFiltered-out.xlsx");

    // Reload the workbook
    workbook = Workbook(u"seriesFiltered-out.xlsx");

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **2. データをフィルターし、グラフを変更します**

データをフィルタリングすると、多くのデータを扱うグラフのフィルター操作が便利になります。データをフィルターすると、グラフも変わります。ただし、フィルター後はグラフが画面から消えないようにする必要があります。フィルターを適用すると、隠された行ができ、その状態ではグラフも隠された行に配置されることがあります。

![todo:image_alt_text](Figure3.png)

### **Excelでチャートを変更するデータフィルターの使用手順**

1. データ範囲の内側をクリックします。
2. **データ** タブをクリックし、フィルターを選択してフィルターをオンにします。 ヘッダー行にはドロップダウン矢印が表示されます。
3. **挿入** タブに移動し、列のチャートを選択して、チャートを作成します。
4. 今、データをドロップダウン矢印を使用してフィルタリングします。 チャートフィルターは使用しないでください。

### **サンプルコード**
次のサンプルコードは、Aspose.Cellsを使用した同じ機能を示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the First sheet.
    Worksheet sheet = workbook.GetWorksheets().Get(u"Sheet1");

    // Add data into details cells.
    sheet.GetCells().Get(0, 0).PutValue(u"Fruits Name");
    sheet.GetCells().Get(0, 1).PutValue(u"Fruits Price");
    sheet.GetCells().Get(1, 0).PutValue(u"Apples");
    sheet.GetCells().Get(2, 0).PutValue(u"Bananas");
    sheet.GetCells().Get(3, 0).PutValue(u"Grapes");
    sheet.GetCells().Get(4, 0).PutValue(u"Oranges");
    sheet.GetCells().Get(1, 1).PutValue(5);
    sheet.GetCells().Get(2, 1).PutValue(2);
    sheet.GetCells().Get(3, 1).PutValue(1);
    sheet.GetCells().Get(4, 1).PutValue(4);

    // Add a chart to the worksheet
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);

    // Access the instance of the newly added chart
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B5", true);

    // Set AutoFilter range
    sheet.GetAutoFilter().SetRange(u"A1:B5");

    // Add filters for a filter column.
    sheet.GetAutoFilter().AddFilter(0, u"Bananas");
    sheet.GetAutoFilter().AddFilter(0, u"Oranges");

    // Apply the filters
    sheet.GetAutoFilter().Refresh();

    // Save the chart as an image
    chart.ToImage(u"Autofilter.png");

    // Save the workbook
    workbook.Save(u"Autofilter.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **3. テーブルを使用してデータをフィルターし、グラフを変更します**

テーブルを使用することは、範囲を使用する方法2と似ていますが、テーブルには範囲よりも優れた点があります。 テーブルに範囲を変更してデータを追加すると、チャートが自動的に更新されます。 範囲の場合、データソースを変更する必要があります。

### **Excelでテーブルとしてフォーマット**

データ内をクリックし、**CTRL + T** を使用するか、**ホーム** タブ、**テーブルの書式設定** を使用します。

![todo:image_alt_text](Figure4.png)

### **サンプルコード**
次のサンプルコードは、[サンプルExcelファイル](TableFilters.xlsx)を読み込み、Aspose.Cellsを使用した同じ機能を示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Tables;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook
    Workbook workbook(u"TableFilters.xlsx");

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the instance of the newly added chart
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B7", true);

    // Convert the chart to image
    chart.ToImage(u"TableFilters.before.png");

    // Add a new List Object to the worksheet
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(u"A1", u"B7", true));

    // Add default style to the table
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium10);

    // Show Total
    listObject.SetShowTotals(false);

    // Add filters for a filter column
    listObject.GetAutoFilter().AddFilter(0, u"James");

    // Apply the filters
    listObject.GetAutoFilter().Refresh();

    // After adding new value the chart will change
    listObject.PutCellValue(7, 0, Object(u"Me"));
    listObject.PutCellValue(7, 1, Object(1000));

    // Check the changed images
    chart.ToImage(u"TableFilters.after.png");

    // Saving the Excel file
    workbook.Save(u"TableFilter.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
