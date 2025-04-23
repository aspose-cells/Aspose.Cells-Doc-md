---
title: Node.js経由のC++を使った前提セルと従属セルの追跡
linktitle: 先行および従属
type: docs
weight: 230
url: /ja/nodejs-cpp/precedents-and-dependents/
description: Aspose.Cells for Node.js via C++ を使ったスプレッドシートの先行セルと従属セルの追跡方法を学びます。複雑な財務ワークシート内のリンクされたセルの特定方法を理解します。
---

{{% alert color="primary" %}} 

特に共同で開発された複雑な財務ワークシートは、最も恥ずかしいエラーを隠すことがあります。式の正確さをチェックし、エラーの原因を特定することは、先行セルおよび従属セルを使用する式をチェックする際に困難になるかもしれません。

{{% /alert %}} 
## **紹介**
- **先行セル** は、他のセルの数式で参照されているセルです。たとえば、セル D10 が数式 =B5 を含む場合、セル B5 はセル D10 の先行セルです。
- **従属セル** は、他のセルを参照する数式を含むセルです。例えば、セル D10 に式 `=B5` がある場合、D10 は B5 に依存しています。

スプレッドシートをわかりやすくするために、スプレッドシートに含まれるセルが式で使用されているかを明確に表示することがあります。同様に、他のセルの従属セルを抽出することがあります。

Aspose.Cells を使用すると、セルをトレースしてリンクされているセルを特定することができます。
## **先行および従属セルのトレース： Microsoft Excel**
例えば、セル C1 が式を含む C3 および C4 に依存しており、C1 が変更される場合（つまり式が上書きされる場合）、C3 および C4 などの他のセルは、ビジネスルールに基づいてスプレッドシートをバランスさせるために変更する必要があります。

同様に、C1 に式 "=(B1*22)/(M2*N32)" を含むとします。C1 が依存しているセルである先行セル B1、M2、N32 を見つけたいとします。

特定のセルの依存関係を他のセルにトレースする必要があるかもしれません。ビジネスルールが式に埋め込まれている場合、依存関係を見つけ、それに基づいていくつかのルールを実行したいと思うかもしれません。同様に、特定のセルの値が変更される場合、その変更に影響を受けるワークシート内のセルを見つけたいと思うかもしれません。

Microsoft Excel を使用すると、先行および従属をトレースすることができます。

1. **表示ツールバー**から**数式監査**を選択します。数式監査ダイアログが表示されます。
1. 先行をトレース：
   1. 先行セルを特定したい式を含むセルを選択します。
   1. 直接データを提供する各セルにトレーサーアローを表示するには、 **式監査** ツールバーの **先行をトレース** をクリックします。
1. 特定のセルを参照する式をトレースする（従属）
   1. 従属セルを特定したいセルを選択します。
   1. アクティブセルに依存する各セルにトレーサー矢印を表示するには、数式監査ツールバーの **参照先トレース** をクリックします。
## **先行および従属セルをトレース： Aspose.Cells**
### **先行をトレース**
Aspose.Cells を使用すると、先行セルを取得することが容易になります。シンプルな式の先行セルに提供されているセルだけでなく、名前付き範囲で複雑な式の先行セルに提供されているセルを見つけることもできます。

以下の例では、テンプレートの Excel ファイルである Book1.xls を使用しています。スプレッドシートには最初のワークシートにデータと数式が含まれています。

Aspose.Cellsは、[Cell](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスの[Cell.getPrecedents()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedents--)メソッドを提供しており、これを使ってセルの前提を追跡できます。返されるのは参照された範囲のコレクションです。上記の例では、「Book1.xls」のセル B7 には 「=SUM(A1:A3)」という式があり、A1:A3 のセルが B7 の前提セルです。


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
### **従属をトレース**
Aspose.Cellsは、スプレッドシート内の依存セルを取得できます。Aspose.Cellsは、単純な数式のデータを提供するセルだけでなく、名前付き範囲を含む複雑な数式の従属セルも見つけることができます。

Aspose.Cellsは、[Cell](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスの[Cell.getDependents(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependents-boolean-)メソッドを提供しており、これを使ってセルの従属セルを追跡します。例えば、「Book1.xlsx」には、「=A1+20」と「=A1+30」の数式がそれぞれ B2 および C2 にあります。以下の例は、A1 セルの従属セルを追跡する方法を示しています。


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
### **計算チェーンに従って直前および依存セルを追跡する**
上記の前提セルと従属セルの追跡APIは、数式表現自体に沿っており、少数の数式に対して相互依存関係を追跡する便利な方法を提供します。ただし、ワークブック内に多くの数式があり、すべてのセルについて前提または従属を追跡する必要がある場合、パフォーマンスが低下します。このような場合は、[Cell.getPrecedentsInCalculation()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedentsInCalculation--)と[Cell.getDependentsInCalculation(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependentsInCalculation-boolean-)を検討してください。これらのメソッドは計算チェーンに沿って依存性を追跡します。使用前に[FormulaSettings.getEnableCalculationChain()](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--)で計算チェーンを有効にし、その後[Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)で全計算を実行します。そうすれば、全セルの前提や従属を追跡できます。

一部の数式では、`getPrecedents`と`getPrecedentsInCalculation`の結果が異なる場合や、`getDependents`と`getDependentsInCalculation`の結果が異なる場合があります。例えば、セルA1の数式が `=IF(TRUE,B2,C3)` の場合、`getPrecedents`はA1の前提セルとしてB2とC3を提供します。これにより、B2とC3の両方がA1に対して従属セルとなるためです。ただし、この数式の計算においては、B2だけが結果に影響を与えることが明らかです。したがって、`getPrecedentsInCalculation`はC3をA1の前提に提供せず、`getDependentsInCalculation`はC3に対してA1を提供しません。Workbookの現在のデータに基づき、真に結果に影響する依存関係の追跡だけが必要な場合は、`getDependentsInCalculation`や`getPrecedentsInCalculation`を使用してください。

次の例は、計算チェーンに沿って前提セルと従属セルを追跡する方法を示しています:


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
