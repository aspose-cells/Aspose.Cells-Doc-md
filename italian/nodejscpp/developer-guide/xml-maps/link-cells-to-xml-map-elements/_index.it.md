---
title: Collega le celle agli elementi della mappa XML con Node.js tramite C++
linktitle: Collega le celle agli elementi della mappa XML
type: docs
weight: 50
url: /it/nodejs-cpp/link-cells-to-xml-map-elements/
---

## **Possibili Scenari di Utilizzo**

Puoi collegare le tue celle agli elementi della mappa XML usando Aspose.Cells for Node.js via C++. Utilizza il metodo [**Cells.linkToXmlMap(string, number, number, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#linkToXmlMap-string-number-number-string-) per questo scopo.

## **Collega le celle agli elementi della mappa XML**

Il seguente codice di esempio carica il [file Excel di origine](5115471.xlsx) che contiene la mappa XML e quindi collega le celle A1, B2, C3, D4, E5 e F6 agli elementi della mappa XML FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 e FIELD8 rispettivamente e quindi salva il workbook in [file Excel di output](5115467.xlsx).

Se si apre il [file Excel di output](5115467.xlsx) e si fa clic sul pulsante Sviluppatore > Origine, si vedrà che le celle sono collegate agli elementi della mappa XML e saranno anche evidenziate da Microsoft Excel come mostrato in questa immagine.

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
