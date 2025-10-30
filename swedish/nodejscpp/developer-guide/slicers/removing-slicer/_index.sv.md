---
title: Ta bort slicer med Node.js via C++
linktitle: Ta bort slicer
type: docs
weight: 30
url: /sv/nodejs-cpp/removing-slicer/
---

## **Möjliga användningsscenario**

Om du vill ta bort en slicer i Excel, välj den och tryck på *Delete*-knappen. På liknande sätt, om du vill ta bort den programatiskt med Aspose.Cells API, använd [**SlicerCollection.remove(Slicer)**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#remove-slicer-)-metoden. Det tar bort slicern från kalkylbladet.

## **Ta bort slicer**

Följande exempel laddar [exempel-Excel-filen](67338478.xlsx) som innehåller en befintlig slicer. Det kommer åt slicern och tar bort den. Slutligen sparar det arbetsboken som [utdata-Excel-fil](67338477.xlsx). Föreställningen nedan visar slicern som kommer att tas bort efter utförandet av exempel-koden.

![todo:image_alt_text](removing-slicer_1.png)

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRemovingSlicer.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Remove slicer.
worksheet.getSlicers().remove(slicer);

// Save the workbook in output XLSX format.
workbook.save("outputRemovingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
