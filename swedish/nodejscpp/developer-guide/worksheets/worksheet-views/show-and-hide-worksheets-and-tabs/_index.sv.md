---  
title: Visa och Dölj Arbetsblad och Flikar med Node.js via C++  
linktitle: Visa och Dölja Kalkylblad och Flikar  
type: docs  
weight: 10  
url: /sv/nodejs-cpp/show-and-hide-worksheets-and-tabs/  
description: Denna artikel ger kodexempel för att använda Node.js API eller Node.js bibliotek för att programmatiskt visa och dölja ett Excel ark samt hur man visar och döljer Excel arbetsboksflikar.  
---  

{{% alert color="primary" %}}  
Aspose.Cells tillåter användaren att visa och dölja element i en arbetsbok inklusive kalkylblad och flikar.  
{{% /alert %}}  

## **Visa och dölj ett arbetsblad**  

En Excel-fil kan ha ett eller flera arbetsblad. När vi skapar en Excel-fil lägger vi till arbetsblad i Excel-filen där vi arbetar. Varje arbetsblad i en Excel-fil är oberoende från det andra arbetsbladet genom att ha sina egna data och formateringsinställningar osv. Ibland kan utvecklare behöva dölja några arbetsblad och göra andra synliga i Excel-filen för deras eget intresse. Så, **Aspose.Cells** låter utvecklare kontrollera synligheten av arbetsbladen i deras Excel-filer.  

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) klassen innehåller en [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) samling som ger åtkomst till varje arbetsblad i Excel-filen.  

Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad. För att kontrollera arbetsbladets synlighet, använd egenskapen [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) är en boolesk egenskap, vilket betyder att den endast kan lagra ett **true** eller **false** värde.  

### **Göra ett arbetsblad synligt**  

Gör ett arbetsblad synligt genom att ställa in egenskapen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) för [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--)-klassen till **true**.  

### **Dölja ett arbetsblad**  

Dölj ett kalkylblad genom att ställa in egenskapen [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) för klassen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) till **falskt**.  

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.createReadStream(filePath);

// Instantiating a Workbook object with opening the Excel file through the file stream
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(chunks)); // Fixed from stream to Blob

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the first worksheet of the Excel file
worksheet.setIsVisible(false);

// Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

## **Visa och dölj flikar**  

Om du tittar noga längst ner i en Microsoft Excel-fil, kommer du att se ett antal kontroller. Dessa inkluderar:  

- Arkflikar.  
- Flikbläddringsknappar.  

Arkflikar representerar arbetsbladen i Excel-filen. Klicka på vilken flik som helst för att växla till det arbetsbladet. Ju fler arbetsblad i arbetsboken, desto fler arkflikar finns det. Om Excel-filen har ett bra antal arbetsblad behöver du knappar för att navigera genom dem. Så tillhandahåller Microsoft Excel flikbläddringsknappar för att bläddra igenom arkflikarna.  

Genom att använda Aspose.Cells kan utvecklare kontrollera synligheten av arkflikar och flikbläddringsknappar i Excel-filer.  

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) erbjuder ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att kontrollera synligheten för flikar i en Excel-fil kan utvecklare använda egenskapen [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) för klassen [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) är en Boolean-egenskap, vilket betyder att den bara kan lagra ett **true** eller **false** värde.  

### **Göra flikar synliga**  

Gör flikar synliga med egenskapen [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) för klassen [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) till **true**.  

### **Gömma flikar**  

Dölj flikar i en Excel-fil genom att ställa in egenskapen [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) för klassen [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) till **falskt**.  

Här är ett komplett exempel som öppnar en Excel-fil (book1.xls), döljer dess flikar och sparar den modifierade filen som output.xls. Efter att kodexekveringen har utförts kommer du att se att arbetsbokens flikar är dolda.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(false);

// Shows the tabs of the Excel file
// workbook.getSettings().setShowTabs(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

### **Styra fliken Bredd**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Loading the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(true);

// Adjusting the sheet tab bar width
workbook.getSettings().setSheetTabBarWidth(800);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
