---  
title: Node.js経由のC++を使用して各ワークシートを異なるPDFファイルに保存  
linktitle: 異なるPDFファイルにそれぞれのワークシートを保存する  
type: docs  
weight: 130  
url: /ja/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/  
---  

{{% alert color="primary" %}}  
Aspose.Cellsは、画像やチャートなどを含むXLSファイルをPDFドキュメントに変換することをサポートします。Aspose.Cells for Node.js via C++は、スプレッドシートをPDFに変換するために独立して動作できます。変換にはAspose.PDF for Node.jsをC++経由で使用する必要はありません。変換には一時ファイルの作成や使用は不要で、すべてメモリ内で完了できます。  
{{% /alert %}}  

## **異なるPDFファイルごとに各ワークシートを保存**  
テンプレートのExcelファイル内の各ワークシートを保存して異なるPDFファイルを生成したい場合は、簡単に実現できます。各シートのインデックスを[**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/nodejs-cpp/pdfs saveoptions/#sheetSet)オプションに設定してPDFにレンダリングしてみてください。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Get the Excel file path
const filePath = path.join(dataDir, "input.xlsx");

// Instantiate a new workbook and open the Excel file from its location
const workbook = new AsposeCells.Workbook(filePath);

// Get the count of the worksheets in the workbook
const sheetCount = workbook.getWorksheets().getCount();

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Take PDFs of each sheet
for (let j = 0; j < sheetCount; j++) {
const ws = workbook.getWorksheets().get(j);

// set worksheet to output
const sheetSet = new AsposeCells.SheetSet([ws.getIndex()]);
pdfSaveOptions.setSheetSet(sheetSet);

workbook.save(path.join(dataDir, `worksheet-${ws.getName()}.out.pdf`), pdfSaveOptions);
}
```  

{{% alert color="primary" %}}  
スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。  
{{% /alert %}}  

