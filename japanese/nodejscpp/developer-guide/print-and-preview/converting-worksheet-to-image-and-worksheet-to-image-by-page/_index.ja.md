---  
title: ページごとにワークシートを画像に変換・ワークシートをページ単位の画像に変換（Node.js+C++経由）  
linktitle: ワークシートを画像に変換し、ページごとにワークシートを画像に変換  
type: docs  
weight: 80  
url: /ja/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/  
---  

{{% alert color="primary" %}}  
このドキュメントは、開発者に対し、ワークシートを画像ファイルに変換し、複数ページのワークシートをページごとに画像化する方法について詳しく解説します。  

時には、アプリケーションやWebページでワークシートを画像として表示する必要があります。たとえば、その画像をWord文書、PDFファイル、PowerPointプレゼンテーションに挿入したり、他のシナリオで使用する必要があるかもしれません。単純に言えば、ワークシートを画像としてレンダリングしたいと思います。Aspose.Cellsは、Microsoft Excelファイルのワークシートを画像に変換することをサポートしています。また、Aspose.Cellsは、ワークブックを複数のページごとに1つの画像ファイルに変換することもサポートしています。  

これを達成するためには、Office Automationを使用することができますが、Office Automationには独自の欠点があります。セキュリティ、安定性、拡張性/処理速度、価格、機能など、いくつかの理由や問題があります。簡単に言えば、多くの理由がありますが、その中でも主な理由の1つは、Microsoft自体がOffice Automationを強く推奨していないことです。  
{{% /alert %}}  

## **Aspose.Cells for Node.js via C++を使用してワークシートを画像ファイルに変換**  

この解説では、シンプルなコード行数でAspose.Cells APIを使用して、コンソールアプリケーションを作成し、ワークシートを画像に変換し、各ワークシートを一つの画像に変換する方法を示します。  

レンダリング機能に関連するいくつかの重要なクラスをプログラムまたはプロジェクトにインポートする必要があります。例えば、[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/)、[**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender/)などです。[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/)クラスは、ワークシートを画像にレンダリングするためのクラスで、オーバーロードされた[**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)メソッドを持ち、属性やオプションを設定してワークシートを直接画像ファイルに変換できます。これにより画像オブジェクトが返され、画像ファイルをディスクまたはストリームに保存可能です。対応フォーマットにはBMP、PNG、GIF、JPG、JPEG、TIFF、EMFなどがあります。  

この記事では以下の方法について説明します:  

- ワークシートを画像に変換する  
- ワークシートの各ページを画像に変換する  

このタスクでは、Aspose.Cellsを使用して、テンプレートワークブックからワークシートを画像ファイルに変換する方法を示します。  

### **プロジェクトのセットアップ**  

1. まず、[Aspose.Cells for Node.js via C++をダウンロード](https://downloads.aspose.com/cells/nodejs-cpp)。  
1. 開発用コンピューターにインストールします。すべての[Aspose](http://www.aspose.com/)コンポーネントは、インストール時に評価モードで動作します。評価モードは時間制限がなく、生成されるドキュメントにウォーターマークを挿入するだけです。開発環境を起動し、新しいコンソールアプリケーションを作成します。本例はNode.jsのコンソールアプリケーションですが、Node.jsと連携可能な任意のセットアップでも構いません。作成したプロジェクトにAspose.Cellsを参照として追加します。  

### **ワークシートを画像ファイルに変換**  

Microsoft Excelで新しいワークブックを作成し、最初のワークシートにいくつかのデータを追加しました：**Testbook.xlsx**（1つのワークシート）。次に、テンプレートファイルのワークシートSheet1をSheetImage.jpgという画像ファイルに変換します。  

コンポーネントがタスクを達成するために使用したコードは以下の通りです。**Testbook.xlsx**のSheet1を画像ファイルに変換し、この変換がどれほど簡単であるかを説明します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleConvertWorksheettoImageFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setOnePagePerSheet(true);

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the image file
const outputFilePath = outputDir + "outputConvertWorksheettoImageFile.jpg";

sr.toImage(0, outputFilePath);
```  

## **Aspose.Cells for Node.js via C++を使用したページ単位のワークシートの画像変換**  

この例では、Aspose.Cellsを使用して、複数のページを持つテンプレートワークブックからワークシートを1つの画像ファイルに変換する方法を示します。  

### **ページ単位でシートを画像に変換**  

私はMicrosoft Excelで新しいワークブックを作成し、最初のワークシートにいくつかのデータを追加しました: **Testbook2.xlsx** (1 ワークシート)。  

これで、テンプレートファイルのワークシート Sheet1 を画像ファイルに変換します（1ページごとのファイル）。すでにコンソールアプリケーションを作成してコピー作業を行う準備ができているため、コンソールアプリケーションの作成手順をスキップして、直接ワークシートの変換手順に移ります。  

以下は、そのタスクを実現するためにコンポーネントが使用するコードです。Testbook2.xlsxのSheet1をページごとに画像ファイルに変換します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleConvertWorksheetToImageByPage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(200);
options.setVerticalResolution(200);
options.setImageType(AsposeCells.ImageType.Tiff);

// Sheet2Image By Page conversion
const sr = new AsposeCells.SheetRender(sheet, options);
for (let j = 0; j < sr.getPageCount(); j++) 
{
sr.toImage(j, outputDir + "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif");
}
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
