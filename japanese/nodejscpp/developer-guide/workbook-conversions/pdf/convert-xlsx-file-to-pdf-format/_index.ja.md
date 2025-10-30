---
title: Node.js経由のC++を使用してXLSXファイルをPDFフォーマットに変換します。
linktitle: XLSX ファイルを PDF フォーマットに変換する
type: docs
weight: 30
url: /ja/nodejs-cpp/convert-xlsx-file-to-pdf-format/
description: このガイドでは、Aspose.Cells for Node.js via C++を使用してExcelファイル（XLSX）をPDFフォーマットに変換する方法を説明します。 
---

{{% alert color="primary" %}}

PDF（Portable Document Format）は、ドキュメントの作成に使用されるソフトウェア、ハードウェア、およびオペレーティングシステムに依存せずにドキュメントを表現するフォーマットです。PDF ファイルには、テキスト、グラフィックス、画像の任意の組み合わせをデバイスに依存せず、解像度に依存しない方法で表現することができます。PDF ファイルはしばしば圧縮されるため、元のファイルよりも少ないスペースを占めます。

時々、Microsoft ExcelファイルをPDFに変換する必要があります。そのためには、迅速で安全、正確で信頼性のある解決策が必要です。さまざまな変換ツールがこの作業を行えますが、元のExcelドキュメントのレイアウトが出力されるPDFファイルに保持されていることを確認する必要があります。画像、チャート、図形、データの書式設定、フォント、属性、色、ページ設定、テキストの方向、境界線、チャートなどは正確かつ精密にレンダリングされるべきです。[Aspose.Cells](https://products.aspose.com/cells/nodejs-cpp/)は高忠実度の変換を保証します。

このドキュメントは、画像、チャート、書式設定などを含むMicrosoft ExcelドキュメントをPDFに変換する方法について包括的な理解を提供することを目的としています。そのために、Aspose.Cells APIを使用してExcelファイルをPDFに変換する簡単なコンソールアプリケーションをNode.jsで作成する方法を示しています。変換は高精度と正確さを持って行われます。

{{% /alert %}}

## **ExcelをPDFに変換する**

この例では、テンプレートとしてExcelファイル（SampleInput.xlsx）を使用しています。ワークブックにはチャートと画像が含まれたシートがあります。各シートにはフォント、属性、色、シェーディング効果、境界線を使用したさまざまな書式があります。最初のシートには縦列チャート、最後には画像があります。

### **テンプレートの Excel ファイル**

テンプレートファイルには、チャートやメディアとしての画像を含む3つのワークシートがあります。最初のワークシートにはチャートがあり、最後のワークシートには画像があります（以下のスクリーンショット参照）。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|最初のワークシート**(売上予測)**|2番目のワークシート**(売上報告)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|3番目のワークシート**(データ入力)**|最後のワークシート**(画像)**|

### **変換プロセス**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const designerFile = path.join(dataDir, "SampleInput.xlsx");
const pdfFile = path.join(dataDir, "Output.out.pdf");

try {
// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、[Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)を呼び出してからPDFにレンダリングするのが最良です。これにより、数式依存の値が再計算され、PDFに正しい値が表示されます。

{{% /alert %}}

### **結果**

上記のコードを実行すると、アプリケーションディレクトリのFilesフォルダにPDFファイルが作成されます。
以下のスクリーンショットは、PDFページを示しています。ヘッダーとフッターも出力されたPDFファイルに保持されていることに注意してください。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|最初のワークシート**(売上予測)**|2番目のワークシート**(売上報告)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|3番目のワークシート**(データ入力)**|最後のワークシート**(画像)**|
{{< app/cells/assistant language="nodejs-cpp" >}}
