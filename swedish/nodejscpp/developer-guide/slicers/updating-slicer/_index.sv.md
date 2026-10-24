---
title: Uppdatera en slicer med Node.js via C++
linktitle: Uppdatera en slicer
type: docs
weight: 50
url: /sv/nodejs-cpp/updating-slicer/
description: Den här artikeln visar hur man uppdaterar en slicer för att filtrera data i den länkade pivottabellen eller tabellen med Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells Node.js via C++, Uppdatera slicer Node.js, hur man ändrar slicern Node.js, hur man filtrerar en pivottabell med slicer i Node.js, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Att uppdatera en slicer innebär att filtrera data i pivottabellen eller tabellen som slicern är kopplad till. När du markerar eller avmarkerar slicerobjekt i Microsoft Excel beräknas den länkade pivottabellen eller tabellen om därefter. Med Aspose.Cells for Node.js via C++ behöver du inte iterera över slicer-cacheobjekten och uppdatera slicern manuellt — metoden [**Slicer.selectItems(labels, append)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/) uppdaterar slicern och beräknar om den länkade pivottabellen eller tabellen direkt från filterobjekten:
- `Slicer.selectItems(labels, append)` — markerar de angivna etiketterna och beräknar om den länkade pivottabellen eller tabellen. När `append` är `true` behålls de ursprungligen markerade etiketterna och de angivna etiketterna läggs till i urvalet; när `append` är `false` rensas alla ursprungliga markeringar och endast de angivna etiketterna förblir markerade.
- `Slicer.unselectItems(labels)` — avmarkerar en del av de för närvarande markerade objekten.
- `Slicer.clearFilter()` — tar bort filtret och markerar alla objekt.

{{% alert color="primary" %}}
Från och med Aspose.Cells for Node.js via C++ 26.10 blir egenskapen `SlicerCacheItem.Selected` skrivskyddad och dess setter stöds inte längre. Använd metoderna `Slicer.selectItems`, `Slicer.unselectItems` och `Slicer.clearFilter` istället för att sätta `SlicerCacheItem.Selected` objekt för objekt.
{{% /alert %}}

## **Hur man uppdaterar en slicer**
Följande exempelkod laddar [exempel-Excel-filen](67338475.xlsx) som innehåller en befintlig slicer som är kopplad till en pivottabell. Den markerar endast objekten "Blue" och "Pink" i slicern med `Slicer.selectItems(labels, false)` — pivottabellen beräknas om direkt från filterobjekten, utan ett manuellt anrop av `Slicer.refresh()`. Därefter sparas arbetsboken som [utdata-Excel-filen](67338476.xlsx). Skärmbilden nedan visar effekten av exempelkoden på exempel-Excel-filen. Som du kan se på skärmbilden visar pivottabellen endast de filtrerade objekten.
![todo:image_alt_text](updating-slicer_1.png)

## **Exempelkod**
Ersätt den aktuella markeringen (endast de angivna etiketterna förblir markerade) och beräkna om den länkade pivottabellen eller tabellen:

```javascript
const AsposeCells = require("aspose.cells.node");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const ws = wb.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.selectItems(["Blue", "Pink"], false);
// Save the modified workbook.
wb.save("out.xlsx");
```

Behåll de för närvarande markerade etiketterna och markera ytterligare objekt:

```javascript
const AsposeCells = require("aspose.cells.node");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const ws = wb.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);
// Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], true);
```

Avmarkera en del av de markerade objekten:

```javascript
const AsposeCells = require("aspose.cells.node");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const ws = wb.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);
// Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"]);
```

Ta bort filtret (markera alla objekt):

```javascript
const AsposeCells = require("aspose.cells.node");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const ws = wb.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="nodejs-cpp" >}}