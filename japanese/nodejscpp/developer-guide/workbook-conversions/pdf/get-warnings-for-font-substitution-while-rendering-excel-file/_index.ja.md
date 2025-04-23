---  
title: Excelファイルのレンダリング時にフォント置換の警告を取得する  
linktitle: Excelファイルをレンダリングする際にフォントの置換ワーニングを取得  
type: docs  
weight: 230  
url: /ja/nodejs-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/  
description: Aspose.Cells for Node.js via C++を使用してExcelファイルをPDFにレンダリングしたときのフォント置換の警告を取得する方法を学びます。  
---  

{{% alert color="primary" %}}  

Microsoft ExcelファイルをPDFにレンダリングする際、Aspose.Cellsはフォントを置換する場合があります。Aspose.Cellsには、特定のフォントが置換されたことを開発者に知らせる機能が備わっており、警告を表示することができます。これは、Aspose.Cellsがレンダリング結果が元のMicrosoft Excelファイルと異なって見える理由を特定し、適切な対策を取るための有用な機能です。たとえば、不足しているフォントをインストールして、レンダリング結果が同じに見えるようにできます。

{{% /alert %}}  

ExcelファイルをPDFにレンダリングする際のフォント置換警告を取得するには、IWarningCallbackインターフェースを実装し、PdfSaveOptions.warningCallbackプロパティに設定します。

以下のスクリーンショットは、次のコードで使用する元のExcelファイルを示しています。セルA6およびA7には、Microsoft Excelによって正しくレンダリングされないフォントでテキストが含まれています。

|**すべてのフォントが正しくレンダリングされているわけではありません**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|  
Aspose.Cellsは、セルA6とA7のフォントを適切なフォントで置き換えます。

|**置き換えフォント**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|  
## **ソースファイルと出力PDFのダウンロード**  
以下のリンクからソースExcelファイルと出力PDFをダウンロードできます

- [source.xlsx](5112611.xlsx)  
- [output.pdf](5112616.pdf)  
## **コード**  
以下のコードは、IWarningCallbackを実装し、PdfSaveOptions.warningCallbackプロパティに設定しています。これにより、セル内でフォントが置換された場合、Aspose.CellsはWarningCallback.Warning()メソッド内で警告を発します。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

class GetWarningsForFontSubstitution {
static warning(info) {
if (info.getType() === AsposeCells.WarningType.FontSubstitution) {
console.log("WARNING INFO: " + info.getDescription());
}
}

static run() {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setWarningCallback(GetWarningsForFontSubstitution);
const outputFilePath = path.join(dataDir, "output_out.pdf");
workbook.save(outputFilePath, options);
}
}
```  
## **出力**  
ExcelファイルをPDFに変換した後、警告は次のようにデバッグコンソールに出力されます。

{{< highlight java >}}  

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].  

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].  

{{< /highlight >}}  

{{% alert color="primary" %}}  

スプレッドシートに数式が含まれている場合、スプレッドシートをPDF形式にレンダリングする直前にWorkbook.calculateFormulaメソッドを呼び出すのがベストです。これにより、数式に依存する値が再計算され、正しい値がPDFに表示されます。

{{% /alert %}}  

