---  
title: تحويل النص إلى أعمدة باستخدام Aspose.Cells for Node.js via C++  
linktitle: تحويل النص إلى أعمدة  
type: docs  
weight: 30  
url: /ar/nodejs-cpp/convert-text-to-columns-using-aspose-cells/  
description: تعلم كيفية تحويل النص إلى أعمدة في Excel باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

 يمكنك تحويل النص إلى أعمدة باستخدام Microsoft Excel. تتوفر هذه الميزة من خلال *أدوات البيانات* تحت علامة التبويب *البيانات*. من أجل تقسيم محتويات العمود إلى أعمدة متعددة، يجب أن يحتوي البيانات على فاصل معين مثل فاصلة (أو أي حرف آخر) يتم على أساسه تقسيم محتويات الخلية إلى خلايا متعددة. يقدم Aspose.Cells for Node.js via C++ أيضًا هذه الميزة عبر [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-).  

## **تحويل النص إلى أعمدة باستخدام Aspose.Cells for Node.js via C++**  

يوضح رمز العينة التالي استخدام أسلوب [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-). يضيف الرمز أولاً بعض أسماء الأشخاص في العمود أ من ورقة العمل الأولى. يتم فصل الاسم الأول واسم العائلة بواسطة مسافة. ثم يطبق أسلوب [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) على العمود أ ويحفظه كملف إكسل للإخراج. إذا فتحت ملف إكسل الناتج [ملف الإكسل](25395213.xlsx)، سترى أن الأسماء الأولى موجودة في العمود أ بينما أسماء العائلة في العمود ب كما هو موضح في لقطة الشاشة هذه.  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add people name in column A. First name and last name are separated by space.
ws.getCells().get("A1").putValue("John Teal");
ws.getCells().get("A2").putValue("Peter Graham");
ws.getCells().get("A3").putValue("Brady Cortez");
ws.getCells().get("A4").putValue("Mack Nick");
ws.getCells().get("A5").putValue("Hsu Lee");

// Create text load options with space as separator.
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(' ');

// Split the column A into two columns using TextToColumns() method.
// Now column A will have first name and column B will have second name.
ws.getCells().textToColumns(0, 0, 5, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputTextToColumns.xlsx"));
```  

