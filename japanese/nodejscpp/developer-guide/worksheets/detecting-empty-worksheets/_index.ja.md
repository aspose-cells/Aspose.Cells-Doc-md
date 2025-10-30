---  
title: Node.js経由のC++で空のシートを検出  
linktitle: 空のワークシートを検出する  
type: docs  
weight: 410  
url: /ja/nodejs-cpp/detecting-empty-worksheets/  
description: この記事では、Node.js APIとC++ライブラリを使用してExcelワークブックの空のシートをプログラム的に検出する方法を説明します。  
keywords: 空のシートを検出 Node.js via C++、空のExcelシートを見つける Node.js via C++  
---  

## **空の初期化されたセルのチェック**

シートには値が設定されているセルが一つまたは複数あり、これらの値は単純なもの（テキスト、数値、日時）や数式または数式に基づく値である場合があります。そのため、シートが空かどうかを検出するのは容易です。確認すべきプロパティは[**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--)または[**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--)です。前述したプロパティがゼロまたは正の値を返す場合、そのシートには一つ以上のセルが値で埋まっています。逆に、これらのプロパティが-1を返す場合、そのシートにはセルが値で埋まっていないことを示します。

{{% alert color="primary" %}}

行と列のコレクションはゼロベースのインデックスを持つため、行0、列0のセルはシートの最初のセル、すなわちA1を意味します。

{{% /alert %}}

## **空の初期化されたセルのチェック**

値が設定されているすべてのセルは自動的に初期化されます。ただし、シートに書式のみが適用されたセルが存在する可能性もあります。この場合、[**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--)または[**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--)のプロパティは-1を返し、値が設定されていないことを示します。ただし、セルの書式によりセルが初期化されているかどうかはこの方法では検出できません。空の初期化済みセルがあるかどうかを確認するには、[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションから取得した列挙子の`Enumerator.MoveNext`メソッドを使用することを推奨します。`MoveNext`がtrueを返す場合、シート内に1つ以上の初期化済みセルが存在します。

## **図形のチェック**

特定のシートに値が設定されたセルが一つもない可能性がありますが、コントロール、チャート、画像などの形状やオブジェクトが含まれている場合もあります。シートに形状が含まれているかどうかを確認するには、[**ShapeCollection.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#getCount--)プロパティを調べます。正の値は、シートに形状が存在することを示します。

## **プログラミングサンプル**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);

// Loop over all worksheets in the workbook
for (let i = 0; i < book.getWorksheets().getCount(); i++) {
const sheet = book.getWorksheets().get(i);
// Check if worksheet has populated cells
if (sheet.getCells().getMaxDataRow() !== -1) {
console.log(`${sheet.getName()} is not empty because one or more cells are populated`);
}
// Check if worksheet has shapes
else if (sheet.getShapes().getCount() > 0) {
console.log(`${sheet.getName()} is not empty because there are one or more shapes`);
}
// Check if worksheet has empty initialized cells
else {
const range = sheet.getCells().getMaxDisplayRange();
const rangeIterator = range.getEnumerator();
if (rangeIterator.moveNext()) {
console.log(`${sheet.getName()} is not empty because one or more cells are initialized`);
}
}
}
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
