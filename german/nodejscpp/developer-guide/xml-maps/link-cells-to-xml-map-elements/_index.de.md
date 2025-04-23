---
title: Zellen mit XML Karten Elementen verlinken mit Node.js via C++
linktitle: Zellen mit XML Map Elementen verknüpfen
type: docs
weight: 50
url: /de/nodejs-cpp/link-cells-to-xml-map-elements/
---

## **Mögliche Verwendungsszenarien**

Sie können Ihre Zellen mit XML-Karten-Elementen mit Aspose.Cells for Node.js via C++ verlinken. Verwenden Sie hierfür die [**Cells.linkToXmlMap(string, number, number, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#linkToXmlMap-string-number-number-string-)-Methode.

## **Zellen mit XML-Map-Elementen verknüpfen**

Der folgende Beispielcode lädt die [Quell-Excel-Datei](5115471.xlsx), die eine XML-Map enthält, und verknüpft dann die Zellen A1, B2, C3, D4, E5 und F6 mit den XML-Map-Elementen FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 und FIELD8 und speichert anschließend die Arbeitsmappe in der [Ausgabe-Excel-Datei](5115467.xlsx).

Wenn Sie die [Ausgabe-Excel-Datei](5115467.xlsx) öffnen und auf die Schaltfläche Entwickler > Quelle klicken, sehen Sie, dass die Zellen mit XML-Map-Elementen verknüpft sind und sie auch von Microsoft Excel hervorgehoben werden, wie in diesem Bild gezeigt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-xml-map.xlsx"));

// Access the Xml Map inside it
const map = workbook.getWorksheets().getXmlMaps().get(0);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Map FIELD1 and FIELD2 to cell A1 and B2
ws.getCells().linkToXmlMap(map.getName(), 0, 0, "/root/row/FIELD1");
ws.getCells().linkToXmlMap(map.getName(), 1, 1, "/root/row/FIELD2");

// Map FIELD4 and FIELD5 to cell C3 and D4
ws.getCells().linkToXmlMap(map.getName(), 2, 2, "/root/row/FIELD4");
ws.getCells().linkToXmlMap(map.getName(), 3, 3, "/root/row/FIELD5");

// Map FIELD7 and FIELD8 to cell E5 and F6
ws.getCells().linkToXmlMap(map.getName(), 4, 4, "/root/row/FIELD7");
ws.getCells().linkToXmlMap(map.getName(), 5, 5, "/root/row/FIELD8");

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output.xlsx"));
```
