---  
title: Läs av axeletiketter efter att ha beräknat diagrammet med Node.js via C++  
linktitle: Läs av axeletiketter efter att ha beräknat diagrammet  
description: Lär dig hur du kan läsa axeletiketter i Aspose.Cells for Node.js via C++ efter att ha beräknat diagrammet. Vår guide visar hur du kan få åtkomst till och hämta axeletiketter, inklusive deras formatering och positionering.  
keywords: Aspose.Cells för Node.js, diagram, axelmarkeringar, beräkning, läsning, åtkomst, hämtning, formatering, positionering, Node.js via C++  
type: docs  
weight: 90  
url: /sv/nodejs-cpp/read-axis-labels-after-calculating-the-chart/  
---  

## **Möjliga användningsscenario**

Du kan läsa av axeletiketter för ditt diagram efter att ha beräknat dess värden med hjälp av metoden [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--). Använd gärna metoden [**Axis.getAxisTexts()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getAxisTexts--) för detta syfte som returnerar listan med axeletiketter.

## **Läs av axeletiketter efter att ha beräknat diagrammet**

Vänligen se följande kodexempel som laddar in den [exempel Excel-filen](ReadAxisLabels.xlsx) och läser kategoriaxlarna i diagrammet på den första arbetsbladet. Den skriver sedan ut värdena för axelmärkena på konsolen. Se konsolresultatet för kodexemplet nedan för referens.

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "ReadAxisLabels_new.xlsx");

// Load the Excel file containing chart
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart
const chart = worksheet.getCharts().get(0);

// Calculate the chart
chart.calculate();

// Read axis labels of category axis
const lstLabels = chart.getCategoryAxis().getAxisTexts();

// Print axis labels on console
console.log("Category Axis Labels: ");
console.log("---------------------");

// Iterate axis labels and print them one by one
for (let i = 0; i < lstLabels.length; i++) {
console.log(lstLabels[i]);
}
```

## **Konsoloutput**

{{< highlight javascript >}}  
 Category Axis Labels:  

\---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
