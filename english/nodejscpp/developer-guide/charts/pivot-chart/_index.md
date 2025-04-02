---
title: How to add a PivotChart using Aspose.Cells for Node.js via C++
linktitle: Pivot Chart
type: docs
weight: 100
url: /nodejs-cpp/how-to-add-pivot-chart/
description: How to add a PivotChart using Aspose.Cells for Node.js via C++.
keywords: PivotChart Node.js via C++
---
## What is PivotChart

A pivot chart is a visual representation of the data in a pivot table. Pivot charts provide a way to summarize, analyze, explore, and present summary data. Here are some key features and aspects of pivot charts:

1. Dynamic Data Representation: Pivot charts automatically update to reflect changes in the pivot table. If you add or remove fields in the pivot table, the pivot chart updates accordingly.

1. Interactive: Pivot charts are interactive, allowing users to filter, sort, and drill down into data. This makes it easy to explore different aspects of the data set.

1. Flexible Layout: Users can change the layout of the pivot chart by dragging and dropping fields, which offers flexibility in how data is visualized.

1. Various Chart Types: Pivot charts can be created using various chart types such as bar charts, line charts, pie charts, and more, depending on the nature of the data and the insights you wish to gain.

1. Summarization: Pivot charts summarize large amounts of data and can show totals, averages, counts, or other summary statistics.

1. Filtering: They provide filtering capabilities, allowing you to display only the data that meets certain criteria.

<br>
Pivot charts are commonly used in business intelligence and data analysis to provide a clear and concise visual summary of complex data sets. They are a powerful tool for making data-driven decisions.

## How to add a PivotChart using Aspose.Cells for Node.js via C++

### **Adding a Pivot Table**

To create a pivot table using Aspose.Cells for Node.js via C++:

1. Add some data to a worksheet using a Cell object's `putValue` method. You can also use a template file already filled with data. The data will be used as the pivot table's data source.
1. Add a pivot table to the worksheet by calling the `add` method of the `PivotTables` collection.
1. Access the new PivotTable object from the `PivotTables` collection by passing its index. Use any of the pivot table objects encapsulated in the PivotTable object to manage the table.

Code examples are given below.

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Obtaining the reference of the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Name the sheet
sheet.setName("Data");
const cells = sheet.getCells();

// Setting the values to the cells
cells.get("A1").putValue("Employee");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Product");
cells.get("D1").putValue("Continent");
cells.get("E1").putValue("Country");
cells.get("F1").putValue("Sale");

const namesAndValues = [
["David", 1, "Maxilaku", "Asia", "China", 2000],
["David", 2, "Maxilaku", "Asia", "India", 500],
["David", 3, "Chai", "Asia", "Korea", 1200],
["David", 4, "Maxilaku", "Asia", "India", 1500],
["James", 1, "Chang", "Europe", "France", 500],
["James", 2, "Chang", "Europe", "France", 1500],
["James", 3, "Chang", "Europe", "Germany", 800],
["James", 4, "Chang", "Europe", "Italy", 900],
["James", 4, "Chang", "Europe", "France", 500],
["Miya", 1, "Geitost", "America", "U.S.", 1600],
["Miya", 2, "Chai", "America", "U.S.", 600],
["Miya", 3, "Geitost", "America", "Brazil", 2000],
["Miya", 2, "Geitost", "America", "U.S.", 500],
["Miya", 3, "Maxilaku", "America", "Canada", 900],
["Miya", 4, "Geitost", "America", "U.S.", 700],
["Miya", 5, "Geitost", "America", "U.S.", 1400],
["Miya", 6, "Ikuru", "Europe", "Italy", 1350],
["Miya", 7, "Ikuru", "Europe", "France", 300],
["Miya", 8, "Ikuru", "Europe", "Italy", 500],
["Miya", 9, "Ikuru", "America", "New Zealand", 1000],
["Miya", 10, "Ipoh Coffee", "Oceania", "Australia", 1500],
["Miya", 11, "Chocolade", "Oceania", "Australia", 500],
["Miya", 12, "Chocolade", "Oceania", "New Zealand", 1500],
["Miya", 13, "Chocolade", "Oceania", "S.Africa", 1600],
["Miya", 14, "Chocolade", "Africa", "Egypt", 1000],
["Miya", 15, "Chocolade", "Africa", "Egypt", 1200],
["Miya", 16, "Chocolade", "Africa", "Egypt", 1300],
];

namesAndValues.forEach((item, index) => {
const rowIndex = index + 2;
cells.get(`A${rowIndex}`).putValue(item[0]);
cells.get(`B${rowIndex}`).putValue(item[1]);
cells.get(`C${rowIndex}`).putValue(item[2]);
cells.get(`D${rowIndex}`).putValue(item[3]);
cells.get(`E${rowIndex}`).putValue(item[4]);
cells.get(`F${rowIndex}`).putValue(item[5]);
```

### **Adding a Pivot Chart**

To create a PivotChart using Aspose.Cells for Node.js via C++:

1. Add a chart.
1. Set the `PivotSource` of the chart to refer to an existing pivot table in the spreadsheet.
1. Set other attributes.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating an Workbook object
// Opening the excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "pivotTable_test.xlsx"));
// Adding a new sheet
const sheetIndex = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);
const sheet3 = workbook.getWorksheets().get(sheetIndex);
sheet3.setName("PivotChart");
// Adding a column chart
const index = sheet3.getCharts().add(AsposeCells.ChartType.Column, 0, 5, 28, 16);
// Setting the pivot chart data source
sheet3.getCharts().get(index).setPivotSource("PivotTable!PivotTable1");
sheet3.getCharts().get(index).setHidePivotFieldButtons(false);
// Saving the Excel file
workbook.save(path.join(dataDir, "pivotChart_test_out.xlsx"));
```

