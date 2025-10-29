---
title: مخرجات صفحة فارغة عندما لا يوجد شيء للطباعة باستخدام Node.js عبر C++
linktitle: إخراج صفحة فارغة عند عدم وجود شيء للطباعة
type: docs
weight: 90
url: /ar/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/
---

## **سيناريوهات الاستخدام المحتملة**

إذا كانت الورقة فارغة، فلن تطبع Aspose.Cells شيئًا عند تصدير ورقة العمل إلى صورة. يمكنك تغيير هذا السلوك باستخدام خاصية [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--). عند ضبطها **true**، ستطبع الصفحة الفارغة.

## **إخراج صفحة فارغة عند عدم وجود شيء للطباعة**

المثال التالي ينشئ دفتر عمل فارغ يحتوي على ورقة عمل فارغة ويعرض ورقة العمل الفارغة على صورة بعد تعيين خاصية [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--) إلى **true**. ونتيجة لذلك، يتم إنشاء صفحة فارغة لأنه لا يوجد شيء للطباعة، كما يمكنك رؤية ذلك في الصورة أدناه.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet - it is empty sheet
const ws = wb.getWorksheets().get(0);

// Specify image or print options
// Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
// So that empty page gets printed
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Png);
opts.setOutputBlankPageWhenNothingToPrint(true);

// Render empty sheet to png image
const sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, path.join(outputDir, "OutputBlankPageWhenNothingToPrint.png"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
