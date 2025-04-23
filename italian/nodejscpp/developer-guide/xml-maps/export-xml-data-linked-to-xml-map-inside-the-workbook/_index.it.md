---
title: Esporta i dati XML collegati alla mappa XML all’interno del workbook con Node.js tramite C++
linktitle: Esporta dati XML collegati alla mappa XML all interno del foglio di lavoro
type: docs
weight: 20
url: /it/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Impara come esportare i dati XML collegati alle mappe XML all’interno del tuo libro di lavoro usando Aspose.Cells for Node.js via C++. 
---

## **Esporta dati XML collegati alla mappa XML all'interno del Workbook**

Per favore, utilizza il metodo [**Workbook.exportXml()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#exportXml-string-) per esportare dati XML collegati alle tue Maps XML nel workbook. Il seguente codice di esempio esporta i dati XML di tutte le Maps XML dal workbook una per una. Controlla il [file Excel di esempio](5115497.xlsx) usato in questo codice e i [dati XML esportati della prima Map XML](5472487.xml).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Export all XML data from all XML Maps from the Workbook.
for (let i = 0; i < workbook.getWorksheets().getXmlMaps().getCount(); i++) {
// Access the XML Map.
const map = workbook.getWorksheets().getXmlMaps().get(i);

// Exports its XML Data to file.
workbook.exportXml(map.getName(), path.join(dataDir, `${map.getName()}.xml`));
}
```
