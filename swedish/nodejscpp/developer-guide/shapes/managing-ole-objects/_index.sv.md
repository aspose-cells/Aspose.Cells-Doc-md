---  
title: Hantera OLE objekt med Node.js via C++  
linktitle: Hantera OLE objekt  
type: docs  
weight: 50  
url: /sv/nodejs-cpp/managing-ole-objects/  
description: Lär dig hur du hanterar OLE objekt i Aspose.Cells for Node.js via C++. Lägg till, extrahera och manipulera OLE objekt i kalkblad.  
---  

## **Introduktion**  

OLE (Object Linking and Embedding) är ett ramverk för sammansatta dokumentteknologier. Kort sagt är ett sammansatt dokument något som en skrivbordsmiljö som kan innehålla visuella och informationsobjekt av alla slag: text, kalendrar, animationer, ljud, rörelsevideo, 3D, kontinuerligt uppdaterade nyheter, kontroller och så vidare. Varje skrivbordsobjekt är en självständig programenhet som kan interagera med användaren och även kommunicera med andra objekt på skrivbordet.  

OLE stöds av många olika program och används för att göra innehåll som skapats i ett program tillgängligt i ett annat. Till exempel kan du infoga ett Microsoft Word-dokument i Microsoft Excel. För att se vilka typer av innehåll du kan infoga, klicka på **Objekt** i **Infoga**-menyn. Endast program som är installerade på datorn och stödjer OLE-objekt visas i rutan **Objekttyp**.  

### **Infoga OLE-objekt i arbetsbladet**  

Aspose.Cells for Node.js via C++ stöder att lägga till, extrahera och manipulera OLE-objekt i kalkblad. Av den anledning har Aspose.Cells klassen [**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection), som används för att lägga till ett nytt OLE-objekt i samlingen. En annan klass, [**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject), representerar ett OLE-objekt. Den har några viktiga medlemmar:  

- Egenskapen [**getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--) specificerar bild (ikonen) data av typ byte-array. Bilden kommer att visas för att visa OLE-objektet i kalkbladet.  
- Egenskapen [**getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--) specificerar objektets data i form av en byte-array. Denna data kommer att visas i det relaterade programmet när du dubbelklickar på OLE-objektets ikon.  

Följande exempel visar hur man lägger till en OLE-objekt/-objekt i ett arbetsblad.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "logo.jpg");

// Get the picture into the streams.
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const filePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(filePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **Extrahera OLE-objekt i arbetsboken**  

Följande exempel visar hur man extraherar OLE-objekt i en arbetsbok. Exemplet hämtar olika OLE-objekt från en befintlig XLS-fil och sparar olika filer (DOC, XLS, PPT, PDF etc.) baserat på OLE-objektets filformatstyp.  

Efter att ha kört koden kan vi spara olika filer baserat på deras respektive OLE-objektets format.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();

// Loop through all the oleobjects and extract each object.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);

// Specify the output filename.
let fileName = path.join(dataDir, `ole_${i}.`);

// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Xlsx:
fileName += "xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "jpg";
break;
default:
//........
break;
}

// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = new Uint8Array(ole.getObjectData());
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, `Excel_File${i}.out.xlsx`));
}

// Create the files based on the oleobject format types.
else {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
```  

### **Extrahera inbäddad MOL-fil**  

Aspose.Cells for Node.js via C++ stöder extrahering av objekt av ovanliga typer som MOL (molekylär datafil som innehåller information om atomer och bindningar). Följande kodsnutt visar hur man extraherar en inbäddad MOL-fil och sparar den på disk med detta [exempelfil i Excel](94896196.xlsx).  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "EmbeddedMolSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
let index = 1;

const worksheets = workbook.getWorksheets();
const sheetCount = worksheets.getCount();
for (let i = 0; i < sheetCount; i++) {
const sheet = worksheets.get(i);
const oles = sheet.getOleObjects();
const oleCount = oles.getCount();
for (let j = 0; j < oleCount; j++) {
const ole = oles.get(j);
const fileName = path.join(outputDir, `OleObject${index}.mol`);
const fileStream = fs.createWriteStream(fileName);
fileStream.write(Buffer.from(ole.getObjectData()));
fileStream.end();
index++;
}
}
```  

## **Fortsatta ämnen**  
- [Åtkomst och ändring av visningsmärket för det länkade OLE-objektet](/cells/sv/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [Automatisk uppdatering av OLE-objekt via Microsoft Excel med Aspose.Cells](/cells/sv/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [Extrahera OLE-objekt från arbetsboken](/cells/sv/nodejs-cpp/extract-ole-objects-from-workbook/)  
- [Hämta eller ange klassidentifieraren för det inbäddade OLE-objektet](/cells/sv/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [Infoga en WAV-fil som ett Ole-objekt](/cells/sv/nodejs-cpp/inserting-a-wav-file-as-an-ole-object/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
