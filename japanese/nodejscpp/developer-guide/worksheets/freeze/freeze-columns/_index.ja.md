---  
title: Excel ワークシートの最初の列を固定する方法[Node.js/C++]  
linktitle: 列を固定する  
type: docs  
weight: 190  
url: /ja/nodejs-cpp/how-to-freeze-columns-of-excel-worksheet  
description: プログラムを通じて左側の列を固定する方法を学びます。Aspose.Cells for Node.js via C++ を使用。  
keywords: 左の列を固定、最初の列を固定、列をロックする  
---  

## **紹介**  

この記事では、左列を固定する方法について学びます。行内の大量のデータを扱う場合、水平にスクロールしたときに左列が見えなくなることがあります。左列を固定してロックすれば、その固定部分を見ることができ、スクロールしてもヘッダーが見えるままです。  

## **Excelでの列の固定**  

**![Excelで左列を固定する](freeze-columns.png)**  

1. 左の列を固定したい場合、その列の下の列を最初に選択します。
2. 表示 > ウィンドウ枠の固定をクリックします。
3. ドロップダウンメニューで「最初の列を固定」をクリックします。
4. 下にスクロールしても、最初の列は常に左側のビューに固定されます。

**![固定された列](frozen-columns.png)**  

ご覧の通り、最左列が固定されており、横スクロールしても最上部にロックされたままです。

列を固定すると、長いデータも心配せずに閲覧できます。

## **Aspose.Cells for Node.js via C++ で列を固定する**  
Aspose.Cells for Node.js via C++を使用すると、最初の列を固定するのは簡単です。  
選択した列に列を固定するには、[**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-)メソッドを使用してください。  
1. ファイルを開くためにワークブックを作成します。または空のファイルを作成します。
2. Worksheet.freezePanes() メソッドを使用して最初の列を固定します。
3. ファイルを保存します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Freezing panes at the second column
workbook.getWorksheets().get(0).freezePanes("B1", 0, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

添付 [サンプルExcelファイル](Freeze.xlsx)。  

