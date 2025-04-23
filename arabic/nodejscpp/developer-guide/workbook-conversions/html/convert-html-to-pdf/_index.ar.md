---
title: كيفية تحويل HTML إلى PDF باستخدام Node.js عبر C++
linktitle: كيفية تحويل HTML إلى PDF
type: docs
weight: 80
url: /ar/nodejs-cpp/convert-html-to-pdf/
description: يعرض هذا الموضوع كيفية تحويل HTML إلى PDF و MHTML إلى PDF باستخدام Aspose.Cells for Node.js via C++.
keywords: تحويل HTML إلى PDF و MHTML إلى PDF باستخدام Node.js عبر C++. 
---

## **نظرة عامة**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>تحويل HTML إلى PDF</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">HTML إلى PDF باستخدام جافا سكريبت</a></li>
<li><a href="#js-convert-html-to-pdf">تحويل HTML إلى PDF باستخدام جافا سكريبت</a></li>
<li><a href="#js-convert-html-to-pdf">كيفية تحويل HTML إلى PDF باستخدام جافا سكريبت</a></li>
</ul>

## **تحويل HTML إلى PDF في Node.js باستخدام كود Node.js**
كيفية تحويل HTML إلى PDF؟ مع مكتبة [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) ، يمكنك بسهولة تحويل HTML إلى PDF برمجياً مع بضعة أسطر من الكود. Aspose.Cells for Node.js via C++ قادر على بناء تطبيقات متعددة المنصات مع القدرة على إنشاء، تعديل، تحويل، عرض وطباعة جميع ملفات Excel.

## **تحويل HTML إلى PDF باستخدام جافا سكريبت**
يعرض مثال كود جافا سكريبت التالي كيفية تحويل وثيقة HTML إلى PDF باستخدام [Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/).

1. إنشاء نسخة من فئة [HtmlLoadOptions](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/).
1. تهيئة كائن [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/).
1. حفظ مستند PDF الناتج باستدعاء طريقة Workbook.save().

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.html");

// Loads the workbook which contains hidden external links
const options = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
const book = new AsposeCells.Workbook(filePath, options);
book.save("out.pdf");
```

## **محاولة تحويل HTML إلى PDF عبر الإنترنت**

[Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML إلى PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
