---  
title: تحويل Excel إلى HTML مع أداة التلميح باستخدام Node.js عبر C++  
linktitle: تحويل Excel إلى HTML مع تلميح سريع  
type: docs  
weight: 200  
url: /ar/nodejs-cpp/convert-excel-to-html-with-tooltip/  
description: تعرف على كيفية تحويل ملفات Excel إلى تنسيق HTML مع أداة التلميح لعرض النص الكامل باستخدام Aspose.Cells for Node.js via C++.  
---  

## **تحويل Excel إلى HTML مع تلميحة**

قد تكون هناك حالات يتم فيها قطع النص في HTML الناتج وتريد عرض النص الكامل كأداة تلميح عند hover. تدعم Aspose.Cells for Node.js via C++ ذلك من خلال توفير خاصية [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--). تعيين الخاصية [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--) إلى **true** سيضيف النص الكامل كأداة تلميح في HTML الناتج.

تُظهر الصورة التالية التلميح السريع في ملف HTML المولد.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

الرمز التالي يحمل ملف Excel [المصدر](98107416.xlsx) ويولد ملف HTML [الناتج](98107417.zip) مع أداة التلميح.

الكود المثالي

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "AddTooltipToHtmlSample.xlsx"));

const options = new AsposeCells.HtmlSaveOptions();
options.setAddTooltipText(true);

// Save as Markdown
workbook.save(path.join(outputDir, "AddTooltipToHtmlSample_out.html"), options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
