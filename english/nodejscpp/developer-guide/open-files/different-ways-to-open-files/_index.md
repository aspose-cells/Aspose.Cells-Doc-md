---
title: Different Ways to Open Files with Node.js via C++
linktitle: Different Ways to Open Files
type: docs
weight: 10
url: /nodejs-cpp/different-ways-to-open-files/
description: This article explains how to open an Excel file using Aspose.Cells for Node.js via C++ API.
keywords: Node.js Open an Excel file without Excel, How do I open an Excel File using Node.js.
---

{{% alert color="primary" %}}

With Aspose.Cells, it is simple to open files, for example, to retrieve data, or to use a designer template to speed up the development process.

{{% /alert %}}

## **How to Open an Excel File via a Path**

Developers can open a Microsoft Excel file using its file path on the local computer by specifying it in the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class constructor. Simply pass the path in the constructor as a *string*. Aspose.Cells will automatically detect the file format type.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(filePath);
console.log("Workbook opened using path successfully!");
```

## **How to Open an Excel File via a Stream**

It is also simple to open an Excel file as a stream. To do so, use an overloaded version of the constructor that takes the *Stream* object that contains the file.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book2.xls");
// Opening through Stream
// Create a Stream object
const fstream = fs.createReadStream(filePath);

// Creating a Workbook object, open the file from a Stream object
// That contains the content of file and it should support seeking
const chunks = [];
fstream.on('data', (chunk) => {
chunks.push(chunk);
```

## **How to Open a File with Data only**

To open a file with data only, use the [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) and [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) classes to set the related attributes and options of the classes for the template file to be loaded.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load only specific sheets with data and formulas
// Other objects, items etc. would be discarded

// Instantiate LoadOptions specified by the LoadFormat
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Set LoadFilter property to load only data & cell formatting
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), loadOptions);
console.log("File data imported successfully!");
```

## **How to Load Visible Sheets only**

While loading a [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), sometimes you may only need data in visible worksheets in a workbook. Aspose.Cells allows you to skip data in invisible worksheets while loading a workbook. To do this, create a custom function that inherits the [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) class and pass its instance to [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) property.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sampleFile = "output.xlsx";
const samplePath = path.join(dataDir, sampleFile);

// Create a sample workbook
// and put some data in first cell of all 3 sheets
const createWorkbook = new AsposeCells.Workbook();
createWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet2").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet3").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().get("Sheet3").setIsVisible(false);
createWorkbook.save(samplePath);

// Load the sample workbook
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setLoadFilter(new AsposeCells.LoadFilter()); // Corrected line by defining LoadFilter properly

const loadWorkbook = new AsposeCells.Workbook(samplePath, loadOptions);
console.log(`Sheet1: A1: ${loadWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A2: ${loadWorkbook.getWorksheets().get("Sheet2").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A3: ${loadWorkbook.getWorksheets().get("Sheet3").getCells().get("A1").getValue()}`);
```

Here is the implementation of the *CustomLoad* class referenced in the above snippet.

```javascript
const { Workbook, LoadDataFilterOptions } = require("aspose.cells.node");

class CustomLoad {
startSheet(sheet) {
if (sheet.isVisible()) {
// Load everything from visible worksheet
this.loadDataFilterOptions = LoadDataFilterOptions.All;
} else {
// Load nothing
this.loadDataFilterOptions = LoadDataFilterOptions.Structure;
}
}
}
```

{{% alert color="primary" %}}

An exception will be thrown if you try to open non-native Excel files or other file formats (for example PPT/PPTX, DOC/DOCX, etc.) using Aspose.Cells.

{{% /alert %}} 

{{% alert color="primary" %}}

There are fair chances that the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) constructor may throw *OutOfMemoryError* while loading large spreadsheets. This exception suggests that the available memory is insufficient to completely load the spreadsheet into memory; therefore, the spreadsheet has to be loaded while enabling the Memory Preferences.

{{% /alert %}}

