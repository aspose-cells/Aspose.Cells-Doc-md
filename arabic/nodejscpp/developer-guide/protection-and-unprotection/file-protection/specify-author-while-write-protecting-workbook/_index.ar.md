---  
title: تحديد المؤلف أثناء حماية حقوق الطباعة للملف باستخدام Node.js عبر C++  
linktitle: تحديد المؤلف أثناء حماية كتاب العمل  
type: docs  
weight: 40  
url: /ar/nodejs-cpp/specify-author-while-write-protecting-workbook/  
description: تحديد اسم مؤلف أثناء حماية حقوق الطباعة لمصنف باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**

 يمكنك تحديد اسم مؤلف أثناء حماية حقوق الطباعة لمصنف باستخدام Aspose.Cells API. يرجى استخدام خاصية [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--) لهذا الغرض.

## **تحديد المؤلف أثناء حماية كتاب العمل**

يوضح رمز النموذج التالي استخدام خاصية [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--). ينشئ الكود مصنف فارغ، ويحميه بكلمة مرور، ويحدد اسم المؤلف، ويحفظه باسم [ملف Excel الناتج](67338582.xlsx). توضح لقطة الشاشة التالية تأثير رمز النموذج على ملف Excel الناتج لمعاينتك.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Create empty workbook.
const workbook = new AsposeCells.Workbook();

// Write protect workbook with password.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Specify author while write protecting workbook.
workbook.getSettings().getWriteProtection().setAuthor("SimonAspose");

// Save the workbook in XLSX format.
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx"));
```  

