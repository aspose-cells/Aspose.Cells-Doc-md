---
title: シートを画像に変換  C++経由のNode.jsを使用してデータ周辺の空白を除去
linktitle: ワークシートを画像に変換  データ周りの余白を削除する
type: docs
weight: 40
url: /ja/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Microsoft Excelのワークシートを画像に変換し、データ周辺の空白を除去する方法についてAspose.Cells for Node.js via C++で解説します。 
---

{{% alert color="primary" %}}

時には、ワークシートの画像をアプリケーションやWebページで表示する必要があります。たとえば、画像をWord文書、PDFファイル、PowerPointプレゼンテーション、あるいは他のドキュメントに挿入する必要があるかもしれません。基本的に、ワークシートを画像としてレンダリングして、他のアプリケーションに貼り付けられるようにしたいと思うでしょう。Aspose.Cellsを使用すると、Microsoft Excelのワークシートを画像に変換することができます。

{{% /alert %}}

## **データ周りの余白を削除してください**

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender)APIは、ワークシートを指定された属性（たとえば、画像形式、ページ化されたシートなど）で画像ファイルに変換します。いくつかの画像形式がサポートされており、BMP、GIF、JPG、TIFF、EMFなどが含まれています。

シートを画像化する際、出力画像にはデフォルトで余白（ボーダー）があります。これを削除するには、元のワークシートの上部、下部、左側、右側のページ設定のマージンを0に設定し、それに応じて[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions)属性を指定してください。

次のコードスニペットは、出力画像のデータ周りの余白を削除します。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
const options = new AsposeCells.LoadOptions();
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All));
// Specify your print area if you want
// sheet.getPageSetup().setPrintArea("A1:H8");

// To remove the white border around the image.
sheet.getPageSetup().setLeftMargin(0);
sheet.getPageSetup().setRightMargin(0);
sheet.getPageSetup().setBottomMargin(0);
sheet.getPageSetup().setTopMargin(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Emf);

// Set only one page would be rendered for the image
imgOptions.setOnePagePerSheet(true);
imgOptions.setPrintingPage(AsposeCells.PrintingPageType.IgnoreBlank);

// Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Convert the image
sr.toImage(0, path.join(outputDir, "outputRemoveWhitespaceAroundData.emf"));
```
