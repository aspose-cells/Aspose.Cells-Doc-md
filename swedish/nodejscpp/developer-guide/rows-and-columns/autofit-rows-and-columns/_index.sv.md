---  
title: Automatiskt anpassa rader och kolumner med Node.js via C++  
linktitle: Automatisk anpassning av rader och kolumner  
type: docs  
weight: 20  
url: /sv/nodejs-cpp/autofit-rows-and-columns/  
description: Denna artikel visar hur man autoAnpassar rader, kolumner, rader av sammanslagna celler och rader i ett cellområde med Aspose.Cells for Node.js via C++.  
keywords: Autofit rader Node.js via C++, autofit kolumner Node.js via C++, autofit rad i ett cellområde Node.js via C++, autofit rader av sammanslagna celler Node.js via C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel tillåter användare att auto-anpassa bredd och höjd på celler efter deras innehåll. Denna funktion finns även tillgänglig via Aspose.Cells for Node.js via C++, så att utvecklare kan auto-anpassa dimensionerna på en cell under körning.  
{{% /alert %}}  

## **Autostorlek**  

Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som ger åtkomst till varje arbetsblad i en Excel-fil. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen erbjuder ett brett utbud av egenskaper och metoder för att hantera ett arbetsblad. Denna artikel tittar på hur man använder [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen för att autofit-rader eller kolumner.  

### **AutoFit Row - Enkelt**  

Det enklaste sättet att auto-anpassa bredd och höjd på en rad är att anropa [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassens [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-)-metod. [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-)-metoden tar ett radindex (på raden som ska ändras storlek på) som parameter.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileBuffer = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1);

// Saving the modified Excel file
const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath);
```  

### **Hur man Autofitrad i ett område av celler**  

En rad består av många kolumner. Aspose.Cells tillåter utvecklare att autofit-a en rad baserat på innehållet i ett cellområde inom raden genom att anropa en överlagrad version av [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-)-metoden. Den tar följande parametrar:  

- **Radindex**, index för raden som ska autofit.  
- **Första kolumnindex**, index för radens första kolumn.  
- **Sista kolumnindex**, index för radens sista kolumn.  

[**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-)-metoden kontrollerar innehållet i alla kolumner i raden och autofitar sedan raden.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileData = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1, 0, 5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **Hur man Autofittar kolumn i ett område av celler**  

En kolumn består av många rader. Det är möjligt att auto-anpassa en kolumn baserat på innehållet i ett cellområde i kolumnen genom att anropa en överlagrad version av [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-)-metoden som tar följande parametrar:  

- **Kolumnindex**, index för kolumnen som ska autofit.  
- **Första radindex**, index för kolumnens första rad.  
- **Sista radindex**, index för kolumnens sista rad.  

[**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-)-metoden kontrollerar innehållet i alla rader i kolumnen och autofitar sedan kolumnen.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const workbook = new AsposeCells.Workbook(fs.readFileSync(inputPath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the Column of the worksheet
worksheet.autoFitColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **Hur man Autofittar rader för sammanfogade celler**  

Med Aspose.Cells är det möjligt att autofit-a rader även för celler som har sammanslagits med hjälp av [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions)-API:et. [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions)-klassen tillhandahåller en [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--)-egenskap som kan användas för att autofit-a rader för sammanslagna celler. [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--) accepterar [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/nodejs-cpp/autofitmergedcellstype)-enumeration som har följande medlemmar.  

- Ingen: Ignorera sammanslagna celler.  
- FörstaLinjen: Utökar endast höjden på den första raden.  
- SistaLinjen: Utökar endast höjden på den sista raden.  
- VarjeRad: Utökar endast höjden på varje rad.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a new Workbook
const wb = new AsposeCells.Workbook();

// Get the first (default) worksheet
const worksheet = wb.getWorksheets().get(0);

// Create a range A1:B1
const range = worksheet.getCells().createRange(0, 0, 1, 2);

// Merge the cells
range.merge();

// Insert value to the merged cell A1
worksheet.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style = worksheet.getCells().get(0, 0).getStyle();

// Set wrapping text on
style.setIsTextWrapped(true);

// Apply the style to the cell
worksheet.getCells().get(0, 0).setStyle(style);

// Create an object for AutoFitterOptions
const options = new AsposeCells.AutoFitterOptions();

// Set auto-fit for merged cells
options.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.EachLine);

// Autofit rows in the sheet (including the merged cells)
worksheet.autoFitRows(options);

// Save the Excel file
wb.save(path.join(outputDir, "AutofitRowsforMergedCells.xlsx"));
```  

{{% alert color="primary" %}}  
Du kan också försöka använda de överlagrade versionerna av [**autoFitRows**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-) & [**autoFitColumns**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-)-metoderna som accepterar ett rad- eller kolumnområde och en instans av [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) för att autofit-a de valda raderna/kolumnerna med önskad [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions).  

Signaturerna för dessa metoder är som följer:  

1. autoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) options)  
1. autoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) options)  
{{% /alert %}}  

## **Viktigt att veta**  

{{% alert color="primary" %}}  
Om en cell är sammanslagen kommer inte autoFit-metoderna att tillämpas, vilket är samma beteende som i Microsoft Excel. Du kan kringgå detta genom att använda autofilter-API:et. Dessutom, om texten i en cell är omsluten, kommer inte heller [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-)-metoden att tillämpas. En annan sak du bör veta är att *autoFit*-metoderna är tidskrävande. Så du bör använda dessa metoder så sällan som möjligt för att säkerställa att din applikation är effektiv.  
{{% /alert %}}  

## **Fortsatta ämnen**  
- [Automatisk justering av rader för sammanfogade celler](/cells/sv/nodejs-cpp/autofit-rows-for-merged-cells/)  

