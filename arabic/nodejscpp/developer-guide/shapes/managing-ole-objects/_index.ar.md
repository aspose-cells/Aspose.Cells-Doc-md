---  
title: إدارة كائنات OLE باستخدام Node.js عبر C++  
linktitle: إدارة كائنات OLE  
type: docs  
weight: 50  
url: /ar/nodejs-cpp/managing-ole-objects/  
description: تعلم كيفية إدارة كائنات OLE في Aspose.Cells for Node.js via C++. أضف، استخرج، وتفاعل مع كائنات OLE داخل أوراق العمل.  
---  

## **مقدمة**  

OLE (الربط والدمج بالكائنات) هو إطار عمل لتقنية المستندات المركبة. باختصار، المستند المركب هو شيء مثل سطح مكتبي يمكن أن يحتوي على الكائنات المرئية والمعلوماتية من جميع الأنواع: النصوص، التقاويم، الرسوم المتحركة، الصوت، الفيديو الحركي، 3D، الأخبار المحدثة باستمرار، عناصر التحكم، وهكذا. كل كائن سطح مكتبي هو كيان برنامج مستقل يمكنه التفاعل مع المستخدم والتواصل مع الكيانات الأخرى على سطح المكتب.  

يدعم الكثير من البرامج نظام OLE ويستخدم لجعل المحتوى الذي تم إنشاؤه في برنامج واحد متاحًا في آخر. على سبيل المثال، يمكنك إدراج مستند Microsoft Word في Microsoft Excel. لمعرفة أنواع المحتوى التي يمكنك إدراجها، انقر على **الكائن** في قائمة **إدراج**. تظهر البرامج المثبتة على الكمبيوتر والتي تدعم كائنات OLE في مربع **نوع الكائن**.  

### **إدراج كائنات OLE في ورقة العمل**  

يدعم Aspose.Cells for Node.js via C++ إضافة واستخراج والتعامل مع كائنات OLE في أوراق العمل. لهذا السبب، تحتوي Aspose.Cells على class [**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection)، الذي يُستخدم لإضافة كائن OLE جديد إلى المجموعة. وclass آخر، [**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject)، يمثل كائن OLE وله بعض الأعضاء المهمة:  

- تحدد الخاصية [**getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--) بيانات الصورة (الأيقونة) من نوع مصفوفة البايت. سيتم عرض الصورة لعرض كائن OLE في ورقة العمل.  
- تحدد الخاصية [**getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--) بيانات الكائن على شكل مصفوفة البايت. سيتم عرض هذه البيانات في البرنامج المعني عند النقر المزدوج على أيقونة كائن OLE.  

المثال التالي يوضح كيفية إضافة كائنات OLE إلى ورقة العمل.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "logo.jpg");

// Get the picture into the streams.
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const filePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(filePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **استخراج كائنات OLE في الدفتر**  

المثال التالي يوضح كيفية استخراج كائنات OLE في كتاب العمل. يقوم المثال بالحصول على كائنات OLE مختلفة من ملف XLS موجود ويحفظ ملفات مختلفة (DOC، XLS، PPT، PDF، إلخ) استنادًا إلى نوع تنسيق ملف كائن OLE.  

بعد تشغيل الكود، يمكننا حفظ ملفات مختلفة استنادًا إلى أنواع تنسيق كائنات OLE الخاصة بها.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();

// Loop through all the oleobjects and extract each object.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);

// Specify the output filename.
let fileName = path.join(dataDir, `ole_${i}.`);

// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Xlsx:
fileName += "xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "jpg";
break;
default:
//........
break;
}

// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = new Uint8Array(ole.getObjectData());
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, `Excel_File${i}.out.xlsx`));
}

// Create the files based on the oleobject format types.
else {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
```  

### **استخراج ملف MOL المضمن**  

يدعم Aspose.Cells for Node.js via C++ استخراج الكائنات غير الشائعة مثل MOL (ملف بيانات الجزيء التي تحتوي على معلومات حول الذرات والروابط). يوضح رمز المثال التالي استخراج ملف MOL مدمج وحفظه على القرص باستخدام هذا [ملف إكسل النموذجي](94896196.xlsx).  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "EmbeddedMolSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
let index = 1;

const worksheets = workbook.getWorksheets();
const sheetCount = worksheets.getCount();
for (let i = 0; i < sheetCount; i++) {
const sheet = worksheets.get(i);
const oles = sheet.getOleObjects();
const oleCount = oles.getCount();
for (let j = 0; j < oleCount; j++) {
const ole = oles.get(j);
const fileName = path.join(outputDir, `OleObject${index}.mol`);
const fileStream = fs.createWriteStream(fileName);
fileStream.write(Buffer.from(ole.getObjectData()));
fileStream.end();
index++;
}
}
```  

## **مواضيع متقدمة**  
- [الوصول إلى وتعديل التسمية العرضية لكائن Ole المرتبط](/cells/ar/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [تحديث كائن Ole تلقائيًا عبر Microsoft Excel باستخدام Aspose.Cells](/cells/ar/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [استخراج كائنات OLE من كتاب العمل](/cells/ar/nodejs-cpp/extract-ole-objects-from-workbook/)  
- [الحصول على معرف الفئة الخاص بكائن OLE المضمّن أو تعيينه](/cells/ar/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [إدراج ملف WAV ككائن Ole](/cells/ar/nodejs-cpp/inserting-a-wav-file-as-an-ole-object/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
