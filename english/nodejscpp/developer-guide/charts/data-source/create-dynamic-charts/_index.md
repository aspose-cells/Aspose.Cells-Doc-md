---  
title: Create Dynamic Charts with Node.js via C++  
linktitle: Create Dynamic Charts  
description: Learn how to create dynamic charts in Aspose.Cells for Node.js via C++. This guide will show you how to dynamically update chart data, series, and formatting based on your requirements, allowing you to present changing data visually in your worksheets.  
keywords: Aspose.Cells for Node.js, charting, dynamic charts, data, series, formatting, worksheets, updating.  
type: docs  
weight: 240  
url: /nodejs-cpp/create-dynamic-charts/  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  
Dynamic (or interactive) charts have the ability to change when you change the scope of data. In other words, the dynamic charts can automatically reflect changes when the data source is changed. In order to trigger the change in the data source, one can use the filtering option of Excel Tables or use a control such as ComboBox or Dropdown list.

This article demonstrates the usage of Aspose.Cells for Node.js via C++ APIs to create dynamic charts using both of the aforementioned approaches.  
{{% /alert %}}  

## **Using Excel Tables**  

{{% alert color="primary" %}}  
Excel tables are referred to as ListObjects in Aspose.Cells' perspective, therefore, we will use the term "ListObject" instead of "Table" for clarity. Please read in detail on how to [create ListObjects](/cells/nodejs-cpp/create-and-format-table/) with Aspose.Cells for Node.js via C++.  
{{% /alert %}}  

ListObjects provides the in-built functionality to sort & filter the data upon user interaction. Both sorting & filtering options are provided through the drop-down lists which are automatically added to the header row of the [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject). Due to these features (sorting & filtering), the [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) seems to be the perfect candidate to serve as the data source to a dynamic chart because when sorting or filtering is changed, the representation of data in the chart will be changed to reflect the current state of the [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject).

In order to keep the demonstration simple to understand, we will create the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) from scratch and move forward step by step as outlined below.

1. Create an empty [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Access the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) of the first [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) in the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Insert some data to the cells.
1. Create [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) based on the inserted data.
1. Create [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) based on the data range of [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject).
1. Save the result on the disk.  

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

## **Using Dynamic Formulas**  

In case you do not wish to use the [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) as a data source to the dynamic chart, the other option is to use Excel functions (or formulas) to create a dynamic range of data, and a control (such as ComboBox) to trigger the change in data. In this scenario, we will use the VLOOKUP function to fetch the appropriate values based on the selection of ComboBox. When selection is changed, the VLOOKUP function will refresh the cell value. If a range of cells is using the VLOOKUP function, the whole range can be refreshed upon user interaction, therefore it can be used as a source to the dynamic chart.

In order to keep the demonstration simple to understand, we will create the Workbook from scratch and move forward step by step as outlined below.

1. Create an empty [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Access the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) of the first [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) in the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).
1. Insert some data to the cells by creating a Named Range. This data will serve as a series to the dynamic chart.
1. Create [**ComboBox**](https://reference.aspose.com/cells/nodejs-cpp/combobox) based on the Named Range created in the previous step.
1. Insert some more data to the cells that will serve as a source to the VLOOKUP function.
1. Insert VLOOKUP function (with appropriate parameters) to a range of cells. This range will serve as a source to the dynamic chart.
1. Create [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) based on the range created in the previous step.
1. Save the result on the disk.  

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
