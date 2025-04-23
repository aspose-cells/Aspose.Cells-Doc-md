---  
title: Node.jsとC++を用いてExcelシートの固定ペインを設定  
linktitle: ウィンドウ枠の固定  
type: docs  
weight: 190  
url: /ja/nodejs-cpp/how-to-freeze-panes-of-excel-worksheet  
description: この記事では、Aspose.Cells for Node.js via C++を使ってExcelシートのペインをプログラム的に固定する方法を説明します。  
keywords: ペインを固定、ウィンドウを固定。  
---  

## **紹介**  

この記事では、ペインを固定する方法を学びます。共通の見出しの下に大量のデータがある場合、ヘッダーがスクロールダウン時に見えなくなることがあります。このとき、ペインを固定すると、その固定部分はスクロールしても見えるままです。ヘッダー行や最初の列を簡単に見ることができます。ペインの固定と解除は、データの表示を変更せずにデータ自体を変更しません。  

## **Excelで**  

**![Excelでのウィンドウ枠の固定](Freeze-panes.png)**  

1. 固定ペインを作成したい場合は、行と列を固定します。まずセル（例：B2）を選択してください。  
2. 表示 > ウィンドウ枠の固定をクリックします。  
3. ドロップダウンメニューで、ウィンドウ枠の固定をクリックします。  
4. 下または右にスクロールすると、最初の行と列が固定されます。  

**![固定ペイン](Frozen-Panes.png)**  

ご覧のとおり、最初の行と列Aが固定されており、2行目は32、2番目に見える列はDです。  

固定ペインは、大きなデータを閲覧しながら行や列のラベルを追跡しなくても済むようにする機能です。  

## **Aspose.Cells for Node.js via C++を使用した固定ペイン**  
Aspose.Cells for Node.js via C++を使えば、簡単に固定ペインを作成できます。[**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-)メソッドを使用して、選択したセルに固定ペインを設定してください。  
1. ファイルを開くためにワークブックを作成します。または空のファイルを作成します。  
2. Worksheet.freezePanes()メソッドを使用して固定ペインを設定。  
3. ファイルを保存します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Freeze.xlsx")); 
// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("B2", 1, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

添付 [サンプルExcelファイル](Freeze.xlsx)。  

