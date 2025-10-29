---  
title: استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML باستخدام Node.js عبر C++  
linktitle: استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML  
type: docs  
weight: 30  
url: /ar/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/  
description: تعلم كيفية استبعاد الأنماط غير المستخدمة عند تحويل Excel إلى HTML باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

قد يحتوي ملفات Microsoft Excel على العديد من الأنماط غير المستخدمة. عند تصدير ملف Excel إلى تنسيق HTML، يتم تصدير هذه الأنماط غير المستخدمة أيضًا. يمكن أن يزيد ذلك من حجم الـ HTML. يمكنك استبعاد الأنماط غير المستخدمة أثناء تحويل ملفات Excel إلى HTML باستخدام الخاصية [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--). عند تعيينها على **true**، يتم استبعاد جميع الأنماط غير المستخدمة من الـ HTML الناتج. تعرض لقطة الشاشة التالية مثالًا على نمط غير مستخدم داخل الـ HTML الناتج.  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML**  

ينشئ رمز المثال التالي كتاب عمل ويُنشئ نمطًا باسم غير مستخدم. بما أن [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--) مَعين على **true**، فلن يتم تصدير هذا النمط غير المستخدم إلى [HTML الناتج](61767778.zip). ولكن إذا قمت بضبطها على **false**، فسيكون هذا النمط غير المستخدم موجودًا داخل الـ HTML الناتج ويمكنك رؤيته في تنسيق HTML كما هو موضح في لقطة الشاشة أعلاه.  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const wb = new AsposeCells.Workbook();

// Create an unused named style
wb.createStyle().setName("UnusedStyle_XXXXXXXXXXXXXX");

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Put some value in cell C7
ws.getCells().get("C7").putValue("This is sample text.");

// Specify html save options, we want to exclude unused styles
const opts = new AsposeCells.HtmlSaveOptions();

// Comment this line to include unused styles
opts.setExcludeUnusedStyles(true);

// Save the workbook in html format
wb.save("outputExcludeUnusedStylesInExcelToHTML.html", opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
