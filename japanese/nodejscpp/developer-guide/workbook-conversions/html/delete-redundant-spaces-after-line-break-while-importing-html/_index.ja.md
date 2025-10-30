---
title: Node.jsとC++を使用してHTMLのインポート時に余分なスペースを削除
linktitle: HTMLのインポート時に改行後の余分なスペースを削除する
type: docs
weight: 20
url: /ja/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Aspose.Cells for Node.js via C++を使ってHTMLインポート時に余分なスペースを削除する方法を学びます。
---

{{% alert color="primary" %}}

[**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--) プロパティを使用し、それを **true** に設定して、改行タグの後に来るすべての余分なスペースを削除してください。デフォルトではこのプロパティは **false** であり、余分なスペースは出力されるExcelファイルに保持されます。

{{% /alert %}}

## HTMLLoadOptions.deleteRedundantSpacesプロパティをfalseとtrueに設定した場合の効果

このプロパティを**false**と**true**に設定した効果を以下のスクリーンショットで示します。

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

HTMLをインポートする際に改行後の余分なスペースを削除する効果

### プログラミングサンプル

以下のサンプルコードは、[**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--)プロパティの使用例を示しています。出力結果を上記スクリーンショットのように得るには、**true**または**false**に設定してください。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Sample Html containing redundant spaces after <br> tag
const html = "<html> <body> <table> <tr> <td> <br>    This is sample data <br>    This is sample data<br>    This is sample data</td> </tr> </table> </body> </html>";

// Convert Html to byte array
const byteArray = Buffer.from(html, 'utf-8');

// Set Html load options and keep precision true
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
loadOptions.setDeleteRedundantSpaces(true);

// Convert byte array into stream
const stream = Uint8Array.from(byteArray);

// Create workbook from stream with Html load options
const workbook = new AsposeCells.Workbook(stream, loadOptions);

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Auto fit the sheet columns
sheet.autoFitColumns();

// Save the workbook
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputDeleteRedundantSpacesWhileImportingFromHtml.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
