---
title: Aspose.Cells for Node.js via C++を使用したIFNA関数の計算
description: Aspose.Cellsライブラリを使用して、Node.js via C++でIFNA関数を計算する方法。既存のExcelファイルをロードするか新規作成し、IFNA関数を計算して結果を得ます。最後に変更したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、IFNA関数、計算、Node.js via C++
type: docs
weight: 40
url: /ja/nodejs-cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.CellsはExcelのIFNA関数の計算をサポートしています。IFNA関数は、式が#N/Aエラーを返した場合に指定した値を返し、それ以外の場合は式の結果を返します。

{{% /alert %}} 
## **Aspose.Cells for Node.js via C++を使ったIFNA関数の計算例**
以下のサンプルコードは、Aspose.Cells for Node.js via C++を用いてIFNA関数の計算を示しています。


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create new workbook
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add data for VLOOKUP
worksheet.getCells().get("A1").putValue("Apple");
worksheet.getCells().get("A2").putValue("Orange");
worksheet.getCells().get("A3").putValue("Banana");

// Access cell A5 and A6
const cellA5 = worksheet.getCells().get("A5");
const cellA6 = worksheet.getCells().get("A6");

// Assign IFNA formula to A5 and A6
cellA5.setFormula('=IFNA(VLOOKUP("Pear",$A$1:$A$3,1,0),"Not found")');
cellA6.setFormula('=IFNA(VLOOKUP("Orange",$A$1:$A$3,1,0),"Not found")');

// Calculate the formula of workbook
workbook.calculateFormula();

// Print the values of A5 and A6
console.log(cellA5.getStringValue());
console.log(cellA6.getStringValue());
```
## **コンソール出力**
上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight javascript >}}
 Not found

Orange
{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
