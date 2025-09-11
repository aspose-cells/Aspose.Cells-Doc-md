---  
title: Convert CSV, TSV and TXT to Excel with Node.js via C++  
linktitle: Convert CSV, TSV and TXT to Excel  
type: docs  
weight: 30  
url: /nodejs-cpp/convert-csv-tsv-and-txt-to-excel/  
---  

{{% alert color="primary" %}}  
Using Aspose.Cells, you can convert CSV files to Excel, OpenOffice, PDF, JSON, and many other formats.  
{{% /alert %}}  

## **Opening CSV Files**  

Comma Separated Values (CSV) files contain records where the values are separated by commas. Data is stored as a table where each column is separated by the comma character and quoted by the double quote character. If a field value contains a double quote character it is escaped with a pair of double quote characters. You can also use Microsoft Excel to export spreadsheet data to CSV.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions4 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);
// Create a Workbook object and opening the file from its path
const wbCSV = new AsposeCells.Workbook(path.join(dataDir, "Book_CSV.csv"), loadOptions4);
console.log("CSV file opened successfully!");
```  

## **Opening CSV files and replacing invalid characters**  

In Excel, when a CSV file with special characters is opened, the characters are automatically replaced. The same is done by the Aspose.Cells API which is demonstrated in the code example given below.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "[20180220142533][ASPOSE_CELLS_TEST].csv");

const options = new AsposeCells.TxtLoadOptions();
options.setSeparator(",");
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));
options.setCheckExcelRestriction(false);
options.setConvertNumericData(false);
options.setConvertDateTimeData(false);
// Load CSV file
const workbook = new AsposeCells.Workbook(filePath, options);

console.log(workbook.getWorksheets().get(0).getName()); // (20180220142533)(ASPOSE_CELLS_T
console.log(workbook.getWorksheets().get(0).getName().length); // 31
console.log("CSV file opened successfully!");
```  


### **Opening Text Files with Custom Separator**  

Text files are used to hold spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book11.csv");

// Instantiate Text File's LoadOptions
const txtLoadOptions = new AsposeCells.TxtLoadOptions();

// Specify the separator
txtLoadOptions.setSeparator(",");

// Specify the encoding type
txtLoadOptions.setEncoding(AsposeCells.EncodingType.UTF8);

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath, txtLoadOptions);

// Save file
wb.save(path.join(dataDir, "output.txt"));
```  

### **Opening Tab Delimited Files**  

Tab delimited (Text) files contain spreadsheet data but without any formatting. Data is arranged in rows and columns like in tables and spreadsheets. Basically, a tab delimited file is a special kind of plain text file with a tab between each column.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening Tab Delimited Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions5 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.TabDelimited);

// Create a Workbook object and opening the file from its path
const wbTabDelimited = new AsposeCells.Workbook(path.join(dataDir, "Book1TabDelimited.txt"), loadOptions5);
console.log("Tab delimited file opened successfully!");
```  

### **Opening Tab-Separated Values (TSV) Files**  

Tab-separated values (TSV) files contain spreadsheet data but without any formatting. It is the same as a Tab Delimited file where data is arranged in rows and columns like in tables and spreadsheets.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Tsv);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTSVFile.tsv"), loadOptions);

// Using the Sheet 1 in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Accessing a cell using its name
const cell = worksheet.getCells().get("C3");

console.log("Cell Name: " + cell.getName() + " Value: " + cell.getStringValue());
```  

## **Advance topics**  
- [Load or Import CSV file with Formulas](/cells/nodejs-cpp/load-or-import-csv-file-with-formulas/)  
- [Reading CSV File with Multiple Encodings](/cells/nodejs-cpp/reading-csv-file-with-multiple-encodings/)  

  
{{< app/cells/assistant language="nodejs-cpp" >}}