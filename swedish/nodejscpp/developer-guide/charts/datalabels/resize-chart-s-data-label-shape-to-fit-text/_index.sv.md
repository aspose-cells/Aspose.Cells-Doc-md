---  
title: Ändra storlek på diagrammets datalabelsform för att passa texten med Node.js via C++  
linktitle: Ändra diagrammets datamärkenes form för att passa texten  
description: Lär dig hur du ändrar storlek på datalabelsformen i ett diagram för att passa texten i Aspose.Cells for Node.js via C++. Vår guide visar hur du justerar storleken och formen på etikettens behållare för att säkerställa att texten visas korrekt utan avklippning eller överlappning.  
keywords: Aspose.Cells for Node.js via C++, diagram, datalabels, formförändring, textpassning, avklippning, överlappning.  
type: docs  
weight: 220  
url: /sv/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  
Excel-programmet tillhandahåller alternativet **Ändra form för att passa text** för diagrammets datamärken för att öka storleken på formen så att texten passar inuti den.  
{{% /alert %}}  

## **Hur man ändrar diagrammets mikroform för att passa texten i Microsoft Excel**  

Detta alternativ kan nås via Excel-gränssnittet genom att välja någon av datalabels på diagrammet. Högerklicka och välj menyn **Format Data Labels**. Under fliken **Storlek & Egenskaper** expanderar du **Anpassning** för att visa relaterade egenskaper inklusive **Ändra storlek på formen för att fixa texten**.  

## **Hur du ändrar storlek på diagrammets datalabelsform för att passa text med Aspose.Cells for Node.js via C++**  

För att efterlikna Excels funktion för att ändra storlek på datalabelsformer för att passa texten har Aspose.Cells API:erna exponerat den booleska egenskapen [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--). Följande kod visar ett enkelt exempel på hur du använder egenskapen [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Create an instance of Workbook containing the Chart
const workbook = new AsposeCells.Workbook(filePath);

// Access the Worksheet that contains the Chart
const sheet = workbook.getWorksheets().get(0);

for (let c = 0; c < sheet.getCharts().getCount(); c++) 
{
// Access the Chart
const chart = sheet.getCharts().get(c);

for (let index = 0; index < chart.getNSeries().getCount(); index++) {
// Access the DataLabels of indexed NSeries
const labels = chart.getNSeries().get(index).getDataLabels();

// Set ResizeShapeToFitText property to true
labels.setIsResizeShapeToFitText(true);
}

// Calculate Chart
chart.calculate();
}

// Save the result
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

