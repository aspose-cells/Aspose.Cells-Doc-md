---  
title: إضافة أو حذف الصفوف في ورقة إكسل باستخدام Node.js عبر C++  
linktitle: إدراج أو حذف الصفوف في ورقة عمل Excel  
type: docs  
weight: 20  
url: /ar/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/  
description: يوفر هذا المقال كود Node.js باستخدام C++ لإضافة وحذف الصفوف في ورقة إكسل.  
keywords: Node.js أضف أو احذف الصفوف في ورقة إكسل، Node.js أضف أو احذف الصفوف في إكسل، Node.js أضف صفوف في إكسل، Node.js احذف الصفوف في إكسل، أضف أو احذف الصفوف في ورقة إكسل باستخدام Node.js، أضف أو احذف صفوف في إكسل باستخدام Node.js، أضف صفوف في إكسل باستخدام Node.js، احذف الصفوف في إكسل باستخدام Node.js  
---  

{{% alert color="primary" %}}  

عند إنشاء ورقة عمل جديدة أو العمل مع ورقة موجودة، قد تحتاج إلى إضافة صفوف أو أعمدة إضافية لاستيعاب البيانات. وفي أوقات أخرى، قد تحتاج إلى حذف صفوف أو أعمدة من مواقع محددة في ورقة العمل.  

{{% /alert %}}  

Aspose.Cells for Node.js via C++ يقدم وطريقتين لإدراج وحذف الصفوف: [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) و [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-). هذه الطرق محسنة للأداء وتؤدي المهمة بسرعة كبيرة.  

لإدراج أو إزالة عدد من الصفوف ، نوصي دائمًا باستخدام طرق [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) و [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) بدلاً من استخدام طرق [**Cells.insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) أو [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRow-number-) في حلقة.  

تعمل Aspose.Cells بنفس الطريقة التي يعمل بها برنامج Microsoft Excel. عند إضافة صفوف أو أعمدة، يتم نقل محتوى ورقة العمل لأسفل ولليمين. وعند إزالة صفوف أو أعمدة، يتم نقل محتوى ورقة العمل لأعلى أو لليسار. يتم تحديث أي مراجع في ورقات العمل والخلايا الأخرى عند إضافة أو إزالة الصفوف.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object.
// Load a template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));

// Get the first worksheet in the book.
const sheet = workbook.getWorksheets().get(0);

// Insert 10 rows at row index 2 (insertion starts at 3rd row)
sheet.getCells().insertRows(2, 10);

// Delete 5 rows now. (8th row - 12th row)
sheet.getCells().deleteRows(7, 5);

// Save the excel file.
workbook.save(path.join(dataDir, "out_book1.out.xlsx"));
```  

