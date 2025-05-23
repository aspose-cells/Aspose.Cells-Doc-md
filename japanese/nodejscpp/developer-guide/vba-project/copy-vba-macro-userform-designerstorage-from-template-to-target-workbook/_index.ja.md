---  
title: Node.js経由でC++を使用してテンプレートからターゲットブックにVBAマクロユーザーフォームデザイナーストレージをコピーする  
linktitle: テンプレートから対象のブックへVBAマクロのUserForm DesignerStorageをコピー  
type: docs  
weight: 130  
url: /ja/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/  
description: Aspose.Cells for Node.js via C++を使用して、一つのExcelファイルから別のExcelファイルへVBAプロジェクト（デザイナーストレージを含む）をコピーする方法を学びます。  
---  

## **可能な使用シナリオ**  

Aspose.Cellsを使用すると、一つのExcelファイルから別のExcelファイルにVBAプロジェクトをコピーできます。VBAプロジェクトは、ドキュメント、手続き型、デザイナーなど、さまざまなタイプのモジュールで構成されています。すべてのモジュールはシンプルなコードでコピー可能ですが、デザイナーモジュールには追加のデータであるデザイナーストレージがあります。以下の二つの方法は、デザイナーストレージに関わっています。  

- [**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-)  
- [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-)  

## **テンプレートからターゲットワークブックへのVBAマクロUserForm DesignerStorageのコピー**  

以下のサンプルコードをご覧ください。このコードは、[テンプレートExcelファイル](50528345.xlsm)から空のブックにVBAプロジェクトをコピーし、それを[出力Excelファイル](50528346.xlsm)として保存します。テンプレートExcelファイルのVBAプロジェクトを開くと、以下のようなユーザーフォームが見えます。ユーザーフォームはデザイナーストレージから構成されており、[**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-)と[**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-)の方法を使ってコピーされます。  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**  

以下のスクリーンショットは、テンプレートExcelファイルからコピーされた出力Excelファイルとその内容を示しています。ボタン1をクリックすると、VBAユーザーフォームが開き、その中のコマンドボタンをクリックするとメッセージボックスが表示されます。  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**  

## **サンプルコード**  

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

