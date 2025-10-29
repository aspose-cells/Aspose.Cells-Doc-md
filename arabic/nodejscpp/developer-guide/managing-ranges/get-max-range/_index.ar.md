---  
title: الحصول على أقصى نطاق في ورقة عمل باستخدام Node.js عبر C++  
linktitle: الحصول على أقصى مجال في ورقة العمل  
type: docs  
weight: 360  
url: /ar/nodejs-cpp/get-max-range-in-a-worksheet/  
description: تصف هذه المقالة كيفية الحصول على أقصى نطاق، وأقصى نطاق بيانات، وأقصى نطاق عرض لملفات Excel باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

عند قراءة البيانات من ورقة العمل ، نحتاج إلى معرفة المساحة القصوى.  

عند نسخ جميع البيانات من ورقة العمل ، نحتاج إلى معرفة المساحة القصوى.  

عند تصدير منطقة محددة إلى HTML و PDF، نحتاج إلى معرفة المنطقة القصوى.  

يحتوي Aspose.Cells for Node.js via C++ على طرق مختلفة لإيجاد أقصى نطاق في ورقة عمل.  

{{% /alert %}}  

## **الحصول على أقصى مجال**  
في Aspose.Cells، إذا تم تهيئة كائنات [**row**](https://reference.aspose.com/cells/nodejs-cpp/row/) و [**column**](https://reference.aspose.com/cells/nodejs-cpp/column/)، فسيتم حساب هذه الصفوف والأعمدة ضمن الحد الأقصى للمنطقة، حتى لو لم تكن هناك بيانات في الصفوف أو الأعمدة الفارغة.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxRow();
let maxColumn = sheet.getCells().getMaxColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxRow();
maxColumn = sheet.getCells().getMaxColumn();
// The range is updated to A1:B10.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **الحصول على أقصى مجال للبيانات**  
في معظم الحالات ، نحتاج إلى الحصول على جميع المجالات التي تحتوي على جميع البيانات ، حتى لو كانت الخلايا الفارغة خارج المجال مهيأة.  
وستُتجاهل الإعدادات الخاصة بالأشكال، والجداول، والجداول المحورية.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxDataRow();
let maxColumn = sheet.getCells().getMaxDataColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxDataRow();
maxColumn = sheet.getCells().getMaxDataColumn();
// The range is still A1:B3.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **الحصول على أقصى مجال للعرض**  
عند تصدير جميع البيانات من ورقة العمل إلى HTML ، PDF ، أو الصور ، نحتاج إلى الحصول على منطقة تحتوي على جميع الكائنات المرئية ، بما في ذلك البيانات والأنماط والرسومات والجداول والجداول المدورة.  
توضح الرموز التالية كيفية عرض النطاق العرضي الأقصى في HTML:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Gets the max display range.
const range = worksheets.get(0).getCells().getMaxDisplayRange();

// Save the range to html
const saveOptions = new AsposeCells.HtmlSaveOptions();
saveOptions.setExportActiveWorksheetOnly(true);
saveOptions.setExportArea(AsposeCells.CellArea.createCellArea(range.getFirstRow(), range.getFirstColumn(), range.getFirstRow() + range.getRowCount() - 1, range.getFirstColumn() + range.getColumnCount() - 1));

// Save the range.
workbook.save("html.html", saveOptions);
```  

هنا [ملف اكسل المصدر](Book1.xlsx).  

{{< app/cells/assistant language="nodejs-cpp" >}}
