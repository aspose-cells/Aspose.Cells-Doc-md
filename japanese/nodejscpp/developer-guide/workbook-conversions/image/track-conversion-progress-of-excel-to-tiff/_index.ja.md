---
title: Node.jsとC++を使用してExcelからTIFFへの変換進行状況を追跡
linktitle: ExcelからTIFFへの変換の進行状況を追跡
type: docs
weight: 190
url: /ja/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/
description: Aspose.Cells for Node.js via C++を使用してExcelファイルのTIFFへの変換進捗を追跡する方法を学び、変換プロセス中のユーザーエクスペリエンスを向上させます。
---

## **可能な使用シナリオ**

大きなExcelファイルの変換には時間がかかる場合があります。この間、アプリケーションの使いやすさを向上させるために、単なる読み込み画面ではなく、ドキュメントの変換進行状況を表示したいことがあります。Aspose.Cells for Node.js via C++は、[**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback)インターフェースを提供して、ドキュメント変換の進行状況を追跡します。[**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback)インターフェースは、[**pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-)や[**pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-)メソッドを提供し、カスタムクラスに実装可能です。ページがどのようにレンダリングされるかも制御できます（*TestPageSavingCallback*カスタムクラスの例参照）。

## **ExcelからTIFFへの変換の進行状況を追跡**

次のコード例は、[ソースExcelファイル](95584311.xlsx)をロードし、*TestPageSavingCallback*カスタムクラスを使用してその変換進行状況をコンソールに出力し、生成された出力ファイルを参照のために添付します。

[Output File](95584312.tiff)

## **サンプルコード**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const opts = new AsposeCells.ImageOrPrintOptions();

// Define TestTiffPageSavingCallback
class TestTiffPageSavingCallback {
// Implement required methods for the callback here
}

opts.setPageSavingCallback(new TestTiffPageSavingCallback());
opts.setImageType(AsposeCells.ImageType.Tiff);

const wr = new AsposeCells.WorkbookRender(workbook, opts);
wr.toImage(path.join(outputDir, "DocumentConversionProgressForTiff_out.tiff"));
```

以下は、*TestTiffPageSavingCallback*カスタムクラスのコードです。

```javascript
const AsposeCells = require("aspose.cells.node");

class TestTiffPageSavingCallback {
pageStartSaving(args) {
console.log(`Start saving page index ${args.pageIndex} of pages ${args.pageCount}`);

// Don't output pages before page index 2.
if (args.pageIndex < 2) {
args.setIsToOutput(false);
}
}

pageEndSaving(args) {
console.log(`End saving page index ${args.pageIndex} of pages ${args.pageCount}`);

// Don't output pages after page index 8.
if (args.pageIndex >= 8) {
args.setHasMorePages(false);
}
}
}
```

## **コンソール出力**

{{< highlight java >}}

Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10</br>

{{< /highlight >}}
