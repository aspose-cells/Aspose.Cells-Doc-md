---  
title: Kopiera VBA Macro UserForm DesignerStorage från mall till målarbetsbok med Node.js via C++  
linktitle: Kopiera VBA makro UserForm DesignerStorage från mallen till mål arbetsboken  
type: docs  
weight: 130  
url: /sv/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/  
description: Lär dig hur man kopierar ett VBA projekt, inklusive Designer Storage, från en Excel fil till en annan med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Aspose.Cells låter dig kopiera ett VBA-projekt från en Excel-fil till en annan Excel-fil. Ett VBA-projekt består av olika typer av moduler dvs. Dokument, Procedur, Designer etc. Alla moduler kan kopieras med enkel kod, men för Designer-modulen finns det extra data kallad Designer Storage som måste nås eller kopieras. Följande två metoder hanterar Designer Storage.  

- [**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-)  
- [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-)  

## **Kopiera VBA-makro UserForm DesignerStorage från mallen till mål arbetsboken**  

Se följande kodexempel. Det kopierar VBA-projektet från [mallens Excel-fil](50528345.xlsm) till en tom arbetsbok och sparar den som [utdata Excel-fil](50528346.xlsm). Om du öppnar VBA-projektet i mallen för Excel-fil ser du en användarform som visas nedan. User Form består av Designer Storage, så den kommer att kopieras med hjälp av [**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-)- och [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-)-metoder.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**  

Följande skärmbild visar utdata Excel-filen och dess innehåll som kopierades från mall Excel-filen. När du klickar på Knapp 1 öppnas VBA-användarformuläret som i sig har en kommando-knapp som visar ett meddelandefönster vid klick.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**  

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create empty target workbook
const target = new AsposeCells.Workbook();

// Load the Excel file containing VBA-Macro Designer User Form
const templateFile = new AsposeCells.Workbook(path.join(sourceDir, "sampleDesignerForm.xlsm"));

// Copy all template worksheets to target workbook
const sheets = templateFile.getWorksheets();
const sheetCount = sheets.getCount();
for (let i = 0; i < sheetCount; i++) {
const ws = sheets.get(i);
if (ws.getType() === AsposeCells.SheetType.Worksheet) 
{
const s = target.getWorksheets().add(ws.getName());
s.copy(ws);

// Put message in cell A2 of the target worksheet
s.getCells().get("A2").putValue("VBA Macro and User Form copied from template to target.");
}
}


// Copy the VBA-Macro Designer UserForm from Template to Target 
const modules = templateFile.getVbaProject().getModules();
const moduleCount = modules.getCount();
for (let i = 0; i < moduleCount; i++) {
const vbaItem = modules.get(i);
if (vbaItem.getName() === "ThisWorkbook") 
{
// Copy ThisWorkbook module code
target.getVbaProject().getModules().get("ThisWorkbook").setCodes(vbaItem.getCodes());
} 
else 
{
console.log(vbaItem.getName());

let vbaMod = 0;
const sheet = target.getWorksheets().getSheetByCodeName(vbaItem.getName());
if (sheet.isNull()) 
{
vbaMod = target.getVbaProject().getModules().add(vbaItem.getType(), vbaItem.getName());
} 
else 
{
vbaMod = target.getVbaProject().getModules().add(sheet);
}

target.getVbaProject().getModules().get(vbaMod).setCodes(vbaItem.getCodes());

if (vbaItem.getType() === AsposeCells.VbaModuleType.Designer) 
{
// Get the data of the user form i.e. designer storage
const designerStorage = modules.getDesignerStorage(vbaItem.getName());

// Add the designer storage to target Vba Project
target.getVbaProject().getModules().addDesignerStorage(vbaItem.getName(), designerStorage);
}
}
}


// Save the target workbook
target.save(outputDir + "outputDesignerForm.xlsm", AsposeCells.SaveFormat.Xlsm);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
