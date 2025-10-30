---  
title: Copiar Macro VBA UserForm DesignerStorage desde la plantilla al libro de trabajo destino con Node.js vía C++  
linktitle: Copiar el Diseñador de Almacenamiento de Macros VBA de la Plantilla al Libro de Trabajo Destino  
type: docs  
weight: 130  
url: /es/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/  
description: Aprende cómo copiar un proyecto VBA, incluyendo Designer Storage, de un archivo Excel a otro usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

Aspose.Cells permite copiar un proyecto VBA de un archivo Excel a otro archivo Excel. Un proyecto VBA consta de varios tipos de módulos, como Documento, Procedural, Diseñador, etc. Todos los módulos pueden copiarse con código simple, pero para el módulo de Diseñador, hay datos adicionales llamados Designer Storage que necesitan ser accedidos o copiados. Los siguientes dos métodos se ocupan de Designer Storage.  

- [**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-)  
- [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-)  

## **Copiar el diseñador de almacenamiento de formularios de usuario Macro de VBA de la plantilla al libro de Excel de destino**  

Por favor, vea el siguiente código de muestra. Copia el proyecto VBA del [archivo de Excel plantilla](50528345.xlsm) en un libro en blanco y lo guarda como el [archivo de Excel de salida](50528346.xlsm). Si abre el proyecto VBA dentro del archivo de Excel plantilla, verá un Formulario de usuario como se muestra abajo. El Formulario de usuario consiste en Almacenamiento del Diseñador, por lo que se copiará usando [**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-) y [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-) métodos.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**  

La siguiente captura de pantalla muestra el archivo de Excel de salida y su contenido que fue copiado del archivo de Excel plantilla. Cuando hace clic en el Botón 1, se abre el Formulario de usuario VBA que tiene un botón de comando que muestra un cuadro de mensaje al hacer clic.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**  

## **Código de muestra**  

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
