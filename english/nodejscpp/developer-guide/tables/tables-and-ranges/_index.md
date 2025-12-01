---  
title: Tables and Ranges with Node.js via C++  
linktitle: Tables and Ranges  
type: docs  
weight: 50  
url: /nodejs-cpp/tables-and-ranges/  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Introduction**  

Sometimes you create a table in Microsoft Excel and do not want to keep working with the table functionality that it comes with. Instead, you want something that looks like a table. To keep data in a table without losing formatting, convert the table to a regular range of data.  
Aspose.Cells does support this feature of Microsoft Excel for tables and list objects.  

## **Using Microsoft Excel**  

Use the **Convert to Range** feature to quickly convert a table to a range without losing formatting. In Microsoft Excel 2007/2010:  

1. Click anywhere in the table to make sure that the active cell is in a table column.  
1. On the **Design** tab, in the **Tools** group, click **Convert to Range**.  

## **Using Aspose.Cells**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");

// Open an existing file that contains a table/list object in it
const wb = new AsposeCells.Workbook(filePath);

// Convert the first table/list object (from the first worksheet) to normal range
wb.getWorksheets().get(0).getListObjects().get(0).convertToRange();

// Save the file
wb.save(path.join(dataDir, "output.xlsx"));
```  

{{% alert color="primary" %}}  

The table features are no longer available after the table has been converted to a range. For example, row headers no longer include the sort and filter arrows, and structured references (references that use table names) that were used in formulas turn into regular cell references.  

{{% /alert %}}  

## **Convert Table to Range with Options**  

Aspose.Cells provides additional options while converting Table to Range through the [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/) class. The [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/) class provides [**getLastRow()**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/#getLastRow--) property which allows you to set the last index of the table row. The table formatting will be retained up to the specified row index and the rest of the formatting will be removed.  

The sample code given below demonstrates the use of [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/) class.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");
// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.TableToRangeOptions();
options.setLastRow(5);

// Convert the first table/list object (from the first worksheet) to normal range
workbook.getWorksheets().get(0).getListObjects().get(0).convertToRange(options);

// Save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
