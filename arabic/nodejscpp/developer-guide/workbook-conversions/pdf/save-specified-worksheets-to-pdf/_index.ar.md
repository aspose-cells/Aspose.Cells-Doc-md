---
title: حفظ أوراق عمل محددة إلى PDF باستخدام Node.js عبر C++
linktitle: حفظ أوراق العمل المحددة إلى PDF
type: docs
weight: 140
url: /ar/nodejs-cpp/save-specified-worksheets-to-pdf/
description: تعرف على كيفية حفظ أوراق العمل المحددة إلى PDF باستخدام Aspose.Cells for Node.js via C++. 
---


 بشكل افتراضي، يحفظ Aspose.Cells جميع أوراق العمل **المرئية** في ملف العمل إلى ملف PDF. باستخدام خيار [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--)، يمكنك حفظ أوراق عمل محددة إلى ملف PDF. على سبيل المثال، يمكنك حفظ الورقة النشطة كـ PDF، أو حفظ جميع أوراق العمل (المرئية والمخفية) كـ PDF، أو حفظ أوراق عمل مخصصة متعددة إلى PDF.

## **حفظ الورقة العمل النشطة إلى PDF**

إذا كنت تريد تصدير الورقة النشطة فقط إلى PDF، يمكنك تحقيق ذلك عن طريق تمرير [**SheetSet.getActive()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getActive--) إلى خيار [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--).

ورقة `Sheet2` هي الورقة النشطة في ملف المصدر [sheetset-example.xlsx](sheetset-example.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");

// Open the template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Set active sheet to output
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(AsposeCells.SheetSet.getActive());

// Save the pdf file with PdfSaveOptions
workbook.save("output.pdf", pdfSaveOptions);
```

## **حفظ جميع أوراق العمل إلى PDF**

[**SheetSet.getVisible()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getVisible--) يشير إلى الأوراق المرئية في ملف العمل، و[**SheetSet.getAll()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getAll--) يشير إلى جميع الأوراق بما في ذلك الأوراق المرئية والمخفية/غير الظاهرة في ملف العمل. إذا كنت تريد تصدير جميع الأوراق إلى PDF، يمكنك ببساطة تمرير [**SheetSet.getAll()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getAll--) إلى خيار [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--).

يحتوي ملف المصدر [sheetset-example.xlsx](sheetset-example.xlsx) على جميع الأوراق الأربع مع الورقة المخفية `Sheet3`.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");

// Open the template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Set all sheets to output
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(AsposeCells.SheetSet.getAll());

// Save the pdf file with PdfSaveOptions
workbook.save("output.pdf", pdfSaveOptions);
```

## **حفظ ورقات العمل المحددة في ملف PDF**

إذا كنت تريد تصدير أوراق متعددة مرغوبة/مخصصة إلى PDF، يمكنك تحقيق ذلك بتمرير فهارس أوراق متعددة إلى خيار [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");

// Open the template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Set custom multiple sheets(Sheet1, Sheet3) to output
const sheetSet = new AsposeCells.SheetSet([0, 2]);
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(sheetSet);

// Save the pdf file with PdfSaveOptions
workbook.save("output.pdf", pdfSaveOptions);
```

## **إعادة ترتيب أوراق العمل إلى PDF**

 إذا كنت تريد إعادة ترتيب الأوراق (على سبيل المثال، بالترتيب المعكوس) إلى PDF بدون تعديل ملف المصدر، يمكنك تحقيق ذلك بتمرير فهارس الأوراق المعادة الترتيب إلى خيار [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");
// Open the template excel file
const wb = new AsposeCells.Workbook(filePath);

// Reorder sheets(Sheet1, Sheet2, Sheet3, Sheet4) to sheets(Sheet4, Sheet3, Sheet2, Sheet1)
const sheetSet = new AsposeCells.SheetSet([3, 2, 1, 0]);
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(sheetSet);

// Save the pdf file with PdfSaveOptions
wb.save("output.pdf", pdfSaveOptions);
```

{{% alert color="primary" %}} 

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.

{{% /alert %}}
