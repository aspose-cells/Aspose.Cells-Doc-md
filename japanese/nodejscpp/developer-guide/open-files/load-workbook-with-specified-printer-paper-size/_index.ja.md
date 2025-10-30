---  
title: 特定のプリンタ用紙サイズでワークブックを読み込む：Node.jsとC++  
linktitle: 指定したプリンター用紙サイズでワークブックをロード  
type: docs  
weight: 430  
url: /ja/nodejs-cpp/load-workbook-with-specified-printer-paper-size/  
description: Aspose.Cells for Node.js via C++を使用して、ワークブックを読み込む際のプリンタ用紙サイズを設定する方法を学びます。  
---  

{{% alert color="primary" %}}  
[**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-)メソッドを使用してワークブックをロードする際に、希望のプリンター用紙サイズを指定できます。新しいファイルをMS Excelで作成した場合、プリンターの設定と同じ用紙サイズになりますのでご注意ください。  
{{% /alert %}}  

以下のサンプルコードは、[**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-)メソッドの使用例です。最初にワークブックを作成し、次にメモリストリームにXLSX形式で保存します。その後、A5用紙サイズで読み込み、PDF形式で保存します。次に、A3用紙サイズで再度読み込み、再度PDFで保存します。出力されたPDFを開き、その用紙サイズを確認すると、違いがわかります。コードによって生成された[A5出力PDF](5115234.pdf)と[A3出力PDF](5115233.pdf)をダウンロードしてご参考ください。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a sample workbook and add some data inside the first worksheet
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("P30").putValue("This is sample data.");

// Save the workbook in memory stream
const ms = workbook.saveToStream();

// Now load the workbook from memory stream with A5 paper size
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
opts.setPaperSize(AsposeCells.PaperSizeType.PaperA5);
let workbookA5 = new AsposeCells.Workbook(ms, opts);

// Save the workbook in pdf format
workbookA5.save(path.join(dataDir, "LoadWorkbookWithPrinterSize-a5_out.pdf"));

// Now load the workbook again from memory stream with A3 paper size
ms.position = 0;
opts.setPaperSize(AsposeCells.PaperSizeType.PaperA3);
let workbookA3 = new AsposeCells.Workbook(ms, opts);

// Save the workbook in pdf format
workbookA3.save(path.join(dataDir, "LoadWorkbookWithPrinterSize-a3_out.pdf"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
