---
title: Add Pivot Connection with Node.js via C++
linktitle: Add Pivot Connection
type: docs
weight: 30
url: /nodejs-cpp/add-pivot-connection/
description: Learn how to add a pivot connection using Aspose.Cells for Node.js via C++.
keywords: Add pivot connection without Office 2013, Office 2016, Office 2019, and Office 365 using Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

If you want to associate a slicer and a pivot table in Excel, you need to right‑click the slicer and select the **"Report Connections..."** item. In the option list, you can check the box. Similarly, if you want to associate a slicer and a pivot table using the Aspose.Cells API programmatically, please use the [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#addPivotConnection-PivotTable-) method. It will associate the slicer and the pivot table.

## **Associate Slicer and PivotTable**

The following sample code loads the [sample Excel file](add-pivot-connection.xlsx) that contains an existing slicer. It accesses the slicer and then associates the slicer and pivot table. Finally, it saves the workbook as the [output Excel file](add-pivot-connection-out.xlsx).

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "add-pivot-connection.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0); 

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Add PivotTable connection.
slicer.addPivotConnection(pivotTable);

workbook.save(path.join(dataDir, "add-pivot-connection-out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
