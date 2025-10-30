---  
title: Konvertera kalkylblad till bild och kalkylblad till bild per sida med Node.js via C++  
linktitle: Konvertera kalkylblad till bild och Kalkylblad till bild per sida  
type: docs  
weight: 80  
url: /sv/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/  
---  

{{% alert color="primary" %}}  
Detta dokument är avsett att ge utvecklare en detaljerad förståelse för hur man konverterar ett kalkylblad till en bildfil och ett kalkylblad med flera sidor till en bildfil per sida.  

Ibland kan du behöva presentera kalkylblad som bilder, till exempel för att använda dem i applikationer eller webbsidor. Du kanske behöver infoga bilderna i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller använda dem i något annat scenario. Kort sagt, du vill rendera kalkylbladet som en bild. Aspose.Cells stöder konvertering av kalkylblad i Microsoft Excel-filer till bilder. Dessutom stöder Aspose.Cells konvertering av en arbetsbok till flera bildfiler, en per sida.  

Du kan använda Office Automation för att uppnå detta, men Office Automation har sina egna nackdelar. Det finns flera skäl och problem involverade: till exempel säkerhet, stabilitet, skalbarhet/hastighet, pris och funktioner. Kort sagt, det finns många skäl, men det främsta är att Microsoft själva starkt rekommenderar att inte använda Office Automation.  
{{% /alert %}}  

## **Använda Aspose.Cells for Node.js via C++ för att konvertera kalkylblad till bildfil**  

Denna artikel visar hur man skapar en konsolapplikation, konverterar ett kalkylblad till en bild och konverterar ett kalkylblad till en bild för varje kalkylblad med några få och enkla kodrader med Aspose.Cells API.  

Du måste importera flera värdefulla klasser relaterade till renderingfunktioner till ditt program eller projekt, såsom [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender/) och så vidare. Klassen [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) representerar ett kalkylblad för att rendera bilder för kalkylbladet och har en överlastad [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-) metod som kan konvertera ett kalkylblad till bildfiler direkt med alla attribut eller alternativ som anges. Den kan returnera ett bildobjekt och du kan spara en bildfil till disk/ström. Flera bildformat stöds, t.ex. BMP, PNG, GIF, JPG, JPEG, TIFF, EMF och andra.  

Den här artikeln förklarar hur man:  

- Konvertera ett kalkylblad till en bild  
- Konvertera varje sida i ett kalkylblad till en bild  

Det här exemplet visar hur man använder Aspose.Cells för att konvertera ett kalkylblad från en mallarbok till en bildfil.  

### **Installationsprojekt**  

1. Först, [ladda ner Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
1. Installera den på din utvecklingsdator. Alla [Aspose](http://www.aspose.com/) komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och tillför endast vattenstämplar till de producerade dokumenten. Starta nu din utvecklingsmiljö och skapa en ny konsolapplikation. Detta exempel använder en Node.js konsolapplikation, men du kan använda vilken som helst konfiguration som integrerar med Node.js. Lägg till referens till Aspose.Cells i projektet.  

### **Konvertera kalkylblad till bildfil**  

Jag skapade en ny arbetsbok i Microsoft Excel och lade till lite data i det första kalkylbladet: **Testbook.xlsx** (1 kalkylblad). Nästa steg är att konvertera mallfilens kalkylblad Sheet1 till en bildfil som kallas SheetImage.jpg.  

Följande är koden som används av komponenten för att utföra uppgiften. Den konverterar Sheet1 i **Testbook.xlsx** till en bildfil för att förklara hur enkel denna konvertering är.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleConvertWorksheettoImageFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setOnePagePerSheet(true);

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the image file
const outputFilePath = outputDir + "outputConvertWorksheettoImageFile.jpg";

sr.toImage(0, outputFilePath);
```  

## **Använda Aspose.Cells for Node.js via C++ för att konvertera kalkylblad till bildfil per sida**  

Detta exempel visar hur man använder Aspose.Cells för att konvertera ett arbetsblad från en mallarbok som har flera sidor till en bildfil per sida.  

### **Konvertera kalkylblad till bild per sida**  

Jag skapade en ny arbetsbok i Microsoft Excel och lade till lite data i det första arbetsbladet: **Testbook2.xlsx** (1 arbetsblad).  

Nu, konvertera mallfilens arbetsblad Sheet1 till bildfiler (en fil per sida). Eftersom jag redan skapat konsolapplikationen för att utföra kopieringsuppgiften, kommer jag att hoppa över de stegen för att skapa konsolapplikationen och gå direkt till arbetsbladskonverteringsstegen.  

Följande är koden som används av komponenten för att slutföra uppgiften. Den konverterar Sheet1 i Testbook2.xlsx till bildfiler per sida.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleConvertWorksheetToImageByPage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(200);
options.setVerticalResolution(200);
options.setImageType(AsposeCells.ImageType.Tiff);

// Sheet2Image By Page conversion
const sr = new AsposeCells.SheetRender(sheet, options);
for (let j = 0; j < sr.getPageCount(); j++) 
{
sr.toImage(j, outputDir + "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif");
}
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
