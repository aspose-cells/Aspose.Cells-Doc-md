---
title: تحديد عدد الصفحات المُنتجة  تحويل إكسيل إلى PDF عبر Node.js باستخدام C++
linktitle: تحديد عدد الصفحات المولدة  تحويل Excel إلى PDF
type: docs
weight: 180
url: /ar/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: تعلم كيفية تحديد عدد الصفحات التي يتم إنشاؤها عند تحويل جدول بيانات إكسيل إلى PDF باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

أحيانًا، تريد طباعة مدى معين من الصفحات إلى ملف PDF خارجي. Aspose.Cells for Node.js via C++ لديه القدرة على ضبط حد لعدد الصفحات التي يتم إنشاؤها عند تحويل جدول بيانات إكسيل إلى صيغة ملف PDF.

{{% /alert %}}

## **تحديد الحد الأقصى لعدد الصفحات المولدة**

المثال التالي يظهر كيفية عرض مجموعة من الصفحات (3 و 4) في ملف Microsoft Excel إلى صيغة PDF.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Instantiate the PdfSaveOption
const options = new AsposeCells.PdfSaveOptions();

// Print only Page 3 and Page 4 in the output PDF
// Starting page index (0-based index)
options.setPageIndex(3);
// Number of pages to be printed
options.setPageCount(2);

// Save the PDF file
workbook.save(path.join(dataDir, "outPDF1.out.pdf"), options);
```

{{% alert color="primary" %}}

إذا كانت الورقة تحتوي على صيغ، فمن الأفضل استدعاء [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) قبل عرضها كملف PDF. يضمن ذلك إعادة حساب القيم المعتمدة على الصيغة، وعرض القيم الصحيحة في الملف الناتج.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
