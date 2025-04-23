---  
title: Hantera DataLabels för Excel diagram med Node.js via C++  
description: Lär dig hur man effektivt hanterar datamärkningar i Excel diagram med Aspose.Cells for Node.js via C++. Denna omfattande guide täcker olika hanteringsuppgifter, inklusive att lägga till, ta bort och modifiera etiketter för att förbättra diagramläsbarhet och användbarhet.  
keywords: Aspose.Cells för Node.js, Excel diagram, datamärkningar, hantering, läsbarhet, användbarhet, lägga till, ta bort, modifiera.  
linktitle: Datamärken  
type: docs  
weight: 50  
url: /sv/nodejs-cpp/insert-datalabels-to-chart/  
---  

{{% alert color="primary" %}}  

Datamärken är en viktig del av ett diagram.  
Vi kan enkelt känna till värdet, procenten, etc. av varje serie.  

{{% /alert %}}  

## **Datamärkenalternativ**  
Aspose.Cells for Node.js via C++ tillåter också att hantera diagrammets datamärkningar vid körning, med {DataLabels}-objektet, det är enkelt att flytta, uppdatera och formatera datamärkningarna för diagrammet.  

|![todo:image_alt_text](chart_datalabels.png)|  

## **Hantera datamärken för diagram**  
Det är enkelt att hantera datamärkningar för diagrammet med Aspose.Cells [DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/).  

Följande kodavsnitt visar hur man hanterar DataLabels:  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Show value labels
chart.getNSeries().get(0).getDataLabels().setShowValue(true);
// Show series name labels
chart.getNSeries().get(1).getDataLabels().setShowSeriesName(true);
// Move labels to center
chart.getNSeries().get(1).getDataLabels().setPosition(AsposeCells.LabelPositionType.Center);

// Save the file
workbook.save("chart_datalabels.xlsx");
```  

## **Fortsatta ämnen**  
- [Lägg till anpassade etiketter till datapunkter i diagramserien](/cells/sv/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [Inaktivera textbrytning för datamärken på diagrammet](/cells/sv/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [Ändra diagrammets datamärkesform för att passa texten](/cells/sv/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [Riktextanpassade datamärken för diagrammet](/cells/sv/nodejs-cpp/rich-text-custom-data-label-of-chart-point/)  
- [Ställ in datamärkenas formtyp i diagram](/cells/sv/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [Visa cellområde som datamärken](/cells/sv/nodejs-cpp/showing-cell-range-as-the-data-labels/)  

