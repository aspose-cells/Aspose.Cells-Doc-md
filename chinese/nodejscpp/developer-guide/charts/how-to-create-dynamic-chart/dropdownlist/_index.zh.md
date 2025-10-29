---
title: 如何使用Node.js通过C++创建带有下拉列表的动态图表
linktitle: 如何创建具有下拉列表的动态图表
description: 学习如何使用Aspose.Cells for Node.js via C++创建根据下拉列表选择更新的动态图表。我们的逐步指南将演示如何将下拉列表集成到您的图表中以实现灵活的数据可视化。
keywords: Aspose.Cells for Node.js via C++, 动态图表, 下拉列表, 数据可视化, 集成, 灵活的可视化。
type: docs
weight: 76
url: /zh/nodejs-cpp/create-dynamic-chart-with-dropdownlist/
---

## **可能的使用场景**
在Excel中，具有下拉列表的动态图表是一种强大的工具，可以根据所选数据动态更新创建交互式图表。这个功能在需要分析多个数据集或比较不同情况的情况下特别有用。

具有下拉列表的动态图表的一个常见应用是在财务分析中。例如，公司可能对不同年份或部门的多个财务数据集。通过使用下拉列表，用户可以选择他们想要分析的特定数据集，图表会自动更新以显示相应的信息。这有助于轻松比较和识别趋势或模式。

另一个应用是在销售和营销中。公司可能有不同产品或地区的销售数据。使用具有下拉列表的动态图表，用户可以从下拉列表中选择特定产品或区域，图表会动态更新以显示所选选项的销售业绩。这有助于识别高效领域或产品，并做出数据驱动的决策。

总之，Excel中具有下拉列表的动态图表提供了一种灵活而互动的方式来可视化和分析数据。这在需要比较多个数据集或探索不同情况的情况下非常有价值，使其成为财务分析、销售和营销以及许多其他应用的多功能工具。

## **使用Aspose Cells创建具有下拉列表的动态图表**
接下来的段落中，我们将向您展示如何使用Aspose.Cells for Node.js via C++创建带有下拉列表的动态图表。我们会提供示例代码，以及用此代码生成的Excel文件。

## **示例代码**
以下示例代码将生成[具有下拉列表的动态图表文件](DynamicChartWithDropdownlist.xlsx)。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const localPath = "";

// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);

// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A3").putValue("Tea");
sheet.getCells().get("A4").putValue("Coffee");
sheet.getCells().get("A5").putValue("Sugar");

// In this example, we will add 12 months of data
sheet.getCells().get("B2").putValue("Jan");
sheet.getCells().get("C2").putValue("Feb");
sheet.getCells().get("D2").putValue("Mar");
sheet.getCells().get("E2").putValue("Apr");
sheet.getCells().get("F2").putValue("May");
sheet.getCells().get("G2").putValue("Jun");
sheet.getCells().get("H2").putValue("Jul");
sheet.getCells().get("I2").putValue("Aug");
sheet.getCells().get("J2").putValue("Sep");
sheet.getCells().get("K2").putValue("Oct");
sheet.getCells().get("L2").putValue("Nov");
sheet.getCells().get("M2").putValue("Dec");
const allMonths = 12;
const iCount = 3;
for (let i = 0; i < iCount; i++) {
for (let j = 0; j < allMonths; j++) {
const _row = i + 2;
const _column = j + 1; 
sheet.getCells().get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
}
}

// This is the Dropdownlist for Dynamic Data
const ca = AsposeCells.CellArea.createCellArea(9, 0, 9, 0);
const _index = sheet.getValidations().add(ca);
const _va = sheet.getValidations().get(_index);
_va.setType(AsposeCells.ValidationType.List);
_va.setInCellDropDown(true);
_va.setFormula1("=$B$2:$M$2");
sheet.getCells().get("A9").putValue("Current Month");
sheet.getCells().get("A10").putValue("Jan");
const _style = sheet.getCells().get("A10").getStyle();
_style.getFont().setIsBold(true);
_style.setPattern(AsposeCells.BackgroundType.Solid);
_style.setForegroundColor(AsposeCells.Color.Yellow);
sheet.getCells().get("A10").setStyle(_style);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtMonthData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtXLabels");
sheets.getNames().get(index).setRefersTo("=Sheet1!$A$3:$A$5");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 8, 2, 20, 8);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("month", true);
chart.getNSeries().get(0).setName("=Sheet1!$A$10");
chart.getNSeries().get(0).setValues("Sheet1!ChtMonthData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtXLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicChartWithDropdownlist.xlsx"));
```

## **备注**
在生成的文件中，图表会根据所选月份动态计算数据。这是通过示例代码中的“OFFSET”公式完成的：

```
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

您可以尝试更改单元格“Sheet1!$ A $ 10”中的下拉列表值，您将看到图表的动态变化。现在，我们已成功使用Aspose.Cells创建了具有下拉列表的动态图表。
{{< app/cells/assistant language="nodejs-cpp" >}}
