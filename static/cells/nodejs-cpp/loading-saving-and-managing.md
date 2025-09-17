##Loading and managing Excel, OpenOffice, Json, Csv and Html files
With Aspose.Cells, it is simple to create, open, and manage Excel, CSV, TSV, ODS, HTML, Numbers, Json, XML, Pdf, Jpg, Tiff, Image, Mht, and XPS files using Node.js via C++.
With Aspose.Cells, it is simple to create, open, and manage Excel files, for example, to retrieve data, or to use a designer template to speed up the development process.
## **Creating a New Workbook**
The following example creates a new workbook from scratch.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const licensePath = path.join(dataDir, "Aspose.Cells.lic");
try {
// Create a License object
const license = new AsposeCells.License();
// Set the license of Aspose.Cells to avoid the evaluation limitations
license.setLicense(licensePath);
} catch (ex) {
console.log(ex.message);
}
// Instantiate a Workbook object that represents Excel file.
const wb = new AsposeCells.Workbook();
// When you create a new workbook, a default "Sheet1" is added to the workbook.
const sheet = wb.getWorksheets().get(0);
// Access the "A1" cell in the sheet.
const cell = sheet.getCells().get("A1");
// Input the "Hello World!" text into the "A1" cell
cell.putValue("Hello World!");
// Save the Excel file.
wb.save(path.join(dataDir, "MyBook_out.xlsx"));
```
## **Opening and saving a File**
With Aspose.Cells, it is simple to open, save and manage Excel files.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Adding new sheet
const sheet = workbook1.getWorksheets().add("MySheet");
// Setting active sheet
workbook1.getWorksheets().setActiveSheetIndex(1);
// Setting values.
const cells = sheet.getCells();
// Setting text
cells.get("A1").putValue("Hello!");
// Setting number
cells.get("A2").putValue(1000);
// Setting Date Time
const cell = cells.get("A3");
cell.putValue(new Date());
const style = cell.getStyle();
style.setNumber(14);
cell.setStyle(style);
// Setting formula
cells.get("A4").setFormula("=SUM(A1:A3)");
// Saving the workbook to disk.
workbook1.save(path.join(dataDir, "dest.xlsx"));
```
## **Advanced Topics**
- [Different Ways to Open Files](https://docs.aspose.com/cells/nodejs-cpp/different-ways-to-open-files/)
- [Filter Defined Names while loading Workbook](https://docs.aspose.com/cells/nodejs-cpp/filter-defined-names-while-loading-workbook/)
- [Filter Objects while loading Workbook or Worksheet](https://docs.aspose.com/cells/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Filtering the kind of data while loading the workbook from template file](https://docs.aspose.com/cells/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Get Warnings while Loading Excel File](https://docs.aspose.com/cells/nodejs-cpp/get-warnings-while-loading-excel-file/)
- [Load Source Excel File Without Charts](https://docs.aspose.com/cells/nodejs-cpp/load-source-excel-file-without-charts/)
- [Load Specific Worksheets in a Workbook](https://docs.aspose.com/cells/nodejs-cpp/load-specific-worksheets-in-a-workbook/)
- [Load Workbook with specified Printer Paper Size](https://docs.aspose.com/cells/nodejs-cpp/load-workbook-with-specified-printer-paper-size/)
- [Opening Different Microsoft Excel Versions Files](https://docs.aspose.com/cells/nodejs-cpp/opening-different-microsoft-excel-versions-files/)
- [Opening Files with Different Formats](https://docs.aspose.com/cells/nodejs-cpp/opening-files-with-different-formats/)
- [Optimizing Memory Usage while Working with Big Files having Large Datasets](https://docs.aspose.com/cells/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Read Numbers Spreadsheet Developed by Apple Inc. using Aspose.Cells](https://docs.aspose.com/cells/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Stop conversion or loading using InterruptMonitor when it is taking too long](https://docs.aspose.com/cells/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Using LightCells API](https://docs.aspose.com/cells/nodejs-cpp/using-lightcells-api/)
- [Convert CSV to JSON](https://docs.aspose.com/cells/nodejs-cpp/convert-csv-to-json/)
- [Convert Excel to JSON](https://docs.aspose.com/cells/nodejs-cpp/convert-excel-to-json/)
- [Convert JSON to CSV](https://docs.aspose.com/cells/nodejs-cpp/convert-json-to-csv/)
- [Convert JSON to Excel](https://docs.aspose.com/cells/nodejs-cpp/convert-json-to-excel/)
- [Convert Excel to Html](https://docs.aspose.com/cells/nodejs-cpp/convert-excel-to-html/)
