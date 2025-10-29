---  
title: الوصول إلى الجدول من الخلية وإضافة القيم بداخله باستخدام إزاحات الصف والعمود مع Node.js عبر C++  
linktitle: الوصول إلى الجدول من الخلية وإضافة القيم داخله باستخدام إزاحة الصف والعمود  
type: docs  
weight: 230  
url: /ar/nodejs-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
---  

{{% alert color="primary" %}}  

عادةً ما تضيف القيم داخل الجدول أو كائن القائمة باستخدام الطريقة [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-). ولكن في بعض الأحيان، قد تحتاج إلى إضافة القيم داخل الجدول أو كائن القائمة باستخدام إزاحة الصف والعمود.  

للوصول إلى كائن جدول أو قائمة من خلية، استخدم الطريقة [**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--). لإضافة قيم بداخله باستخدام إزاحات الصف والعمود، استخدم الطريقة [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-).  

{{% /alert %}}  

يوضح لقطة الشاشة التالية ملف Excel المصدر المستخدم داخل الكود. يحتوي على جدول فارغ ويبرز الخلية D5 التي تقع داخل الجدول. سنصل إلى هذا الجدول من الخلية D5 باستخدام طريقة [**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--) ثم نضيف القيم بداخله باستخدام طريقتي [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) و [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-).  

## مثال  

### لقطات شاشة تقارن الملفات المصدرية والإخراجية  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

اللقطة الشاشية التالية تُظهر ملف Excel الناتج الذي تم إنشاؤه بواسطة الكود. كما يمكنك رؤية الخلية D5 التي تحتوي على قيمة والخلية F6 والتي تقع في الإزاحة 2،2 من الجدول وتحتوي على قيمة.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### كود Node.js للوصول إلى جدول من خلية وإضافة قيم داخله باستخدام إزاحات الصف والعمود  

يقوم الكود النموذجي التالي باستخدام ملف Excel المصدر كما هو موضح في اللقطة الشاشية أعلاه ويضيف القيم داخل الجدول ويولد ملف Excel الناتج كما هو موضح أعلاه.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Accessing_Table.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell D5 which lies inside the table
const cell = worksheet.getCells().get("D5");

// Put value inside the cell D5
cell.putValue("D5 Data");

// Access the Table from this cell
const table = cell.getTable();

// Add some value using Row and Column Offset
table.putCellValue(2, 2, "Offset [2,2]");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
