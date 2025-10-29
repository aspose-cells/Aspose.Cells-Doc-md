---  
title: Copier l UserForm Macro VBA DesignerStorage du Template vers le classeur cible avec Node.js via C++  
linktitle: Copier le UserForm DesignerStorage du macro VBA du modèle vers le classeur cible  
type: docs  
weight: 130  
url: /fr/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/  
description: Apprenez comment copier un projet VBA, y compris le Designer Storage, d un fichier Excel à un autre en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Aspose.Cells vous permet de copier un projet VBA d’un fichier Excel dans un autre fichier Excel. Un projet VBA comprend différents modules, c’est-à-dire Document, Procédural, Designer, etc. Tous les modules peuvent être copiés avec un code simple, mais pour le module Designer, il y a des données supplémentaires appelées Designer Storage qui doivent être accessibles ou copiées. Les deux méthodes suivantes traitent du Designer Storage.  

- [**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-)  
- [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-)  

## **Copier le stockage de concepteur de formulaire utilisateur de macro VBA du modèle vers le classeur cible**  

Veuillez voir le code d'exemple suivant. Il copie le projet VBA du [fichier Excel modèle](50528345.xlsm) dans un classeur vide et le sauvegarde sous le nom de [fichier Excel de sortie](50528346.xlsm). Si vous ouvrez le projet VBA dans le fichier Excel modèle, vous verrez un formulaire utilisateur comme illustré ci-dessous. Le formulaire utilisateur contient un Designer Storage, il sera donc copié en utilisant [**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-) et [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-) methods.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**  

La capture d'écran suivante montre le fichier Excel de sortie et son contenu, qui ont été copiés du fichier Excel modèle. Lorsque vous cliquez sur le bouton 1, cela ouvre le formulaire utilisateur VBA qui a lui-même un bouton de commande affichant une boîte de message lors du clic.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**  

## **Code d'exemple**  

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
