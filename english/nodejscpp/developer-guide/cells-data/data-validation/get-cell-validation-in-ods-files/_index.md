---  
title: Get Cell Validation in ODS Files with Node.js via C++  
type: docs  
weight: 180  
url: /nodejs-cpp/get-cell-validation-in-ods-files/  
description: Learn how to Get Cell Validation in ODS Files through the Aspose.Cells for Node.js via C++ API.  
keywords: Get Cell Validation Node.js via C++, Obtain Cell Validation Node.js via C++  
---  

## **Get Cell Validation in ODS Files**  

With Aspose.Cells for Node.js via C++, you can get the validation applied to a cell in ODS files. For this, the API provides the [**getValidation**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getvalidation) method of the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell/) class.  

The following code sample demonstrates the use of the [**getValidation**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getvalidation) method by loading the [source ODS](101089354.ods) file and reading the validation of the cell A9.  

### **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleBook1.ods"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

const cell = worksheet.getCells().get("A9");

if (cell.getValidation() !== null) {
    console.log(cell.getValidation().getType());
}
```  
  