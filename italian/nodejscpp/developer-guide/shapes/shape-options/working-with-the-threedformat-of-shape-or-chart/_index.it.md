---
title: Lavorare con il formato 3D di forma o grafico con Node.js tramite C++
linktitle: Lavorare con il ThreeDFormat della forma o del grafico
type: docs
weight: 250
url: /it/nodejs-cpp/working-with-the-threedformat-of-shape-or-chart/
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells for Node.js via C++ fornisce la proprietà [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) insieme alla classe [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) per lavorare con il formato 3D di forma o grafico. La classe [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) contiene diverse proprietà che possono essere impostate per ottenere risultati diversi in base alle esigenze dell'applicazione.

## **Lavorare con il ThreeDFormat della forma o del grafico**
Il seguente esempio di codice carica il [file excel di origine](5115419.xlsx) e accede alla prima forma nel primo foglio di lavoro e imposta le sotto-proprietà della proprietà [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) e quindi salva il workbook nel [file excel di output](5115410.xlsx).

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
