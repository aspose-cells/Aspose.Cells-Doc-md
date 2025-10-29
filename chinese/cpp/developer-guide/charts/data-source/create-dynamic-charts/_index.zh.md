---
title: 使用C++创建动态图表
linktitle: 创建动态图表
description: 学习如何在Aspose.Cells for C++中创建动态图表。我们的指南将演示如何根据需求动态更新图表数据、系列和格式，从而在工作表中直观展示不断变化的数据。
keywords: Aspose.Cells for C++，制图，动态图表，数据，系列，格式，工作表，更新。
type: docs
weight: 240
url: /zh/cpp/create-dynamic-charts/
---

{{% alert color="primary" %}}

动态（或交互式）图表在更改数据范围时具有更改的能力。换句话说，当数据源更改时，动态图表可以自动反映更改。为了触发数据源的更改，可以使用Excel表的筛选选项，或者使用控件如下拉列表或下拉菜单。

本文展示了使用上述两种方法利用Aspose.Cells for C++ API创建动态图表的示例。

{{% /alert %}}

## **使用Excel表**

{{% alert color="primary" %}}

Excel表格在Aspose.Cells的视角中被称为ListObjects，因此，我们将使用“ListObject”一词代替“表”以确保清晰。请详细阅读关于如何[创建ListObjects](/cells/zh/cpp/create-and-format-table/)以及利用Aspose.Cells for C++ API的方法。

{{% /alert %}}

ListObjects提供了内置的功能，可以在人为操作下对数据进行排序和筛选。这些排序和筛选选项通过自动添加到[**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/)标题行的下拉列表实现。由于这些功能（排序和筛选），[**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/)似乎是用作动态图表数据源的理想候选，因为当排序或筛选变化时，图表中的数据表现也会随之改变，以反映[**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/)的当前状态。

为了让演示更简便易懂，我们将从零开始创建[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)，并按照下面的步骤逐步进行。

1. 创建一个空的[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)。
1. 访问第 [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 中第 [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 的 [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)。
1. 向单元格插入一些数据。
1. 根据插入的数据创建 [**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/)。
1. 根据 [**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) 的数据范围创建 [**Chart**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/)。
1. 将结果保存在磁盘上。

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

    // Create an instance of Workbook
    Workbook book;

    // Access first worksheet from the collection
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Access cells collection of the first worksheet
    Cells cells = sheet.GetCells();

    // Insert data column wise
    cells.Get(u"A1").PutValue(u"Category");
    cells.Get(u"A2").PutValue(u"Fruit");
    cells.Get(u"A3").PutValue(u"Fruit");
    cells.Get(u"A4").PutValue(u"Fruit");
    cells.Get(u"A5").PutValue(u"Fruit");
    cells.Get(u"A6").PutValue(u"Vegetables");
    cells.Get(u"A7").PutValue(u"Vegetables");
    cells.Get(u"A8").PutValue(u"Vegetables");
    cells.Get(u"A9").PutValue(u"Vegetables");
    cells.Get(u"A10").PutValue(u"Beverages");
    cells.Get(u"A11").PutValue(u"Beverages");
    cells.Get(u"A12").PutValue(u"Beverages");

    cells.Get(u"B1").PutValue(u"Food");
    cells.Get(u"B2").PutValue(u"Apple");
    cells.Get(u"B3").PutValue(u"Banana");
    cells.Get(u"B4").PutValue(u"Apricot");
    cells.Get(u"B5").PutValue(u"Grapes");
    cells.Get(u"B6").PutValue(u"Carrot");
    cells.Get(u"B7").PutValue(u"Onion");
    cells.Get(u"B8").PutValue(u"Cabage");
    cells.Get(u"B9").PutValue(u"Potatoe");
    cells.Get(u"B10").PutValue(u"Coke");
    cells.Get(u"B11").PutValue(u"Coladas");
    cells.Get(u"B12").PutValue(u"Fizz");

    cells.Get(u"C1").PutValue(u"Cost");
    cells.Get(u"C2").PutValue(2.2);
    cells.Get(u"C3").PutValue(3.1);
    cells.Get(u"C4").PutValue(4.1);
    cells.Get(u"C5").PutValue(5.1);
    cells.Get(u"C6").PutValue(4.4);
    cells.Get(u"C7").PutValue(5.4);
    cells.Get(u"C8").PutValue(6.5);
    cells.Get(u"C9").PutValue(5.3);
    cells.Get(u"C10").PutValue(3.2);
    cells.Get(u"C11").PutValue(3.6);
    cells.Get(u"C12").PutValue(5.2);

    cells.Get(u"D1").PutValue(u"Profit");
    cells.Get(u"D2").PutValue(0.1);
    cells.Get(u"D3").PutValue(0.4);
    cells.Get(u"D4").PutValue(0.5);
    cells.Get(u"D5").PutValue(0.6);
    cells.Get(u"D6").PutValue(0.7);
    cells.Get(u"D7").PutValue(1.3);
    cells.Get(u"D8").PutValue(0.8);
    cells.Get(u"D9").PutValue(1.3);
    cells.Get(u"D10").PutValue(2.2);
    cells.Get(u"D11").PutValue(2.4);
    cells.Get(u"D12").PutValue(3.3);

    // Create ListObject, Get the List objects collection in the first worksheet
    ListObjectCollection listObjects = sheet.GetListObjects();

    // Add a List based on the data source range with headers on
    int32_t index = listObjects.Add(0, 0, 11, 3, true);

    sheet.AutoFitColumns();

    // Create chart based on ListObject
    index = sheet.GetCharts().Add(ChartType::Column, 21, 1, 35, 18);
    Chart chart = sheet.GetCharts().Get(index);
    chart.SetChartDataRange(u"A1:D12", true);
    chart.GetNSeries().SetCategoryData(u"A2:B12");

    // Save spreadsheet
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Spreadsheet created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **使用动态公式**

如果您不希望使用 [**ListObject**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) 作为动态图表的数据源，另一种选择是使用 Excel 函数（或公式）创建动态数据范围，并使用控件（如组合框）触发数据更改。在此场景中，我们将使用 VLOOKUP 函数根据组合框的选择提取相应的值。当选择更改时，VLOOKUP 函数将刷新单元格值。如果某个范围的单元格使用了 VLOOKUP 函数，则可以在用户交互时刷新整个范围，因此它可以作为动态图表的数据源。

为了使演示简单易懂，我们将从头开始创建工作簿，并按照下面的步骤一步步地前进。

1. 创建一个空的[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)。
1. 访问第 [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 中第 [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 的 [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)。
1. 通过创建命名范围在单元格中插入一些数据。这些数据将作为动态图表的系列。
1. 根据在上一步中创建的命名范围创建 [**ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/)。
1. 在作为VLOOKUP函数源的单元格中插入更多数据。
1. 插入VLOOKUP函数（带适当参数）以一系列单元格。该范围将作为动态图表的数据源。
1. 根据前一步创建的范围创建 [**Chart**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/)。
1. 将结果保存在磁盘上。

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

    // Create a workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a range in the second worksheet
    Range range = worksheet.GetCells().CreateRange(u"C21", u"C24");

    // Name the range
    range.SetName(u"MyRange");

    // Fill different cells with data in the range
    range.Get(0, 0).PutValue(u"North");
    range.Get(1, 0).PutValue(u"South");
    range.Get(2, 0).PutValue(u"East");
    range.Get(3, 0).PutValue(u"West");

    // Add a combo box to the worksheet
    ComboBox comboBox = worksheet.GetShapes().AddComboBox(15, 0, 2, 0, 17, 64);
    comboBox.SetInputRange(u"=MyRange");
    comboBox.SetLinkedCell(u"=B16");
    comboBox.SetSelectedIndex(0);

    // Get the cell and set its style
    Cell cell = worksheet.GetCells().Get(u"B16");
    Style style = cell.GetStyle();
    style.GetFont().SetColor(Color::White());
    cell.SetStyle(style);

    // Set formula for cell C16
    worksheet.GetCells().Get(u"C16").SetFormula(u"=INDEX(Sheet1!$C$21:$C$24,$B$16,1)");

    // Put some data for chart source
    // Data Headers
    worksheet.GetCells().Get(u"D15").PutValue(u"Jan");
    worksheet.GetCells().Get(u"D20").PutValue(u"Jan");

    worksheet.GetCells().Get(u"E15").PutValue(u"Feb");
    worksheet.GetCells().Get(u"E20").PutValue(u"Feb");

    worksheet.GetCells().Get(u"F15").PutValue(u"Mar");
    worksheet.GetCells().Get(u"F20").PutValue(u"Mar");

    worksheet.GetCells().Get(u"G15").PutValue(u"Apr");
    worksheet.GetCells().Get(u"G20").PutValue(u"Apr");

    worksheet.GetCells().Get(u"H15").PutValue(u"May");
    worksheet.GetCells().Get(u"H20").PutValue(u"May");

    worksheet.GetCells().Get(u"I15").PutValue(u"Jun");
    worksheet.GetCells().Get(u"I20").PutValue(u"Jun");

    // Data
    worksheet.GetCells().Get(u"D21").PutValue(304);
    worksheet.GetCells().Get(u"D22").PutValue(402);
    worksheet.GetCells().Get(u"D23").PutValue(321);
    worksheet.GetCells().Get(u"D24").PutValue(123);

    worksheet.GetCells().Get(u"E21").PutValue(300);
    worksheet.GetCells().Get(u"E22").PutValue(500);
    worksheet.GetCells().Get(u"E23").PutValue(219);
    worksheet.GetCells().Get(u"E24").PutValue(422);

    worksheet.GetCells().Get(u"F21").PutValue(222);
    worksheet.GetCells().Get(u"F22").PutValue(331);
    worksheet.GetCells().Get(u"F23").PutValue(112);
    worksheet.GetCells().Get(u"F24").PutValue(350);

    worksheet.GetCells().Get(u"G21").PutValue(100);
    worksheet.GetCells().Get(u"G22").PutValue(200);
    worksheet.GetCells().Get(u"G23").PutValue(300);
    worksheet.GetCells().Get(u"G24").PutValue(400);

    worksheet.GetCells().Get(u"H21").PutValue(200);
    worksheet.GetCells().Get(u"H22").PutValue(300);
    worksheet.GetCells().Get(u"H23").PutValue(400);
    worksheet.GetCells().Get(u"H24").PutValue(500);

    worksheet.GetCells().Get(u"I21").PutValue(400);
    worksheet.GetCells().Get(u"I22").PutValue(200);
    worksheet.GetCells().Get(u"I23").PutValue(200);
    worksheet.GetCells().Get(u"I24").PutValue(100);

    // Dynamically load data on selection of Dropdown value
    worksheet.GetCells().Get(u"D16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,2,FALSE),0)");
    worksheet.GetCells().Get(u"E16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,3,FALSE),0)");
    worksheet.GetCells().Get(u"F16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,4,FALSE),0)");
    worksheet.GetCells().Get(u"G16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,5,FALSE),0)");
    worksheet.GetCells().Get(u"H16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,6,FALSE),0)");
    worksheet.GetCells().Get(u"I16").SetFormula(u"=IFERROR(VLOOKUP($C$16,$C$21:$I$24,7,FALSE),0)");

    // Create Chart
    int index = worksheet.GetCharts().Add(ChartType::Column, 0, 3, 12, 9);
    Chart chart = worksheet.GetCharts().Get(index);
    chart.GetNSeries().Add(u"='Sheet1'!$D$16:$I$16", false);
    chart.GetNSeries().Get(0).SetName(u"=C16");
    chart.GetNSeries().SetCategoryData(u"=$D$15:$I$15");

    // Save result on disc
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
