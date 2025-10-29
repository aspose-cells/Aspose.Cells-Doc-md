---
title: إعادة العينات للصور المضافة  تحويل Excel إلى PDF باستخدام Node.js عبر C++
linktitle: إعادة العينات للصور المضافة
type: docs
weight: 150
url: /ar/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/
description: تعرف على كيفية ضغط الصور المضافة في ملفات Excel لتقليل حجم ملف PDF وتحسين أداء التحويل باستخدام Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

عند العمل مع ملفات Excel الكبيرة التي تحتوي على الكثير من الصور، قد تحتاج إلى ضغط الصور التي تم إضافتها لتقليل حجم ملف PDF الناتج وتحسين أداء التحويل بشكل عام. Aspose.Cells for Node.js via C++ يدعم إعادة العينات للصور المضافة لتقليل حجم ملف PDF الناتج وتحسين الأداء إلى حد ما.

{{% /alert %}}

يرجى الاطلاع على الكود النموذجي التالي الذي يصف كيفية إجراء المهمة باستخدام واجهة برمجة التطبيقات Aspose.Cells. النموذج يحول ملف Microsoft Excel إلى ملف PDF مع ضغط الصور في الملف.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Instantiate the PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
// Set Image Resample properties
pdfSaveOptions.setImageResample(300, 70);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile_out_pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}

باستخدام خيار [**setImageResample(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#setImageResample-number-number-) يقلل من حجم ملف PDF الناتج ولكنه قد يؤثر على جودة الصورة قليلاً.

{{% /alert %}} {{% alert color="primary" %}}

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
