---  
title: Node.js kullanarak Template den Target Çalışma Kitabına VBA Macro UserForm DesignerStorage Kopyalama  
linktitle: Taslak ve Hedef Çalışbook Arasında VBA Makro Kullanıcı Formu Tasarımcı Depolama Alanını Kopyalama  
type: docs  
weight: 130  
url: /tr/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/  
description: Aspose.Cells for Node.js via C++ kullanarak bir VBA projesini, Designer Storage dahil olmak üzere, bir Excel dosyasından diğerine nasıl kopyalayacağınızı öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Aspose.Cells, bir Excel dosyasından diğerine VBA projesi kopyalamanıza olanak tanır. Bir VBA projesi, çeşitli modül tiplerinden oluşur: Belge, Yordam, Designer vb. Tüm modüller basit kodla kopyalanabilir, ancak Designer modülü için erişilmesi veya kopyalanması gereken Designer Storage adı verilen ek veriler vardır. Aşağıdaki iki yöntem Designer Storage ile ilgilidir.  

- [**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-)  
- [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-)  

## **Taslak ve Hedef Çalışbook Arasında VBA Makro Kullanıcı Formu Tasarımcı Depolama Alanını Kopyalama**  

Lütfen aşağıdaki örnek kodu inceleyin. Bu kod, [şablon Excel dosyasından](50528345.xlsm) VBA projesini boş bir çalışma kitabına kopyalar ve [çıktı Excel dosyası](50528346.xlsm) olarak kaydeder. Şablon Excel dosyasının içindeki VBA projesini açarsanız, aşağıda gösterildiği gibi bir Kullanıcı Formu göreceksiniz. Kullanıcı Formu, Tasarımcı Depolama içerir, bu nedenle [**VbaModuleCollection.getDesignerStorage(string)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#getDesignerStorage-string-) ve [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-) metodları kullanılarak kopyalanacaktır.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**  

Aşağıdaki ekran görüntüsü, kopyalanan şablon Excel dosyasından çıktı Excel dosyasını ve içeriğini gösterir. Buton 1'e tıkladığınızda VBA Kullanıcı Formu açılır ve kendisi de tıklamada mesaj kutusu gösteren bir komut düğmesine sahiptir.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**  

## **Örnek Kod**  

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

