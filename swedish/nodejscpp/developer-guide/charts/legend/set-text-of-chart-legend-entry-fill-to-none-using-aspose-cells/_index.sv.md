---
title: Sätt texten för diagramlegenden till ingen med Aspose.Cells for Node.js via C++
linktitle: Ställ in text för diagrammets legendpostfyllnad till none med hjälp av Aspose.Cells
description: Lär dig att använda Aspose.Cells for Node.js via C++ för att sätta texten för ett diagramlegendar fyllning till ingen. Denna guide visar hur man modifierar fyllnadsfärgen på legendens poster i Microsoft Excel diagram för bättre visualisering och anpassning.
keywords: Aspose.Cells for Node.js via C++, Diagramlegendens Posterfyllning, Microsoft Excel, Visualisering, Anpassning.
type: docs
weight: 320
url: /sv/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Om du vill att texten på diagrammets legendarepresentant ska vara tom så att den inte visas inom diagramlegenden, ställ in [**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/nodejs-cpp/legendentry/#isTextNoFill--) till **true**.

{{% /alert %}}

Följande exempelkod ställer in texten för diagrammets andra legendpostfyllnad till none. Vänligen ladda ner den [exempelfil för Excel](5115219.xlsx) som används i denna kod och den [utfärdade Excelfilen](5115217.xlsx) som genererats av den som referens.

Följande skärmbild visar effekten av denna kod på den [exempelfilen i Excel](5115219.xlsx).

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Sample.xlsx"));

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = sheet.getCharts().get(0);

// Set text of second legend entry fill to none
chart.getLegend().getLegendEntries().get(1).setIsTextNoFill(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "ChartLegendEntry_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
