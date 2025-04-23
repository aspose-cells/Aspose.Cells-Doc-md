---
title: إدارة التعليقات والملاحظات باستخدام Node.js عبر C++
linktitle: التعليقات والملاحظات
type: docs
weight: 128
url: /ar/nodejs-cpp/comments-and-notes/
description: إدراج وإدارة التعليقات أو الملاحظات مع Aspose.Cells for Node.js via C++.
keywords: إدراج تعليقات، إدراج ملاحظات Node.js عبر C++
---

## **مقدمة**

تُستخدم التعليقات لإضافة معلومات إضافية إلى الخلايا. يوفر Aspose.Cells for Node.js via C++ طريقتين لإضافة تعليقات إلى الخلايا. الأولى هي إنشاء تعليقات يدويًا في ملف المصمم. يتم استيراد هذه التعليقات باستخدام Aspose.Cells. الثانية هي إضافة تعليقات باستخدام واجهة برمجة تطبيقات Aspose.Cells خلال التشغيل. يناقش هذا الموضوع إضافة تعليقات إلى الخلايا باستخدام API Aspose.Cells. سيتم أيضًا شرح تنسيق التعليقات.

## **إضافة تعليق**

إضافة تعليق إلى خلية عن طريق استدعاء طريقة مجموعة [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection) (الم encapsulated في كائن [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). يمكن الوصول إلى كائن [**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment) الجديد من مجموعة [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection) عن طريق تمرير فهرس التعليق. بعد الوصول إلى كائن [**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment)، قم بتخصيص ملاحظة التعليق باستخدام الخاصية [**getNote()**](https://reference.aspose.com/cells/nodejs-cpp/comment/#getNote--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **تنسيق التعليق**

من الممكن أيضًا تنسيق مظهر التعليقات عن طريق تكوين ارتفاعها، وعرضها وإعدادات الخط.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Setting the font size of a comment to 14
comment.getFont().setSize(14);

// Setting the font of a comment to bold
comment.getFont().setIsBold(true);

// Setting the height of the font to 10
comment.setHeightCM(10);

// Setting the width of the font to 2
comment.setWidthCM(2);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **إضافة صورة إلى التعليق**

مع Microsoft Excel 2007، من الممكن أيضًا وضع صورة كخلفية لتعليق الخلية. في Excel 2007، يمكن القيام بذلك من خلال الخطوات التالية. (يلزم أن يكون قد تم بالفعل إضافة تعليق للخلية.)

1. انقر بزر الماوس الأيمن فوق الخلية التي تحتوي على التعليق.
1. حدد **إظهار/إخفاء التعليقات**، وامسح أي نص من التعليق.
1. انقر على الحد للتعليق لتحديده.
1. حدد **تنسيق**، ثم **تعليق**.
1. على علامة تبويب **الألوان والخطوط**، قم بتوسيع قائمة **اللون**.
1. انقر على **ملء الآثار**.
1. على علامة تبويب **الصورة**، انقر على **تحديد صورة**.
1. العثور على الصورة وتحديدها.
1. انقر على **موافق** حتى يتم إغلاق جميع الحوارات.

توفر Aspose.Cells أيضًا هذه الميزة. فيما يلي عينة من الشفرة التي تنشئ ملف XLSX من البداية، مع إضافة تعليق إلى الخلية "A1" وتعيين صورة كخلفية لها.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
const workbook = new AsposeCells.Workbook();

// Get a reference of comments collection with the first sheet
const comments = workbook.getWorksheets().get(0).getComments();

// Add a comment to cell A1
const commentIndex = comments.add(0, 0);
const comment = comments.get(commentIndex);
comment.setNote("First note.");
comment.getFont().setName("Times New Roman");

// Load an image into stream
const bmpPath = path.join(dataDir, "logo.jpg");
const bmpData = fs.readFileSync(bmpPath);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(bmpData);

// Save the workbook
workbook.save(path.join(dataDir, "book1.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **مواضيع متقدمة**
- [تغيير اتجاه النص للتعليق](/cells/ar/nodejs-cpp/change-text-direction-of-the-comment/)
- [كيفية تغيير لون خط التعليق](/cells/ar/nodejs-cpp/how-to-change-the-comment-font-color/)
- [كيفية تعيين خلفية التعليق](/cells/ar/nodejs-cpp/how-to-set-comment-background/)
- [تعليقات متداخلة](/cells/ar/nodejs-cpp/threaded-comments/)

