---
title: تصفية الأسماء المحددة أثناء تحميل دفتر العمل بواسطة Node.js عبر C++
linktitle: تصفية أسماء محددة أثناء تحميل المصنف
type: docs
weight: 50
url: /ar/nodejs-cpp/filter-defined-names-while-loading-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

يسمح Aspose.Cells لك بتصفية أو إزالة الأسماء المعرفة الموجودة داخل المصنف. يرجى استخدام [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) لتحميل الأسماء المعرف عليها واستخدام [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) لإزالتها أثناء تحميل المصنف. يرجى ملاحظة، إذا قمت بإزالة الأسماء المعرفة، قد تتعطل الصيغ داخل المصنف.

## **تصفية أسماء محددة أثناء تحميل المصنف**

يقوم الرمز النموذجي التالي بتحميل [ملف Excel النموذجي](61767860.xlsx) الذي يحتوي على صيغة في الخلية **C1** تحتوي على الأسماء المحددة i.e. * =SUM(MyName1, MyName2)*. نظرًا لأننا نستخدم [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) لإزالة الأسماء المحددة أثناء تحميل دفتر العمل، تتعطل الصيغة في الخلية C1 في [ملف Excel الناتج](61767861.xlsx) وتظهر *#NAME?*. يرجى الاطلاع على الصورة التالية التي تُظهر تأثير الكود على ملف Excel النموذجي.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFilterDefinedNamesWhileLoadingWorkbook.xlsx");
// Specify the load options
let opts = new AsposeCells.LoadOptions();
// We do not want to load defined names
opts.setLoadFilter(new AsposeCells.LoadFilter(~AsposeCells.LoadDataFilterOptions.DefinedNames));

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath, opts);

// Save the output Excel file, it will break the formula in C1
workbook.save(path.join(dataDir, "outputFilterDefinedNamesWhileLoadingWorkbook.xlsx"));

console.log("FilterDefinedNamesWhileLoadingWorkbook executed successfully.");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
