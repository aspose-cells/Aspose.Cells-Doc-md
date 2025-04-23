---
title: تعيين نص مدخلات أسطورة المخطط لملء لا شيء باستخدام Aspose.Cells for Node.js via C++
linktitle: ضبط نص إدخال وسام الرسم البياني على لا شيء باستخدام Aspose.Cells
description: تعلم كيفية استخدام Aspose.Cells for Node.js via C++ لضبط نص مدخلات أسطورة المخطط إلى لا شيء. سيُظهر دليلنا كيفية تعديل لون ملء مداخل الأسطورة في مخططات Microsoft Excel لتحسين التصور والتخصيص.
keywords: Aspose.Cells for Node.js via C++، ملء مدخلات أسطورة المخطط، Microsoft Excel، التصور، التخصيص.
type: docs
weight: 320
url: /ar/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

إذا كنت ترغب في تعيين نص مدخلات أسطورة المخطط إلى لا شيء حتى لا يتم عرضها داخل أسطورة المخطط، يرجى تعيين [**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/nodejs-cpp/legendentry/#isTextNoFill--) إلى **true**.

{{% /alert %}}

يقوم الكود العينة التالي بتعيين نص إدخال تسمية المخطط الثاني إلى لا شيء. يرجى تنزيل [ملف Excel عينة](5115219.xlsx) المستخدم في هذا الكود و[ملف Excel الخرج](5115217.xlsx) الذي تم إنشاؤه به للرجوع إليه.

 تبرز لقطة الشاشة التالية تأثير هذا الكود على [ملف Excel النموذجي](5115219.xlsx).

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Sample.xlsx"));

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = sheet.getCharts().get(0);

// Set text of second legend entry fill to none
chart.getLegend().getLegendEntries().get(1).setIsTextNoFill(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "ChartLegendEntry_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
