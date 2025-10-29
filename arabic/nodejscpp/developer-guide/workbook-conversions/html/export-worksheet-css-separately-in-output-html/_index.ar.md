---  
title: تصدير تنسيق CSS للورقة بشكل منفصل في ملف HTML الناتج باستخدام Node.js عبر C++  
linktitle: تصدير ورقة العمل CSS بشكل منفصل في ملف HTML الناتج  
type: docs  
weight: 80  
url: /ar/nodejs-cpp/export-worksheet-css-separately-in-output/  
description: تعلم كيف تصدر CSS للورقة بشكل منفصل عند تحويل ملف إكسل إلى HTML باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**

يوفر Aspose.Cells for Node.js via C++ ميزة تصدير CSS للورقة بشكل منفصل عند تحويل ملف إكسل إلى HTML. يرجى استخدام خاصية [**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--) لهذا الغرض وضبطها على **true** عند حفظ الملف بصيغة HTML.

## **تصدير ورق العمل CSS بشكل منفصل في ملف HTML الناتج**

يُنشئ الكود النموذجي التالي ملف إكسل، يضيف بعض النصوص في الخلية **B5** باللون **الأحمر**، ثم يحفظه بصيغة HTML باستخدام خاصية [**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--). يرجى الاطلاع على [ملف HTML الناتج](60489766.zip) المولَّد بواسطة الكود للمرجعة. ستجد داخله ملف **stylesheet.css** كنتيجة للكود النموذجي.

## **الكود المثالي**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and put value inside it
const cell = ws.getCells().get("B5");
cell.putValue("This is some text.");

// Set the style of the cell - font color is Red
const st = cell.getStyle();
st.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(st);

// Specify html save options - export worksheet css separately
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportWorksheetCSSSeparately(true);

// Save the workbook in html 
wb.save("outputExportWorksheetCSSSeparately.html", opts);
```

## **تصدير جدول عمل واحد إلى HTML**

عند تحويل مصنف Excel يتضمن عدة أوراق إلى HTML باستخدام Aspose.Cells for Node.js via C++، يتم إنشاء ملف HTML جنبًا إلى جنب مع مجلد يحتوي على CSS وملفات HTML متعددة. عند فتح هذا الملف في المتصفح، تكون الألسنة مرئية. والنفس السلوك مطلوب لمصنف يتضمن ورقة عمل واحدة عند تحويله إلى HTML. سابقًا، لم يتم إنشاء مجلد منفصل للمصنفات ذات الورقة الواحدة، وتم إنشاء ملف HTML فقط. مثل هذا الملف لا يعرض الألسنة عند فتحه في المتصفح. تقوم أرقام Excel بإنشاء مجلد وملف HTML مناسبين لورقة واحدة أيضًا، لذلك تم تنفيذ نفس السلوك باستخدام واجهات برمجة التطبيقات Aspose.Cells. يمكن تنزيل الملف النموذجي من الرابط التالي للاستخدام في الكود أدناه:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleSingleSheet.xlsx");
// Load the sample Excel file containing single sheet only
const wb = new AsposeCells.Workbook(sourceFilePath);

// Specify HTML save options
const options = new AsposeCells.HtmlSaveOptions();

// Set optional settings if required
options.setEncoding(AsposeCells.EncodingType.UTF8);
options.setExportImagesAsBase64(true);
options.setExportGridLines(true);
options.setExportSimilarBorderStyle(true);
options.setExportBogusRowData(true);
options.setExcludeUnusedStyles(true);
options.setExportHiddenWorksheet(true);

// Save the workbook in Html format with specified Html Save Options
wb.save(path.join(dataDir, "outputSampleSingleSheet.htm"), options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
