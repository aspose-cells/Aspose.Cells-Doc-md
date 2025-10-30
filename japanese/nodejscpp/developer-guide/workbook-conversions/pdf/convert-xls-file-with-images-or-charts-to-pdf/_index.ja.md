---
title: C++を使用してNode.js経由で画像やチャートを含むXLSファイルをPDFに変換します。
linktitle: 画像やグラフが含まれる XLS ファイルを PDF ドキュメントに変換する
type: docs
weight: 50
url: /ja/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cellsは、画像やチャートを含むXLSファイルをPDFドキュメントに変換することをサポートしています。Aspose.Cells for Node.js via C++は、スプレッドシートをPDFに変換する際に独立して動作します。Aspose.PDF for Node.js via C++は、変換に必要ありません。このプロセスはインメモリで行われ、一時的または中間のXMLファイルに依存しません。これにより、画像、チャート、その他の描画オブジェクトを含む大きなExcelファイルも迅速かつ効率的に変換できます。

{{% /alert %}} 
## **サンプルコード**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
try {
// Get the template excel file path.
const designerFile = path.join(dataDir, "SampleInput.xls");

// Specify the pdf file path.
const pdfFile = path.join(dataDir, "Output.out.pdf");

// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合、PDFにレンダリングする直前に[Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)を呼び出すのが最良です。これにより、数式依存の値が再計算され、正しい値がPDFにレンダリングされます。

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
