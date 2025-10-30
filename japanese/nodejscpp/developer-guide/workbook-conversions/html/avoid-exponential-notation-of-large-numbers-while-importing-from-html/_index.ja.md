---  
title: HTMLからの大きな数値の指数表記を避ける  
linktitle: HTMLからの大きな数値の指数表記を避ける  
type: docs  
weight: 10  
url: /ja/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/  
description: HTMLからのインポート時に大きな数字が指数表記に変換されるのを防ぐ方法について、Aspose.Cells for Node.js via C++を使用して学びます。  
---  

{{% alert color="primary" %}}  

時々、あなたのHTMLには1234567890123456のような数字が含まれており、15桁を超えています。これらの数字をExcelファイルにインポートすると、1.23457E+15のような指数表記に変換されてしまいます。数字をそのままインポートし、指数表記に変換されないようにするには、[**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--)プロパティを使用し、読み込み時に**true**を設定してください。  

{{% /alert %}}  

以下のサンプルコードは、[**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--)プロパティの使用法を説明しています。APIは数字をそのままインポートし、指数表記に変換しません。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Sample Html containing large number with digits greater than 15
const html = "<html><body><p>1234567890123456</p></body></html>";

// Convert Html to byte array
const byteArray = new TextEncoder().encode(html);

// Set Html load options and keep precision true
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
loadOptions.setKeepPrecision(true);

// Convert byte array into stream
const stream = byteArray;

// Create workbook from stream with Html load options
const workbook = new AsposeCells.Workbook(stream, loadOptions);

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Auto fit the sheet columns
sheet.autoFitColumns();

// Save the workbook
const outputDir = path.join(__dirname, "output/");
workbook.save(path.join(outputDir, "outputAvoidExponentialNotationWhileImportingFromHtml.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
