---  
title: Node.jsで列挙子を使用する方法と使用場所について  
linktitle: データの反復  
type: docs  
weight: 55  
url: /ja/nodejs-cpp/how-and-where-to-use-enumerators/  
description: Aspose.Cells for Node.js via C++ APIを通じて列挙子の使い方を学びます。  
keywords: Node.jsでの列挙子の使い方、セルの列挙子Node.js、行の列挙子Node.js、列の列挙子Node.js  
---  

{{% alert color="primary" %}}  

列挙子とは、コンテナやコレクションを横断する能力を提供するオブジェクトです。列挙子はコレクション内のデータを読み取るために使用できますが、基本的なコレクションの変更には使用できません。一方、Arrayは`getEnumerator`メソッドを定義するインターフェースであり、これにより`IEnumerator`インターフェースを返します。これはコレクションへの読み取り専用アクセスを可能にします。  

Aspose.CellsのAPIはたくさんの列挙子を提供していますが、この記事では主に以下にリストされている3つのタイプについて説明しています。  

1. セル列挙子  
1. 行列挙子  
1. 列列挙子  

{{% /alert %}}  

## **列挙子の使用方法**  

### **セル列挙子**  

セル列挙子へのアクセス方法にはさまざまな方法があり、アプリケーションの要件に基づいてこれらのメソッドのいずれかを使用できます。セル列挙子を返すメソッドは次のとおりです。  

1. [**Cells.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getEnumerator--)  
1. [**Row.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getEnumerator--)  
1. [**Range.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getEnumerator--)  

上記のすべての方法は、初期化されたセルコレクションをトラバースする列挙子を返します。  

{{% alert color="primary" %}}  

セルをトラバースする際には、コレクションを修正してはいけません（新しいセルを作成する操作や既存のセルを削除する操作）。そうしない場合、列挙子はすべてのセルを正しくトラバースできなくなる可能性があります（一部の要素が繰り返しトラバースされたり、スキップされたりすることがあります）。  

{{% /alert %}}  

次のコード例は、Cellsコレクションに対するIEnumeratorインターフェースの実装例を示しています。  

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

### **行列挙子**  

行列挙子は、[**RowCollection.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection/#getEnumerator--)メソッドを使用中にアクセスできます。次のコード例は、[**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection)に対する`IEnumerator`インターフェースの実装例を示しています。  

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

### **列列挙子**  

列の列挙子は、[**ColumnCollection.getEnumerator**](https://reference.aspose.com/cells/nodejs-cpp/columncollection)メソッドを使用中にアクセスできます。次のコード例は、[**ColumnCollection**](https://reference.aspose.com/cells/nodejs-cpp/columncollection)に対する`IEnumerator`インターフェースの実装例を示しています。  

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

## **列挙子の使用場所**  

列挙子の使用の利点について議論するために、実例を見てみましょう。  

**シナリオ**  

アプリケーションの要件は、与えられた[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)内のすべてのセルを走査してその値を読み取ることです。この目標を実装するための方法はいくつかあります。いくつかを以下で示します。  

### **表示範囲を使用する**  

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

### **MaxDataRowおよびMaxDataColumnを使用する**  

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

上記のアプローチのそれぞれがほとんど同じロジックを使用していることがわかります。つまり、コレクション内のすべてのセルをループしてセルの値を読み取ります。これにはいくつかの理由で問題が生じる可能性があります。  

1. [**getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxRow--)、[**getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--)、[**getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxColumn--)、および[**getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) などのAPIは、対応する統計情報を収集するための追加時間を必要とします。データ行列（行×列）が大きい場合、これらのAPIを使用するとパフォーマンスにペナルティが課される場合があります。  
1. ほとんどの場合、指定された範囲内のすべてのセルがインスタンス化されていません。そのような状況では、行列内のすべてのセルを確認することは、初期化されたセルのみを確認する場合と比べて効率的ではありません。  
1. Cells row、columnとしてセルにアクセスすることは、範囲内のすべてのセルオブジェクトをインスタンス化することになり、最終的にOutOfMemoryExceptionを引き起こす可能性があります。  

## **結論**  

上記の事実に基づいて、列挙子を使用すべき可能なシナリオが以下に示されています。  

1. セルコレクションの読み取り専用アクセスが必要な場合、つまり、セルの確認のみが必要な場合。  
1. 多数のセルを走査する必要がある場合。  
1. 初期化されたセル/行/列のみを走査する必要がある場合。  

