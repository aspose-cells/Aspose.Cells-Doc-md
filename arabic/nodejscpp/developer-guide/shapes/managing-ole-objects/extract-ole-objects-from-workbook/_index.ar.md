---  
title: استخراج كائنات OLE من دفتر العمل باستخدام Node.js عبر C++  
linktitle: استخراج كائنات Ole من الدفتر  
type: docs  
weight: 110  
url: /ar/nodejs-cpp/extract-ole-objects-from-workbook/  
---  

{{% alert color="primary" %}}  
 في بعض الأحيان، تحتاج إلى استخراج كائنات OLE من دفتر العمل. يدعم Aspose.Cells استخراج وحفظ تلك الكائنات.

يعرض هذا المقال كيفية إنشاء تطبيق سطر أوامر في Node.js عبر C++ واستخراج كائنات OLE مختلفة من دفتر عمل مع بضعة أسطر برمجية بسيطة.  
{{% /alert %}}  

## **استخراج كائنات Ole من دفتر عمل**  

### **إنشاء دفتر عمل قالب**  

1. أنشئ دفتر عمل في Microsoft Excel.  
1. أضف مستند Word، ودفتر عمل Excel، ومستند PDF كعناصر تحكم OLE على الورقة الأولى.  

|**مستند القالب مع كائنات OLE (OleFile.xls)**|  
| :- |  
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|  

التالي، استخرج كائنات OLE واحفظها على القرص الصلب مع أنواع ملفاتها الخاصة.  

### **تنزيل وتثبيت Aspose.Cells**  

1. [تحميل Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
1. قم بتثبيته على كمبيوتر التطوير الخاص بك.  

جميع مكونات Aspose، عند التثبيت، تعمل في وضع التقييم. وضع التقييم لا يحتوي على حد زمني ويقوم فقط بحقن العلامات المائية إلى الوثائق المنتجة.  

### **إنشاء مشروع**  

ابدأ **Node.js** وأنشئ تطبيق وحدة تحكم جديد. ستُظهر هذه المثال تطبيق وحدة تحكم Node.js، لكن يمكنك أيضًا استخدام أي بيئة متوافقة مع JavaScript.  

1. إضافة الاعتمادات  
   1. أضف مرجعًا لمكون Aspose.Cells إلى مشروعك، على سبيل المثال، قم بتضمين الحزمة باستخدام وظيفة `require`:  
   ```javascript  
   const { Cells } = require("aspose.cells");  
   ```

### **استخراج كائنات Ole**  

الرمز أدناه يقوم بالعمل الفعلي للبحث واستخراج كائنات OLE. يتم حفظ كائنات الـ OLE (ملفات DOC، XLS، و PDF) على القرص.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "oleFile.xlsx"));

// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();

// Loop through all the oleobjects and extract each object in the worksheet.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);
// Specify the output filename.
let fileName = path.join(dataDir, "outOle" + i + ".");
// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Excel97To2003:
fileName += "Xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "Ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "Pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "Jpg";
break;
default:
//........
break;
}
// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = Buffer.from(ole.getObjectData());
if (ole.getObjectData() != null) {
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, "outOle" + i + ".out.xlsx"));
}
} else {
if (ole.getObjectData() != null) {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
}
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
