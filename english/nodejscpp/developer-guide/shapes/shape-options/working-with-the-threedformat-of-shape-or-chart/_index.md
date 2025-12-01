---
title: Working with the ThreeDFormat of Shape or Chart with Node.js via C++
linktitle: Working with the ThreeDFormat of Shape or Chart
type: docs
weight: 250
url: /nodejs-cpp/working-with-the-threedformat-of-shape-or-chart/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Aspose.Cells for Node.js via C++ provides the [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) property along with [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) class to work with the 3-D Format of shape or chart. The [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) class contains different properties which can be set to achieve different results as per application requirements.

## **Working with the ThreeDFormat of Shape or Chart**
The following sample code loads the [source excel file](5115419.xlsx) and accesses the first shape in the first worksheet and sets the sub-properties of [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) property and then saves the workbook in the [output excel file](5115410.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load excel file containing a shape
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first shape
const sh = ws.getShapes().get(0);

// Apply different three dimensional settings
const n3df = sh.getThreeDFormat();
n3df.setContourWidth(17);
n3df.setExtrusionHeight(32);

// Save the output excel file in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
