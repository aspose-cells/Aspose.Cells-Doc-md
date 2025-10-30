---  
title: Copia il macro VBA UserForm DesignerStorage dal modello al file di destinazione con Node.js tramite C++  
linktitle: Copia il designer dello UserForm del macro VBA dal modello al workbook di destinazione  
type: docs  
weight: 130  
url: /it/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/  
description: Impara come copiare un progetto VBA, incluso Designer Storage, da un file Excel all altro utilizzando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Aspose.Cells permette di copiare un progetto VBA da un file Excel a un altro. Un progetto VBA è composto da vari tipi di moduli, ad esempio Document, Procedurale, Designer, ecc. Tutti i moduli possono essere copiati con un codice semplice, ma per il modulo Designer, ci sono dati extra chiamati Designer Storage che devono essere accessibili o copiati. I seguenti due metodi si occupano di Designer Storage.  

- [**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-)  
- [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-)  

## **Copia il DesignerStorage del modulo utente VBA Macro dal modello al foglio di lavoro di destinazione**  

Consulta il seguente esempio di codice. Copia il progetto VBA dal [file Excel modello](50528345.xlsm) in una cartella vuota e lo salva come [file Excel di output](50528346.xlsm). Se apri il progetto VBA all'interno del file Excel modello, vedrai un User Form come mostrato di seguito. Il User Form consiste di Designer Storage, quindi verrà copiato utilizzando i metodi [**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-) e [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-).  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**  

lo screenshot seguente mostra il file Excel di output e il suo contenuto, copiato dal file Excel modello. Quando fai clic sul Pulsante 1, si apre il User Form VBA che ha un pulsante di comando che mostra un messaggio quando cliccato.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**  

## **Codice di Esempio**  

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
