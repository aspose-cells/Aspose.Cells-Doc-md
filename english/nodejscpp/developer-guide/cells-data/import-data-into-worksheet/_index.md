---
title: Import Data into Worksheet with Node.js via C++
linktitle: Import Data into Worksheet
type: docs
weight: 170
url: /nodejs-cpp/import-data-into-worksheet/
description: Learn how to import data into Worksheet through the Aspose.Cells for Node.js via C++ API.
keywords: Node.js Import Data into Worksheet, Import data into Excel with ICellsDataTable interface, Import data from Array, Import Data from ArrayList, Import Data from Custom Objects, Import Data from Custom Objects to merged area, Import Data from DataTable, Import Data from dynamic object as data source, Import Data from DataColumn, Import Data from DataView, Import Data from DataGrid, Import Data from GridView, Import HTML formatted data, Import Data from JSON
---

{{% alert color="primary" %}}
This article discusses some data import techniques that developers have access to through Aspose.Cells.
{{% /alert %}}

## **How to Import Data into Worksheet**

When you open an Excel file with Aspose.Cells, all data in the file is automatically imported. Aspose.Cells can also import data from other data sources.

Aspose.Cells provides a [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#worksheets) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#cells) collection. The [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#cells) collection provides useful methods to import data from different data sources. This article explains how these methods can be used.

## **How to Import data into Excel with ICellsDataTable interface**

Implement [ICellsDataTable](https://reference.aspose.com/cells/nodejs-cpp/icellsdatatable) to wrap your various data sources, then use [Cells.importData()](https://reference.aspose.com/cells/nodejs-cpp/cells/importdata/#importdata) to import data to Excel worksheet.

### **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "ICellsDataTable.xlsx");

// Init data source
const customers = [
    { name: "Thomas Hardy", address: "120 Hanover Sq., London" },
    { name: "Paolo Accorti", address: "Via Monte Bianco 34, Torino" }
];

// Create a new file.
const wb = new AsposeCells.Workbook();
const options = new AsposeCells.ImportTableOptions();
options.setIsFieldNameShown(true);

// Import ICellsDataTable with options
wb.getWorksheets().get(0).getCells().importData(new CustomerDataSource(customers), 0, 0, options);
wb.save(filePath);
```

The implementation of *CustomerDataSource*, *Customer*, and *CustomerList* classes is given below

```javascript
class Customer {
    constructor(fullName, address) {
        this.fullName = fullName;
        this.address = address;
    }
}

class CustomerList extends Array {
    constructor() {
        super();
    }

    get(index) {
        return this[index];
    }

    set(index, value) {
        this[index] = value;
    }
}

class CustomerDataSource {
    constructor(customers) {
        this.m_DataSource = customers;
        this.m_Properties = Object.keys(customers[0]);
        this.m_Columns = new Array(this.m_Properties.length);
        this.m_PropHash = new Map();

        for (let i = 0; i < this.m_Properties.length; i++) {
            this.m_Columns[i] = this.m_Properties[i];
            this.m_PropHash.set(this.m_Properties[i], this.m_Properties[i]);
        }
        this.m_IEnumerator = this.m_DataSource.values();
        this.m_Current = this.m_IEnumerator.next();
    }

    get Columns() {
        return this.m_Columns;
    }

    get Count() {
        return this.m_DataSource.length;
    }

    BeforeFirst() {
        this.m_IEnumerator = this.m_DataSource.values();
        this.m_Current = this.m_IEnumerator.next();
    }

    getByIndex(index) {
        return this.m_Current.value[this.m_Properties[index]];
    }

    getByColumnName(columnName) {
        return this.m_Current.value[this.m_PropHash.get(columnName)];
    }

    Next() {
        if (this.m_IEnumerator === null) return false;

        this.m_Current = this.m_IEnumerator.next();
        return !this.m_Current.done;
    }

    get(index) {
        return this.m_Current.value[this.m_Properties[index]];
    }
}
```


## **How to Import Data into Excel from Array**

To import data to a spreadsheet from an array, call the [**importArray**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/importarray/index) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#cells) collection. There are many overloaded versions of the [**importArray**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/importarray/index) method but a typical overload takes the following parameters:

- **Array**, the array object that you're importing content from.
- **Row number**, the row number of the first cell that the data will be imported to.
- **Column number**, the column number of the first cell that the data will be imported to.
- **Is vertical**, a Boolean value that specifies whether to import data vertically or horizontally.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
const fs = require("fs");
if (!fs.existsSync(dataDir)){
    fs.mkdirSync(dataDir);
}

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Creating an array containing names as string values
const names = ["laurence chen", "roman korchagin", "kyle huang"];

// Importing the array of names to 1st row and first column vertically
worksheet.getCells().importArray(names, 0, 0, true);

// Saving the Excel file
workbook.save(path.join(dataDir, "DataImport.out.xls"));
```

## **How to Import Data into Excel from ArrayList**

To import data from an *ArrayList* to worksheets, call the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#cells) collection's [**importArrayList**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/importarraylist) method. The importArray method takes the following parameters:

- **Array list**, represents the *ArrayList* object you're importing.
- **Row number**, represents the row number of the first cell that the data will be imported to.
- **Column number**, represents the column number of the first cell that the data will be imported to.
- **Is vertical**, a Boolean value that specifies whether to import data vertically or horizontally.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
if (!require('fs').existsSync(dataDir)) {
    require('fs').mkdirSync(dataDir);
}

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Instantiating an Array object
const list = [];

// Add few names to the list as string values
list.push("laurence chen");
list.push("roman korchagin");
list.push("kyle huang");
list.push("tommy wang");

// Importing the contents of Array to 1st row and first column vertically
worksheet.getCells().importFormulaArray(list, 0, 0, true);

// Saving the Excel file
workbook.save(path.join(dataDir, "DataImport.out.xls"));
```

## **How to Import Data into Excel from Custom Objects**

To import data from a collection of objects to a worksheet, use [**importCustomObjects**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/importcustomobjects/index). Provide a list of columns/properties to the method to display your desired list of objects.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
if (!require("fs").existsSync(dataDir)) {
    require("fs").mkdirSync(dataDir);
}

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

const sheet = book.getWorksheets().get(0);

// Define List
const list = [
    new Person("Mike", 25),
    new Person("Steve", 30),
    new Person("Billy", 35)
];

const imp = new AsposeCells.ImportTableOptions();
imp.setInsertRows(true);

// We pick a few columns not all to import to the worksheet
sheet.getCells().importCustomObjects(
    list,
    ["Name", "Age"],
    true,
    0,
    0,
    list.length,
    true,
    "dd/mm/yyyy",
    false
);

// Auto-fit all the columns
book.getWorksheets().get(0).autoFitColumns();

// Save the Excel file
book.save(path.join(dataDir, "ImportedCustomObjects.out.xls"));

class Person {
    constructor(name, age) {
        this._name = name;
        this._age = age;
    }

    get Age() {
        return this._age;
    }

    set Age(value) {
        this._age = value;
    }

    get Name() {
        return this._name;
    }

    set Name(value) {
        this._name = value;
    }
}
```

## **How to Import Data into Excel from Custom Objects and Check Merged Area**

To import data from a collection of objects to a worksheet containing merged cells, use [**ImportTableOptions.checkMergedCells**](https://reference.aspose.com/cells/nodejs-cpp/importtableoptions/#checkMergedCells) property. If the Excel template has merged cells, set the value of [**ImportTableOptions.checkMergedCells**](https://reference.aspose.com/cells/nodejs-cpp/importtableoptions/#checkMergedCells) property to true. Pass the [**ImportTableOptions**](https://reference.aspose.com/cells/nodejs-cpp/importtableoptions) object along with the list of columns/properties to the method to display your desired list of objects. The following code sample demonstrates the use of [**ImportTableOptions.checkMergedCells**](https://reference.aspose.com/cells/nodejs-cpp/importtableoptions/#checkMergedCells) property to import data from Custom Objects to merged cells. Please see the attached [source Excel](90112033.xlsx) file and the [output Excel](90112034.xlsx) file for reference.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = RunExamples.Get_SourceDirectory();

// Output directory
const outputDir = RunExamples.Get_OutputDirectory();

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleMergedTemplate.xlsx"));
const productList = [];

// Creating collection of test items
for (let i = 0; i < 3; i++) {
    const product = {
        ProductId: i,
        ProductName: `Test Product - ${i}`
    };
    productList.push(product);
}

const tableOptions = new AsposeCells.ImportTableOptions();
tableOptions.setCheckMergedCells(true);
tableOptions.setIsFieldNameShown(false);

// Insert data to excel template
workbook.getWorksheets().get(0).getCells().importCustomObjects(productList, 1, 0, tableOptions);
workbook.save(path.join(outputDir, "sampleMergedTemplate_out.xlsx"), AsposeCells.SaveFormat.Xlsx);

console.log("ImportCustomObectsToMergedArea executed successfully.\r\n");
```

## **How to Import Data into Excel from DataTable**

To import data from a *DataTable*, call the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#cells) collection's [**importDataTable**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/importdatatable/index) method. There are many overloaded versions of the [**importDataTable**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/importdatatable/index) method but a typical overload takes the following parameters:

- **Data table**, the *DataTable* object that you're importing the content from.
- **Is field name shown**, specifies whether the names of the *DataTable* columns should be imported to the worksheet as a first row or not.
- **Start cell**, represents the name of the start cell (for example "A1") from where to import the contents of the *DataTable*.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
const fs = require("fs");
if (!fs.existsSync(dataDir)){
    fs.mkdirSync(dataDir);
}

// Instantiating a Workbook object            
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Instantiating a "Products" DataTable object
const dataTable = {
    name: "Products",
    columns: [
        { name: "Product ID", type: "Int32" },
        { name: "Product Name", type: "string" },
        { name: "Units In Stock", type: "Int32" },
    ],
    rows: []
};

// Adding data to the DataTable object
dataTable.rows.push([1, "Aniseed Syrup", 15]);
dataTable.rows.push([2, "Boston Crab Meat", 123]);

const tableOptions = new AsposeCells.ImportTableOptions();
// Importing the contents of DataTable to the worksheet starting from "A1" cell,
// Where true specifies that the column names of the DataTable would be added to
// The worksheet as a header row
tableOptions.setFieldNameShown(true);
worksheet.getCells().importTable(dataTable.rows, 0, 0, tableOptions);

// Saving the Excel file
workbook.save(path.join(dataDir, "DataImport.out.xls"));
```

## **How to Import Data into Excel from dynamic object as data source**

Aspose.Cells provides features to work with dynamic objects as a datasource. It helps in using datasource where properties are added dynamically to the objects. Once the properties are added to the object, Aspose.Cells considers the first entry as the template and handles the rest accordingly. It means if some dynamic property is added to a first item only and not to other objects, Aspose.Cells considers that all items in the collection should be the same.

In this example, a template model is used which initially contains two variables only. This List is converted to a List of dynamic objects. Then some additional field is added into it and finally loaded into the workbook. The workbook picks only those values which are in the template XLSX file. This template workbook uses Smart Markers which also contain parameters. Parameters allow you to modify how the information is laid out. Details about the Smart Markers can be obtained from the following article:

[Using Smart Markers](/cells/nodejs-cpp/using-smart-markers/)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class ImportingFromDynamicDataTable {
    static sourceDir = RunExamples.Get_SourceDirectory();
    static outputDir = RunExamples.Get_OutputDirectory();

    static async run() {
        // Here data is filled into a list of Model class containing two fields only
        const data = this.getData();

        // Based upon business some additional fields e.g. unique id is added
        const modifiedData = new Converter().getModifiedData(data);

        // Modified data is still an object but it is a dynamic one now
        modifiedData[0].Id = 20;

        // Following field is added in the dynamic objects list, but it will not be added to workbook as template file does not have this field
        modifiedData[0].Id2 = 200;

        // Create workbook and fill it with the data
        const workbook = new AsposeCells.Workbook(path.join(this.sourceDir, "ExcelTemplate.xlsx"));
        const designer = new AsposeCells.WorkbookDesigner(workbook);
        designer.setDataSource("modifiedData", modifiedData);
        designer.process();
        await designer.workbook.saveAsync(path.join(this.outputDir, "ModifiedData.xlsx"));

        // Base Model does work but doesn't have the Id
        const workbookRegular = new AsposeCells.Workbook(path.join(this.sourceDir, "ExcelTemplate.xlsx"));
        const designerRegular = new AsposeCells.WorkbookDesigner(workbookRegular);
        designerRegular.setDataSource("ModifiedData", data);
        designerRegular.process();
        await designerRegular.workbook.saveAsync(path.join(this.outputDir, "ModifiedDataRegular.xlsx"));
    }

    static getData() {
        return [
            { Code: 1, Name: "One" },
            { Code: 2, Name: "Two" },
            { Code: 3, Name: "Three" },
            { Code: 4, Name: "Four" },
            { Code: 5, Name: "Five" }
        ];
    }
}

class Converter {
    _uniqueNumber = 0;

    getModifiedData(data) {
        const result = [];

        result.push(...data.map(item => this.addId(item)));

        return result;
    }

    addId(item) {
        const result = this.transformToDynamic(item);
        result.Id = this.getUniqueNumber();
        return result;
    }

    getUniqueNumber() {
        const result = this._uniqueNumber;
        this._uniqueNumber++;
        return result;
    }

    transformToDynamic(dataObject) {
        const expando = {};

        for (const property of Object.keys(dataObject)) {
            expando[property] = dataObject[property];
        }

        return expando;
    }
}
```

## **How to Import DataColumn into Excel**

A *DataTable* or *DataView* object is composed of one or more columns. Developers can also import data from any Column/Columns of the *DataTable* or *DataView* by calling the [**importData**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/importdata/index) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#cells) collection. The [**importData**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/importdata/index) method accepts a parameter of type [**ImportTableOptions**](https://reference.aspose.com/cells/nodejs-cpp/importtableoptions). The [**ImportTableOptions**](https://reference.aspose.com/cells/nodejs-cpp/importtableoptions) class provides a [**columnIndexes**](https://reference.aspose.com/cells/nodejs-cpp/importtableoptions/#columnIndexes) property that accepts an array of columns indexes.

The sample code given below demonstrates the use of [**ImportTableOptions.columnIndexes**](https://reference.aspose.com/cells/nodejs-cpp/importtableoptions/#columnIndexes) to import selective columns.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
if (!require("fs").existsSync(dataDir)) {
    require("fs").mkdirSync(dataDir);
}

// Instantiating a "Products" DataTable object
const dataTable = new AsposeCells.DataTable("Products");

// Adding columns to the DataTable object
dataTable.getColumns().add("Product ID", AsposeCells.Int32);
dataTable.getColumns().add("Product Name", AsposeCells.String);
dataTable.getColumns().add("Units In Stock", AsposeCells.Int32);

// Creating an empty row in the DataTable object
let dr = dataTable.newRow();

// Adding data to the row
dr[0] = 1;
dr[1] = "Aniseed Syrup";
dr[2] = 15;

// Adding filled row to the DataTable object
dataTable.getRows().add(dr);

// Creating another empty row in the DataTable object
dr = dataTable.newRow();

// Adding data to the row
dr[0] = 2;
dr[1] = "Boston Crab Meat";
dr[2] = 123;

// Adding filled row to the DataTable object
dataTable.getRows().add(dr);

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

const sheet = book.getWorksheets().get(0);

// Create import options
const importOptions = new AsposeCells.ImportTableOptions();
importOptions.setIsFieldNameShown(true);
importOptions.setIsHtmlString(true);

// Importing the values of 2nd column of the data table
sheet.getCells().importData(dataTable, 1, 1, importOptions);

// Save workbook
book.save(path.join(dataDir, "DataImport.out.xls"));
```

## **How to Import DataView into Excel**

To import data from a *DataView*, call the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#cells) collection's [**importData**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/importdata/index) method. There are many overloaded versions of the [**importData**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/importdata/index) method but the one for DataView takes the following parameters:

- **DataView:** The *DataView* object that you're about to import content from.
- **First Row:** the row number of the first cell that the data will be imported to.
- **First Column:** the column number of the first cell that the data will be imported to.
- **ImportTableOptions:** The import options.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Obtaining the reference of the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Instantiating a "Products" DataTable object
const dataTable = new AsposeCells.DataTable("Products");

// Adding columns to the DataTable object
dataTable.getColumns().add("Product ID", AsposeCells.Type.Int32);
dataTable.getColumns().add("Product Name", AsposeCells.Type.String);
dataTable.getColumns().add("Units In Stock", AsposeCells.Type.Int32);

// Creating an empty row in the DataTable object
let dr = dataTable.newRow();

// Adding data to the row
dr.set(0, 1);
dr.set(1, "Aniseed Syrup");
dr.set(2, 15);

// Adding filled row to the DataTable object
dataTable.getRows().add(dr);

// Creating another empty row in the DataTable object
dr = dataTable.newRow();

// Adding data to the row
dr.set(0, 2);
dr.set(1, "Boston Crab Meat");
dr.set(2, 123);

// Adding filled row to the DataTable object
dataTable.getRows().add(dr);

// Importing the contents of the data view to the worksheet
const options = new AsposeCells.ImportTableOptions();
options.setIsFieldNameShown(true);

worksheet.getCells().importData(dataTable.getDefaultView(), 0, 0, options);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **How to Import DataGrid into Excel**

It is possible to import data from a *DataGrid* by calling the [**importDataGrid**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/importdatagrid/index) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#cells) collection. There are many overloaded versions of the [**importDataGrid**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/importdatagrid/index) method but a typical overload takes the following parameters:

- **Data grid**, the *DataGrid* object that you're importing content from.
- **Row Number**, the row number of the first cell that the data will be imported to.
- **Column Number**, the column number of the first cell that the data will be imported to.
- **Insert Rows**, a Boolean property that indicates whether extra rows should be added to the worksheet to fit data or not.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create a DataTable object
const dataTable = {
    name: "Products",
    columns: [
        { name: "Product ID", type: "Int32" },
        { name: "Product Name", type: "string" },
        { name: "Units In Stock", type: "Int32" }
    ],
    rows: []
};

// Adding rows to the DataTable
dataTable.rows.push([1, "Aniseed Syrup", 15]);
dataTable.rows.push([2, "Boston Crab Meat", 123]);

// Now take care of DataGrid
const dg = {
    dataSource: dataTable.rows
};

// We have a DataGrid object with some data in it.
// Lets import it into our spreadsheet

// Create a new workbook
const worksheet = workbook.getWorksheets().get(0);

// Importing the contents of the data grid to the worksheet
worksheet.getCells().importDataGrid(dg, 0, 0, false);

// Save it as Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```

## **How to Import GridView into Excel**

To import data from a *GridView* control, call the [**importGridView**](https://reference.aspose.com/cells/nodejs-cpp/cells/methods/importgridview) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#cells) collection.

Aspose.Cells allows us to respect HTML formatted values while importing data to the spreadsheet. When HTML parsing is enabled while importing data, Aspose.Cells converts the HTML into corresponding cell formatting.

## **How to Import HTML formatted data into Excel**

Aspose.Cells provides a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) class that provides very useful methods for importing data from external data sources. This article shows how to parse HTML formatted text while importing data and convert the HTML into formatted cell values.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const output1Path = path.join(dataDir, "Output.out.xlsx");
const output2Path = path.join(dataDir, "Output.out.ods");

// Prepare a DataTable with some HTML formatted values
const dataTable = new AsposeCells.DataTable("Products");
dataTable.getColumns().add("Product ID", AsposeCells.Int32);
dataTable.getColumns().add("Product Name", AsposeCells.String);
dataTable.getColumns().add("Units In Stock", AsposeCells.Int32);

let dr = dataTable.newRow();
dr.set(0, 1);
dr.set(1, "<i>Aniseed</i> Syrup");
dr.set(2, 15);
dataTable.getRows().add(dr);

dr = dataTable.newRow();
dr.set(0, 2);
dr.set(1, "<b>Boston Crab Meat</b>");
dr.set(2, 123);
dataTable.getRows().add(dr);

// Create import options
const importOptions = new AsposeCells.ImportTableOptions();
importOptions.setIsFieldNameShown(true);
importOptions.setIsHtmlString(true);

// Create workbook
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().importData(dataTable, 0, 0, importOptions);
worksheet.autoFitRows();
worksheet.autoFitColumns();

workbook.save(output1Path);
workbook.save(output2Path);
```

## **How to Import Data into Excel from JSON**

Aspose.Cells provides a [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/utilities/jsonutility) class for processing JSON. The [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/utilities/jsonutility) class has an [**importData**](https://reference.aspose.com/cells/nodejs-cpp/utilities/jsonutility/methods/importdata) method for importing JSON data. Aspose.Cells also provides a [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/utilities/jsonlayoutoptions) class that represents the options of JSON layout. The [**importData**](https://reference.aspose.com/cells/nodejs-cpp/utilities/jsonutility/methods/importdata) method accepts [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/utilities/jsonlayoutoptions) as a parameter. The [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/utilities/jsonlayoutoptions) class provides the following properties:

- [**arrayAsTable**](https://reference.aspose.com/cells/nodejs-cpp/utilities/jsonlayoutoptions/#arrayAsTable): Indicates if the array should be processed as a table or not.
- [**convertNumericOrDate**](https://reference.aspose.com/cells/nodejs-cpp/utilities/jsonlayoutoptions/#convertNumericOrDate): Gets or sets a value that indicates whether the string in JSON is to be converted to numeric or date.
- [**dateFormat**](https://reference.aspose.com/cells/nodejs-cpp/utilities/jsonlayoutoptions/#dateFormat): Gets and sets the format of the date value.
- [**ignoreArrayTitle**](https://reference.aspose.com/cells/nodejs-cpp/utilities/jsonlayoutoptions/#ignoreArrayTitle): Indicates whether to ignore the title if the property of the object is an array.
- [**ignoreNull**](https://reference.aspose.com/cells/nodejs-cpp/utilities/jsonlayoutoptions/#ignoreNull): Indicates whether the null value should be ignored or not.
- [**ignoreObjectTitle**](https://reference.aspose.com/cells/nodejs-cpp/utilities/jsonlayoutoptions/#ignoreObjectTitle): Indicates whether to ignore the title if the property of the object is an object.
- [**numberFormat**](https://reference.aspose.com/cells/nodejs-cpp/utilities/jsonlayoutoptions/#numberFormat): Gets and sets the format of numeric value.
- [**titleStyle**](https://reference.aspose.com/cells/nodejs-cpp/utilities/jsonlayoutoptions/#titleStyle): Gets and sets the style of the title.

The sample code given below demonstrates the use of the [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/utilities/jsonutility) and [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/utilities/jsonlayoutoptions) classes to import JSON data.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Read File
const fs = require("fs");
const jsonInput = fs.readFileSync(path.join(dataDir, "Test.json"), "utf-8");

// Set Styles
const factory = new AsposeCells.CellsFactory();
const style = factory.createStyle();
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
style.getFont().setColor(AsposeCells.Color.BlueViolet);
style.getFont().setIsBold(true);

// Set JsonLayoutOptions
const options = new AsposeCells.JsonLayoutOptions();
options.setTitleStyle(style);
options.setArrayAsTable(true);

// Import JSON Data
AsposeCells.JsonUtility.importData(jsonInput, worksheet.getCells(), 0, 0, options);

// Save Excel file
workbook.save(path.join(dataDir, "ImportingFromJson.out.xlsx"));
```

## **Advance topics**
- [Specify Formula Fields while Importing Data to Worksheet](/cells/nodejs-cpp/specify-formula-fields-while-importing-data-to-worksheet/)
- [Shift First Row down when inserting Cells Data Table Rows](/cells/nodejs-cpp/shift-first-row-down-when-inserting-cells-data-table-rows/)
