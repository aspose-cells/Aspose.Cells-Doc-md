---  
title: Konvertera ett Excel diagram till bild med Node.js via C++  
linktitle: Konvertera en Excel diagram till bild  
type: docs  
weight: 20  
url: /sv/nodejs-cpp/convert-an-excel-chart-to-image/  
description: Lär dig hur man konverterar Excel diagram till bilder med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Diagram är visuellt tilltalande och gör det enkelt för användare att se jämförelser, mönster och trender i data. Till exempel visar ett diagram på ett överskådligt sätt om försäljningen ökar eller minskar, eller hur faktisk försäljning jämförs med projicerad försäljning. Människor ombeds ofta att presentera statistisk och grafisk information på ett lättförståeligt och lätt underhållet sätt. En bild hjälper till.  

Ibland behövs diagram i en applikation eller webbsidor. Eller det kan behövas för ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller någon annan applikation. I varje fall vill du rendera diagrammet som en bild så att du kan använda det någon annanstans.  

{{% /alert %}}  

## **Konvertera diagram till bilder**  

I exemplen här konverteras en pajdiagram och ett kolumndiagram till bilder.  

### **Konvertera ett cirkeldiagram till en bildfil**  

Först, skapa en pajdiagram i Microsoft Excel och konvertera den sedan till en bildfil med Aspose.Cells for Node.js via C++. Koden i detta exempel skapar en EMF-bild baserad på pajdiagrammet i mallfilen Microsoft Excel.  

|**Utgång: cirkeldiagramsbild**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|  

1. Skapa ett cirkeldiagram i Microsoft Excel:  
   1. Öppna en ny arbetsbok i Microsoft Excel.  
   1. Ange några data i ett kalkylblad.  
   1. Skapa ett cirkeldiagram baserat på data.  
   1. Spara filen.  

|**Ingångsfilen.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|  

1. Ladda ner och installera Aspose.Cells:  
   1. [Ladda ner Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
   1. Installera det på din utvecklingsdator.  

Alla [Aspose](http://www.aspose.com/) komponenter fungerar i utvärderingsläge när de först installeras. Utvärderingsläget har ingen tidsbegränsning och det lägger bara vattenstämplar i utdata dokument.  

1. Skapa ett projekt:  
   1. Starta din föredragna IDE.  
   1. Skapa ett nytt konsolprogram. Detta exempel använder en Node.js-applikation, men du kan skapa den med vilken JavaScript-runtime som helst.  
   1. Lägg till en referens. Detta projekt använder Aspose.Cells, så lägg till en referens till Aspose.Cells for Node.js via C++.  
   1. Skriv koden som hittar och konverterar diagrammet. Nedan är koden som används av komponenten för att utföra uppgiften. Mycket få rader kod används.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file which contains the pie chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "PieChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "PieChart.out.emf"), AsposeCells.ImageType.Emf);
```  

### **Konvertera ett kolumndiagram till en bildfil**  

Först, skapa ett kolumndiagram i Microsoft Excel och konvertera det till en bildfil, som ovan. Efter att ha kört exempel koden, skapas en JPEG-fil baserad på kolumndiagrammet i mall-Excel-filen.  

|**Utmatningsfil: en kolumndiagramsbild.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|  

1. Skapa ett kolumndiagram i Microsoft Excel:  
   1. Öppna en ny arbetsbok i Microsoft Excel.  
   1. Ange några data i ett kalkylblad.  
   1. Skapa ett kolumndiagram baserat på datan.  
   1. Spara filen.  

|**Ingångsfil.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|  

1. Bygg ett projekt, med referenser, enligt beskrivningen ovan.  
1. Konvertera diagrammet till en bild dynamiskt. Följande är koden som används av komponenten för att utföra uppgiften. Koden är liknande den tidigare:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing excel file which contains the column chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "ColumnChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "ColumnChart.out.jpeg"), AsposeCells.ImageType.Jpeg);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
