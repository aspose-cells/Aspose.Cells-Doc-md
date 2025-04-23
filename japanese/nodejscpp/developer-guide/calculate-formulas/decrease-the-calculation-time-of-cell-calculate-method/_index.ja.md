---  
title: Node.jsをC++経由でセルの計算時間を短縮する  
linktitle: Cell.Calculateメソッドの計算時間の短縮  
description: この記事では、Node.jsをC++経由で使用してExcelのセル計算メソッドの計算時間を短縮する方法を紹介します。  
keywords: Aspose.Cells、Excel、セル計算メソッド、最適化、パフォーマンス、計算時間短縮、Node.jsをC++経由で  
type: docs  
weight: 100  
url: /ja/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/  
---  

## **可能な使用シナリオ**

通常、[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)メソッドを一度呼び出し、その後個別のセルの計算済み値を取得することを推奨します。しかし、時にはユーザーは全体のワークブックを計算したくない場合もあります。特定のセルだけを計算したい場合、Aspose.Cellsは[**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--)プロパティを提供しており、これを**false**に設定することで個々のセルの計算時間を大幅に短縮できます。recursiveプロパティを**true**に設定すると、すべての依存セルが各呼び出し時に再計算されますが、**false**の場合、依存セルは一度だけ計算され、その後再計算されません。

## **Cell.calculate()メソッドの計算時間を短縮**

以下のサンプルコードは、[**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--)プロパティの使用例です。このコードを指定された[サンプルExcelファイル](5113710.xlsx)で実行し、そのコンソール出力を確認してください。recursiveプロパティを**false**に設定することで、計算時間が大幅に短縮されることがわかります。また、このプロパティについての詳細理解のためにコメントもお読みください。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Test calculation time after setting recursive true
workbook.calculateFormula(); // Call calculateFormula method to initiate calculation

// Test calculation time after setting recursive false
workbook.calculateFormula(false); // Specify ignoreError as false
```  
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

function testCalcTimeRecursive(rec) {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Set the calculation option, set recursive true or false as per parameter
const opts = new AsposeCells.CalculationOptions();
opts.setRecursive(rec);

// Start stop watch            
const start = process.hrtime();

// Calculate cell A1 one million times
for (let i = 0; i < 1000000; i++) {
ws.getCells().get("A1").calculate(opts);
}

// Stop the watch
const end = process.hrtime(start);

// Calculate elapsed time in seconds
const estimatedTime = end[0] + end[1] / 1e9;

// Print the elapsed time in seconds
console.log(`Recursive ${rec}: ${estimatedTime} seconds`);
}

// Call the function for testing
testCalcTimeRecursive(true);
testCalcTimeRecursive(false);
```

## **コンソール出力**

上記サンプルコードの実行結果のコンソール出力例です。[サンプルExcelファイル](5113710.xlsx)を使用しています。ご注意：出力は異なる場合がありますが、recursiveプロパティを**false**に設定した後の経過時間は、常に**true**に設定した場合よりも短くなります。

{{< highlight java >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}  

