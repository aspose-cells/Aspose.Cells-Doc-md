---
title: Export Excel Data to DataTable and Check Mixed Data Type with Node.js via C++
linktitle: Export Excel Data to DataTable and Check Mixed Data Type
type: docs
weight: 280
url: /nodejs-cpp/export-excel-data-to-datatable-and-check-mixed-data-type/
description: Learn how to Export Excel Data to DataTable and Check Mixed Data Type through the Aspose.Cells for Node.js via C++ API.
keywords: Export Excel Data to DataTable and Check Mixed Data Type Node.js via C++, Export Workbook Data to DataTable Node.js via C++, Export Data to DataTable Node.js via C++, Export Worksheet Data to DataTable Node.js via C++.
---

## **Possible Usage Scenarios**
If a column contains data of various types, the program will throw a type exception when exporting data to a DataTable. For exporting data table, by default, Aspose.Cells evaluates the data type for the values based on the very first (cell) value in the column. So, if the value is a number, it means that the data type of the column would be numeric, which is reasonable. If the very first value is a number but there are alphanumeric data or values in the column, a string data type should be assigned. To cope with it, please use [ExportDataTable overload](https://reference.aspose.com/cells/nodejs-cpp/aspose.cells/cells/#exportDataTable) which involves [ExportDataTableOptions](https://reference.aspose.com/cells/nodejs-cpp/aspose.cells/exporttableoptions/) and try to set [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/nodejs-cpp/aspose.cells/exporttableoptions/#checkMixedValueType) Boolean attribute to "true" if a column has both numeric and string values to escape from error.

## **Export Excel Data to DataTable and Check Mixed Data Type**

The following sample explains the use of [ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/nodejs-cpp/aspose.cells/exporttableoptions/#checkMixedValueType) property to export excel data to data table. Please see the [sample Excel file](sample.xlsx), its screenshot and the console output for a reference.

### **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Export Data Table Options
const opts = new AsposeCells.ExportTableOptions();
opts.setCheckMixedValueType(true);

// Export Data Table
const dt = worksheet.getCells().exportDataTable(0, 0, 7, 5, opts);

// Display the type of DataColumn
const columns = dt.getColumns();

columns.getEnumerator().forEach(column => {
    console.log(column.getColumnName() + " = " + column.getDataType());
});
```

### **Screenshot**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

### **Console Output**

Below is the console debug output of the above sample code

{{< highlight java >}}
Column1 = string
Column2 = string
Column3 = number
Column4 = number
Column5 = string
{{< /highlight >}}
