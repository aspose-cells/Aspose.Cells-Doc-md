---
title: Lägg till pivottabelanslutning med Node.js via C++
linktitle: Lägg till pivottabellanslutning
type: docs
weight: 30
url: /sv/nodejs-cpp/add-pivot-connection/
description: Lär dig hur man lägger till pivottabelanslutning med Aspose.Cells for Node.js via C++.
keywords: Lägg till pivottabelanslutning utan Office 2013, Office 2016, Office 2019 och Office 365 med Node.js via C++.
---

## **Möjliga användningsscenario**

Om du vill koppla en slicer och pivottabell i Excel måste du högerklicka på slicern och välja "Rapportanslutningar...". I funktionslistan kan du operera på kryssrutan. På liknande sätt, om du vill koppla en slicer och pivottabell programmatiskt med Aspose.Cells API, använd [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#addPivotConnection-PivotTable-)-metoden. Det kommer att koppla slicern och pivottabellen.

## **Associera slicer och Pivottabell**

Följande exempel laddar [exempel-Excel-filen](add-pivot-connection.xlsx) som innehåller en befintlig slicer. Det kommer åt slicern och kopplar sedan slicern och pivottabellen. Slutligen sparar det arbetsboken som [utdata-Excel-fil](add-pivot-connection-out.xlsx).

## **Exempelkod**

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

// Adds PivotTable connection.
slicer.addPivotConnection(pivotTable);

workbook.save(path.join(dataDir, "add-pivot-connection-out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
