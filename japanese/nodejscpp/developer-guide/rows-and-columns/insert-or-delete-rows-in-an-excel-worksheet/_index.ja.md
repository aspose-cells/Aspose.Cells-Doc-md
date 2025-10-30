---  
title: Node.js経由のC++を使用してExcelワークシートに行を挿入または削除する  
linktitle: Excelワークシートで行を挿入または削除する  
type: docs  
weight: 20  
url: /ja/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/  
description: この記事では、C++を使用したNode.jsコードを使って、Excelワークシートに行を挿入および削除する方法を紹介します。  
keywords: node.jsでExcelワークシートに行を挿入または削除、node.jsでExcelに行を挿入または削除、node.jsを使ってExcelに行を挿入、node.jsを使ってExcelの行を削除、node.jsを使用したExcelワークシートへの行の挿入または削除、node.jsでExcelの行を挿入または削除、node.jsでExcelに行を挿入、node.jsでExcelの行を削除  
---  

{{% alert color="primary" %}}  

新しいワークシートを作成する場合や既存のワークシートを操作する場合、データに合わせて追加の行や列を追加する必要がある場合があります。その他のときには、指定された位置から行または列を削除する必要があることもあります。  

{{% /alert %}}  

Aspose.Cells for Node.js via C++は、行の挿入と削除のための二つのメソッド[**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-)と[**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-)を提供します。これらのメソッドは、パフォーマンス最適化されており、非常に迅速に処理を行います。  

行の挿入または削除の際は、ループ内で[**Cells.insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-)や[**Cells.deleteRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRow-number-)メソッドを使用するのではなく、常に[**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-)と[**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-)メソッドを使用することを推奨します。  

Aspose.CellsはMicrosoft Excelと同様に動作します。行または列が追加されると、ワークシートの内容は下方向や右方向にシフトされます。行または列が削除されると、ワークシートの内容は上方向や左方向にシフトされます。行が追加または削除された場合、他のワークシートやセル内の参照が更新されます。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object.
// Load a template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));

// Get the first worksheet in the book.
const sheet = workbook.getWorksheets().get(0);

// Insert 10 rows at row index 2 (insertion starts at 3rd row)
sheet.getCells().insertRows(2, 10);

// Delete 5 rows now. (8th row - 12th row)
sheet.getCells().deleteRows(7, 5);

// Save the excel file.
workbook.save(path.join(dataDir, "out_book1.out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
