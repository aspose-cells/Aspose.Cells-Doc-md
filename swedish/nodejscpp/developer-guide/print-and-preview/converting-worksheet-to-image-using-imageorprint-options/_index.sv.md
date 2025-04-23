---  
title: Konvertera kalkylblad till bild med bild eller utskriftsalternativ med Node.js via C++  
linktitle: Konvertera arbetsblad till bild med hjälp av alternativ för bild eller utskrift  
type: docs  
weight: 90  
url: /sv/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/  
description: Lär dig hur du konverterar ett kalkylblad till en bildfil och tillämpar olika bild och utskriftsalternativ med Aspose.Cells for Node.js via C++.   
---  

{{% alert color="primary" %}}  
Detta dokument är utformat för att ge en detaljerad förståelse för hur man konverterar ett arbetsblad till en bildfil och tillämpar olika bild- och utskriftsalternativ för bilden, såsom upplösning, TIFF-komprimering, bildformat och sidkvalitet.  
{{% /alert %}}  

## **Spara arbetsblad till bilder - Olika tillvägagångssätt**  

Ibland kan det hända att du behöver presentera dina arbetsblad som en bildlig representation. Du kan behöva infoga bilderna i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller använda dem på annat sätt. Du vill helt enkelt ha ett arbetsblad renderat som en bild så att du kan använda det någon annanstans. Aspose.Cells stödjer konvertering av arbetsblad i Excel-filer till bilder. Dessutom stödjer Aspose.Cells inställning av olika alternativ som bildformat, upplösning (både vertikal och horisontell), bildkvalitet och andra bild- och utskriftsalternativ.  

Du kan prova Office Automation, men det har sina nackdelar. Det finns flera skäl och problem: till exempel säkerhet, stabilitet, skalbarhet och hastighet, pris och funktioner. Kort sagt, det finns många skäl, varav det viktigaste är att Microsoft själva starkt rekommenderar att undvika Office-automation från mjukvarulösningar.  

Denna artikel visar hur man skapar en konsolapplikation i Visual Studio .NET, utför konvertering av ett arbetsblad till bild med olika bild- och utskriftsalternativ med några enkla kodrader med hjälp av Aspose.Cells API.  

Klassen [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) representerar ett kalkylblad för att rendera bilder för kalkylbladet, den har en överlastad [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-) metod som direkt kan konvertera ett kalkylblad till bildfil(er) med angivna attribut eller alternativ. Den kan returnera ett objekt som du kan spara som en bildfil till disk/ström. Flera bildformat stöds, t.ex BMP, PNG, GIFF, JPEG, TIFF, EMF och andra.  

## **Använda Aspose.Cells för att konvertera arbetsblad till bild med hjälp av alternativ för bild eller utskrift**  

### **Skapa en mallarbok i Microsoft Excel**  

Jag skapade en ny arbetsbok i MS Excel och lade till lite data i det första arbetsbladet. Nu kommer jag att konvertera mallfilens arbetsblad “Sheet1” till en bildfil “SheetImage.tiff” och tillämpa olika bildalternativ som horisontell och vertikal upplösning, TiffCompression med mera.  

### **Ladda ner och installera Aspose.Cells**  

Först måste du [ladda ner](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++. Installera det på din utvecklingsdator. Alla [Aspose](http://www.aspose.com/) komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och inför endast vattenstämplar i de producerade dokumenten.  

### **Skapa ett projekt**  

Starta din föredragna utvecklingsmiljö (t.ex. Visual Studio). Skapa ett nytt konsolprogram.  

### **Lägg till referenser**  

Detta projekt kommer att använda Aspose.Cells. Så du måste lägga till en referens till Aspose.Cells-komponenten i ditt projekt. Till exempel, lägg till en referens till ….\Program Files\Aspose\Aspose.Cells for Node.js via C++\Bin\Aspose.Cells.node  

### **Konvertera arbetsblad till en bildfil**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Open template
const filePath = path.join(sourceDir, "sampleWorksheetToAnImage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Apply different Image and Print options
const options = new AsposeCells.ImageOrPrintOptions(); // Corrected: Added the instantiation for ImageOrPrintOptions.

// Set Horizontal Resolution
options.setHorizontalResolution(300);

// Set Vertical Resolution
options.setVerticalResolution(300);

// Set TiffCompression
options.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

// Set Image Format
options.setImageType(AsposeCells.ImageType.Tiff);

// Set printing page type
options.setPrintingPage(AsposeCells.PrintingPageType.Default);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, options);

// Render/save the image for the sheet
const pageIndex = 3;
sr.toImage(pageIndex, path.join(outputDir, `outputWorksheetToAnImage_${pageIndex + 1}.tiff`));
```  

## **Konverteringsalternativ**  

Det är möjligt att spara specifika sidor som bild. Följande kod konverterar arbetsböckerets första och andra kalkylblad till JPG-bilder.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleSpecificPagesToImages.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Specify page index to be rendered
const idxPage = 3;

// Render the third image for the sheet
const bitmap = sr.toImage(idxPage);

// Save the image file
const fs = require("fs");
fs.writeFileSync(path.join(outputDir, `outputSpecificPagesToImage_${idxPage + 1}.jpg`), bitmap);
```  

## **Bildkonvertering med användning av WorkbookRender**  

Ett TIFF-bild kan innehålla mer än en frame. Du kan spara hela arbetsboken som en enskild TIFF-bild med flera frames eller sidor:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Tiff);

const workbookRender = new AsposeCells.WorkbookRender(workbook, opts);
workbookRender.toImage(path.join(outputDir, "outputUseWorkbookRenderForImageConversion.tiff"));
```  


