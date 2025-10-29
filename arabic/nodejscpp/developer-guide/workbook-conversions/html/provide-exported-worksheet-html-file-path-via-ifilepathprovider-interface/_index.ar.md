---
title: توفير مسار ملف HTML للمصنف المصدَّر عبر واجهة IFilePathProvider باستخدام Node.js عبر C++
linktitle: توفير مسار ملف HTML لورقة العمل المصدرة عبر واجهة IFilePathProvider
type: docs
weight: 70
url: /ar/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **سيناريوهات الاستخدام المحتملة**
افترض أن لديك ملف إكسل يتضمن عدة أوراق، وتريد تصدير كل ورقة إلى ملف HTML منفصل. إذا كان لبعض الأوراق روابط إلى أوراق أخرى، فسيتم كسر تلك الروابط في الملف المصدر. لمعالجة هذه المشكلة، يوفر Aspose.Cells for Node.js via C++ واجهة [IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider)، والتي يمكنك تنفيذها لإصلاح الروابط المعطوبة.

## **توفير مسار ملف HTML لواجهة IFilePathProvider**
يرجى تنزيل [ملف إكسل النموذجي](5115213.zip) المستخدم في الكود التالي وملفات HTML المصدرة. كل هذه الملفات داخل مجلد Temp. ينبغي فك ضغطه على محرك C:. بعدها، سيصبح المجلد C:\Temp. بعدها، يمكنك فتح ملف Sheet1.html في المتصفح والنقر على الرابطين بداخله. هذه الروابط تشير إلى هذين المصنفين HTML المصدَّرين اللذين داخل مجلد C:\Temp\OtherSheets.

{{< highlight javascript >}}
 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1
{{< /highlight >}}

اللقطة الشاشية التالية تظهر كيفية الرؤية C:\Temp\Sheet1.html وروابطها

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

يعرض لقطة الشاشة التالية المصدر الخاص بـ HTML. كما ترى، فإن الروابط الآن تشير إلى مجلد C:\Temp\OtherSheets. تم تحقيق ذلك باستخدام واجهة [IFilePathProvider](https://reference.aspose.com/cells/nodejs-cpp/ifilepathprovider).

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)

## **الكود المثالي**
يرجى ملاحظة أن مجلد C:\Temp هو فقط لأغراض التوضيح. يمكنك استخدام أي مجلد تفضله ووضع [ملف إكسل النموذجي](5115211.xlsx) بداخله وتشغيل الكود المقدم. وسوف ينشئ مجلد فرعي باسم OtherSheets داخل مجلدك، ويصدر ملفات HTML لأوراق العمل الثانية والثالثة بداخله. يرجى تغيير المتغير dirPath داخل الكود المقدم وإحالته إلى المجلد الذي تختاره قبل التنفيذ.

{{% alert color="primary" %}} 

سيعمل الكود النموذجي فقط عند ضبط ترخيص Aspose.Cells. إذا حاولت تشغيل الكود بدون ضبط الترخيص، فسيدخل في حلقة لانهائية. لذلك، أضفنا عملية فحص لطباعة رسالة وإيقاف التنفيذ عندما لا يكون الترخيص مضبوطًا. يمكنك إما شراء ترخيص أو طلب ترخيص مؤقت لمدة 30 يومًا من فريق Aspose.Purchase.

{{% /alert %}} 

يرجى ملاحظة أن تعليق هذه الأسطر داخل الكود سوف يكسر الروابط في Sheet1.html، ولن تُفتح Sheet2.html أو Sheet3.html عند النقر على روابطها داخل Sheet1.html.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// Implementation of IFilePathProvider interface
class FilePathProvider extends AsposeCells.IFilePathProvider
{
// Constructor
constructor() 
{
super();
}

// Gets the full path of the file by worksheet name when exporting worksheet to html separately.
// So the references among the worksheets could be exported correctly.
getFullName(sheetName) 
{
if (sheetName === "Sheet2")
{
return "file:///" + path.join("OtherSheets", "Sheet2.html");
} 
else if (sheetName === "Sheet3") 
{
return "file:///" + path.join("OtherSheets", "Sheet3.html");
}

return "";
}
}

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
// If you will comment this line, then hyperlinks will be broken
const options = new AsposeCells.HtmlSaveOptions();
options.setFilePathProvider(new FilePathProvider());
```

إليك الكود النموذجي الكامل الذي يمكنك تنفيذه باستخدام [ملف إكسل النموذجي](5115211.xlsx) المقدم.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Implementation of IFilePathProvider interface
class FilePathProvider extends AsposeCells.IFilePathProvider
{
// Constructor
constructor() 
{
super();
}

// Gets the full path of the file by worksheet name when exporting worksheet to html separately.
// So the references among the worksheets could be exported correctly.
getFullName(sheetName) 
{
if (sheetName === "Sheet2")
{
return "file:///" + path.join("OtherSheets", "Sheet2.html");
} 
else if (sheetName === "Sheet3") 
{
return "file:///" + path.join("OtherSheets", "Sheet3.html");
}

return "";
}
}

// This is the directory path which contains the sample.xlsx file
const dirPath = path.join(__dirname, "data");

// because Aspose.Cells will always make the warning worksheet as active sheet in Evaluation mode.
//setLicense();

// Check if license is set, otherwise do not proceed
const wb = new AsposeCells.Workbook();
if (!wb.isLicensed()) {
console.log("You must set the license to execute this code successfully.");
} else {
// Test IFilePathProvider interface
testFilePathProvider();
}

function setLicense() {
const licPath = "Aspose.Cells.lic";

const lic = new AsposeCells.License();
lic.setLicense(licPath);

console.log(AsposeCells.CellsHelper.getVersion());
console.debug(AsposeCells.CellsHelper.getVersion());

process.chdir(dirPath);
}

function testFilePathProvider() {
// Create subdirectory for second and third worksheets
const otherSheetsDir = path.join(dirPath, "OtherSheets");
if (!fs.existsSync(otherSheetsDir)) {
fs.mkdirSync(otherSheetsDir);
}

// Load sample workbook from your directory
const wb = new AsposeCells.Workbook(path.join(dirPath, "Sample_filepath.xlsx"));

// Save worksheets to separate html files
// Because of IFilePathProvider, hyperlinks will not be broken.
for (let i = 0; i < wb.getWorksheets().getCount(); i++)
{
// Set the active worksheet to current value of variable i
wb.getWorksheets().setActiveSheetIndex(i);

// Create html save option
const options = new AsposeCells.HtmlSaveOptions();
options.setExportActiveWorksheetOnly(true);
// If you will comment this line, then hyperlinks will be broken
options.setFilePathProvider(new FilePathProvider());
// Sheet actual index which starts from 1 not from 0
const sheetIndex = i + 1;

let filePath = "";

// Save first sheet to same directory and second and third worksheets to subdirectory
if (i === 0) 
{
filePath = path.join(dirPath, "Sheet1.html");
} 
else 
{
filePath = path.join(otherSheetsDir, `Sheet${sheetIndex}_out.html`);
}

// Save the worksheet to html file
wb.save(filePath, options);
}
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
