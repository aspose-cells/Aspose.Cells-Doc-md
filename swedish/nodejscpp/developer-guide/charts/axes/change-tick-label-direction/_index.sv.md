---
title: Ändra riktning för ticketiketter med Node.js via C++
linktitle: Ändra riktning för ticketiketter
description: Lär dig hur du ändrar riktningen på ticketiketter i Aspose.Cells för Node.js. Vår guide hjälper dig att förstå hur du justerar orienteringen av ticketiketter på axlar, inklusive horisontellt, vertikalt och vinklat.
keywords: Aspose.Cells för Node.js, ticketiketter, riktning, orientering, axlar, horisontell, vertikal, vinklad.
type: docs
weight: 170
url: /sv/nodejs-cpp/change-tick-label-direction/
---

## **Ändra riktning för ticketiketter**

Aspose.Cells ger dig möjlighet att ändra riktningen på diagrammets ticketiketter genom att använda egenskapen [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--). Egenskapen [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--) accepterar värdet för [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype) ENUMERATION. ENUMERATION [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype) innehåller följande medlemmar:

- Horisontell
- Vertikal
- Rotera 90
- Rotera 270
- Staplad

Följande bild jämför käll- och utdatafilerna

### **Källfilens bild**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Utdatasfilens bild**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Följande kodsnutt ändrar ticketikettens riktning från Rotera 90 till Horisontell.

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
const filePath = path.join(sourceDir, "SampleChangeTickLabelDirection.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Load the chart from source worksheet
const chart = worksheet.getCharts().get(0);

chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Horizontal);

// Output the file
workbook.save(path.join(outputDir, "outputChangeChartDataLableDirection.xlsx"));
```

Käll- och utdatafilerna kan laddas ned från följande länkar.

[Källfil](105480221.xlsx)

[Utdatasfil](105480223.xlsx)
{{< app/cells/assistant language="nodejs-cpp" >}}
