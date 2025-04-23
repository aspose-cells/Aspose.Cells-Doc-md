---
title: إدراج صورة خلفية إلى Excel عبر Node.js باستخدام C++
linktitle: إدراج صورة خلفية إلى إكسل
type: docs
weight: 90
url: /ar/nodejs-cpp/insert-background-image-to-excel/
description: "كيفية إدراج صورة خلفية إلى Excel باستخدام Aspose.Cells for Node.js via C++."
---

{{% alert color="primary" %}} 

يمكنك تحسين جاذبية ورقة العمل عن طريق إضافة صورة كخلفية. يمكن أن يكون هذا الميزة فعالًا إذا كان لديك صورة توضيحية خاصة للشركة تضيف لمسة من الخلفية دون حجب البيانات على الورقة. يمكنك تعيين صورة خلفية لورقة باستخدام واجهة برمجة التطبيقات Aspose.Cells.

{{% /alert %}} 

## **تعيين خلفية الورقة في Microsoft Excel**

لتعيين صورة خلفية لورقة في Microsoft Excel (على سبيل المثال، Microsoft Excel 2019):

1. من القائمة **تخطيط الصفحة**، ابحث عن خيار **إعداد الصفحة**، ثم انقر فوق خيار **الخلفية**.
1. حدد صورة لتعيين صورة خلفية للورقة.

   **تعيين خلفية لورقة**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **تعيين خلفية الورقة باستخدام Aspose.Cells for Node.js via C++**

يقوم الكود أدناه بتعيين صورة خلفية باستخدام صورة من مصدر بيانات.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const backgroundImagePath = path.join(dataDir, "background.jpg");

// Create a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Set the background image for the worksheet.
sheet.setBackgroundImage(fs.readFileSync(backgroundImagePath).buffer);

// Save the Excel file
workbook.save("outputBackImageSheet.xlsx");

// Save the HTML file
workbook.save("outputBackImageSheet.html", AsposeCells.SaveFormat.Html);
```

## مقالات ذات صلة

- [العمل مع الخلفية في ملفات ODS](/cells/ar/nodejs-cpp/working-with-background-in-ods-files/)

