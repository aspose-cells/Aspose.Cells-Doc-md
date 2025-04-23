---  
title: نسخ مصمم عنصر نموذج الماكرو VBA من القالب إلى المصنف الهدف باستخدام Node.js عبر C++  
linktitle: نسخ مصمم مستخدم النموذج التقديمي للماكرو VBA من القالب إلى كتاب العمل الهدف  
type: docs  
weight: 130  
url: /ar/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/  
description: تعلم كيفية نسخ مشروع VBA، بما في ذلك Designer Storage، من ملف Excel إلى آخر باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

 تسمح Aspose.Cells بنسخ مشروع VBA من ملف Excel إلى آخر. يتكون مشروع VBA من أنواع مختلفة من الوحدات، مثل المستند، والإجرائية، والمصمم، وغيرها. يمكن نسخ كل الوحدات باستخدام رمز بسيط، ولكن لوحدة المصمم، هناك بعض البيانات الإضافية تسمى Designer Storage التي يلزم الوصول إليها أو نسخها. تتعلق الطريقتان التاليتان بـ Designer Storage.  

- [**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-)  
- [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-)  

## **نسخ تصميم الاستوديو Form UserForm VBA Macro من القالب إلى دفتر العمل الهدف**  

يرجى الاطلاع على نموذج الشفرة التالي. ينسخ مشروع VBA من [ملف إكسل النموذجي](50528345.xlsm) إلى مصنف فارغ ويقوم بحفظه كـ [ملف إكسل الإخراج](50528346.xlsm). إذا قمت بفتح مشروع VBA داخل ملف إكسل النموذجي، سترى نموذج مستخدم كما هو موضح أدناه. يتكون نموذج المستخدم من تخزين المصمم، لذلك سيتم نسخه باستخدام طريقتي [**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-) و [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-).  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**  

تُظهر لقطة الشاشة التالية ملف إكسل الناتج ومحتوياته التي تم نسخها من ملف إكسل النموذجي. عند النقر على الزر 1، يفتح نموذج VBA المستخدم الذي يحتوي على زر أمر يظهر رسالة عند النقر عليه.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**  

## **الكود المثالي**  

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

