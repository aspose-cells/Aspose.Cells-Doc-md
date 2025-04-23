---
title: تحويل ملف XLS مع الصور أو المخططات إلى PDF باستخدام Node.js عبر C++
linktitle: تحويل ملف XLS الذي يحتوي على صور أو رسومات إلى PDF
type: docs
weight: 50
url: /ar/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

يدعم Aspose.Cells تحويل ملفات XLS التي تحتوي على صور ومخططات إلى مستندات PDF. يمكن لـ Aspose.Cells for Node.js via C++ العمل بشكل مستقل لتحويل جدول بيانات إلى PDF: لا يلزم Aspose.PDF لـ Node.js عبر C++ لإتمام التحويل. يمكن إتمام العملية في الذاكرة حيث لا تعتمد على ملفات XML مؤقتة أو وسيطة. هذا يعني أن ملفات Excel الكبيرة، مثل تلك التي تحتوي على صور ومخططات وأشياء رسومية أخرى، يمكن تحويلها بسرعة وفعالية.

{{% /alert %}} 
## **الكود المثالي**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
try {
// Get the template excel file path.
const designerFile = path.join(dataDir, "SampleInput.xls");

// Specify the pdf file path.
const pdfFile = path.join(dataDir, "Output.out.pdf");

// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}} 

إذا كان جدول البيانات يحتوي على صيغ، من الأفضل استدعاء طريقة [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) قبل تصديره إلى PDF. يضمن ذلك إعادة حساب القيم المعتمدة على الصيغ، وظهور القيم الصحيحة في PDF.

{{% /alert %}}
