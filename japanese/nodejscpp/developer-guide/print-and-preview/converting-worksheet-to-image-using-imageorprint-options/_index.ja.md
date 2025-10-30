---  
title: Node.jsを使用してC++経由でImageOrPrint Optionsを使ったワークシートの画像変換  
linktitle: ImageOrPrintオプションを使用してワークシートを画像に変換する  
type: docs  
weight: 90  
url: /ja/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/  
description: Aspose.Cells for Node.js via C++を使ってワークシートを画像ファイルに変換し、さまざまな画像および印刷オプションを適用する方法を学びます。   
---  

{{% alert color="primary" %}}  
このドキュメントは、ワークシートを画像ファイルに変換し、画像と印刷オプションを適用し、解像度、TIFF圧縮、画像形式、ページ品質などのオプションを適用する方法について詳しく説明します。  
{{% /alert %}}  

## **ワークシートをイメージとして保存する - 異なるアプローチ**  

時々、ワークシートを図解的に表示する必要があります。ワークシートの画像をアプリケーションやWebページに挿入する必要があります。画像をWord文書、PDFファイル、PowerPointプレゼンテーションに挿入したり、他のシナリオで使用する必要があります。別の場所で使用するためにワークシートを画像としてレンダリングしたいと思うだけです。Aspose.CellsはExcelファイルのワークシートを画像に変換することをサポートしています。また、Aspose.Cellsは画像形式、解像度（縦と横の両方）、画像品質、およびその他の画像および印刷オプションを設定することをサポートしています。  

Office Automationを試すかもしれませんが、Office Automationには欠点もあります。その理由や問題点はいくつかあります：たとえば、セキュリティ、安定性、スケーラビリティと速度、価格、機能などです。要するに、多くの理由がありますが、その中でも最も重要なのは、Microsoft自身がソフトウェアソリューションからのOffice Automationを強く推奨していない点です。  

この記事は、Aspose.Cells APIを使用して、C#コンソールアプリケーションを作成し、わずかなコード行でさまざまなイメージと印刷オプションを使用してワークシートをイメージに変換する方法を示しています。  

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/)クラスはワークシートの画像レンダリング用のワークシートを表し、オーバーロードされた[**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)メソッドを持ち、これを直接使ってワークシートを画像ファイルに変換し、希望の属性やオプションを指定できます。画像ファイルをディスクまたはストリームに保存できるオブジェクトを返します。サポートされる画像形式にはBMP、PNG、GIF、JPEG、TIFF、EMFなどがあります。  

## **ImageOrPrintオプションを使用して、Aspose.Cellsを使用してワークシートをイメージに変換する。**  

### **Microsoft Excelでテンプレートワークブックを作成する**  

私はMS Excelで新しいワークブックを作成し、最初のワークシートにいくつかのデータを追加しました。これで、テンプレートファイルのワークシート **Sheet1** を画像ファイル **SheetImage.tiff** に変換し、水平および垂直解像度、TiffCompressionなどの異なるイメージオプションを適用します。  

### **Aspose.Cellsをダウンロードしてインストールする**  

まず、[ダウンロード](https://downloads.aspose.com/cells/nodejs-cpp)Aspose.Cells for Node.js via C++を行い、開発用コンピューターにインストールしてください。すべての[Aspose](http://www.aspose.com/)コンポーネントは、インストール時に評価モードで動作します。評価モードは時間制限がなく、生成されるドキュメントに透かしが入るだけです。  

### **プロジェクトを作成する**  

お好みの開発環境（例：Visual Studio）を起動します。新しいコンソールアプリケーションを作成します。  

### **参照の追加**  

このプロジェクトではAspose.Cellsを使用します。したがって、プロジェクトにAspose.Cellsコンポーネントへの参照を追加する必要があります。例：…\.\Program Files\Aspose\Aspose.Cells for Node.js via C++\Bin\Aspose.Cells.nodeへの参照を追加します。  

### **ワークシートを画像ファイルに変換**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Open template
const filePath = path.join(sourceDir, "sampleWorksheetToAnImage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Apply different Image and Print options
const options = new AsposeCells.ImageOrPrintOptions(); // Corrected: Added the instantiation for ImageOrPrintOptions.

// Set Horizontal Resolution
options.setHorizontalResolution(300);

// Set Vertical Resolution
options.setVerticalResolution(300);

// Set TiffCompression
options.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

// Set Image Format
options.setImageType(AsposeCells.ImageType.Tiff);

// Set printing page type
options.setPrintingPage(AsposeCells.PrintingPageType.Default);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, options);

// Render/save the image for the sheet
const pageIndex = 3;
sr.toImage(pageIndex, path.join(outputDir, `outputWorksheetToAnImage_${pageIndex + 1}.tiff`));
```  

## **変換オプション**  

特定のページを画像に保存することが可能です。次のコードは、ワークブック内の最初と2番目のワークシートをJPG画像に変換します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleSpecificPagesToImages.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Specify page index to be rendered
const idxPage = 3;

// Render the third image for the sheet
const bitmap = sr.toImage(idxPage);

// Save the image file
const fs = require("fs");
fs.writeFileSync(path.join(outputDir, `outputSpecificPagesToImage_${idxPage + 1}.jpg`), bitmap);
```  

## **WorkbookRenderを使用した画像変換**  

TIFF画像は複数のフレームを含むことができます。ワークブック全体を複数のフレームまたはページを持つ単一のTIFF画像に保存できます。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Tiff);

const workbookRender = new AsposeCells.WorkbookRender(workbook, opts);
workbookRender.toImage(path.join(outputDir, "outputUseWorkbookRenderForImageConversion.tiff"));
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
