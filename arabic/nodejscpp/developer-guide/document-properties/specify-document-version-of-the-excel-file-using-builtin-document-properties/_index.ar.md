---  
title: تحديد إصدار المستند لملف إكسل باستخدام خصائص المستند المدمجة مع Node.js عبر C++  
linktitle: تحديد إصدار المستند لملف الإكسل باستخدام خصائص المستند المضمنة  
type: docs  
weight: 20  
url: /ar/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/  
description: تعلم كيفية تحديد إصدار مستند ملف إكسل برمجيًا باستخدام خصائص المستند المدمجة مع Node.js عبر C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

 يمكنك تغيير **رقم الإصدار** لملف إكسل بالنقر بزر الماوس الأيمن على الملف ثم اختيار خصائص > تفاصيل ثم تحرير حقل **رقم الإصدار**. يرجى استخدام الخاصية [**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--) لتغييره برمجيًا باستخدام واجهات برمجة تطبيقات Aspose.Cells.  

## **تحديد إصدار المستند لملف الإكسل باستخدام خصائص المستند المضمنة**  

 يخلق رمز النموذج التالي دفتر عمل ويغير خصائص المستند المدمجة التي تشمل العنوان، المؤلفين، ورقم الإصدار. يرجى الاطلاع على ملف إكسل الناتج (64716811.xlsx) المولد بواسطة الكود وصورة الشاشة التي تظهر رقم الإصدار المعدل بواسطة الخاصية [**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--).  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "outputSpecifyDocumentVersionOfExcelFile.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access built-in document property collection
const bdpc = wb.getBuiltInDocumentProperties();

// Set the title
bdpc.setTitle("Aspose File Format APIs");

// Set the author
bdpc.setAuthor("Aspose APIs Developers");

// Set the document version
bdpc.setDocumentVersion("Aspose.Cells Version - 18.3");

// Save the workbook in xlsx format
wb.save(filePath, AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
