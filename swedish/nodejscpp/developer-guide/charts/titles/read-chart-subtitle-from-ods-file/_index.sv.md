---
title: Läs diagram underrubrik från ODS fil med Node.js via C++
linktitle: Läs diagramrubriken från en ODS fil
description: Lär dig hur du använder Aspose.Cells for Node.js via C++ för att läsa diagramets underrubrik från en OpenDocument Spreadsheet (ODS) fil. Vår guide visar hur du extraherar och får tillgång till diagramets underrubrik för vidare analys eller visning.
keywords: Aspose.Cells for Node.js via C++, Läsa diagram underrubrik, OpenDocument Spreadsheet, ODS fil, diagramutdrag, dataanalys.
type: docs
weight: 160
url: /sv/nodejs-cpp/read-chart-subtitle-from-ods-file/
---

## **Läs diagramunderrubrik från ODS-fil**

Aspose.Cells ger dig möjlighet att läsa diagram underrubriker i ODS-filer genom att använda egenskapen [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--). Följande exempel kod laddar [exempel ODS-fil](89620481.ods) och läser diagram underrubrik med egenskapen [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--) och skriver ut den i konsolfönstret. Se den givna kodens konsolutdata nedan för referens.

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Load excel file containing charts
const filePath = path.join(sourceDir, "SampleChart.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

console.log("Chart Subtitle: " + chart.getSubTitle().getText());
```

## **Konsoloutput**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
