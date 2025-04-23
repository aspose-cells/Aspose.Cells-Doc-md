---  
title: Visa cellområde som datalabels med Node.js via C++  
linktitle: Visar cellområdet som datamärken  
description: Lär dig hur du visar ett cellområde som datalabels i diagram med Aspose.Cells for Node.js via C++. Vår guide visar hur du länkar etiketten till din datakälla och formaterar dem för att tillhandahålla korrekt och meningsfull information i dina diagram.  
keywords: Aspose.Cells for Node.js via C++, diagram, datalabels, cellområde, datakälla, formatering, noggrannhet, meningsfull information.  
type: docs  
weight: 130  
url: /sv/nodejs-cpp/showing-cell-range-as-the-data-labels/  
---  

{{% alert color="primary" %}}  
I Microsoft Excel 2013 kan du visa ett cellområde för datamärkningar. Aspose.Cells för Node.js stödjer denna funktion.  
{{% /alert %}}  

## **Kryssrutan för att visa cellområde som datamärken**  

Att visa cellområdet som datamärken i Microsoft Excel:  

1. Välj seriens datamärken och högerklicka för att öppna snabbmenyn.  
1. Välj **Formatera datamärken**. Etikettalternativ visas.  
1. Välj eller avmarkera alternativet **Etiketten innehåller - Värde från celler**.  

Koden nedan ger tillgång till en diagramserie datamärkningar och ställer in [**DataLabels.getShowCellRange()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getShowCellRange--)-egenskapen till **true** för att välja alternativet **Label Contains - Value From Cells**.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source_show_range.xlsx");

// Create workbook from the source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Check the "Label Contains - Value From Cells"
const dataLabels = chart.getNSeries().get(0).getDataLabels();
dataLabels.setShowCellRange(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

