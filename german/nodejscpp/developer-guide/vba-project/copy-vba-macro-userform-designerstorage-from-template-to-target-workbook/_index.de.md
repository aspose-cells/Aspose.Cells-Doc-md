---  
title: Kopieren Sie den VBA Makro UserForm DesignerStorage von Vorlage in Zielarbeitsmappe mit Node.js via C++  
linktitle: Kopieren des VBA Makro UserForm DesignerStorage von der Vorlage in die Zieltabelle  
type: docs  
weight: 130  
url: /de/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/  
description: Erfahren Sie, wie Sie ein VBA Projekt, einschließlich Designer Storage, von einer Excel Datei in eine andere kopieren, mit Aspose.Cells for Node.js via C++.  
---  

## **Mögliche Verwendungsszenarien**  

Aspose.Cells ermöglicht das Kopieren eines VBA-Projekts von einer Excel-Datei in eine andere. Ein VBA-Projekt besteht aus verschiedenen Modultypen, z.B. Dokument, procedural, Designer usw. Alle Module können mit einfachem Code kopiert werden, aber für das Designer-Modul gibt es zusätzliche Daten, genannt Designer Storage, die zugänglich gemacht oder kopiert werden müssen. Die folgenden zwei Methoden behandeln Designer Storage.  

- [**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-)  
- [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-)  

## **Kopieren Sie den VBA-Makro UserForm-DesignerStorage von der Vorlage in die Zieldatei**  

Bitte sehen Sie sich den folgenden Beispielcode an. Er kopiert das VBA-Projekt aus der [Vorlagen-Excel-Datei](50528345.xlsm) in eine leere Arbeitsmappe und speichert sie als [Ausgabedatei Excel](50528346.xlsm). Wenn Sie das VBA-Projekt in der Vorlage-Excel-Datei öffnen, sehen Sie ein Userform wie unten gezeigt. Das Userform besteht aus Designer Storage, das mit [**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-) und [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-) Methoden kopiert wird.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**  

Das folgende Screenshot zeigt die Ausgabedatei Excel und deren Inhalte, die aus der Vorlage-Excel-Datei kopiert wurden. Wenn Sie auf Button 1 klicken, öffnet sich das VBA-Userform, das einen Befehlsknopf enthält, der bei Klick eine Meldung anzeigt.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**  

## **Beispielcode**  

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
