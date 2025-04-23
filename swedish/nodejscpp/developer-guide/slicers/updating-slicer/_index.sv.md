---
title: Uppdatera slicer med Node.js via C++
linktitle: Uppdatera slicer
type: docs
weight: 50
url: /sv/nodejs-cpp/updating-slicer/
description: Den här artikeln visar hur man uppdaterar länkade pivottabeller genom att uppdatera slicer med Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells Node.js via C++, Uppdatera slicer Node.js, hur man ändrar slicern Node.js, hur man justerar slicern i Node.js, hur man väljer eller avmarkerar slicerobjekt i Node.js via C++.
---

## **Möjliga användningsscenario**

Om du vill uppdatera en slicer i Microsoft Excel, välj eller avmarkera dess objekt, och den kommer då att uppdatera slicer-tabellen eller pivottabellen i enlighet därmed. Använd gärna [**Slicer.getSlicerCacheItems()**](https://reference.aspose.com/cells/nodejs-cpp/slicercache/#getSlicerCacheItems--) för att välja eller avmarkera slicer-objekt med Aspose.Cells och kalla sedan på [**Slicer.refresh()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#refresh--)-metoden för att uppdatera slicer-tabellen eller pivottabellen.

## **Hur man uppdaterar snittet**

Följande exempelkod laddar [provmappen](67338475.xlsx) som innehåller en befintlig snitt. Den avmarkerar den 2:a och 3:e objekten i snittet och uppdaterar snittet sedan. Den sparar sedan arbetsboken som [utmatningsmapp](67338476.xlsx). Skärmbilden nedan visar effekten av exempelkoden på provmappen. Som du kan se på skärmbilden, har uppdateringen av snittet med markerade objekt också uppdaterat pivottabellen.

![todo:image_alt_text](updating-slicer_1.png)

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleUpdatingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Access the slicer items.
const scItems = slicer.getSlicerCache().getSlicerCacheItems();

const items = slicer.getSlicerCache().getSlicerCacheItems();

for (let i = 0; i < items.getCount(); i++) {
const item = items.get(i);
if (item.getValue() === "Pink" || item.getValue() === "Green") {
item.setSelected(false);
}
}
slicer.refresh();
wb.save("out.xlsx");
```
