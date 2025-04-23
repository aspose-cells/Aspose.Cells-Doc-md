---
title: Enkel metod för diagramuppsättning med Chart.SetChartDataRange metoden med Node.js via C++
linktitle: Enkel metod för diagraminställning med hjälp av Chart.SetChartDataRange metoden
description: Lär dig hur du enkelt ställer in diagram med hjälp av Chart.SetChartDataRange metoden i Aspose.Cells for Node.js via C++. Vår guide visar hur du specificerar dataintervallet för ditt diagram, vilket gör att du kan skapa professionella och exakta diagram med minimal ansträngning.
keywords: Aspose.Cells for Node.js via C++, diagram, SetChartDataRange metod, dataintervall, professionell, exakt, diagram.
type: docs
weight: 190
url: /sv/nodejs-cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller nu [**Chart.setChartDataRange(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#setChartDataRange-string-boolean-)-metoden för att enkelt ställa in diagram. Genom att använda denna metod behöver du inte längre lägga till serie och kategoriaxel data separat.

{{% /alert %}}

Följande exempel kod förklarar användningen av [**Chart.setChartDataRange(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#setChartDataRange-string-boolean-)-metoden för att enkelt ställa in diagram.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbook
const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add data for chart

// Category Axis Values
worksheet.getCells().get("A2").putValue("C1");
worksheet.getCells().get("A3").putValue("C2");
worksheet.getCells().get("A4").putValue("C3");

// First vertical series
worksheet.getCells().get("B1").putValue("T1");
worksheet.getCells().get("B2").putValue(6);
worksheet.getCells().get("B3").putValue(3);
worksheet.getCells().get("B4").putValue(2);

// Second vertical series
worksheet.getCells().get("C1").putValue("T2");
worksheet.getCells().get("C2").putValue(7);
worksheet.getCells().get("C3").putValue(2);
worksheet.getCells().get("C4").putValue(5);

// Third vertical series
worksheet.getCells().get("D1").putValue("T3");
worksheet.getCells().get("D2").putValue(8);
worksheet.getCells().get("D3").putValue(4);
worksheet.getCells().get("D4").putValue(2);

// Create Column chart with easy way
const idx = worksheet.getCharts().add(AsposeCells.ChartType.Column, 6, 5, 20, 13);
const ch = worksheet.getCharts().get(idx);
ch.setChartDataRange("A1:D4", true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
