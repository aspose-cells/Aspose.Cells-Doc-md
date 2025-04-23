---  
title: ابحث عن أقصى عدد من الصفوف والأعمدة المدعومة بواسطة صيغ XLS و XLSX مع Node.js عبر C++  
linktitle: العثور على الصفوف والأعمدة القصوى المدعومة من قبل تنسيقات XLS و XLSX  
type: docs  
weight: 20  
url: /ar/nodejs-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/  
---  

## **سيناريوهات الاستخدام المحتملة**  

هناك أعداد مختلفة من الصفوف والأعمدة المدعومة بواسطة تنسيقات Excel. على سبيل المثال، تدعم XLS 65536 صفًا و 256 عمودًا، بينما تدعم XLSX 1048576 صفًا و 16384 عمودًا. إذا كنت تريد معرفة عدد الصفوف والأعمدة التي يدعمها تنسيق معين، يمكنك استخدام الخصائص [**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--) و [**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--).  

## **العثور على الصفوف والأعمدة القصوى المدعومة من قبل تنسيقات XLS و XLSX**  

يخلق المثال التالي ملف عمل أولاً بصيغة XLS ثم بصيغة XLSX. بعد الإنشاء، يطبع قيم خصائص [**WorkbookSettings.getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRow--) و [**WorkbookSettings.getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxColumn--). يرجى مراجعة مخرجات وحدة التحكم الخاصة بالكود أدناه للمرجعية.  

## **الكود المثالي**  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Print message about XLS format.
console.log("Maximum Rows and Columns supported by XLS format.");

// Create workbook in XLS format.
let wb = new AsposeCells.Workbook(AsposeCells.FileFormatType.Excel97To2003);

// Print the maximum rows and columns supported by XLS format.
let maxRows = wb.getSettings().getMaxRow() + 1;
let maxCols = wb.getSettings().getMaxColumn() + 1;
console.log("Maximum Rows: " + maxRows);
console.log("Maximum Columns: " + maxCols);
console.log();

// Print message about XLSX format.
console.log("Maximum Rows and Columns supported by XLSX format.");

// Create workbook in XLSX format.
wb = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Print the maximum rows and columns supported by XLSX format.
maxRows = wb.getSettings().getMaxRow() + 1;
maxCols = wb.getSettings().getMaxColumn() + 1;
console.log("Maximum Rows: " + maxRows);
console.log("Maximum Columns: " + maxCols);
```  

## **مخرجات الوحدة**  

{{< highlight java >}}  

Maximum Rows and Columns supported by XLS format.  

Maximum Rows: 65536  

Maximum Columns: 256  

Maximum Rows and Columns supported by XLSX format.  

Maximum Rows: 1048576  

Maximum Columns: 16384  

{{< /highlight >}}  

