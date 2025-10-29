---
title: تحويل ملف XLSX إلى صيغة PDF باستخدام Node.js عبر C++
linktitle: تحويل ملف XLSX إلى تنسيق PDF
type: docs
weight: 30
url: /ar/nodejs-cpp/convert-xlsx-file-to-pdf-format/
description: يوضح هذا الدليل كيفية تحويل ملف Excel (XLSX) إلى تنسيق PDF باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

يمثّل ملف PDF (تنسيق المستندات المحمول) المستندات بشكل مستقل عن البرمجيات والأجهزة ونظام التشغيل المستخدمة في إنشاء تلك المستندات. يمكن أن يكون ملف PDF مستندات تحتوي على أي تجميع من النصوص والرسومات والصور بطريقة مستقلة عن الجهاز ومستقلة عن الدقة. غالبًا ما تكون ملفات PDF مضغوطة، حيث يستغرق حجمها مساحة أقل من الملف الأصلي.

في بعض الأحيان، تحتاج إلى تحويل ملف Microsoft Excel إلى PDF. لذلك، تحتاج إلى حلاً سريعًا وآمنًا ودقيقًا وموثوقًا يتيح لك توزيع مستندات PDF حول العالم. هناك العديد من أدوات التحويل التي يمكنها أداء هذه المهمة. ولكن يجب التأكد من أن تنسيق المستند الأصلي في Excel محفوظ في ملف PDF الناتج. يجب أن تُعرض الصور والرسوم البيانية والأشكال وتنسيقات البيانات والخطوط والسمات والألوان وإعدادات صفحة الطباعة واتجاه النص والحدود والرسوم البيانية بشكل دقيق ومحدد. يضمن Aspose.Cells تحويلًا عالي الجودة.

تم تصميم هذا المستند لتوفير فهم شامل لكيفية تحويل مستند Microsoft Excel (يحتوي على الصور والرسوم البيانية والتنسيقات وما إلى ذلك) إلى PDF. ولتحقيق ذلك، يوضح كيفية إنشاء تطبيق Console بسيط في Node.js يقوم بتحويل ملف Excel إلى PDF باستخدام Aspose.Cells API. يتم إجراء التحويل بدقة عالية وبدقة فائقة.

{{% /alert %}}

## **تحويل Excel إلى PDF**

يستخدم هذا المثال ملف Excel (SampleInput.xlsx) كنموذج. يحتوي دفتر العمل على أوراق عمل مع مخططات وصور. كل ورقة تحتوي على أنواع مختلفة من التنسيقات باستخدام الخطوط والصفات والألوان وتأثيرات التظليل والحدود. توجد مخطط عمود على الورقة الأولى وصورة في الأخيرة.

### **ملف Excel القالب**

ملف النموذج يحتوي على ثلاث أوراق عمل، بما في ذلك الرسوم البيانية والصور كوسائط. تحتوي الورقة الأولى على رسوم بيانية، والورقة الأخيرة تحتوي على صورة كما هو موضح في لقطات الشاشة أدناه.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|الورقة العمل الأولى **(توقعات المبيعات)**|الورقة العمل الثانية **(تقرير المبيعات)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|الصفحة العملية الثالثة **(ادخال البيانات)**|الصفحة العملية الأخيرة **(الصورة)**|

### **عملية التحويل**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const designerFile = path.join(dataDir, "SampleInput.xlsx");
const pdfFile = path.join(dataDir, "Output.out.pdf");

try {
// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}}

إذا كانت ورقة العمل تحتوي على صيغ، فمن الأفضل استدعاء [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) مباشرة قبل تحويل ورقة العمل إلى PDF. يضمن ذلك إعادة حساب قيم الصيغ التي تعتمد عليها، وتقديم القيم الصحيحة في PDF.

{{% /alert %}}

### **النتيجة**

عند تشغيل الرمز أعلاه، يتم إنشاء ملف PDF في مجلد Files في دليل التطبيق الخاص بك.
توضح اللقطات الشاشة التالية صفحات ملف PDF. يرجى ملاحظة أن الهوامش العلوية والسفلية محتفظ بها أيضًا في ملف PDF الناتج.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|الورقة العمل الأولى **(توقعات المبيعات)**|الورقة العمل الثانية **(تقرير المبيعات)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|الصفحة العملية الثالثة **(ادخال البيانات)**|الصفحة العملية الأخيرة **(الصورة)**|
{{< app/cells/assistant language="nodejs-cpp" >}}
