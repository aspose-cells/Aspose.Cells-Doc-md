---  
title: احتفظ بالمفاصل للفواصل الفارغة عند تصدير جداول البيانات إلى تنسيق CSV باستخدام Node.js عبر C++  
linktitle: الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير أوراق الجدول إلى تنسيق CSV  
type: docs  
weight: 160  
url: /ar/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/  
---  

## **الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV**  

تقدم Aspose.Cells القدرة على الاحتفاظ بفواصل الأسطر أثناء تحويل جداول البيانات إلى تنسيق CSV. لاستخدام ذلك، يمكنك استخدام خاصية [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) من [**TxtSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/). [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) هي خاصية منطقية. للحفاظ على المفاصل للفواصل الفارغة أثناء تحويل ملف Excel إلى CSV، قم بضبط الخاصية [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) على **true**.  

يعرض الرمز النموذجي التالي تحميل ملف Excel [المصدر](84378743.xlsx). حيث يضبط الخاصية [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) على **true** ويحفظه كـ [ملف CSV الناتج](84378744.csv). تظهر الصورة المجمعة المقارنة بين ملف Excel المصدر، والناتج الافتراضي عند تحويل ورقة العمل إلى CSV، والناتج الناتج عن ضبط [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) على **true**.  

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Set KeepSeparatorsForBlankRow to true to show separators in blank rows
options.setKeepSeparatorsForBlankRow(true);

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
