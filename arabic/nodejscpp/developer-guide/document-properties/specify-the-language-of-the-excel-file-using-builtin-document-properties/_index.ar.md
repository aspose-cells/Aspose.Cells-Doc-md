---
title: تحديد لغة ملف إكسل باستخدام خصائص المستند المدمجة مع Node.js عبر C++
linktitle: تحديد لغة ملف إكسل باستخدام الخصائص المدمجة للمستند
type: docs
weight: 30
url: /ar/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **سيناريوهات الاستخدام المحتملة**

 يمكنك تغيير لغة ملف إكسل بالنقر بزر الماوس الأيمن على الملف ثم اختيار خصائص > تفاصيل ثم تحرير حقل اللغة. يرجى استخدام الخاصية [**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--) لتغييره برمجيًا باستخدام واجهات برمجة تطبيقات Aspose.Cells for Node.js via C++.

## **تحديد لغة ملف إكسل باستخدام الخصائص المدمجة للمستند**

 يخلق رمز النموذج التالي دفتر عمل ويغير الخاصية المدمجة لاسم اللغة. يرجى الاطلاع على ملف إكسل الناتج (64716891.xlsx) المولد بواسطة الكود وصورة الشاشة التي تظهر حقل اللغة المعدل بواسطة الخاصية [**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--).

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object.
const wb = new AsposeCells.Workbook();

// Access built-in document property collection.
const bdpc = wb.getBuiltInDocumentProperties();

// Set the language of the Excel file.
bdpc.setLanguage("German, French");

// Save the workbook in xlsx format.
wb.save(path.join(outputDir, "outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
