---  
title: Generate Chart by Processing Smart Markers with Node.js via C++  
linktitle: Generate Chart by Processing Smart Markers  
description: Learn how to generate charts with smart markers using Aspose.Cells for Node.js via C++. Our guide will show you how to process smart markers and their properties to enhance the appearance and usability of your charts.  
keywords: Aspose.Cells for Node.js, chart generation, smart markers, appearance, usability, processing.  
type: docs  
weight: 2100  
url: /nodejs-cpp/generate-chart-by-processing-smart-markers/  
---  

{{% alert color="primary" %}}  
Aspose.Cells APIs provide the [**WorkbookDesigner**](https://reference.aspose.com/cells/nodejs-cpp/workbookdesigner) class to work with Smart Markers where the formatting & formulas are placed in the designer spreadsheets and then processed with [**WorkbookDesigner**](https://reference.aspose.com/cells/nodejs-cpp/workbookdesigner) class to fill up the data according to specified Smart Markers. It is also possible to create Excel charts by processing Smart Markers, which will require the following steps.  

- Creation of designer spreadsheet  
- Processing designer spreadsheet against the specified data source  
- Creation of chart based on populated data  
{{% /alert %}}  

## Creation of Designer Spreadsheet  

A designer spreadsheet is a simple Excel file created with Microsoft Excel application or Aspose.Cells APIs containing the visual formatting, formulas and smart markers, where the contents can be populated at runtime.  

For the sake of simplicity, we will create the designer spreadsheet using the Aspose.Cells for Node.js via C++ API and later process it against a dynamically created data source for demonstration purposes.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create an instance of Workbook
const book = new AsposeCells.Workbook();

// Access the first, default Worksheet by passing its index
const dataSheet = book.getWorksheets().get(0);

// Name the Worksheet for later reference
dataSheet.setName("ChartData");

// Access the CellsCollection of first Worksheet
const cells = dataSheet.getCells();

// Insert static data (headers)
cells.get("B1").putValue("Item 1");
cells.get("C1").putValue("Item 2");
cells.get("D1").putValue("Item 3");
cells.get("E1").putValue("Item 4");
cells.get("F1").putValue("Item 5");
cells.get("G1").putValue("Item 6");
cells.get("H1").putValue("Item 7");
cells.get("I1").putValue("Item 8");
cells.get("J1").putValue("Item 9");
cells.get("K1").putValue("Item 10");
cells.get("L1").putValue("Item 11");
cells.get("M1").putValue("Item 12");

// Place Smart Markers
cells.get("A2").putValue("&=Sales.Year");
cells.get("B2").putValue("&=Sales.Item1");
cells.get("C2").putValue("&=Sales.Item2");
cells.get("D2").putValue("&=Sales.Item3");
cells.get("E2").putValue("&=Sales.Item4");
cells.get("F2").putValue("&=Sales.Item5");
cells.get("G2").putValue("&=Sales.Item6");
cells.get("H2").putValue("&=Sales.Item7");
cells.get("I2").putValue("&=Sales.Item8");
cells.get("J2").putValue("&=Sales.Item9");
cells.get("K2").putValue("&=Sales.Item10");
cells.get("L2").putValue("&=Sales.Item11");
cells.get("M2").putValue("&=Sales.Item12");
```  

## Processing Designer Spreadsheet  

In order to process the designer spreadsheet, one must have a data source that corresponds to the Smart Markers used in the designer spreadsheet. For instance, we have created a Smart Marker entry as &=Sales.Year, that represents the Year column in the DataTable Sales. In case a corresponding column isn't available in the data source, the Aspose.Cells APIs will skip the processing for that particular Smart Marker, and as a result, the data for the particular Smart Marker will not be populated.  

In order to demonstrate this use case, we will create the data source from scratch and process it against the designer spreadsheet created in the previous step. However, in a real-time scenario, data could already be available for further processing so you can skip the creation of data source if data is already available.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of DataTable and name is according to the Smart Markers
const table = new AsposeCells.DataTable("Sales");
/*
 * Add columns to the newly created DataTable while specifying the column type
 * It is important that the DataTable should have at least one column for each
 * Smart Marker entry from the designer spreadsheet
*/
table.Columns.add("Year", AsposeCells.DataType.String);
table.Columns.add("Item1", AsposeCells.DataType.Int32);
table.Columns.add("Item2", AsposeCells.DataType.Int32);
table.Columns.add("Item3", AsposeCells.DataType.Int32);
table.Columns.add("Item4", AsposeCells.DataType.Int32);
table.Columns.add("Item5", AsposeCells.DataType.Int32);
table.Columns.add("Item6", AsposeCells.DataType.Int32);
table.Columns.add("Item7", AsposeCells.DataType.Int32);
table.Columns.add("Item8", AsposeCells.DataType.Int32);
table.Columns.add("Item9", AsposeCells.DataType.Int32);
table.Columns.add("Item10", AsposeCells.DataType.Int32);
table.Columns.add("Item11", AsposeCells.DataType.Int32);
table.Columns.add("Item12", AsposeCells.DataType.Int32);

// Add some rows with data to the DataTable
table.Rows.add(["2000", 2310, 0, 110, 15, 20, 25, 30, 1222, 200, 421, 210, 133]);
table.Rows.add(["2005", 1508, 0, 170, 280, 190, 400, 105, 132, 303, 199, 120, 100]);
table.Rows.add(["2010", 0, 210, 230, 140, 150, 160, 170, 110, 1999, 1229, 1120, 2300]);
table.Rows.add(["2015", 3818, 320, 340, 260, 210, 310, 220, 0, 0, 0, 0, 122]);
```  

The processing of Smart Markers is quite simple as demonstrated by the following code snippet.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook
const book = new AsposeCells.Workbook();

// Access the first, default Worksheet by passing its index
const dataSheet = book.getWorksheets().get(0);

// Name the Worksheet for later reference
dataSheet.setName("ChartData");

// Access the CellsCollection of first Worksheet
const cells = dataSheet.getCells();

// Insert static data (headers)
cells.get("B1").putValue("Item 1");
cells.get("C1").putValue("Item 2");
cells.get("D1").putValue("Item 3");
cells.get("E1").putValue("Item 4");
cells.get("F1").putValue("Item 5");
cells.get("G1").putValue("Item 6");
cells.get("H1").putValue("Item 7");
cells.get("I1").putValue("Item 8");
cells.get("J1").putValue("Item 9");
cells.get("K1").putValue("Item 10");
cells.get("L1").putValue("Item 11");
cells.get("M1").putValue("Item 12");

// Place Smart Markers
cells.get("A2").putValue("&=Sales.Year");
cells.get("B2").putValue("&=Sales.Item1");
cells.get("C2").putValue("&=Sales.Item2");
cells.get("D2").putValue("&=Sales.Item3");
cells.get("E2").putValue("&=Sales.Item4");
cells.get("F2").putValue("&=Sales.Item5");
cells.get("G2").putValue("&=Sales.Item6");
cells.get("H2").putValue("&=Sales.Item7");
cells.get("I2").putValue("&=Sales.Item8");
cells.get("J2").putValue("&=Sales.Item9");
cells.get("K2").putValue("&=Sales.Item10");
cells.get("L2").putValue("&=Sales.Item11");
cells.get("M2").putValue("&=Sales.Item12");

// Create an instance of DataTable and name it according to the Smart Markers
const table = new AsposeCells.DataTable("Sales");
/*
 * Add columns to the newly created DataTable while specifying the column type
 * It is important that the DataTable should have at least one column for each
 * Smart Marker entry from the designer spreadsheet
*/
table.Columns.Add("Year", AsposeCells.DataType.String);
table.Columns.Add("Item1", AsposeCells.DataType.Int32);
table.Columns.Add("Item2", AsposeCells.DataType.Int32);
table.Columns.Add("Item3", AsposeCells.DataType.Int32);
table.Columns.Add("Item4", AsposeCells.DataType.Int32);
table.Columns.Add("Item5", AsposeCells.DataType.Int32);
table.Columns.Add("Item6", AsposeCells.DataType.Int32);
table.Columns.Add("Item7", AsposeCells.DataType.Int32);
table.Columns.Add("Item8", AsposeCells.DataType.Int32);
table.Columns.Add("Item9", AsposeCells.DataType.Int32);
table.Columns.Add("Item10", AsposeCells.DataType.Int32);
table.Columns.Add("Item11", AsposeCells.DataType.Int32);
table.Columns.Add("Item12", AsposeCells.DataType.Int32);

// Add some rows with data to the DataTable
table.Rows.Add("2000", 2310, 0, 110, 15, 20, 25, 30, 1222, 200, 421, 210, 133);
table.Rows.Add("2005", 1508, 0, 170, 280, 190, 400, 105, 132, 303, 199, 120, 100);
table.Rows.Add("2010", 0, 210, 230, 140, 150, 160, 170, 110, 1999, 1229, 1120, 2300);
table.Rows.Add("2015", 3818, 320, 340, 260, 210, 310, 220, 0, 0, 0, 0, 122);

// Create an instance of WorkbookDesigner class
const designer = new AsposeCells.WorkbookDesigner();

// Assign the Workbook property to the instance of Workbook created in first step
designer.setWorkbook(book);

// Set the data source
designer.SetDataSource(table);

// Call Process method to populate data
designer.Process();
```  

{{% alert color="primary" %}}  
The above code snippet uses the existing instance of the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class created in the first step. If you already have the designer spreadsheet file on disk or memory, you can create an instance of [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class by loading the existing designer spreadsheet.  
{{% /alert %}}  

## Creation of Chart  

Once the data is in place, all we need to do is to create a chart based on the data source. In order to keep the example simple, we will use the [**Chart.setChartDataRange(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#setChartDataRange-string-boolean-) method so that we do not have to configure the chart further.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook
const book = new AsposeCells.Workbook();

// Access the first, default Worksheet by passing its index
const dataSheet = book.getWorksheets().get(0);

// Name the Worksheet for later reference
dataSheet.setName("ChartData");

// Access the CellsCollection of first Worksheet
const cells = dataSheet.getCells();

// Insert static data (headers)
cells.get("B1").putValue("Item 1");
cells.get("C1").putValue("Item 2");
cells.get("D1").putValue("Item 3");
cells.get("E1").putValue("Item 4");
cells.get("F1").putValue("Item 5");
cells.get("G1").putValue("Item 6");
cells.get("H1").putValue("Item 7");
cells.get("I1").putValue("Item 8");
cells.get("J1").putValue("Item 9");
cells.get("K1").putValue("Item 10");
cells.get("L1").putValue("Item 11");
cells.get("M1").putValue("Item 12");

// Place Smart Markers
cells.get("A2").putValue("&=Sales.Year");
cells.get("B2").putValue("&=Sales.Item1");
cells.get("C2").putValue("&=Sales.Item2");
cells.get("D2").putValue("&=Sales.Item3");
cells.get("E2").putValue("&=Sales.Item4");
cells.get("F2").putValue("&=Sales.Item5");
cells.get("G2").putValue("&=Sales.Item6");
cells.get("H2").putValue("&=Sales.Item7");
cells.get("I2").putValue("&=Sales.Item8");
cells.get("J2").putValue("&=Sales.Item9");
cells.get("K2").putValue("&=Sales.Item10");
cells.get("L2").putValue("&=Sales.Item11");
cells.get("M2").putValue("&=Sales.Item12");

// Create an instance of DataTable and name is according to the Smart Markers
const table = new AsposeCells.DataTable("Sales");
/*
 * Add columns to the newly created DataTable while specifying the column type
 * It is important that the DataTable should have at least one column for each
 * Smart Marker entry from the designer spreadsheet
*/
table.Columns.Add("Year", AsposeCells.Type.GetType("System.String"));
table.Columns.Add("Item1", AsposeCells.Type.GetType("System.Int32"));
table.Columns.Add("Item2", AsposeCells.Type.GetType("System.Int32"));
table.Columns.Add("Item3", AsposeCells.Type.GetType("System.Int32"));
table.Columns.Add("Item4", AsposeCells.Type.GetType("System.Int32"));
table.Columns.Add("Item5", AsposeCells.Type.GetType("System.Int32"));
table.Columns.Add("Item6", AsposeCells.Type.GetType("System.Int32"));
table.Columns.Add("Item7", AsposeCells.Type.GetType("System.Int32"));
table.Columns.Add("Item8", AsposeCells.Type.GetType("System.Int32"));
table.Columns.Add("Item9", AsposeCells.Type.GetType("System.Int32"));
table.Columns.Add("Item10", AsposeCells.Type.GetType("System.Int32"));
table.Columns.Add("Item11", AsposeCells.Type.GetType("System.Int32"));
table.Columns.Add("Item12", AsposeCells.Type.GetType("System.Int32"));

// Add some rows with data to the DataTable
table.Rows.Add(["2000", 2310, 0, 110, 15, 20, 25, 30, 1222, 200, 421, 210, 133]);
table.Rows.Add(["2005", 1508, 0, 170, 280, 190, 400, 105, 132, 303, 199, 120, 100]);
table.Rows.Add(["2010", 0, 210, 230, 140, 150, 160, 170, 110, 1999, 1229, 1120, 2300]);
table.Rows.Add(["2015", 3818, 320, 340, 260, 210, 310, 220, 0, 0, 0, 0, 122]);

// Create an instance of WorkbookDesigner class
const designer = new AsposeCells.WorkbookDesigner();

// Assign the Workbook property to the instance of Workbook created in first step
designer.setWorkbook(book);

// Set the data source
designer.SetDataSource(table);

// Call Process method to populate data
designer.Process();

/*
 * Save the number of rows & columns from the source DataTable in separate variables. 
 * These values will be used later to identify the chart's data range from DataSheet
*/
const chartRows = table.Rows.Count;
const chartCols = table.Columns.Count;

// Add a new Worksheet of type Chart to Workbook
const chartSheetIdx = book.getWorksheets().add(AsposeCells.SheetType.Chart);

// Access the newly added Worksheet via its index
const chartSheet = book.getWorksheets().get(chartSheetIdx);

// Name the Worksheet
chartSheet.setName("Chart");

// Add a chart of type ColumnStacked to newly added Worksheet
const chartIdx = chartSheet.getCharts().add(AsposeCells.ChartType.ColumnStacked, 0, 0, chartRows, chartCols);

// Access the newly added Chart via its index
const chart = chartSheet.getCharts().get(chartIdx);

// Set the data range for the chart
chart.setChartDataRange(dataSheet.getName() + "!A1:" + AsposeCells.CellsHelper.columnIndexToName(chartCols - 1) + (chartRows + 1).toString(), false);

// Set the chart to size with window
chart.setSizeWithWindow(true);

// Set the format for the tick labels
chart.getValueAxis().getTickLabels().setNumberFormat("$###,### K");

// Set chart title
chart.getTitle().setText("Sales Summary");

// Set ChartSheet an active sheet
book.getWorksheets().setActiveSheetIndex(chartSheetIdx);

// Save the final result
book.save(path.join(dataDir, "report_out.xlsx"));
```  
  