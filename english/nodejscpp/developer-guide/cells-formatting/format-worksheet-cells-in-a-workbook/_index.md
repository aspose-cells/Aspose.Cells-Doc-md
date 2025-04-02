---  
title: Format Worksheet Cells in a Workbook with Node.js via C++  
linktitle: Format Worksheet Cells in a Workbook  
description: Learn how to format worksheet cells in a workbook using Aspose.Cells for Node.js via C++. Customize the appearance and style of data in spreadsheets.  
keywords: Aspose.Cells, Workbook, Worksheet, Cell, Formatting, Appearance, Style, Node.js via C++  
type: docs  
weight: 2000  
url: /nodejs-cpp/format-worksheet-cells-in-a-workbook/  
---  

{{% alert color="primary" %}}  

This article shows how to:

1. Use styles to quickly format data.
2. Format cells in rows and columns.
3. Use borders and colors to emphasize data.
4. Apply number formats to emphasize data.
5. Use fonts and attributes to highlight data.
6. Format data in a named range.
7. Change data alignment and orientation.
8. Set row height and column width.

The example project performs all of these tasks and provides developers with a detailed description of how to create a workbook, add data into and apply formatting using [Aspose.Cells](https://products.aspose.com/cells/nodejs-cpp/).

{{% /alert %}}  

## **Data Formatting**

Formatting is used to distinguish between different types of information and to display data clearly.

A format represents a style and is defined as a set of characteristics, such as fonts and font sizes, number formats, cell borders, cell shading, indentation, alignment and text orientation. Borders provide further ways to highlight information. A border is a line drawn around a cell or a group of cells.

Number formats also make data more meaningful. By applying different number formats, you can change the appearance of numbers without changing the number behind the appearance.

Aspose.Cells lets you draw borders around cells and ranges easily. It also lets you apply fonts and shade cells. The component is efficient enough that you can format a complete row or column, set alignments, wrap and rotate text in cells. Aspose.Cells further supports all number formats supported by Microsoft Excel.

This article shows how to create a console application that generates an annual sales report. The workbook is created from scratch, then data is inserted and the worksheet is formatted. We show how to create a simple console application that creates an Excel workbook (you can also use a template file), insert sales data into the first worksheet, format the data and save an Excel file.

### **Process**

Below are the steps involved how to create a spreadsheet and format different cells in different rows and columns of a worksheet.

1. Download and install Aspose.Cells:
   1. [Download](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++.
   1. Install it on your development computer.
2. Create a project and add references:
   1. Start your code editor/IDE.
   1. Create a new console application.
   1. Add a reference to Aspose.Cells in your Node.js project.
3. Add the following code to the project:

```javascript
try
{
const AsposeCells = require("aspose.cells.node");
const path = require("path");

class FormatWorksheetCells 
{
static run() {
const dataDir = path.join(__dirname, "data");
const filename = path.join(dataDir, "FormatWorksheet.xls");
FormatWorksheetCells.createSalesReport(filename);
}

static createSalesReport(filename) {
const cellsLicense = new AsposeCells.License();
cellsLicense.setLicense("Aspose.Cells.lic");

const workbook = new AsposeCells.Workbook();
workbook.changePalette(new AsposeCells.Color(155, 204, 255), 55);
workbook.changePalette(new AsposeCells.Color(0, 51, 105), 54);
workbook.changePalette(new AsposeCells.Color(250, 250, 200), 53);
workbook.changePalette(new AsposeCells.Color(124, 199, 72), 52);

FormatWorksheetCells.createReportData(workbook);
FormatWorksheetCells.createCellsFormatting(workbook);

const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Sales Report");
workbook.save(filename);
}

static createReportData(workbook) {
const cells = workbook.getWorksheets().get(0).getCells();
cells.get("B1").putValue("Western Product Sales 2006");

const headers = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "Total"];
headers.forEach((header, index) => {
cells.get(1, index + 1).putValue(header);
```  
  