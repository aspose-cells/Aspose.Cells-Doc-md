---
title: تصفية مشروع VBA أثناء تحميل مصنف باستخدام Node.js عبر C++
linktitle: تصفية مشروع VBA أثناء تحميل جدول عمل
type: docs
weight: 140
url: /ar/nodejs-cpp/filter-vba-project-while-loading-a-workbook/
description: تعلم كيف تصفِّ مشروع VBA أثناء تحميل مصنفات Excel باستخدام Aspose.Cells for Node.js via C++.
---

## **تصفية مشروع VBA أثناء تحميل مصنف Excel في Node.js عبر C++**

بعض ملفات .xlsm/.xslb تحتوي على كمية هائلة من الماكرو (أو ماكرو طويل جدًا جدًا). Aspose.Cells for Node.js via C++ سيقوم بتحميل هذه (البيانات الوصفية) بدون شروط عند فتح مثل هذه المصنفات. قد تحتاج إلى التحكم في ذلك [**LoadDataFilterOptions**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) عندما تحتاج حقًا إلى استخراج أسماء الأوراق لمجموعة كبيرة من المصنفات، وبالتالي تتخطى المحتوى غير الضروري. يُقدم هذا الفلتر عن طريق إدخال خيار جديد، [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions).

## **الكود المثالي**

يحمل الرمز العيني التالي عملاق العمل حتى يتم تصفية VBA فقط. يمكن تنزيل ملف عينة لاختبار هذه الميزة من الرابط التالي:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Set the load options, we do not want to load VBA
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);
const loadFilter = new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.VBA);
loadOptions.setLoadFilter(loadFilter);

// Create workbook object from sample excel file using load options
const book = new AsposeCells.Workbook(path.join(sourceDir, "sampleMacroEnabledWorkbook.xlsm"), loadOptions);

// Save the output in pdf format
book.save(outputDir + "OutputSampleMacroEnabledWorkbook.xlsm", AsposeCells.SaveFormat.Xlsm);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
