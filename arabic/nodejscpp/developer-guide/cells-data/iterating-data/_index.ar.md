---  
title: كيف وأين تستخدم عدادات التكرار مع Node.js عبر C++  
linktitle: تكرار البيانات  
type: docs  
weight: 55  
url: /ar/nodejs-cpp/how-and-where-to-use-enumerators/  
description: تعلّم كيفية استخدام العدادات التكرارية من خلال واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.  
keywords: كيفية استخدام العدادات التكرارية Node.js عبر C++، عدادات التكرار للخلايا Node.js عبر C++، عدادات التكرار للصفوف Node.js عبر C++، عدادات التكرار للأعمدة Node.js عبر C++  
---  

{{% alert color="primary" %}}  

العداد التكراري هو كائن يوفر القدرة على عبور حاوية أو مجموعة. يمكن استخدام العدادات التكرارية لقراءة البيانات في المجموعة، لكنها لا يمكن استخدامها لتعديل المجموعة الأساسية، بينما تعد Array واجهة تعرف طريقة واحدة `getEnumerator` التي تعيد واجهة `IEnumerator`، مما يسمح بالوصول المقروء فقط إلى مجموعة.  

توفر واجهات برمجة تطبيقات Aspose.Cells مجموعة من المعدلات الإحصائية، ومع ذلك، يناقش هذا المقال بشكل رئيسي الثلاثة أنواع المذكورة أدناه.  

1. معدل الخلايا  
1. معدل الصفوف  
1. معدل الأعمدة  

{{% /alert %}}  

## **كيفية استخدام المعدلات الإحصائية**  

### **معدل الخلايا**  

هناك طرق مختلفة للوصول إلى معدل الخلايا، ويمكن للشخص استخدام أيًا من هذه الطرق استنادًا إلى متطلبات التطبيق. هنا الطرق التي تُرجع معدل الخلايا.  

1. [**Cells.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getEnumerator--)  
1. [**Row.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getEnumerator--)  
1. [**Range.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getEnumerator--)  

تعود الطرق المذكورة أعلاه جميعًا بمُحدِّد العناصر الذي يسمح بجَولة جمعية الخلايا التي تم تهيئتها.  

{{% alert color="primary" %}}  

أثناء جولة الخلايا، يجب ألا يتم تعديل المجموعة (العمليات التي ستؤدي إلى إنشاء خلية جديدة أو حذف خلية موجودة). وإلا فإن المُحدِّد قد لا يكون قادرًا على جولة جميع الخلايا بشكل صحيح (قد يكون بعض العناصر قد تجولت بشكل متكرر أو تم تخطيها).  

{{% /alert %}}  

يُظهر المثال التالي تنفيذ واجهة `IEnumerator` لمجموعة الخلايا.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells().getEnumerator();
for (const cell of cells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rowCells = workbook.getWorksheets().get(0).getCells().getRows().get(0).getEnumerator();
for (const cell of rowCells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rangeCells = workbook.getWorksheets().get(0).getCells().createRange("A1:B10").getEnumerator();
for (const cell of rangeCells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}
```  

### **مُحدِّد الصفوف**  

يمكن الوصول إلى عداد الصفوف أثناء استخدام طريقة [**RowCollection.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection/#getEnumerator--). يُظهر المثال التالي تنفيذ واجهة `IEnumerator` لمجموعة الصفوف `[**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection)`.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get RowCollection and iterate using index
const rows = workbook.getWorksheets().get(0).getCells().getRows();
const rowCount = rows.getCount();

// Traverse rows in the collection
for (let i = 0; i < rowCount; i++) {
const row = rows.get(i);
console.log(row.getIndex());
}
```  

### **مُحدِّد الأعمدة**  

يمكن الوصول إلى عداد الأعمدة أثناء استخدام طريقة [**ColumnCollection.getEnumerator**](https://reference.aspose.com/cells/nodejs-cpp/columncollection). يُظهر المثال التالي تنفيذ واجهة `IEnumerator` لمجموعة الأعمدة `[**ColumnCollection**](https://reference.aspose.com/cells/nodejs-cpp/columncollection)`.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get columns collection
const columns = workbook.getWorksheets().get(0).getCells().getColumns();
// Traverse columns using index
const count = columns.getCount();
for (let i = 0; i < count; i++) {
const col = columns.get(i);
console.log(col.getIndex());
}
```  

## **أين يجب استخدام المُحدِّدات**  

من أجل مناقشة مزايا استخدام العدادات، دعونا نأخذ مثالاً حقيقياً من الوقت الحقيقي.  

**سيناريو**  

متطلبات التطبيق تتطلب جولة جميع الخلايا في [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) معينة لقراءة قيمها. يمكن تنفيذ هذا الهدف بعدة طرق. يُظهر بعضها أدناه.  

### **استخدام نطاق العرض**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Get the MaxDisplayRange
const displayRange = cells.getMaxDisplayRange();

// Loop over all cells in the MaxDisplayRange
for (let row = displayRange.getFirstRow(); row < displayRange.getRowCount(); row++) {
for (let col = displayRange.getFirstColumn(); col < displayRange.getColumnCount(); col++) {
// Read the Cell value
console.log(displayRange.get(row, col).getStringValue());
}
}
```  

### **استخدام MaxDataRow و MaxDataColumn**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells2 = workbook.getWorksheets().get(0).getCells();
const maxDataRow = cells2.getMaxDataRow();
const maxDataColumn = cells2.getMaxDataColumn();

// Loop over all cells
for (let row = 0; row <= maxDataRow; row++) {
for (let col = 0; col <= maxDataColumn; col++) {
// Read the Cell value
const currentCell = cells2.checkCell(row, col);
if (currentCell) {
console.log(currentCell.getStringValue());
}
}
}
```  

كما يمكنك أن تلاحظ أن كلتا الطريقتين المذكورتين تستخدمان تقريبًا نفس المنطق، وهو: الدوران حول جميع الخلايا في المجموعة لقراءة قيم الخلايا. قد يكون هذا مشكلة لعدة أسباب كما سيتم مناقشتها أدناه.  

1. تتطلب واجهات برمجة التطبيقات مثل [**getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxRow--)، [**getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--)، [**getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxColumn--)، [**getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) و [**getMaxDisplayRange()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--) وقت إضافي لجمع الإحصاءات المقابلة. في حالة كانت المصفوفة البيانات (صفوف × أعمدة) كبيرة، فإن استخدام هذه الواجهات قد يفرض عقوبة أداء.  
1. في معظم الحالات، لا تتم إنشاء جميع الخلايا في النطاق المعطى. في مثل هذه الحالات، فحص كل خلية في البيانات ليس فعَّالًا كمقارنة بفحص الخلايا المهيئة فقط.  
1. الوصول إلى خلية في حلقة مثل Cells row، column سيؤدي إلى إنشاء جميع كائنات الخلايا في النطاق، مما قد يؤدي في النهاية إلى حدوث استثناء نفاد الذاكرة.  

## **الاستنتاج**  

بناءً على الحقائق المذكورة أعلاه، فإن السيناريوهات الممكنة التالية هي التي يجب استخدام المُحدِّدات فيها.  

1. الوصول القراءة فقط لمجموعة الخلايا مطلوب، أي؛ المتطلب هو تفقّد الخلايا فقط.  
1. يتعين عبور عدد كبير من الخلايا.  
1. يجب عبور الخلايا/الصفوف/الأعمدة المهيأة فقط.  

