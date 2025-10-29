---
title: تعيين أولوية خاصية DefaultFont في PdfSaveOptions و ImageOrPrintOptions باستخدام Node.js عبر C++
linktitle: تعيين خاصية DefaultFont في خيارات PdfSave و ImageOrPrint لديها الأولوية
type: docs
weight: 30
url: /ar/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: اكتشف كيفية تعيين خاصية DefaultFont في PdfSaveOptions و ImageOrPrintOptions باستخدام Aspose.Cells for Node.js via C++. ضمان عرض الخط بشكل صحيح عند عدم وجود الخطوط.
---

## **سيناريوهات الاستخدام المحتملة**

أثناء ضبط خاصية **DefaultFont** لـ [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) و [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/)، قد تتوقع أن يقوم الحفظ إلى ملف PDF أو صورة بضبط ذلك DefaultFont لجميع النص في مصفوفة العمل الذي يحتوي على خط مفقود (غير مثبت).

عند الحفظ بصيغة PDF أو كصورة، سيحاول Aspose.Cells for Node.js via C++ أولاً تعيين الخط الافتراضي لكتاب العمل (أي، `Workbook.DefaultStyle.Font`). إذا لم يتمكن الخط الافتراضي للكتاب من عرض النص بشكل صحيح، فسيحاول Aspose.Cells العرض باستخدام الخط المذكور مقابل خاصية DefaultFont في [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/).

للتعامل مع توقعاتك، لدينا خاصية بولية تسمى "**CheckWorkbookDefaultFont**" في [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/). يمكنك ضبطها على **false** لتعطيل محاولة الخط الافتراضي للمصفوفة العمل أو ترك الإعداد **DefaultFont** في [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) ليكون له الأولوية.

## **تعيين خاصية DefaultFont في خيارات PdfSave/ImageOrPrintOptions**

يفتح رمز النموذج التالي ملف Excel. الخلية A1 في ورقة العمل الأولى تحتوي على نص مضبط ليكون "نص خط وقت عيد الميلاد". اسم الخط هو "Christmas Time Personal Use" غير مثبت على الجهاز. نقوم بضبط خاصية **DefaultFont** لـ [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) إلى "Times New Roman". ونضبط الخاصية **CheckWorkbookDefaultFont** إلى **"false"** لضمان عرض نص الخلية A1 باستخدام خط "Times New Roman" وعدم استخدام الخط الافتراضي للملف ("Calibri" في هذه الحالة). يقوم الكود بعرض ورقة العمل الأولى بصيغة PNG و TIFF، وأخيرًا بصيغة ملف PDF.

{{% alert color="primary" %}}

القيمة الافتراضية لخاصية **CheckWorkbookDefaultFont** هي **true**.

{{% /alert %}}

هذه هي صورة الشاشة من [ملف القالب](49446913.xlsx) المستخدم في كود المثال.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

هذه هي صورة PNG الناتجة بعد ضبط الخاصية [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) على "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

انظر الصورة [TIFF](48496672.tiff) الناتجة بعد ضبط الخاصية [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) على "Times New Roman".

انظر ملف [PDF](48496673.pdf) الناتج بعد ضبط الخاصية [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) على "Times New Roman".

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open an Excel file.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleSetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.xlsx"));

// Rendering to PNG file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
const imgOpt = new AsposeCells.ImageOrPrintOptions();
imgOpt.setImageType(AsposeCells.ImageType.Png);
imgOpt.setCheckWorkbookDefaultFont(false);
imgOpt.setDefaultFont("Times New Roman");
const sr = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imgOpt);
sr.toImage(0, path.join(outputDir, "out1_imagePNG.png"));

// Rendering to TIFF file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
imgOpt.setImageType(AsposeCells.ImageType.Tiff);
const wr = new AsposeCells.WorkbookRender(workbook, imgOpt);
wr.toImage(path.join(outputDir, "out1_imageTIFF.tiff"));

// Rendering to PDF file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setDefaultFont("Times New Roman");
saveOptions.setCheckWorkbookDefaultFont(false);
workbook.save(path.join(outputDir, "out1_pdf.pdf"), saveOptions);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
