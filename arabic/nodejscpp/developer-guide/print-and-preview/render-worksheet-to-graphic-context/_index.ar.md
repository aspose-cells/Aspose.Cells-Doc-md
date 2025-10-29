---
title: عرض ورقة العمل على السياق الرسومي مع Node.js عبر C++
linktitle: تقديم ورقة العمل إلى السياق الرسومي
type: docs
weight: 300
url: /ar/nodejs-cpp/render-worksheet-to-graphic-context/
description: تعرف على كيفية عرض ورقة العمل على سياق رسومي باستخدام Aspose.Cells for Node.js via C++. يتضمن ذلك العرض لملفات الصور، والشاشات، والطابعات.
---

{{% alert color="primary" %}}

يمكن الآن لـ Aspose.Cells عرض أوراق العمل على سياق رسومي. يمكن أن يكون السياق الرسومي أي شيء مثل ملف صورة، أو شاشة، أو طابعة، وما إلى ذلك. يرجى استخدام أحد الطريقتين التاليين لعرض ورقة العمل على سياق رسومي.

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

يوضح الكود التالي كيفية استخدام Aspose.Cells لعرض ورقة عمل على سياق رسومي. بمجرد تنفيذ الكود، سيتم طباعة كامل ورقة العمل وملء المساحة الفارغة المتبقية باللون الأزرق في السياق الرسومي وحفظ الصورة كملف **OutputImage_out_.png**. يمكنك استخدام أي ملف Excel كمصدر لتجربة هذا الكود. يرجى أيضًا قراءة التعليقات داخل الكود لفهم أفضل.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleBook.xlsx");
// Create workbook object from source file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create empty image buffer
const bmpOptions = new AsposeCells.ImageOrPrintOptions();
bmpOptions.setOnePagePerSheet(true);

// Render worksheet to image
const sheetRender = new AsposeCells.SheetRender(worksheet, bmpOptions);
sheetRender.toImage(0, dataDir + "/OutputImage_out.png");

// Save the image in Png format
```
{{< app/cells/assistant language="nodejs-cpp" >}}
