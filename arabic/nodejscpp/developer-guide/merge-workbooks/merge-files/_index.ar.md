---
title: دمج الملفات باستخدام Node.js عبر C++
linktitle: دمج الملفات
type: docs
weight: 20
url: /ar/nodejs-cpp/merge-files/
---

## **مقدمة**

يوفر Aspose.Cells طرقًا مختلفة لدمج الملفات. للملفات البسيطة التي تحتوي على بيانات، تنسيقات، وصيغ، يمكن استخدام طريقة [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-) لدمج عدة دفاتر عمل، ويمكن استخدام طريقة [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-) لنسخ أوراق العمل إلى دفتر عمل جديد. هذه الطرق سهلة الاستخدام وفعالة، ولكن إذا كان لديك الكثير من الملفات للدمج، قد تجد أنها تستهلك الكثير من موارد النظام. لتجنب ذلك، استخدم الطريقة الثابتة [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-)، وهو أسلوب أكثر كفاءة لدمج عدة ملفات.

## **دمج الملفات باستخدام Aspose.Cells for Node.js via C++**

يوضح رمز المثال التالي كيفية دمج ملفات كبيرة باستخدام أسلوب [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-). يأخذ ملفين بسيطين لكن كبيرين، Book1.xls وBook2.xls. تحتوي الملفات على بيانات وصيغ منسقة فقط.

{{% alert color="primary" %}}

تدعم الطريقة [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-) فقط دمج البيانات والأنماط والتنسيقات والصيغ. قد لا يتم دمج الكائنات مثل الرسوم البيانية والصور والتعليقات أو الكائنات الأخرى باستخدام هذه الطريقة. علاوة على ذلك، يتم استخدام ملف مخزن مؤقت لتخزين البيانات المؤقتة للعملية.

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an Array (length=2)
const files = new Array(2);
// Specify files with their paths to be merged
files[0] = path.join(dataDir, "book1.xls");
files[1] = path.join(dataDir, "Book2.xlsx");

// Create a cachedFile for the process
const cacheFile = path.join(dataDir, "test.txt");

// Output File to be created
const dest = path.join(dataDir, "output.xlsx");

// Merge the files in the output file. Supports only .xls files
AsposeCells.CellsHelper.mergeFiles(files, cacheFile, dest);
console.log(cacheFile);
// Now if you need to rename your sheets, you may load the output file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "output.xlsx"));

let i = 1;

// Browse all the sheets to rename them accordingly
const worksheets = workbook.getWorksheets();
for (let j = 0; j < worksheets.getCount(); j++) {
worksheets.get(j).setName(`Sheet1${i}`);
i++;
}

// Re-save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
