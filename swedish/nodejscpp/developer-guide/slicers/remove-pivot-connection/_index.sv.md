---
title: Ta bort pivottabellanslutning med Node.js via C++
linktitle: Ta bort pivotkoppling
type: docs
weight: 30
url: /sv/nodejs-cpp/remove-pivot-connection/
description: Lär dig hur man tar bort pivottabellanslutning med Aspose.Cells for Node.js via C++.
keywords: Ta bort pivottabellanslutning utan Office 2013, Office 2016, Office 2019 och Office 365 med Node.js via C++.
---

## **Möjliga användningsscenario**

Om du vill lösgöra en slicer och pivottabell i Excel måste du högerklicka på slicern och välja "Rapportanslutningar...". I funktionslistan kan du operera på kryssrutan. På liknande sätt, om du vill lösgöra en slicer och pivottabell programmatiskt med Aspose.Cells API, använd [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#removePivotConnection-pivottable-)-metoden. Det kommer att lösgöra slicern och pivottabellen.

## **Bryt isär snitt och pivottabell**

Följande exempel laddar [exempel-Excel-filen](remove-pivot-connection.xlsx) som innehåller en befintlig slicer. Det kommer åt slicern och lösgör den från pivottabellen. Slutligen sparar det arbetsboken som [utdata-Excel-fil](remove-pivot-connection-out.xlsx).

## **Exempelkod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "remove-pivot-connection.xlsx");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Remove PivotTable connection.
slicer.removePivotConnection(pivotTable);
// Save the workbook in output XLSX format.
workbook.save(path.join(dataDir, "remove-pivot-connection-out.xlsx"));
``` 
