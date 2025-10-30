---
title: Länka celler till XML kart element med Node.js via C++
linktitle: Länka celler till XML kartelement
type: docs
weight: 50
url: /sv/nodejs-cpp/link-cells-to-xml-map-elements/
---

## **Möjliga användningsscenario**

Du kan länka dina celler till XML-kart element med hjälp av Aspose.Cells for Node.js via C++. Använd metoden [**Cells.linkToXmlMap(string, number, number, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#linkToXmlMap-string-number-number-string-) för detta ändamål.

## **Länka celler till XML-kartelement**

Följande exempelkod laddar den [käll-excel-filen](5115471.xlsx) som innehåller XML-karta och länkar sedan celler A1, B2, C3, D4, E5 och F6 till XML-kartelementen FIELD1, FIELD2, FIELD4, FIELD5 och FIELD7 respektive och sparar sedan arbetsboken som [utdata-excelfil](5115467.xlsx).

Om du öppnar [utdata excel-filen](5115467.xlsx) och klickar på Developer > Source-knappen, kommer du att se att cellerna är länkade med XML-kartelement och de kommer också att markeras av Microsoft Excel som visas på bilden.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
