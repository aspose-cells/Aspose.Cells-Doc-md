---  
title: تصدير نطاق منطقة الطباعة إلى HTML باستخدام Node.js عبر C++  
linktitle: تصدير نطاق منطقة الطباعة إلى HTML  
type: docs  
weight: 60  
url: /ar/nodejs-cpp/export-print-area-range-to/  
---  

## **سيناريوهات الاستخدام المحتملة**

هذا سيناريو شائع حيث نحتاج إلى تصدير منطقة الطباعة المحددة فقط أي مجموعة مختارة من الخلايا بدلاً من الورقة كاملة إلى HTML. تتوفر هذه الميزة بالفعل للطباعة؛ ومع ذلك، يمكنك الآن تنفيذ هذه المهمة لـ HTML أيضًا. أولاً، قم بضبط منطقة الطباعة في كائن إعداد الصفحة لورقة العمل. فيما بعد، استخدم العلامة [**HtmlSaveOptions.getExportPrintAreaOnly()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportPrintAreaOnly--) لتصدير النطاق المحدد فقط.

## كود عينة

يقوم الكود العيني التالي بتحميل دفتر عمل ثم يصدر منطقة الطباعة إلى HTML. يمكن تنزيل ملف العينة لاختبار هذه الميزة من الرابط التالي:

[sampleInlineCharts.xlsx](79527946.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleInlineCharts.xlsx");

// Load the Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access the sheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area.
worksheet.getPageSetup().setPrintArea("D2:M20");

// Initialize HtmlSaveOptions
const options = new AsposeCells.HtmlSaveOptions();

// Set flag to export print area only
options.setExportPrintAreaOnly(true);

// Save to HTML format
const outputFilePath = path.join(dataDir, "outputInlineCharts.html");
workbook.save(outputFilePath, options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
