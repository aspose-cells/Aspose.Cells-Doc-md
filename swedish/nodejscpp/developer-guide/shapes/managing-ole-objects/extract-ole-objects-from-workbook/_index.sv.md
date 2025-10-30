---  
title: Extrahera OLE objekt från arbetsbok med Node.js via C++  
linktitle: Extrahera OLE objekt från arbetsboken  
type: docs  
weight: 110  
url: /sv/nodejs-cpp/extract-ole-objects-from-workbook/  
---  

{{% alert color="primary" %}}  
Ibland måste du extrahera OLE-objekt från en arbetsbok. Aspose.Cells stöder extrahering och sparande av dessa OLE-objekt.

Denna artikel visar hur du skapar en konsolapplikation i Node.js via C++ och extraherar olika OLE-objekt från en arbetsbok med några enkla kodrader.  
{{% /alert %}}  

## **Extrahera OLE-objekt från en arbetsbok**  

### **Skapa en mallarbok**  

1. Skapa en arbetsbok i Microsoft Excel.  
1. Lägg till ett Microsoft Word-dokument, en Excel-arbetsbok och ett PDF-dokument som OLE-objekt på det första arbetsbladet.  

|**Mall-dokument med OLE-objekt (OleFile.xls)**|  
| :- |  
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|  

Nästa steg, extrahera OLE-objekten och spara dem på hårddisken med respektive filtyper.  

### **Ladda ner och installera Aspose.Cells**  

1. [Ladda ner Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
1. Installera det på din utvecklingsdator.  

Alla Aspose-komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar endast vattenstämplar i producerade dokument.  

### **Skapa ett projekt**  

Starta **Node.js** och skapa en ny konsolapplikation. Detta exempel visar en Node.js-konsolapplikation, men du kan använda vilken JavaScript-kompatibel miljö som helst.  

1. Lägg till beroenden  
   1. Lägg till en referens till Aspose.Cells-komponenten i ditt projekt, till exempel inkludera paketet med `require`-funktionen:  
   ```javascript  
   const { Cells } = require("aspose.cells");  
   ```

### **Extrahera OLE-objekt**  

Koden nedan utför det faktiska arbetet med att hitta och extrahera OLE-objekt. OLE-objekten (DOC, XLS och PDF-filer) sparas på disken.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "oleFile.xlsx"));

// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();

// Loop through all the oleobjects and extract each object in the worksheet.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);
// Specify the output filename.
let fileName = path.join(dataDir, "outOle" + i + ".");
// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Excel97To2003:
fileName += "Xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "Ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "Pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "Jpg";
break;
default:
//........
break;
}
// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = Buffer.from(ole.getObjectData());
if (ole.getObjectData() != null) {
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, "outOle" + i + ".out.xlsx"));
}
} else {
if (ole.getObjectData() != null) {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
}
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
