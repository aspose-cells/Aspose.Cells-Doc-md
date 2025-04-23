---  
title: استبدال النص في دفتر العمل باستخدام التعبيرات العادية مع Node.js عبر C++  
linktitle: استبدال النص في دفتر العمل باستخدام التعبير العادي  
type: docs  
weight: 90  
url: /ar/nodejs-cpp/replace-text-in-a-workbook-using-regular-expression/  
description: استبدال النص في دفتر العمل باستخدام التعبيرات العادية في Node.js عبر C++.  
---  

يقدم Aspose.Cells ميزة استبدال النص في دفتر العمل باستخدام التعبيرات العادية. لهذا، توفر API الخاص [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) الخاص بفئة [**ReplaceOptions**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions). تحديد [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) على أنه **true** يشير إلى أن المفتاح المقصود سيكون تعبيرًا عاديًا.

يوضح مقتطف الكود التالي استخدام الخاصية [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) باستخدام ملف Excel النموذجي ([ملف Excel sample](101089318.xlsx)). المخرجات ([ملف الإخراج](101089319.xlsx)) التي تم إنشاؤها بواسطة المقتطف مرفقة للمرجعية.

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "SampleRegexReplace.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const replace = new AsposeCells.ReplaceOptions();
replace.setCaseSensitive(false);
replace.setMatchEntireCellContents(false);
// Set to true to indicate that the searched key is regex
replace.setRegexKey(true);

workbook.replace("\\bKIM\\b", "^^^TIM^^^", replace);
workbook.save(path.join(outputDir, "RegexReplace_out.xlsx"));
```  

