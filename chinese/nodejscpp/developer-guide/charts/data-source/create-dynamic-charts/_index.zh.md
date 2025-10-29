---  
title: 通过C++在Node.js中创建动态图表  
linktitle: 创建动态图表  
description: 学习如何在Aspose.Cells for Node.js via C++中创建动态图表。此指南将向您展示如何根据需求动态更新图表数据、系列和格式，从而在工作表中以视觉方式展示变化的数据。  
keywords: Aspose.Cells for Node.js、图表、动态图表、数据、系列、格式、工作表、更新。  
type: docs  
weight: 240  
url: /zh/nodejs-cpp/create-dynamic-charts/  
---  

{{% alert color="primary" %}}  
动态（或交互式）图表在更改数据范围时具有更改的能力。换句话说，当数据源更改时，动态图表可以自动反映更改。为了触发数据源的更改，可以使用Excel表的筛选选项，或者使用控件如下拉列表或下拉菜单。

本文演示了如何使用Aspose.Cells for Node.js via C++ API结合上述两种方法创建动态图表。  
{{% /alert %}}  

## **使用Excel表**  

{{% alert color="primary" %}}  
在Aspose.Cells的角度，Excel表格被称为ListObjects，因此，为了清晰起见，我们将使用“ListObject”一词代替“表” 。请详细阅读关于如何[创建ListObjects](/cells/zh/nodejs-cpp/create-and-format-table/)的内容，编号为Aspose.Cells for Node.js via C++。  
{{% /alert %}}  

ListObjects提供了内置的功能，可以在人为操作下对数据进行排序和筛选。这些排序和筛选选项通过自动添加到[**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject)标题行的下拉列表实现。由于这些功能（排序和筛选），[**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject)似乎是用作动态图表数据源的理想候选，因为当排序或筛选变化时，图表中的数据表现也会随之改变，以反映[**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject)的当前状态。

为了让演示更简便易懂，我们将从零开始创建[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，并按照下面的步骤逐步进行。

1. 创建一个空的[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)。
1. 访问第 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 中第 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 的 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)。
1. 向单元格插入一些数据。
1. 根据插入的数据创建 [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject)。
1. 根据 [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) 的数据范围创建 [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart)。
1. 将结果保存到磁盘。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook
const book = new AsposeCells.Workbook();
// Access first worksheet from the collection
const sheet = book.getWorksheets().get(0);
// Access cells collection of the first worksheet
const cells = sheet.getCells();

// Insert data column-wise
cells.get("A1").putValue("Category");
cells.get("A2").putValue("Fruit");
cells.get("A3").putValue("Fruit");
cells.get("A4").putValue("Fruit");
cells.get("A5").putValue("Fruit");
cells.get("A6").putValue("Vegetables");
cells.get("A7").putValue("Vegetables");
cells.get("A8").putValue("Vegetables");
cells.get("A9").putValue("Vegetables");
cells.get("A10").putValue("Beverages");
cells.get("A11").putValue("Beverages");
cells.get("A12").putValue("Beverages");

cells.get("B1").putValue("Food");
cells.get("B2").putValue("Apple");
cells.get("B3").putValue("Banana");
cells.get("B4").putValue("Apricot");
cells.get("B5").putValue("Grapes");
cells.get("B6").putValue("Carrot");
cells.get("B7").putValue("Onion");
cells.get("B8").putValue("Cabbage");
cells.get("B9").putValue("Potato");
cells.get("B10").putValue("Coke");
cells.get("B11").putValue("Coladas");
cells.get("B12").putValue("Fizz");

cells.get("C1").putValue("Cost");
cells.get("C2").putValue(2.2);
cells.get("C3").putValue(3.1);
cells.get("C4").putValue(4.1);
cells.get("C5").putValue(5.1);
cells.get("C6").putValue(4.4);
cells.get("C7").putValue(5.4);
cells.get("C8").putValue(6.5);
cells.get("C9").putValue(5.3);
cells.get("C10").putValue(3.2);
cells.get("C11").putValue(3.6);
cells.get("C12").putValue(5.2);

cells.get("D1").putValue("Profit");
cells.get("D2").putValue(0.1);
cells.get("D3").putValue(0.4);
cells.get("D4").putValue(0.5);
cells.get("D5").putValue(0.6);
cells.get("D6").putValue(0.7);
cells.get("D7").putValue(1.3);
cells.get("D8").putValue(0.8);
cells.get("D9").putValue(1.3);
cells.get("D10").putValue(2.2);
cells.get("D11").putValue(2.4);
cells.get("D12").putValue(3.3);

// Create ListObject, Get the List objects collection in the first worksheet
const listObjects = sheet.getListObjects();

// Add a List based on the data source range with headers on
let index = listObjects.add(0, 0, 11, 3, true);

sheet.autoFitColumns();

// Create chart based on ListObject
index = sheet.getCharts().add(AsposeCells.ChartType.Column, 21, 1, 35, 18);
const chart = sheet.getCharts().get(index);
chart.setChartDataRange("A1:D12", true);
chart.getNSeries().setCategoryData("A2:B12");

// Save spreadsheet
book.save(path.join(dataDir, "output_out.xlsx"));
```  

## **使用动态公式**  

如果您不希望使用 [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) 作为动态图表的数据源，另一种选择是使用 Excel 函数（或公式）创建动态数据范围，并使用控件（如组合框）触发数据更改。在此场景中，我们将使用 VLOOKUP 函数根据组合框的选择提取相应的值。当选择更改时，VLOOKUP 函数将刷新单元格值。如果某个范围的单元格使用了 VLOOKUP 函数，则可以在用户交互时刷新整个范围，因此它可以作为动态图表的数据源。

为了使演示简单易懂，我们将从头开始创建工作簿，并按照下面的步骤一步步地前进。

1. 创建一个空的[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)。
1. 访问第 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 中第 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 的 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)。
1. 通过创建命名范围在单元格中插入一些数据。这些数据将作为动态图表的系列。
1. 根据在上一步中创建的命名范围创建 [**ComboBox**](https://reference.aspose.com/cells/nodejs-cpp/combobox)。
1. 在作为VLOOKUP函数源的单元格中插入更多数据。
1. 在一组单元格中插入VLOOKUP函数（带有适当参数）。此范围将作为动态图表的数据源。
1. 根据前一步创建的范围创建 [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart)。
1. 将结果保存到磁盘。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range in the second worksheet
const range = worksheet.getCells().createRange("C21", "C24");

// Name the range
range.setName("MyRange");

// Fill different cells with data in the range
range.get(0, 0).putValue("North");
range.get(1, 0).putValue("South");
range.get(2, 0).putValue("East");
range.get(3, 0).putValue("West");

const comboBox = worksheet.getShapes().addComboBox(15, 0, 2, 0, 17, 64);
comboBox.setInputRange("=MyRange");
comboBox.setLinkedCell("=B16");
comboBox.setSelectedIndex(0);
const cell = worksheet.getCells().get("B16");
const style = cell.getStyle();
style.getFont().setColor(AsposeCells.Color.White);
cell.setStyle(style);

worksheet.getCells().get("C16").setFormula("=INDEX(Sheet1!$C$21:$C$24,$B$16,1)");

// Put some data for chart source
// Data Headers
worksheet.getCells().get("D15").putValue("Jan");
worksheet.getCells().get("D20").putValue("Jan");

worksheet.getCells().get("E15").putValue("Feb");
worksheet.getCells().get("E20").putValue("Feb");

worksheet.getCells().get("F15").putValue("Mar");
worksheet.getCells().get("F20").putValue("Mar");

worksheet.getCells().get("G15").putValue("Apr");
worksheet.getCells().get("G20").putValue("Apr");

worksheet.getCells().get("H15").putValue("May");
worksheet.getCells().get("H20").putValue("May");

worksheet.getCells().get("I15").putValue("Jun");
worksheet.getCells().get("I20").putValue("Jun");

// Data
worksheet.getCells().get("D21").putValue(304);
worksheet.getCells().get("D22").putValue(402);
worksheet.getCells().get("D23").putValue(321);
worksheet.getCells().get("D24").putValue(123);

worksheet.getCells().get("E21").putValue(300);
worksheet.getCells().get("E22").putValue(500);
worksheet.getCells().get("E23").putValue(219);
worksheet.getCells().get("E24").putValue(422);

worksheet.getCells().get("F21").putValue(222);
worksheet.getCells().get("F22").putValue(331);
worksheet.getCells().get("F23").putValue(112);
worksheet.getCells().get("F24").putValue(350);

worksheet.getCells().get("G21").putValue(100);
worksheet.getCells().get("G22").putValue(200);
worksheet.getCells().get("G23").putValue(300);
worksheet.getCells().get("G24").putValue(400);

worksheet.getCells().get("H21").putValue(200);
worksheet.getCells().get("H22").putValue(300);
worksheet.getCells().get("H23").putValue(400);
worksheet.getCells().get("H24").putValue(500);

worksheet.getCells().get("I21").putValue(400);
worksheet.getCells().get("I22").putValue(200);
worksheet.getCells().get("I23").putValue(200);
worksheet.getCells().get("I24").putValue(100);

// Dynamically load data on selection of Dropdown value
worksheet.getCells().get("D16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,2,FALSE),0)");
worksheet.getCells().get("E16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,3,FALSE),0)");
worksheet.getCells().get("F16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,4,FALSE),0)");
worksheet.getCells().get("G16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,5,FALSE),0)");
worksheet.getCells().get("H16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,6,FALSE),0)");
worksheet.getCells().get("I16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,7,FALSE),0)");

// Create Chart
const index = worksheet.getCharts().add(AsposeCells.ChartType.Column, 0, 3, 12, 9);
const chart = worksheet.getCharts().get(index);
chart.getNSeries().add("='Sheet1'!$D$16:$I$16", false);
chart.getNSeries().get(0).setName("=C16");
chart.getNSeries().setCategoryData("=$D$15:$I$15");

// Save result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
