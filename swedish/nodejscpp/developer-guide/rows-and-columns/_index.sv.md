---  
title: Formatera rader och kolumner med Node.js via C++  
linktitle: Rader och kolumner  
type: docs  
weight: 100  
url: /sv/nodejs-cpp/adjusting-row-height-and-column-width/  
description: Aspose.Cells for Node.js via C++ kan stödja ändring av radhöjd eller kolumnbredd samt tillämpa formatering på rader eller kolumner.  
keywords: Ange radhöjd och kolumnbredd, Justera radhöjd och kolumnbredd, ändra radhöjd eller kolumnbredd, formatera rader och kolumner, hur man anger radhöjd och kolumnbredd.  
---  

{{% alert color="primary" %}}  
 När du arbetar med kalkylblad och lägger till data i rader eller kolumner kan du behöva ändra radens höjd eller kolumnens bredd. Ibland innebär tillämpning av formatering på rader eller kolumner att den aktuella höjden eller bredden måste ändras för att visa datan. Normalt justerar användare radhöjd och kolumnbredd i en WYSIWYG-miljö med Microsoft Excel. Men med Aspose.Cells kan utvecklare utföra dessa operationer i realtid.  
{{% /alert %}}  

## **Arbeta med rader**  

### **Hur man justerar radhöjden**  

 Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) som tillåter åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samling som representerar alla celler i arbetsbladet.  

 Samlingen [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) erbjuder flera metoder för att hantera rader eller kolumner i ett arbetsblad. Några av dessa diskuteras nedan i mer detalj.  

### **Hur man ställer in höjden på en rad**  

 Det är möjligt att ange höjden för en enskild rad genom att anropa {}-samlingens {}-metod. {}-metoden tar följande parametrar:

- **Radindex**, index för den rad vars höjd du ändrar.  
- **Radhöjd**, radhöjden som ska tillämpas på raden.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const buffer = Buffer.concat(chunks);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the height of the second row to 13
worksheet.getCells().setRowHeight(1, 13);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

### **Hur man ställer in höjden på alla rader i ett kalkylblad**  

 Om utvecklare behöver sätta samma radhöjd för alla rader i arbetsbladet kan de göra det genom att använda [**getStandardHeight()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardHeight--)-egenskapen hos [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen.  

**Exempel:**  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the height of all rows in the worksheet to 15
worksheet.getCells().setStandardHeight(15);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// (Note: Closing the file stream is unnecessary in this context as it's a 
// synchronous read performed using fs.readFileSync, which does not require
// explicit closure, but if using fs.createReadStream, you would handle it accordingly)
```  

## **Arbeta med kolumner**  

### **Hur man ställer in bredden på en kolumn**  

 Sätt kolumnbredden genom att anropa [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingens [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-)-metod. [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-)-metoden tar följande parametrar:  

- **Kolumnindex**, index för den kolumn vars bredd du ändrar.  
- **Kolumnbredd**, önskad kolumnbredd.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the width of the second column to 17.5
worksheet.getCells().setColumnWidth(1, 17.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream; // Note: No explicit close needed for fs.readFileSync
```  

### **Hur man ställer in kolumnbredd i pixlar**  

 Sätt kolumnbredden genom att anropa [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingens [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-)-metod. [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-)-metoden tar följande parametrar:  

- **Kolumnindex**, index för den kolumn vars bredd du ändrar.  
- **Kolumnbredd**, önskad kolumnbredd i pixlar.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the width of the column in pixels
worksheet.getCells().setColumnWidthPixel(7, 200);

workbook.save(path.join(outDir, "SetColumnWidthInPixels_Out.xlsx"));
```  

### **Hur man ställer in bredden på alla kolumner i en arbetsbok**  

 För att sätta samma kolumnbredd för alla kolumner i arbetsbladet använd [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingens [**getStandardWidth()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardWidth--)-egenskap.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the width of all columns in the worksheet to 20.5
worksheet.getCells().setStandardWidth(20.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// No explicit close needed in Node.js
```  

## **Fortsatta ämnen**  
- [AutoAnpassa rader och kolumner](/cells/sv/nodejs-cpp/autofit-rows-and-columns/)  
- [Konvertera Text till Kolumner med Aspose.Cells](/cells/sv/nodejs-cpp/convert-text-to-columns-using-aspose-cells/)  
- [Kopiera rader och kolumner](/cells/sv/nodejs-cpp/copying-rows-and-columns/)  
- [Ta bort tomma rader och kolumner i en arbetsbok](/cells/sv/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/)  
- [Gruppering och avgruppering av rader och kolumner](/cells/sv/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/)  
- [Dölja och visa rader och kolumner](/cells/sv/nodejs-cpp/hiding-and-showing-rows-and-columns/)  
- [Infoga eller ta bort rader i en Excel-arbetsbok](/cells/sv/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/)  
- [Infoga och ta bort rader och kolumner i Excel-fil](/cells/sv/nodejs-cpp/inserting-and-deleting-rows-and-columns/)  
- [Ta bort dubblettrader i ett kalkylblad](/cells/sv/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/)  
- [Uppdatera referenser i andra arbetsblad samtidigt som tomma kolumner och rader tas bort i ett arbetsblad](/cells/sv/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
