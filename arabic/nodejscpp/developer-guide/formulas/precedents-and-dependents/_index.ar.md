---
title: الأسلاف والمعتمدون باستخدام Node.js عبر C++
linktitle: الدوائر والتبعيات
type: docs
weight: 230
url: /ar/nodejs-cpp/precedents-and-dependents/
description: تعلّم كيف تتبع الخلايا السابقة والمعتمدة في جداول البيانات باستخدام Aspose.Cells for Node.js via C++. فهم كيف تحدد الخلايا المرتبطة في جداول مالية معقدة.
---

{{% alert color="primary" %}} 

ورق العمل المالي المعقد، خصوصًا تلك التي تم تطويرها بالتعاون، يمكن أن تخفي الأخطاء الأكثر إحراجًا. فحص الصيغ لضمان الدقة والعثور على مصدر الخطأ يمكن أن يكون صعبًا عندما تستخدم الصيغ خلايا سابقة وخلايا معولة.

{{% /alert %}} 
## **مقدمة**
- **الخلايا المسبقة** هي الخلايا التي يشير إليها صيغة في خلية أخرى. على سبيل المثال، إذا كانت الخلية D10 تحتوي على الصيغة =B5، فإن الخلية B5 هي مسبقة للخلية D10.
- **الخلايا المعتمدة** تحتوي على صيغ تشير إلى خلايا أخرى. على سبيل المثال، إذا كانت الخلية D10 تحتوي على الصيغة =B5، فإن D10 تعتمد على B5.

لجعل ورق العمل سهل القراءة، قد ترغب في إظهار بشكل واضح الخلايا المستخدمة في صيغة. بالمثل، قد ترغب في استخراج الخلايا المعولة لخلايا أخرى.

تتيح Aspose.Cells لك تتبع الخلايا ومعرفة الخلايا المرتبطة.
## **تتبع خلايا السابقة والتابعة: مايكروسوفت إكسل**
قد تتغير الصيغ استنادًا إلى التعديلات التي قام بها العميل. على سبيل المثال ، إذا كانت الخلية C1 معتمدة على C3 و C4 التي تحتوي على صيغة ، وتم تغيير C1 (بحيث يتم تجاوز الصيغة) ، فيجب تغيير C3 و C4 ، أو غيرها من الخلايا ، لتوازن الجدول الخماسي استنادًا إلى قواعد الأعمال.

بالمثل ، فلنفترض أن C1 تحتوي على الصيغة "=(B1*22)/(M2*N32)". أريد أن أجد الخلايا التي يعتمد C1 عليها ، أي الخلايا السابقة B1 و M2 و N32.

قد تحتاج إلى تتبع التبعية لخلية معينة إلى خلايا أخرى. إذا تم تضمين قواعد الأعمال في الصيغ ، نود معرفة التبعيات وتنفيذ بعض القواعد استنادًا إليها. بالمثل ، إذا تم تعديل قيمة خلية معينة ، فأي الخلايا في ورقة العمل يتأثر بتلك التغيير؟

تسمح مايكروسوفت إكسل للمستخدمين بتتبع الخلايا السابقة والتابعة.

1. في شريط الأدوات **View Toolbar** ، حدد **Formula Auditing**. سيتم عرض مربع حوار Formula Auditing.
1. تتبع السابقين:
   1. حدد الخلية التي تحتوي الصيغة التي تريد العثور على الخلايا السابقة لها.
   1. لعرض السهم التتبع إلى كل خلية توفر بيانات مباشرة للخلية النشطة، انقر على **تتبع السابقين** على شريط أدوات **تدقيق الصيغ**.
1. تتبع الصيغ التي تشير إلى خلية معينة (التوابع)
   1. حدد الخلية التي تريد تحديد الخلايا التابعة لها.
   1. لعرض سهم التتبع لكل خلية تعتمد على الخلية النشطة، انقر على **تتبع المعتمدين** على شريط أدوات تدقيق الصيغ.
## **تتبع خلايا السابقة والتابعة: Aspose.Cells**
### **تتبع السابقين**
يسهل Aspose.Cells الحصول على الخلايا المسبقة. يمكن لها ألا تسترد الخلايا التي تقدم البيانات للسلف المبسط فحسب بل تجد أيضًا الخلايا التي تقدم البيانات للسلف المعقد مع النطاقات المسماة.

في المثال أدناه، يتم استخدام ملف إكسل نموذجي، Book1.xls. يحتوي جدول البيانات على بيانات وصيغ على ورقة العمل الأولى.

توفر Aspose.Cells فئة [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) وطريقة [Cell.getPrecedents()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedents--) المستخدمة لتتبع الخلايا السابقة. تعيد مجموعة من المناطق المعنوية. كما ترى أعلاه، تحتوي الخلية B7 في ملف Book1.xls على صيغة "=SUM(A1:A3)". لذلك، تعتبر الخلايا A1:A3 الخلايا السابقة للخلية B7. المثال التالي يوضح استخدام ميزة تتبع السابقين باستخدام ملف النموذج Book1.xls.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
const cell = cells.get("B4");
// Check if the cell object is not null before proceeding
if (cell) 
{
const ret = cell.getPrecedents();
if (!ret.isNull() && ret.getCount() > 0)
{
const area = ret.get(0);
console.log(area.getSheetName());
console.log(AsposeCells.CellsHelper.cellIndexToName(area.getStartRow(), area.getStartColumn()));
console.log(AsposeCells.CellsHelper.cellIndexToName(area.getEndRow(), area.getEndColumn()));
}
else
{
console.error("No precedents found for the cell.");
}
} 
else 
{
console.error("Cell B4 is null.");
}
```
### **تتبع المعتمدين**
تتيح لك Aspose.Cells الحصول على الخلايا المعتمدة في جداول البيانات. لا تقتصر على استرجاع الخلايا التي توفر البيانات لصيغة بسيطة فحسب، بل أيضًا العثور على الخلايا التي توفر البيانات للمعتمدين على صيغة معقدة مع النطاقات المسماة.

توفر Aspose.Cells فئة [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) وطريقة [Cell.getDependents(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependents-boolean-) لتتبع الخلايا المعتمدة. على سبيل المثال، في ملف Book1.xlsx يوجد صيغ: "=A1+20" و"=A1+30" في الخليتين B2 و C2 على التوالي. يظهر المثال التالي كيف تتبع المعتمدين على الخلية A1 باستخدام ملف النموذج Book1.xlsx.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
const cell = cells.get("B2");
// Ensure dependents is an array
const dependents = cell.getDependents(true);

if (Array.isArray(dependents)) 
{
for (const c of dependents) 
{
console.log(c.getName());
}
} 
else 
{
console.error("Dependents is not an array");
}
```
### **تتبع الخلايا المسبقة والمعتمدة وفقًا لسلسلة الحساب**
واجهات برمجة التطبيقات أعلاه لتتبع السابقين والمعتمدين تعتمد على تعبير الصيغة نفسه. فهي توفر فقط وسيلة مريحة للمستخدمين لتتبع التداخلات بين عدة صيغ. إذا كان هناك عدد كبير من الصيغ في ملف العمل واحتاج المستخدم لتتبع السابقين والمعتمدين لكل خلية، فإن الأداء سيكون ضعيفًا. في مثل هذه الحالة، ينبغي للمستخدم التفكير في استخدام [Cell.getPrecedentsInCalculation()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedentsInCalculation--) و [Cell.getDependentsInCalculation(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependentsInCalculation-boolean-) لمعرفة التداخلات بناءً على سلسلة الحسابات. لذا، لتفعيلها، تحتاج أولاً إلى تمكين سلسلة الحساب باستخدام [FormulaSettings.getEnableCalculationChain()](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--). ثم تقوم بأداء حساب كامل للمصنف باستخدام [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--). بعد ذلك، يمكنك تتبع السابقين أو المعتمدين لكل تلك الخلايا حسب الحاجة.

بالنسبة لبعض الصيغ، قد تكون النتائج السابقة مختلفة بين getPrecedents و getPrecedentsInCalculation، وقد تكون النتائج المعتمدة المختلفة بين getDependents و getDependentsInCalculation. على سبيل المثال، إذا كانت صيغة A1 هي "=IF(TRUE, B2, C3)", فإن getPrecedents ستوفر B2 و C3 كسابقين لـ A1. وبالمثل، يكون كل من B2 و C3 معتمدين على A1 عند التحقق باستخدام getDependents. ومع ذلك، من الواضح أن B2 هو الوحيد الذي يمكن أن يؤثر على الناتج المحسوب في حساب هذه الصيغة، لذلك لن يوفر getPrecedentsInCalculation C3 لـ A1، ولن يوفر getDependentsInCalculation A1 لـ C3. أحيانًا، قد يحتاج المستخدم فقط إلى تتبع تلك التداخلات التي تؤثر فعليًا على النتيجة المحسوبة للصيغ اعتمادًا على بيانات ملف العمل الحالية، ثم عليهم استخدام getDependentsInCalculation/getPrecedentsInCalculation بدلاً من getDependents/getPrecedents.

المثال التالي يوضح كيفية تتبع السابقين والمعتمدين وفقًا لسلسلة الحساب للخلايا:


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
cells.get("A1").setFormula("=B1+SUM(B1:B10)+[Book1.xls]Sheet1!B2");
cells.get("A2").setFormula("=IF(TRUE,B2,B1)");
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);
workbook.calculateFormula();

let en = cells.get("B1").getDependentsInCalculation(false);
console.log("B1's calculation dependents:");
for (var cell of en) {
console.log(cell.getName());
}


en = cells.get("B2").getDependentsInCalculation(false);
console.log("B2's calculation dependents:");
for (var cell of en) {
console.log(cell.getName());
}

en = cells.get("A1").getPrecedentsInCalculation();
console.log("A1's calculation precedents:");
for (var area of en) {
console.log(area.toString());
}


en = cells.get("A2").getPrecedentsInCalculation();
console.log("A2's calculation precedents:");
for (var area of en) {
console.log(area.toString());
}
```
