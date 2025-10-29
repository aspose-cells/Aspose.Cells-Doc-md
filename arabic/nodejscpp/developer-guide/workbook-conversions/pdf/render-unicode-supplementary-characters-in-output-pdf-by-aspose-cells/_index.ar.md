---
title: عرض الأحرف الفرعية المتمددة في PDF المخرجة بواسطة Aspose.Cells for Node.js via C++
linktitle: تقديم الحروف الأعلى من يونيكود في ملف PDF الناتج باستخدام Aspose.Cells
type: docs
weight: 350
url: /ar/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: تعلم كيفية عرض الأحرف الفرعية المتمددة في PDF المخرجة باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

الحروف اليونيكود العادية طول كل منها 2 بايت بينما الحروف اليونيكود الأعلى طول كل منها 4 بايت. Aspose.Cells الآن يدعم تقديم هذه الحروف اليونيكود الأعلى بطول 4 بايت.

في معيار الحروف اليونيكود، الحروف الأعلى هي الحروف التي تم تخصيص نقاط الرموز لها من U+10000 إلى U+10FFFF. وبمعنى آخر، هذه هي الحروف اليونيكود التي تكون أكبر من U+FFFF.

- في UTF-8 طول كل من هذه الحروف هو 4 بايت.
- في UTF-16، هذه الحروف تتطلب 2 حروف دعائية (وحدات بت بطول 16).

{{% /alert %}}

## عرض الأحرف الفرعية المتمددة في PDF المخرجة بواسطة Aspose.Cells for Node.js via C++

تُظهر لقطة الشاشة التالية كيفية عرض Aspose.Cells لملف إكسيل المصدر([ملف إكسيل](5115563.xlsx)) في PDF الناتج([ملف PDF](5115564.pdf)). كما ترى، تم عرض جميع الأحرف الفرعية المتمددة الثلاثة بشكل مطابق تمامًا لما قام به Microsoft Excel.

![todo:image_alt_text](output.png)

## كود عينة

يمكنك استخدام هذا الكود العيني لتحويل [ملف Excel المصدر](5115563.xlsx) إلى [PDF الناتج](5115564.pdf).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file containing Unicode Supplementary characters
const workbook = new AsposeCells.Workbook(path.join(dataDir, "unicode-supplementary-characters.xlsx"));

// Save the workbook
workbook.save(path.join(dataDir, "RenderUnicodeInOutput_out.pdf"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
