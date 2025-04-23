---
title: إنشاء وإدارة جداول ملفات Microsoft Excel باستخدام Node.js عبر C++
linktitle: الجداول
type: docs
weight: 150
url: /ar/nodejs-cpp/create-and-format-table/
description: إدراج، تغيير الحجم، التحرير، الحذف، وتنسيق جداول ملفات إكسل باستخدام Aspose.Cells for Node.js via C++.
---

## **إنشاء جدول**

أحد ميزات الجداول الإلكترونية هو أنها تتيح لك إنشاء أنواع مختلفة من القوائم، على سبيل المثال: قوائم الهواتف، قوائم المهام، قوائم المعاملات، الأصول أو المطلوبات. يمكن لعدة مستخدمين العمل معًا لاستخدام وإنشاء وصيانة قوائم مختلفة.

يدعم Aspose.Cells إنشاء وإدارة القوائم.

### **مزايا كائن القائمة**

هناك العديد من المزايا عند تحويل قائمة البيانات إلى كائن قائمة فعلي

- يتم تضمين صفوف وأعمدة جديدة تلقائيًا.
- يمكن بسهولة إضافة صف إجمالي في أسفل القائمة لعرض الجمع والمتوسط والعد، إلخ.
- يتم دمج الأعمدة المضافة إلى اليمين تلقائيًا في كائن القائمة.
- ستتم توسيع الرسوم البيانية استنادًا إلى الصفوف والأعمدة تلقائيًا.
- ستتم توسيع النطاقات المسماة المخصصة للصفوف والأعمدة تلقائيًا.
- تكون القائمة محمية من حذف الصف والعمود بطريق الخطأ.

### **إنشاء كائن قائمة باستخدام Microsoft Excel**

- اختيار نطاق البيانات لإنشاء كائن القائمة
- يعرض ذلك حوار إنشاء القائمة.
- تنفيذ كائن القائمة للبيانات وتحديد الصف الإجمالي (اختر **البيانات**، ثم **قائمة**، تليها **الصف الإجمالي**).

### **استخدام واجهة برمجة تطبيقات Aspose.Cells**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، التي تمثل ملف Excel لشركة Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

الورقة تمثلها فئة {0}. فئة {1} توفر مجموعة واسعة من الخصائص والطرق لإدارة ورقة العمل. لإنشاء {2} في ورقة العمل، استخدم الخاصية {3} من مجموعة {4} من فئة {5}. كل {6} هو، في الواقع، كائن من فئة {7}، والتي توفر أيضًا طريقة {8} لإضافة كائن قائمة وتحديد نطاق الخلايا الخاص به.

وفقًا لنطاق الخلايا المحدد، يتم إنشاء كائن القائمة بواسطة Aspose.Cells. استخدم سمات (على سبيل المثال، [**getShowTotals()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getShowTotals--)، [**getListColumns()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getListColumns--)، إلخ) من فئة [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) للتحكم في القائمة.

في المثال التالي، قمنا بإنشاء نفس [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) باستخدام API الخاص بـ Aspose.Cells كما أنشأنا باستخدام Microsoft Excel في القسم أعلاه.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Create a Workbook object.
// Open a template excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the List objects collection in the first worksheet.
const listObjects = workbook.getWorksheets().get(0).getListObjects();

// Add a List based on the data source range with headers on.
listObjects.add(1, 1, 7, 5, true);

// Show the total row for the List.
listObjects.get(0).setShowTotals(true);

// Calculate the total of the last (5th) list column.
listObjects.get(0).getListColumns().get(4).setTotalsCalculation(AsposeCells.TotalsCalculation.Sum);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

## **تنسيق الجدول**

لإدارة وتحليل مجموعة من البيانات ذات الصلة، يمكن تحويل نطاق الخلايا إلى كائن قائمة (المعروف أيضًا باسم جدول Excel). الجدول هو سلسلة من الصفوف والأعمدة التي تحتوي على بيانات ذات صلة تدير بشكل مستقل عن البيانات في الصفوف والأعمدة الأخرى. بشكل افتراضي، كل عمود في الجدول له تمكين التصفية في الصف العلوي بحيث يمكنك تصفية أو فرز بيانات كائن القائمة بسرعة. يمكنك إضافة صف إجمالي (صف خاص في القائمة يوفر تشكيلة من الوظائف الإجمالية المفيدة للعمل مع البيانات العددية) إلى كائن القائمة الذي يوفر قائمة منسدلة من الوظائف الإجمالية لكل خلية في صف الإجمالي. توفر Aspose.Cells خيارات لإنشاء وإدارة القوائم (أو الجداول).

### **تنسيق كائن قائمة**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، التي تمثل ملف Excel لشركة Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

تمثلها فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) توفر مجموعة واسعة من الخصائص والطرق لإدارة الأوراق. لإنشاء [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) في ورقة العمل، استخدم خاصية [**getListObjects()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getListObjects--) من class [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). كل [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) هو، في الواقع، كائن من فئة [**ListObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/)، والتي توفر أيضًا طريقة [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/#add-number-number-number-number-boolean-) لإضافة كائن قائمة وتحديد نطاق الخلايا الذي ستتضمنه. وفقًا لنطاق الخلايا المحدد، يتم إنشاء [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) في ورقة العمل بواسطة Aspose.Cells. استخدم السمات (مثال، [**TableStyleType**](https://reference.aspose.com/cells/nodejs-cpp/tablestyletype/)) من [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) لتنسيق الجدول بحسب متطلباتك.

المثال أدناه يضيف بيانات عينة إلى ورقة العمل، يضيف [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) ويطبق أنماطًا افتراضية عليه. دعم أنماط [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) بواسطة Microsoft Excel 2007/2010.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook.
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the default(first) worksheet
const sheet = workbook.getWorksheets().get(0);

// Obtaining Worksheet's cells collection
const cells = sheet.getCells();

// Setting the value to the cells
cells.get(1, 1).putValue("Employee");
cells.get(1, 2).putValue("Quarter");
cells.get(1, 3).putValue("Product");
cells.get(1, 4).putValue("Continent");
cells.get(1, 5).putValue("Country");
cells.get(1, 6).putValue("Sale");

cells.get(2, 1).putValue("David");
cells.get(3, 1).putValue("David");
cells.get(4, 1).putValue("David");
cells.get(5, 1).putValue("David");
cells.get(6, 1).putValue("James");
cells.get(7, 1).putValue("James");
cells.get(8, 1).putValue("James");
cells.get(9, 1).putValue("James");
cells.get(10, 1).putValue("James");
cells.get(11, 1).putValue("Miya");
cells.get(12, 1).putValue("Miya");
cells.get(13, 1).putValue("Miya");
cells.get(14, 1).putValue("Miya");
cells.get(15, 1).putValue("Miya");
cells.get(2, 2).putValue(1);
cells.get(3, 2).putValue(2);
cells.get(4, 2).putValue(3);
cells.get(5, 2).putValue(4);
cells.get(6, 2).putValue(1);
cells.get(7, 2).putValue(2);
cells.get(8, 2).putValue(3);
cells.get(9, 2).putValue(4);
cells.get(10, 2).putValue(4);
cells.get(11, 2).putValue(1);
cells.get(12, 2).putValue(1);
cells.get(13, 2).putValue(2);
cells.get(14, 2).putValue(2);
cells.get(15, 2).putValue(2);

cells.get(2, 3).putValue("Maxilaku");
cells.get(3, 3).putValue("Maxilaku");
cells.get(4, 3).putValue("Chai");
cells.get(5, 3).putValue("Maxilaku");
cells.get(6, 3).putValue("Chang");
cells.get(7, 3).putValue("Chang");
cells.get(8, 3).putValue("Chang");
cells.get(9, 3).putValue("Chang");
cells.get(10, 3).putValue("Chang");
cells.get(11, 3).putValue("Geitost");
cells.get(12, 3).putValue("Chai");
cells.get(13, 3).putValue("Geitost");
cells.get(14, 3).putValue("Geitost");
cells.get(15, 3).putValue("Geitost");

cells.get(2, 4).putValue("Asia");
cells.get(3, 4).putValue("Asia");
cells.get(4, 4).putValue("Asia");
cells.get(5, 4).putValue("Asia");
cells.get(6, 4).putValue("Europe");
cells.get(7, 4).putValue("Europe");
cells.get(8, 4).putValue("Europe");
cells.get(9, 4).putValue("Europe");
cells.get(10, 4).putValue("Europe");
cells.get(11, 4).putValue("America");
cells.get(12, 4).putValue("America");
cells.get(13, 4).putValue("America");
cells.get(14, 4).putValue("America");
cells.get(15, 4).putValue("America");

cells.get(2, 5).putValue("China");
cells.get(3, 5).putValue("India");
cells.get(4, 5).putValue("Korea");
cells.get(5, 5).putValue("India");
cells.get(6, 5).putValue("France");
cells.get(7, 5).putValue("France");
cells.get(8, 5).putValue("Germany");
cells.get(9, 5).putValue("Italy");
cells.get(10, 5).putValue("France");
cells.get(11, 5).putValue("U.S.");
cells.get(12, 5).putValue("U.S.");
cells.get(13, 5).putValue("Brazil");
cells.get(14, 5).putValue("U.S.");
cells.get(15, 5).putValue("U.S.");

cells.get(2, 6).putValue(2000);
cells.get(3, 6).putValue(500);
cells.get(4, 6).putValue(1200);
cells.get(5, 6).putValue(1500);
cells.get(6, 6).putValue(500);
cells.get(7, 6).putValue(1500);
cells.get(8, 6).putValue(800);
cells.get(9, 6).putValue(900);
cells.get(10, 6).putValue(500);
cells.get(11, 6).putValue(1600);
cells.get(12, 6).putValue(600);
cells.get(13, 6).putValue(2000);
cells.get(14, 6).putValue(500);
cells.get(15, 6).putValue(900);

// Adding a new List Object to the worksheet
const index = sheet.getListObjects().add("A1", "F15", true);

const listObject = sheet.getListObjects().get(index);

// Adding Default Style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);

// Show Total
listObject.setShowTotals(true);

// Set the Quarter field's calculation type
listObject.getListColumns().get(1).setTotalsCalculation(AsposeCells.TotalsCalculation.Count);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```

## **مواضيع متقدمة**
- [تحويل الجدول إلى ODS](/cells/ar/nodejs-cpp/convert-table-to-ods/)
- [العثور على جداول الاستعلام وكائنات القائمة المتعلقة باتصالات البيانات الخارجية](/cells/ar/nodejs-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [قراءة وكتابة الجدول مع مصدر بيانات جدول الاستعلام](/cells/ar/nodejs-cpp/read-and-write-table-with-query-table-data-source/)
- [ضبط التعليق للجدول أو كائن القائمة داخل ورقة العمل](/cells/ar/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [الجداول والمدى](/cells/ar/nodejs-cpp/tables-and-ranges/)

