---
title: Inaktivera textomslag för datalabels i diagram med Node.js via C++
description: Lär dig hur du inaktiverar textomslag för datalabels i diagram med hjälp av Aspose.Cells for Node.js via C++. Vår guide visar hur du förhindrar att långa etiketter överlappar och ger mer läsbara och tydliga diagram.
keywords: Aspose.Cells for Node.js via C++, diagram, datalabels, textomslag, överlappning, läsbarhet, visningar.
type: docs
weight: 70
url: /sv/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 tillåter användare att vicka eller avvicka text inne i dataetiketterna för diagrammet. Som standard är texten inne i dataetiketterna för diagrammet i det vikta läget.

Aspose.Cells tillhandahåller en [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#isTextWrapped--) egenskap som du kan ställa in till true eller false för att aktivera eller inaktivera textomslag av datalabels respektive.

{{% /alert %}}

Nedanstående kodexempel visar hur du inaktiverar textvaggning för dataetiketterna i diagrammet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_wrap_label.xlsx");
// Load the sample Excel file inside the workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Disable the Text Wrapping of Data Labels in all Series
chart.getNSeries().get(0).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(1).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(2).getDataLabels().setIsTextWrapped(false);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```
