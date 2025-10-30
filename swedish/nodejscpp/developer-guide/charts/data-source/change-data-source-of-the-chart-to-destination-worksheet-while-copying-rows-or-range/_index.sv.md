---
title: Ändra datakälla för diagrammet till destinationsark medan du kopierar rader eller område med Node.js via C++
linktitle: Ändra datakällan för diagrammet till destinationskalkylbladet samtidigt som du kopierar rader eller område
description: Lär dig hur du ändrar datakällan för ett diagram till ett destinationsark medan du kopierar rader eller ett område i Aspose.Cells for Node.js via C++. Denna guide visar hur du uppdaterar diagrammets dataintervall och länkar det till destinationsarket.
keywords: Aspose.Cells for Node.js via C++, diagram, datakälla, destinationsblad, rader, område, kopiera, uppdatera, dataintervall, koppling.
type: docs
weight: 440
url: /sv/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Möjliga användningsscenario**

När du kopierar rader eller område som innehåller diagram till ett nytt blad, ändras inte datakällan för diagrammet. Till exempel, om datakällan för diagrammet är `=Sheet1!$A$1:$B$4`, kommer datakällan att förbli densamma, dvs `=Sheet1!$A$1:$B$4`, även efter kopiering. Den refererar fortfarande till det gamla bladet, dvs Sheet1. Detta är också beteendet i Microsoft Excel. Men om du vill att den ska referera till det nya destinationsbladet, använd då [**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--)-egendomen och ställ in den på **true** när du anropar [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-)-metoden. Om ditt destinationsblad är DestSheet, kommer datakällan för ditt diagram att ändras från `=Sheet1!$A$1:$B$4` till `=DestSheet!$A$1:$B$4`.

## **Ändra datakällan för diagrammet till destinationskalkylbladet samtidigt som du kopierar rader eller område**

Följande exempel kod förklarar användningen av [**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--)-egendomen vid kopiering av rader eller område som innehåller diagram till ett nytt blad. Koden använder filen [exempel Excel-fil](5113699.xlsx) och genererar [output Excel-fil](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load sample excel file
const wb = new AsposeCells.Workbook(filePath);

// Access the first sheet which contains chart
const source = wb.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = wb.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

// Save workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
