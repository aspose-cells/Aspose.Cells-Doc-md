---  
title: Aspose.Cells for Node.js via C++を使用したテキストの列への変換  
linktitle: テキストを列に変換  
type: docs  
weight: 30  
url: /ja/nodejs-cpp/convert-text-to-columns-using-aspose-cells/  
description: Aspose.Cells for Node.js via C++を使ったExcelのテキストを列に変換する方法を学ぶ。  
---  

## **可能な使用シナリオ**  

Microsoft Excelを使用してテキストを列に変換できます。この機能はデータタブの【データツール】から利用可能です。列の内容を複数の列に分割するには、カンマやその他の区切り文字を含む必要があります。Aspose.Cells for Node.js via C++もこの機能を[**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-)経由で提供しています。  

## **Aspose.Cells for Node.js via C++を使用したテキストの列への変換**  

以下のサンプルコードは[**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-)メソッドの使い方を説明します。最初のワークシートのA列に人名を追加し、名字と名前はスペースで区切っています。その後、A列に対して[**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-)メソッドを適用し、出力Excelファイルに保存します。もし[出力Excelファイル](25395213.xlsx)を開けば、名前がA列に、苗字がB列に表示されているのが確認できます。  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add people name in column A. First name and last name are separated by space.
ws.getCells().get("A1").putValue("John Teal");
ws.getCells().get("A2").putValue("Peter Graham");
ws.getCells().get("A3").putValue("Brady Cortez");
ws.getCells().get("A4").putValue("Mack Nick");
ws.getCells().get("A5").putValue("Hsu Lee");

// Create text load options with space as separator.
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(' ');

// Split the column A into two columns using TextToColumns() method.
// Now column A will have first name and column B will have second name.
ws.getCells().textToColumns(0, 0, 5, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputTextToColumns.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
