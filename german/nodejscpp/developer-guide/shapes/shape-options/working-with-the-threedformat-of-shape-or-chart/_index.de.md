---
title: Arbeiten mit dem ThreeDFormat von Form oder Diagramm mit Node.js über C++
linktitle: Arbeiten mit dem 3D Format von Form oder Diagramm
type: docs
weight: 250
url: /de/nodejs-cpp/working-with-the-threedformat-of-shape-or-chart/
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells for Node.js via C++ bietet die [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) Eigenschaft zusammen mit der [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) Klasse, um mit dem 3D-Format von Form oder Diagramm zu arbeiten. Die [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) Klasse enthält verschiedene Eigenschaften, die je nach Anwendungsanforderung eingestellt werden können.

## **Arbeiten mit dem ThreeDFormat von Shape oder Diagramm**
Der folgende Beispielcode lädt die [Quelldatei Excel](5115419.xlsx) und greift auf die erste Form im ersten Arbeitsblatt zu. Er setzt die Untereigenschaften der [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) Eigenschaft und speichert dann die Arbeitsmappe in der [Ausgabedatei Excel](5115410.xlsx).

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
