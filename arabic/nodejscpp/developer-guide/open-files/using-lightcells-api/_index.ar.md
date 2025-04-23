---  
title: استخدام واجهة برمجة التطبيقات LightCells مع Node.js عبر C++  
linktitle: استخدام واجهة LightCells API  
type: docs  
weight: 160  
url: /ar/nodejs-cpp/using-lightcells-api/  
description: تعلم كيفية قراءة وكتابة ملفات إكسل كبيرة باستخدام واجهة LightCells في Node.js عبر C++. حسن الأداء والكفاءة مع استهلاك أقل للذاكرة.  
---  

{{% alert color="primary" %}}  

في بعض الأحيان تحتاج إلى قراءة وكتابة ملفات Microsoft Excel الكبيرة بقائمة كبيرة من البيانات أو المحتوى في ورقة العمل. واجهة برمجة التطبيقات المبسطة مفيدة لإنشاء جداول بيانات Excel الضخمة: معها، تحتاج إلى أقل كمية من الذاكرة وتحصل على أداء وكفاءة أفضل.  

{{% /alert %}}  
# الهندسة المعمارية المدفوعة بالأحداث  
توفر Aspose.Cells واجهة LightCells API مصممة بشكل رئيسي للتلاعب ببيانات الخلية واحدة تلو الأخرى دون بناء نموذج بيانات كاملاً (باستخدام مجموعة الخلية إلخ) في الذاكرة. تعمل في وضع محفز بالأحداث.  

لحفظ دفاتر العمل، يتم تقديم محتوى الخلية خلية بخلية عند الحفظ، ويقوم المكون بحفظه في ملف الإخراج مباشرةً.  

عند قراءة ملفات القالب، يُحلل المكون كل خلية ويقدم قيمها واحدة تلو الأخرى.  

 في كل من الإجرائين، يتم معالجة كائن خلية واحد ثم يتم التخلص منه؛ كائن دفتر العمل لا يحتفظ بالمجموعة. في هذه الوضعية، يتم توفير الذاكرة عند استيراد وتصدير ملفات إكسل مايكروسوفت التي تحتوي على مجموعة بيانات كبيرة والتي كانت ستستخدم الكثير من الذاكرة.  

على الرغم من أن واجهة LightCells API تعالج الخلايا بنفس الطريقة لملفات XLSX وXLS (حيث لا تقوم فعليًا بتحميل كل الخلايا في الذاكرة ولكن تعالج خلية ومن ثم تتخلص منها)، إلا أنها تحفظ الذاكرة بشكل أكثر فعالية لملفات XLSX من ملفات XLS بسبب النماذج والهياكل المختلفة للصيغتين.  

 مع ذلك، **بالنسبة لملفات XLS**، للمطورين أن يحددوا موقعًا مؤقتًا لحفظ البيانات المؤقتة الناتجة أثناء عملية الحفظ. عادةً، **استخدام واجهة LightCells لحفظ ملفات XLSX قد يوفر 50% أو أكثر من الذاكرة** مقارنة بالطرق التقليدية؛ **حفظ XLS قد يوفر حوالي 20-40% من الذاكرة**.  

## كتابة ملف إكسل كبير  
 توفر Aspose.Cells واجهة، `LightCellsDataProvider`، يجب تنفيذها في برنامجك. تمثل الواجهة مزود البيانات لحفظ ملفات جداول البيانات الكبيرة في وضع خفيف الوزن.  

 عند حفظ دفتر عمل في هذا الوضع، يتم فحص `StartSheet(int)` عند حفظ كل ورقة عمل في دفتر العمل. بالنسبة لورقة واحدة، إذا كانت `StartSheet(int)` صحيحة، يتم توفير جميع البيانات وخصائص الصفوف والخلايا لهذه الورقة بواسطة هذا التنفيذ. أولاً، يتم استدعاء `NextRow()` للحصول على رقم الصف التالي للحفظ. إذا تم إرجاع رقم صف صالح (يجب أن يكون ترتيب الصفوف تصاعديًا للصفوف التي سيتم حفظها)، يتم توفير كائن صف يمثل هذا الصف لتمكين إعداد خصائصه بواسطة `StartRow(Row)`.  

 بالنسبة لصف واحد، يتم التحقق أولاً من `NextCell()`. إذا تم إرجاع رقم عمود صالح (يجب أن يكون ترتيب الأعمدة تصاعديًا لجميع الخلايا في صف واحد ليتم حفظها)، يتم توفير كائن خلية يمثل تلك الخلية لإعداد بياناتها وخصائصها بواسطة `StartCell(Cell)`. بعد إعداد بيانات الخلية، يتم حفظ الخلية مباشرة إلى ملف جدول البيانات الناتج ويتم التحقق ومعالجة الخلية التالية.  
### كتابة ملف إكسل كبير: مثال  
يرجى رؤية الكود النموذجي التالي لرؤية عمل واجهة برمجة التطبيقات (API) LightCells. أضف وأزل، أو حدث الشرائح التوضيحية وفقًا لاحتياجاتك.  

 ينشئ البرنامج ملفًا ضخمًا يحتوي على **10,000 (مصفوفة 10000×30)** سجل في ورقة عمل ويملاها ببيانات وهمية. يمكنك تحديد مصفوفة خاصة بك بتغيير متغيري `rowsCount` و `colsCount` في طريقة `Main()`.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class TestDataProvider {
constructor(workbook, maxRows, maxColumns) {
this._workbook = workbook;
this.maxRows = maxRows;
this.maxColumns = maxColumns;
this._row = -1;
this._column = -1;
}

isGatherString() {
return false;
}

nextCell() {
this._column++;
if (this._column < this.maxColumns) {
return this._column;
} else {
this._column = -1;
return -1;
}
}

nextRow() {
this._row++;
if (this._row < this.maxRows) {
this._column = -1;
return this._row;
} else {
return -1;
}
}

startCell(cell) {
cell.putValue(this._row + this._column);
if (this._row !== 1) {
cell.setFormula("=Rand() + A2");
}
}

startRow(row) {
}

startSheet(sheetIndex) {
return sheetIndex === 0;
}
}

const run = async () => {
const dataDir = path.join(__dirname, "data");

const rowsCount = 10000;
const colsCount = 30;

const workbook = new AsposeCells.Workbook();
const ooxmlSaveOptions = new AsposeCells.OoxmlSaveOptions();

ooxmlSaveOptions.setLightCellsDataProvider(new TestDataProvider(workbook, rowsCount, colsCount));

await workbook.saveAsync(path.join(dataDir, "output.out.xlsx"), ooxmlSaveOptions);
};

run();
```  

## قراءة ملفات إكسل الكبيرة  
 توفر Aspose.Cells واجهة، `LightCellsDataHandler`, يجب تنفيذها في برنامجك. تمثل الواجهة مزود البيانات لقراءة ملفات جداول البيانات الكبيرة في وضع خفيف الوزن.  

 عند قراءة دفتر عمل في هذا الوضع، يتم فحص `StartSheet` عند قراءة كل ورقة عمل في دفتر العمل. بالنسبة لورقة، إذا كانت `StartSheet` تُرجع true، يتم فحص ومعالجة جميع البيانات وخصائص الخلايا في الصفوف والأعمدة للورقة بواسطة تنفيذ هذه الواجهة. لكل صف، يتم استدعاء `StartRow` للتحقق مما إذا كان يتوجب معالجته. إذا كان يتعين معالجته، يقرأ خصائصه أولاً، ويمكن للمطور الوصول إلى خصائصه باستخدام `ProcessRow`. إذا كانت خلايا الصف أيضًا بحاجة إلى المعالجة، فيجب أن تعود `ProcessRow` بقيمة true، ثم يُستدعى `StartCell` لكل خلية موجودة في الصف للتحقق مما إذا كانت خلية واحدة تحتاج إلى المعالجة. إذا كانت خلية تتطلب المعالجة، يُستدعى `ProcessCell` لمعالجة الخلية بواسطة تنفيذ هذه الواجهة.  
### قراءة ملفات إكسل كبيرة: مثال  
يرجى رؤية الكود النموذجي التالي لرؤية عمل واجهة برمجة التطبيقات (API) LightCells. أضف وأزل، أو حدث الشرائح التوضيحية وفقًا لاحتياجاتك.  

 يقرأ البرنامج ملفًا ضخمًا يحتوي على ملايين السجلات في ورقة عمل. يستغرق الأمر وقتًا قليلاً لقراءة كل ورقة في دفتر العمل. يقرأ مثال الشفرة الملف ويسترجع إجمالي عدد الخلايا، وعدد السلاسل، وعدد الصيغ في كل ورقة عمل.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

class LightCellsDataHandlerVisitCells {
constructor() {
this.cellCount = 0;
this.formulaCount = 0;
this.stringCount = 0;
}

get CellCount() {
return this.cellCount;
}

get FormulaCount() {
return this.formulaCount;
}

get StringCount() {
return this.stringCount;
}

StartSheet(sheet) {
console.log("Processing sheet[" + sheet.getName() + "]");
return true;
}

StartRow(rowIndex) {
return true;
}

ProcessRow(row) {
return true;
}

StartCell(column) {
return true;
}

ProcessCell(cell) {
this.cellCount++;
if (cell.isFormula()) {
this.formulaCount++;
} else if (cell.getType() === AsposeCells.CellValueType.IsString) {
this.stringCount++;
}
return false;
}
}

async function run() {
const dataDir = path.join(__dirname, "data");
const opts = new AsposeCells.LoadOptions();
const v = new LightCellsDataHandlerVisitCells();
opts.setLightCellsDataHandler(v);
const wb = new AsposeCells.Workbook(path.join(dataDir, "LargeBook1.xlsx"), opts);
const sheetCount = wb.getWorksheets().getCount();
console.log("Total sheets: " + sheetCount + ", cells: " + v.CellCount
+ ", strings: " + v.StringCount + ", formulas: " + v.FormulaCount);
}

run();
```  

