---
title: Rich Text Anpassad Datalabel för Diagrampunkt med Node.js via C++
description: Lär dig hur du lägger till rika textanpassade datalabels till diagrampunkter i Aspose.Cells for Node.js via C++. Vår guide visar hur du formaterar etiketter med olika fonter, färger och justeringsalternativ för att förbättra utseendet och läsbarheten av dina diagram.
keywords: Aspose.Cells for Node.js via C++, diagram, rik text, anpassade datalabels, fonter, färger, justering, utseende, läsbarhet.
type: docs
weight: 10
url: /sv/nodejs-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för att skapa rik text anpassade datalabels för diagrampunkter. Aspose.Cells tillhandahåller metoden [**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#characters-number-number-) för att returnera [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting)-objektet som kan användas för att ställa in teckenfärger, fetstil etc.

{{% /alert %}}

## Anpassat riktmärke för diagram punkt

Följande kod kommer åt den första diagrampunkten i den första serien, ställer in dess text och sedan formaterar teckensnittet för de första 10 tecknen genom att ställa in dess färg till röd och fetstil till **true**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_custom_datalabel.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = worksheet.getCharts().get(0);

// Access the data label of first series first point
const dlbls = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

// Set data label text
dlbls.setText("Rich Text Label");

// Set the font setting of the first 10 characters
const fntSetting = dlbls.characters(0, 10);
fntSetting.getFont().setColor(AsposeCells.Color.Red);
fntSetting.getFont().setIsBold(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
