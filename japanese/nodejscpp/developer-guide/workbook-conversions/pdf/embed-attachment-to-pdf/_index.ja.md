---  
title: ノード.js経由でC++を使用してPDFに添付ファイルを埋め込む  
linktitle: PDFに添付を埋め込む  
type: docs  
weight: 380  
url: /ja/nodejs-cpp/embed-attachment-to-pdf/  
description: Aspose.Cells for Node.js via C++を使用してOleオブジェクトを添付としてPDFに埋め込む方法を学びます。  
---  

Excelでは、ソースデータを持つOleオブジェクトを挿入できます（[embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)）。Oleオブジェクトをダブルクリックすると、埋め込まれたファイルが開きます。

一般的に、PDFに変換する際、Oleオブジェクトはアイコンまたはサムネイルとして表示され、Oleオブジェクトのソースデータは表示されません。[PdfSaveOptions.getEmbedAttachments()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getEmbedAttachments--) オプションを使用すると、Oleオブジェクトのソースデータを添付ファイルとしてPDFに埋め込むことができます。PDFのアイコンやサムネイルをダブルクリックしてOleオブジェクトのソースファイルを開くことができます。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "embedded-attachments-example.xlsx");

// Open the template file
const wb = new AsposeCells.Workbook(filePath);

// Set to embed Ole Object attachment.
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setEmbedAttachments(true);

// Save the pdf file with PdfSaveOptions
wb.save("output.pdf", pdfSaveOptions);
```

![embedded-attachment.png](embedded-attachment.png)  

