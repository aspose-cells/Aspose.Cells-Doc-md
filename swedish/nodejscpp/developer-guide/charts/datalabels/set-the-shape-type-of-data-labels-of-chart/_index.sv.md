---
title: Sätt Dataetikettformer för Diagram med Node.js via C++
linktitle: Ställ in datamärkenas formtyp i diagrammet
description: Lär dig hur du ställer in formtypen för datalabels i diagram med Aspose.Cells for Node.js via C++. Denna guide kommer att förklara de olika formtyper som finns tillgängliga och visa dig hur du väljer rätt form för dina datalabels för att förbättra presentationen och användbarheten.
keywords: Aspose.Cells for Node.js via C++, diagram, datalabels, formtyper, presentation, användbarhet.
type: docs
weight: 110
url: /sv/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Möjliga användningsscenario**
Du kan ändra formtypen för datalabels i diagrammet med egenskapen `DataLabels.shapeType`. Den tar värdet från `DataLabelShapeType`-enum och ändrar formen på datalabels därefter. Några av dess värden är

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **Ställ in datamärkenas formtyp i diagram**
Följande exempel ändrar formtypen för datalabels i diagrammet till `DataLabelShapeType.WedgeEllipseCallout`. Se gärna [exempel-Excel-filen](60489778.xlsx) som används i denna kod och den [utdata-Excel file](60489779.xlsx) som genereras av den. Skärmbilden visar hur koden påverkar exempel-Excel-filen.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Exempelkod**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetShapeTypeOfDataLabelsOfChart.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Access first series
const series = chart.getNSeries().get(0);

// Set the shape type of data labels i.e. Speech Bubble Oval
series.getDataLabels().setShapeType(AsposeCells.DataLabelShapeType.WedgeEllipseCallout);

// Save the output Excel file
workbook.save(path.join(dataDir, "outputSetShapeTypeOfDataLabelsOfChart.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
