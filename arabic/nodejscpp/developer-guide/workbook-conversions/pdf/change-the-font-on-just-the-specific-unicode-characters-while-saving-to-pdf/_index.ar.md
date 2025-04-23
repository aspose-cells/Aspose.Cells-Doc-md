---
title: تغيير الخط على الأحرف اليونيكود المحددة فقط عند الحفظ إلى PDF باستخدام Node.js عبر C++
linktitle: تغيير الخط فقط في الأحرف اليونيكود المحددة أثناء الحفظ إلى PDF
type: docs
weight: 260
url: /ar/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: تعلم كيفية تغيير خط الأحرف اليونيكود المحددة عند الحفظ إلى PDF باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

بعض الأحرف اليونيكود غير قابلة للعرض بواسطة الخط المحدد من قبل المستخدم. أحد الأحرف اليونيكود هو **الشرطة الغير قابلة للانفصال** (U+2011) ورقمه اليونيكود هو 8209. هذا الحرف لا يمكن عرضه باستخدام الخط **تايمز نيو رومان**, ولكن يمكن عرضه بالخطوط الأخرى مثل **أريال يونيكود ام اس**.

 عندما يحدث مثل هذا الحرف داخل كلمة أو جملة وكانت الخط المستخدم مثل Times New Roman، فإن Aspose.Cells يغير خط كامل الكلمة أو الجملة إلى خط يمكنه عرض هذا الحرف، مثل Arial Unicode إلى MS.

 ومع ذلك، هذا سلوك غير مرغوب لبعض المستخدمين ويرغبون في تغيير خط الحرف المحدد فقط بدلاً من تغيير خط الكلمة أو الجملة بأكملها.

 لمعالجة هذه المشكلة، توفر Aspose.Cells خاصية `PdfSaveOptions.isFontSubstitutionCharGranularity` التي يجب تعيينها على true بحيث يتغير خط الأحرف غير القابلة للعرض فقط إلى خط قابل للعرض، بينما تبقى بقية الكلمة أو الجملة في الخط الأصلي.

{{% /alert %}} 

## **مثال**
الصورة المرفقة تقارن بين ملفي PDF الناتجين من الشفرة النموذجية التالية.

 يتم إنشاء أحد الملفين بدون ضبط خاصية `PdfSaveOptions.isFontSubstitutionCharGranularity` والآخر بعد تعيينها على true.

كما ترى في أول ملف PDF، تغير خط الجملة بأكملها من Times New Roman إلى Arial Unicode MS بسبب الهايبن غير القابل للكسر. بينما في الملف الثاني، تغير خط الهايبن غير القابل للكسر فقط.

|**ملف PDF الأول**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**ملف PDF الثاني**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **الكود المثالي**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cells
const cell1 = worksheet.getCells().get("A1");
const cell2 = worksheet.getCells().get("B1");

// Set the styles of both cells to Times New Roman
let style = cell1.getStyle();
style.getFont().setName("Times New Roman");
cell1.setStyle(style);
cell2.setStyle(style);

// Put the values inside the cell
cell1.putValue("Hello without Non-Breaking Hyphen");
cell2.putValue("Hello" + String.fromCharCode(8209) + " with Non-Breaking Hyphen");

// Autofit the columns
worksheet.autoFitColumns();

// Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
workbook.save(path.join(dataDir, "SampleOutput_out.pdf"));

// Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
const opts = new AsposeCells.PdfSaveOptions();
opts.setIsFontSubstitutionCharGranularity(true);
workbook.save(path.join(dataDir, "SampleOutput2_out.pdf"), opts);
```



