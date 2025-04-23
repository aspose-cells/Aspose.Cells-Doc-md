---
title: Sätt värdeformatkod för diagramserie med Node.js via C++
description: Lär dig hur du ställer in värdeformatkoden för diagramserie i Aspose.Cells for Node.js via C++. Denna guide hjälper dig att förstå hur du formaterar din diagramseriedata med lämplig formatkod, så att du kan presentera dina data noggrant och professionellt.
keywords: Aspose.Cells för Node.js, diagramserie, värdeformatkod, formatering, data presentation, noggrannhet, professionalitet.
linktitle: Nummerformat
type: docs
weight: 100
url: /sv/nodejs-cpp/set-the-values-format-code-of-chart-series/
---

## **Möjliga användningsscenario**
Du kan ställa in värdeformatkoden för diagramserie med hjälp av [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--) egenskapen. Denna egenskap är inte bara användbar för serier baserade på området inom kalkylbladet, utan fungerar också bra för serier skapade med en array av värden.

## **Ställ in värdenas formatkod för diagramserier**
Följande exempel kod lägger till en serie i ett tomt diagram som inte hade någon serie tidigare. Det lägger till serien med hjälp av en värdelista. När serien är tillagd, formateras den med kodet $#,##0 med hjälp av egenskapen [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--), och talet 10000 blir $10,000. Skärmbilden visar effekten av koden på [sample Excel file](51740712.xlsx) och [output Excel file](51740713.xlsx) efter körning.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Exempelkod**
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "51740712.xlsx");

// Load the source Excel file 
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Add series using an array of values
chart.getNSeries().add("{10000, 20000, 30000, 40000}", true);

// Access the series and set its values format code
const series = chart.getNSeries().get(0);
series.setValuesFormatCode("$#,##0");

// Save the output Excel file
workbook.save(path.join(dataDir, "51740713.xlsx"));
```
