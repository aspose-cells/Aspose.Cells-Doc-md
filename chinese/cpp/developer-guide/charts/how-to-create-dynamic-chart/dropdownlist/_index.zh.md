---
title: 如何用C++创建带有下拉列表的动态图表
linktitle: 创建带有下拉列表的动态图表
description: 学习如何使用Aspose.Cells for C++创建一个根据下拉列表选择更新的动态图表。我们的逐步指南将演示如何将下拉列表集成到你的图表中，实现灵活的数据可视化。
keywords: Aspose.Cells for C++，动态图表，下拉列表，数据可视化，集成，灵活的可视化。
type: docs
weight: 76
url: /zh/cpp/create-dynamic-chart-with-dropdownlist/
---

## **可能的使用场景**
在Excel中，具有下拉列表的动态图表是一种强大的工具，可以根据所选数据动态更新创建交互式图表。这个功能在需要分析多个数据集或比较不同情况的情况下特别有用。

具有下拉列表的动态图表的一个常见应用是在财务分析中。例如，公司可能对不同年份或部门的多个财务数据集。通过使用下拉列表，用户可以选择他们想要分析的特定数据集，图表会自动更新以显示相应的信息。这有助于轻松比较和识别趋势或模式。

另一个应用是在销售和营销中。公司可能有不同产品或地区的销售数据。使用具有下拉列表的动态图表，用户可以从下拉列表中选择特定产品或区域，图表会动态更新以显示所选选项的销售业绩。这有助于识别高效领域或产品，并做出数据驱动的决策。

总之，Excel中具有下拉列表的动态图表提供了一种灵活而互动的方式来可视化和分析数据。这在需要比较多个数据集或探索不同情况的情况下非常有价值，使其成为财务分析、销售和营销以及许多其他应用的多功能工具。

## **使用Aspose Cells创建带有下拉列表的动态图表**
在接下来的段落中，我们将向您展示如何使用Aspose.Cells创建带有下拉列表的动态图表。我们会展示示例的代码，以及使用该代码创建的Excel文件。

## **示例代码**
以下示例代码将生成[具有下拉列表的动态图表文件](DynamicChartWithDropdownlist.xlsx)。

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

## **备注**
在生成的文件中，图表会根据所选月份动态计算数据。这是通过示例代码中的“OFFSET”公式完成的：

```cpp
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

您可以尝试更改单元格“Sheet1!$ A $ 10”中的下拉列表值，您将看到图表的动态变化。现在，我们已成功使用Aspose.Cells创建了具有下拉列表的动态图表。
