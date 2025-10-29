---
title: تعيين صيغة لنطاق مسمى باستخدام Node.js عبر C++
linktitle: وضع صيغة لنطاق مسمى
type: docs
weight: 20
url: /ar/nodejs-cpp/setting-formula-for-named-range/
description: تعلم كيفية تعيين الصيغ للنطاقات المسماة في جداول البيانات باستخدام Aspose.Cells for Node.js via C++.
---

## **وضع صيغة لنطاق مسمى**
مثل تطبيق إكسل، توفر واجهات برمجة تطبيقات Aspose.Cells القدرة على تحديد صيغة لنطاق مسمى أثناء استخدام خاصية [Range.getRefersTo()](https://reference.aspose.com/cells/nodejs-cpp/range/#getRefersTo--) الخاصية. قد توجد العديد من سيناريوهات الاستخدام لهذه الميزة، ويتم توضيح بعضها فيما يلي.

### **وضع صيغة بسيطة لنطاق مسمى**
يمكن أن تكون الصيغة البسيطة إشارة إلى خلية أخرى في نفس جدول العمل (أو جداول عمل مختلفة). ينشئ المثال التالي نطاقًا مسمى في جدول بيانات جديد ويحدد إشارته إلى خلية أخرى.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook
const book = new AsposeCells.Workbook();

// Get the WorksheetCollection
const worksheets = book.getWorksheets();

// Add a new Named Range with name "NewNamedRange"
const index = worksheets.getNames().add("NewNamedRange");

// Access the newly created Named Range
const name = worksheets.getNames().get(index);

// Set RefersTo property of the Named Range to a formula. Formula references another cell in the same worksheet
name.setRefersTo("=Sheet1!$A$3");

// Set the formula in the cell A1 to the newly created Named Range
worksheets.get(0).getCells().get("A1").setFormula("NewNamedRange");

// Insert the value in cell A3 which is being referenced in the Named Range
worksheets.get(0).getCells().get("A3").putValue("This is the value of A3");

// Calculate formulas
book.calculateFormula();

// Save the result in XLSX format
book.save(path.join(dataDir, "output_out.xlsx"));
```

### **وضع صيغة معقدة لنطاق مسمى**
يمكن أن تكون الصيغة المعقدة أي شيء مثل نطاق ديناميكي أو صيغة تمتد عبر عدة خلايا في جداول عمل مختلفة. ينشئ المثال التالي نطاقًا ديناميكيًا باستخدام وظيفة INDEX للحصول على القيمة من قائمة استنادًا إلى موقعها.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook();

// Get the WorksheetCollection
const worksheets = book.getWorksheets();

// Add a new Named Range with name "data"
let index = worksheets.getNames().getCount();
worksheets.getNames().add("data");

// Access the newly created Named Range from the collection
const data = worksheets.getNames().get(index);

// Set RefersTo property of the Named Range to a cell range in same worksheet
data.setRefersTo("=Sheet1!$A$1:$A$10");

// Add another Named Range with name "range"
index = worksheets.getNames().getCount();
worksheets.getNames().add("range");

// Access the newly created Named Range from the collection
const range = worksheets.getNames().get(index);

// Set RefersTo property to a formula using the Named Range data
range.setRefersTo("=INDEX(data,Sheet1!$A$1,1):INDEX(data,Sheet1!$A$1,9)");

// Save the workbook
book.save(path.join(dataDir, "output_out.xlsx"));
```

هنا مثال آخر يستخدم نطاقًا مسمى لجمع القيم من 2 خليتين في جداول عمل مختلفة.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook
const book = new AsposeCells.Workbook();

// Get the WorksheetCollection
const worksheets = book.getWorksheets();

// Insert some data in cell A1 of Sheet1
worksheets.get("Sheet1").getCells().get("A1").putValue(10);

// Add a new Worksheet and insert a value to cell A1
worksheets.get(worksheets.add()).getCells().get("A1").putValue(10);

// Add a new Named Range with name "range"
const index = worksheets.getNames().add("range");

// Access the newly created Named Range from the collection
const range = worksheets.getNames().get(index);

// Set RefersTo property of the Named Range to a SUM function
range.setRefersTo("=SUM(Sheet1!$A$1,Sheet2!$A$1)");

// Insert the Named Range as formula to 3rd worksheet
worksheets.get(worksheets.add()).getCells().get("A1").setFormula("range");

// Calculate formulas
book.calculateFormula();

// Save the result in XLSX format
book.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
