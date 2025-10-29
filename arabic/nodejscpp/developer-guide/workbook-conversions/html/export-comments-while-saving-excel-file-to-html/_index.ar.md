---
title: تصدير التعليقات عند حفظ ملف Excel إلى HTML باستخدام Node.js عبر C++
linktitle: تصدير التعليقات أثناء حفظ ملف Excel إلى HTML
type: docs
weight: 40
url: /ar/nodejs-cpp/export-comments-while-saving-excel-file-to/
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel الخاص بك إلى HTML، لن يتم تصدير التعليقات. ومع ذلك، توفر Aspose.Cells for Node.js via C++ هذه الميزة باستخدام الخاصية [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/). عند تعيينها على **true**، ستعرض HTML أيضًا التعليقات الموجودة في ملف Excel الخاص بك.

## **تصدير التعليقات أثناء حفظ ملف Excel إلى HTML**

يشرح الكود العيني التالي استخدام الخاصية [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/). توضح اللقطة الشاشية تأثير الكود على الHTML عندما يتم تعيينها إلى **true**. يرجى تحميل [ملف Excel العيني](50528260.xlsx) و[HTML المُنشئ](5052826.txt) للرجوع إليها.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const sourceDir = path.join(__dirname, "data");
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportCommentsHTML.xlsx"));

// Export comments - set IsExportComments property to true
const opts = new AsposeCells.HtmlSaveOptions();
opts.setIsExportComments(true);

// Save the Excel file to HTML
const outputDir = path.join(__dirname, "output");
wb.save(path.join(outputDir, "outputExportCommentsHTML.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
