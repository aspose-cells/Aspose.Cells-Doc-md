---  
title: レンダリングのための行の自動調整（Node.js経由C++）  
linktitle: 描画用に行を自動調整する  
type: docs  
weight: 130  
url: /ja/nodejs-cpp/autofit-rows-for-rendering/  
description: Aspose.Cells for Node.js via C++を使ったExcelレンダリング用の行の自動調整方法について学習します。保存したPDFファイルでのテキストのクリッピングを防止します。  
---  

一般に、セル内のすべてのテキストを表示したい場合、Microsoft Excelの通常ビューで100%ズームを設定して行を自動調整できます。これにより、通常ビューでテキストが完全に見えるようになり、印刷やPDFとして保存した場合も正しく表示されます。

しかし、一部の場合には、行の自動調整は通常表示では問題なく動作しますが、印刷ビューに切り替えたりファイルをPDFとして保存すると、テキストがクリッピングされることがあります。ソースファイル [Book1.xlsx](Book1.xlsx) とスクリーンショットを確認してください。

![印刷ビューでテキストが切り取られた場合](text_clipped_in_printview.png)

保存したPDFでテキストのクリッピングを防ぐには、[AutoFitterOptions.getForRendering()](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getForRendering--) オプションを使用して行の自動調整を行うことができます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Init workbook instance.
const workbook = new AsposeCells.Workbook(filePath);

// Set autofit options for rendering.
const autoFitterOptions = new AsposeCells.AutoFitterOptions();
autoFitterOptions.setForRendering(true);

// Autofit rows with options.
workbook.getWorksheets().get(0).autoFitRows(autoFitterOptions);

// Save to pdf.
workbook.save("output.pdf", AsposeCells.SaveFormat.Pdf);
```

今、テキストは出力された PDF ファイルで切り取られていません。

![保存した PDF でテキストが切り取られていない場合](text_not_clipped_in_saved_pdf.png)  
