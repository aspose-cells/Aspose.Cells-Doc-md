---  
title: Node.jsとC++を使用したドキュメント変換の進行状況の追跡  
linktitle: ドキュメント変換の進行状況を追跡  
type: docs  
weight: 970  
url: /ja/nodejs-cpp/track-document-conversion-progress/  
description: Aspose.Cells for Node.js via C++を使用してExcelファイルの変換進行状況を追跡する方法を学びます。  
---  

## **可能な使用シナリオ**  

大きなExcelファイルの変換には時間がかかる場合があります。この間、アプリケーションの使いやすさを向上させるために、単なる読み込み画面ではなく、ドキュメントの変換進行状況を表示したいことがあります。Aspose.Cells for Node.js via C++は、[**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback)インターフェースを提供して、ドキュメント変換の進行状況を追跡します。[**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback)インターフェースは、[**IPageSavingCallback.pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-)や[**IPageSavingCallback.pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-)メソッドを提供し、カスタムクラスに実装可能です。ページがどのようにレンダリングされるかも制御できます（*TestPageSavingCallback*カスタムクラスの例参照）。  

## **文書変換の進行状況を追跡する**  

次のコード例は、[ソースExcelファイル](94896151.xlsx)を読み込み、[**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback)インターフェースを実装した*TestPageSavingCallback*カスタムクラスを使用して、その変換進行状況をコンソールに表示するものです。  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Define TestPageSavingCallback class
class TestPageSavingCallback {
// Implement the required methods of this callback as needed
onPageSaving(pageIndex, fileName) {
console.log(`Saving page ${pageIndex} to ${fileName}`);
}
}

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "PagesBook1.xlsx"));

const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setPageSavingCallback(new TestPageSavingCallback());

workbook.save(path.join(outputDir, "DocumentConversionProgress.pdf"), pdfSaveOptions);
```  

以下は、*TestPageSavingCallback*カスタムクラスのコードです。  

```javascript
const AsposeCells = require("aspose.cells.node");

class TestPageSavingCallback {
pageStartSaving(args) {
console.log(`Start saving page index ${args.getPageIndex()} of pages ${args.getPageCount()}`);

// don't output pages before page index 2.
if (args.getPageIndex() < 2) {
args.setIsToOutput(false);
}
}

pageEndSaving(args) {
console.log(`End saving page index ${args.getPageIndex()} of pages ${args.getPageCount()}`);

// don't output pages after page index 8.
if (args.getPageIndex() >= 8) {
args.setHasMorePages(false);
}
}
}
```  

## **コンソール出力**  

{{< highlight java >}}  

Start saving page index 0 of pages 11</br>  
End saving page index 0 of pages 11</br>  
Start saving page index 1 of pages 11</br>  
End saving page index 1 of pages 11</br>  
Start saving page index 2 of pages 11</br>  
End saving page index 2 of pages 11</br>  
Start saving page index 3 of pages 11</br>  
End saving page index 3 of pages 11</br>  
Start saving page index 4 of pages 11</br>  
End saving page index 4 of pages 11</br>  
Start saving page index 5 of pages 11</br>  
End saving page index 5 of pages 11</br>  
Start saving page index 6 of pages 11</br>  
End saving page index 6 of pages 11</br>  
Start saving page index 7 of pages 11</br>  
End saving page index 7 of pages 11</br>  
Start saving page index 8 of pages 11</br>  
End saving page index 8 of pages 11  

{{< /highlight >}}  

