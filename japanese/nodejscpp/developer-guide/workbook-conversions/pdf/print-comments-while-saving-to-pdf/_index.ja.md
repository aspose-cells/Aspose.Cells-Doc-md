---  
title: Node.js経由のC++を使ってPDFに保存する際にコメントを印刷します  
linktitle: PDFへ保存する際にコメントを印刷する  
type: docs  
weight: 10  
url: /ja/nodejs-cpp/print-comments-while-saving-to-pdf/  
description: Aspose.Cells for Node.js via C++を使用してExcelドキュメントをPDFに保存するときにコメントを印刷する方法を学びましょう。  
---  

{{% alert color="primary" %}}  

Microsoft Excelでは、印刷またはPDF形式への保存時にコメントを印刷する機能が以下のオプションで提供されています  

- なし  
- シートの末尾  
- シートに表示されている通り  

Aspose.Cellsは、同じ機能をサポートする[**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype)列挙型を提供します。[**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype)列挙型には以下のメンバーがあります  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **PDFへ保存する際にコメントを印刷する**  

次のサンプルコードは、コメントを印刷してPDFに保存する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook from the source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleWorkbookWithComments.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

/*
* For print no comments use "PrintCommentsType.PrintNoComments"
* and for print the comments as displayed on sheet use "PrintCommentsType.PrintInPlace"
* For Print the comments at the end of sheet we use "PrintCommentsType.PrintSheetEnd"
*/
worksheet.getPageSetup().setPrintComments(AsposeCells.PrintCommentsType.PrintSheetEnd);

// Save workbook in pdf format
workbook.save(path.join(dataDir, "PrintCommentWhileSavingToPdf_out.pdf"));
```  

