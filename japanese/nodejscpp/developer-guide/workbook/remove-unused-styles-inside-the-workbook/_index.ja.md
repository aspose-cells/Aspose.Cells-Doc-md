---  
title: 不要なスタイルをWorkbook内から削除するNode.js経由のC++サンプル  
linktitle: ワークブック内の未使用のスタイルを削除する  
type: docs  
weight: 340  
url: /ja/nodejs-cpp/remove-unused-styles-inside-the-workbook/  
description: Aspose.Cells for Node.js via C++を使用してワークブックから未使用スタイルを削除する方法を学ぶ。  
---  

{{% alert color="primary" %}}  
Excelファイルの未使用スタイルは容量を増やすだけでなく、PDFやHTMLなど他のフォーマットに変換する際にパフォーマンス問題も引き起こします。Aspose.Cellsは、[**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--)を提供し、ワークブック内の未使用スタイルをすべて削除します。  
{{% /alert %}}  

次のコードは [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--) の使用法を説明しています。このコードは提供されたリンクからダウンロード可能な [テンプレートExcelファイル](5115520.xlsx) を読み込みます。これは未使用のスタイル **AsposeStyle** を含んでいます; このスタイル及びすべての未使用スタイルは、コードの実行後に削除されます。  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Template-With-Unused-Custom-Style.xlsx");

// Load template excel file containing unused styles
const workbook = new AsposeCells.Workbook(filePath);

// Remove all unused styles inside the template this will also remove AsposeStyle which is an unused style inside the template
workbook.removeUnusedStyles();

// Save the file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
