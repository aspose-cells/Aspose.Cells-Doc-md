---
title: コメントのエクスポート（ExcelをHTMLに保存）
linktitle: Excel ファイルを HTML に保存する際にコメントをエクスポート
type: docs
weight: 40
url: /ja/nodejs-cpp/export-comments-while-saving-excel-file-to/
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存するとき、コメントはエクスポートされません。ただし、Aspose.Cells for Node.js via C++はこの機能を[**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/)プロパティを使って提供しています。これを**true**に設定すれば、Excelファイルに含まれるコメントもHTMLに表示されるようになります。

## **ExcelファイルをHTMLに保存する際にコメントをエクスポート**

次のサンプルコードでは[**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/)プロパティの使用方法を説明しています。コードによるHTMLへの影響を示すスクリーンショットが**true**として設定されている場合に表示されます。参照用に、[サンプルExcelファイル](50528260.xlsx)と[生成されたHTML](5052826.txt)をダウンロードしてください。

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const sourceDir = path.join(__dirname, "data");
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportCommentsHTML.xlsx"));

// Export comments - set IsExportComments property to true
const opts = new AsposeCells.HtmlSaveOptions();
opts.setIsExportComments(true);

// Save the Excel file to HTML
const outputDir = path.join(__dirname, "output");
wb.save(path.join(outputDir, "outputExportCommentsHTML.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
