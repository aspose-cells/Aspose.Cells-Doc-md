---
title: Предки и зависимые с помощью Node.js через C++
linktitle: Прецеденты и зависимые
type: docs
weight: 230
url: /ru/nodejs-cpp/precedents-and-dependents/
description: Узнайте, как отслеживать предки и зависимые ячейки в электронных таблицах, используя Aspose.Cells for Node.js via C++. Поймите, как идентифицировать связанные ячейки в сложных финансовых листах.
---

{{% alert color="primary" %}} 

Сложные финансовые рабочие листы, особенно те, которые разработаны в сотрудничестве, могут скрывать наиболее нелестные ошибки. Проверка формул на точность и поиск источника ошибки может быть сложной, когда формула использует предшествующие и зависимые ячейки.

{{% /alert %}} 
## **Введение**
- **Предшествующие ячейки** - это ячейки, на которые ссылается формула в другой ячейке. Например, если ячейка D10 содержит формулу =B5, то ячейка B5 является предшествующей по отношению к ячейке D10.
- **Зависимые ячейки** содержат формулы, ссылающиеся на другие ячейки. Например, если ячейка D10 содержит формулу =B5, то D10 зависит от B5.

Чтобы сделать таблицу удобной для чтения, вы можете явно показать, какие ячейки в таблице используются в формулах. Точно так же, вы можете извлечь зависимые ячейки других ячеек.

Aspose.Cells позволяет отслеживать ячейки и выяснять, какие из них связаны между собой.
## **Отслеживание предшествующих и зависимых ячеек: Microsoft Excel**
Формулы могут изменяться в зависимости от изменений, внесенных клиентом. Например, если ячейка C1 зависит от того, что в C3 и C4 содержится формула, и C1 изменяется (что приводит к перезаписи формулы), то C3 и C4 или другие ячейки должны измениться, чтобы сбалансировать таблицу согласно правилам бизнеса.

Точно так же, предположим, что C1 содержит формулу "=(B1*22)/(M2*N32)". Я хочу найти ячейки, от которых зависит C1, то есть предшественники B1, M2 и N32.

Вам может потребоваться определить зависимость конкретной ячейки от других ячеек. Если деловые правила закодированы в формулах, мы хотели бы узнать зависимость и выполнить некоторые правила на ее основе. Точно так же, если значение конкретной ячейки изменено, какие ячейки в листе электронной таблицы затронуты этим изменением?

Microsoft Excel позволяет пользователям отслеживать предшественников и зависимых.

1. На **Панели инструментов Вид** выберите **Аудит формул**. Будет отображено диалоговое окно Аудит формул.
1. Следить за предшественниками:
   1. Выберите ячейку, содержащую формулу, для которой вы хотите найти предшествующие ячейки.
   1. Чтобы отобразить стрелку маршрута к каждой ячейке, которая непосредственно предоставляет данные для активной ячейки, щелкните **Отслеживание предшественников** на **Панели инструментов Проверка формул**.
1. Отследить формулы, которые ссылается на конкретную ячейку (зависимости)
   1. Введите ячейку, для которой вы хотите найти зависимые ячейки.
   1. Чтобы отображать стрелку-трассировщик для каждой зависимой от активной ячейки, нажмите **Следить за зависимыми** на панели инструментов Формульного аудита.
## **Отслеживание предшественников и зависимых ячеек: Aspose.Cells**
### **Отслеживание предшественников**
Aspose.Cells позволяет легко получить предшествующие ячейки. Он может не только извлекать ячейки, которые предоставляют данные для простых предшественников формул, но и находить ячейки, которые предоставляют данные для сложных предшественников формул с именованными диапазонами.

В приведенном ниже примере используется шаблонный файл Excel, Book1.xls. На первом листе электронной таблицы содержатся данные и формулы.

Aspose.Cells предоставляет метод [Cell.getPrecedents()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedents--) класса [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell), используемый для отслеживания предков ячейки. Он возвращает коллекцию ссылочных областей. Как видно из примера, в Book1.xls, в ячейке B7 содержится формула "=SUM(A1:A3)". Поэтому ячейки A1:A3 являются предками ячейки B7. Следующий пример демонстрирует функцию отслеживания предков с использованием файла-шаблона Book1.xls.


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
### **Отслеживание зависимых**
Aspose.Cells позволяет получать зависимые ячейки в электронных таблицах. Aspose.Cells может не только извлекать ячейки, содержащие данные о простой формуле, но и находить ячейки, предоставляющие данные для сложных формул с именованными диапазонами.

Aspose.Cells предоставляет метод [Cell.getDependents(boolean)]](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependents-boolean-) класса [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell), используемый для отслеживания зависимых ячейок. Например, в Book1.xlsx в ячейках B2 и C2 содержатся формулы "=A1+20" и "=A1+30" соответственно. Следующий пример демонстрирует, как отслеживать зависимые ячейки для A1 с использованием файла-шаблона Book1.xlsx.


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
### **Отслеживание предшествующих и зависимых ячеек в соответствии с цепочкой вычислений**
Вышеуказанные API для отслеживания предков и зависимых работают согласно самим выражениям формул. Они просто предоставляют удобный способ отслеживать взаимозависимости для нескольких формул. Если в рабочей книге много формул и необходимо отслеживать предков и зависимых для каждой ячейки, это будет работать плохо. В таком случае рекомендуется использовать методы [Cell.getPrecedentsInCalculation()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedentsInCalculation--) и [Cell.getDependentsInCalculation(boolean)]](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependentsInCalculation-boolean-), которые отслеживают зависимости согласно цепочке вычислений. Для этого сначала нужно включить цепочку вычислений с помощью [FormulaSettings.getEnableCalculationChain()](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--), а затем выполнить полное вычисление рабочей книги с помощью [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--). После этого можно отслеживать предков или зависимых для всех нужных вам ячеек.

Для некоторых формул возможны разные предки при использовании getPrecedents и getPrecedentsInCalculation, а зависимые — при использовании getDependents и getDependentsInCalculation. Например, если формула в ячейке A1 — "=IF(TRUE,B2,C3)", то getPrecedents покажет B2 и C3 как предков A1. Аналогично, B2 и C3 будут зависимыми при проверке через getDependents. Однако для вычисления этой формулы очевидно, что только B2 может повлиять на результат. Поэтому getPrecedentsInCalculation не покажет C3 для A1, и getDependentsInCalculation не покажет A1 для C3. Иногда пользователи могут иметь требования отслеживать только те взаимозависимости, которые действительно влияют на результат формул в текущих данных рабочей книги, и в таком случае рекомендуется использовать getDependentsInCalculation/getPrecedentsInCalculation вместо getDependents/getPrecedents.

Следующий пример демонстрирует, как отслеживать предков и зависимых в соответствии с цепочкой вычислений для ячеек:


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
{{< app/cells/assistant language="nodejs-cpp" >}}
