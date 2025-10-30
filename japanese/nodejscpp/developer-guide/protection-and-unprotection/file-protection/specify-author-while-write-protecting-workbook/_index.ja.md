---  
title: Node.js経由のC++を使用してブックの書き込み保護中に著者を指定する  
linktitle: ブックを書き込み保護する際に著者を指定する  
type: docs  
weight: 40  
url: /ja/nodejs-cpp/specify-author-while-write-protecting-workbook/  
description: Aspose.Cells for Node.js via C++を使ってブックを書き込み保護する際に著者名を指定します。  
---  

## **可能な使用シナリオ**

Aspose.Cells APIを使用して書き込み保護中に著者名を指定可能です。これには[**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--)プロパティを使用してください。

## **ブックを書き込み保護する際に著者を指定する**

以下のサンプルコードは[**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--)プロパティの使用例です。このコードは空のワークブックを作成し、パスワードで書き込み保護し、著者名を指定して、[出力Excelファイル](67338582.xlsx)として保存します。以下のスクリーンショットはサンプルコードが出力Excelファイルに与える影響を示しています。

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Create empty workbook.
const workbook = new AsposeCells.Workbook();

// Write protect workbook with password.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Specify author while write protecting workbook.
workbook.getSettings().getWriteProtection().setAuthor("SimonAspose");

// Save the workbook in XLSX format.
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
