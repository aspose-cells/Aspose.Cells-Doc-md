---  
title: Копировать VBA макрос UserForm DesignerStorage из шаблона в целевую рабочую книгу с помощью Node.js через C++  
linktitle: Копирование макроса VBA UserForm DesignerStorage из шаблона в целевую книгу  
type: docs  
weight: 130  
url: /ru/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/  
description: Узнайте, как скопировать VBA проект, включая Designer Storage, из одного файла Excel в другой с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Aspose.Cells позволяет копировать VBA-проект из одного файла Excel в другой. VBA-проект состоит из различных типов модулей, таких как Документ, Процедурный, Дизайнерский и др. Все модули можно скопировать простым кодом, но для модуля Designer необходим доступ или копирование дополнительных данных, называемых Designer Storage. Следующие два метода работают с Designer Storage.  

- [**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-)  
- [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-)  

## **Копирование макроса VBA UserForm DesignerStorage из шаблона в целевую книгу**  

Пожалуйста, посмотрите следующий пример кода. Он копирует VBA-проект из [шаблонного файла Excel](50528345.xlsm) в пустую рабочую книгу и сохраняет его как [выходной файл Excel](50528346.xlsm). Если открыть VBA-проект внутри шаблонного файла Excel, вы увидите форму пользователя, как показано ниже. Форма пользователя состоит из Designer Storage, поэтому она будет скопирована с использованием методов [**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-) и [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-).  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**  

Следующий скриншот показывает выходной файл Excel и его содержимое, скопированные из шаблонного файла Excel. При нажатии на кнопку 1 откроется форма VBA User Form, которая сама содержит командную кнопку, показывающую сообщение при нажатии.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**  

## **Образец кода**  

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
