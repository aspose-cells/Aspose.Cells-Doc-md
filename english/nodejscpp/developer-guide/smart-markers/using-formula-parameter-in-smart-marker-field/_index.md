---
title: Using Formula parameter in Smart Marker field with Node.js via C++
linktitle: Using Formula parameter in Smart Marker field
type: docs
weight: 40
url: /nodejs-cpp/using-formula-parameter-in-smart-marker-field/
description: Learn how to embed formulas in smart marker fields using Aspose.Cells for Node.js via C++. 
keywords: Smart Marker field formula parameter Node.js via C++, Embed formula smart marker Node.js via C++ 
---

## **Possible Usage Scenarios**
Sometimes, you want to embed a formula in the smart marker field. This article describes how to make use of the *Formula* parameter to embed a formula in the smart marker field.

## **Using Formula parameter in Smart Marker field**
The following sample code embeds the formula in the smart marker field named TestFormula and its data source name is MyDataSource, so the complete field with the formula parameter looks like `&=MyDataSource.TestFormula(formula)`, and after the execution of the code, the [final output Excel file](46465047.xlsx) will have formulas in cells from A1 till A5.

## **Sample Code**
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a data table and add column named TestFormula
const dt = {
    TableName: "MyDataSource",
    Rows: []
};

// Create first row with formula (which basically concatenates three strings)
dt.Rows.push({ TestFormula: "=\"01-This \" & \"is \" & \"concatenation\"" });

// Create second row like above
dt.Rows.push({ TestFormula: "=\"02-This \" & \"is \" & \"concatenation\"" });

// Create third row like above
dt.Rows.push({ TestFormula: "=\"03-This \" & \"is \" & \"concatenation\"" });

// Create fourth row like above
dt.Rows.push({ TestFormula: "=\"04-This \" & \"is \" & \"concatenation\"" });

// Create fifth row like above
dt.Rows.push({ TestFormula: "=\"05-This \" & \"is \" & \"concatenation\"" });

// Create a workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Put the smart marker field with formula parameter in cell A1
ws.getCells().get("A1").putValue("&=MyDataSource.TestFormula(Formula)");

// Create workbook designer, set data source and process it
const wd = new AsposeCells.WorkbookDesigner(wb);
wd.setDataSource(dt);
wd.process();

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "outputUsingFormulaParameterInSmartMarkerField.xlsx"));
```
