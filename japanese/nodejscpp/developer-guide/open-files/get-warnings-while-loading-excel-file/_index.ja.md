---
title: Node.jsとC++を利用したExcelファイル読み込み時の警告取得方法
linktitle: Excelファイルの読み込み時に警告を取得する
type: docs
weight: 110
url: /ja/nodejs-cpp/get-warnings-while-loading-excel-file/
description: Aspose.Cells for Node.js via C++を使用してExcelファイルを読み込む際に警告をキャプチャする方法について学びます。破損しているが読み込み可能なワークブックを効果的に処理します。
---

## **可能な使用シナリオ**

時には、ある程度破損しているが読み込めるワークブックを読み込もうとするユーザーもいます。そのような場合、Aspose.Cellsは読み込み時に警告をスローします。これらの警告は、[**IWarningCallback**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback)インターフェースを実装し、[**LoadOptions.getWarningCallback()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getWarningCallback--)プロパティを設定することでキャッチできます。

## **Excelファイルの読み込み中に警告を受け取る**

以下のサンプルコードは、読み込み時に警告を取得する例です。サンプルExcelファイル（sampleDuplicateDefinedName.xlsx）を読み込むと、[**DuplicateDefinedName**](https://reference.aspose.com/cells/nodejs-cpp/warningtype)警告がスローされます。この警告は、[**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback/#warning-warninginfo-)メソッドによって捕捉され、警告メッセージがコンソールに出力されます。その後、ワークブックは[出力Excelファイル](outputDuplicateDefinedName.xlsx)として保存されます。Microsoft Excelでファイルを開くと、スクリーンショットのようにこの警告も表示されます。

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **サンプルコード**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Implement IWarningCallback interface to catch warnings while loading workbook
class WarningCallback extends AsposeCells.IWarningCallback {
    warning(warningInfo) {
        if (warningInfo.getType() === AsposeCells.WarningType.DuplicateDefinedName) {
            console.log("Duplicate Defined Name Warning: " + warningInfo.getDescription());
        }
    }
}

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create load options and set the WarningCallback property 
// to catch warnings while loading workbook
const options = new AsposeCells.LoadOptions();
options.setWarningCallback(new WarningCallback());

// Load the source excel file
const book = new AsposeCells.Workbook(path.join(dataDir, "sampleDuplicateDefinedName.xlsx"), options);

// Save the workbook 
book.save(path.join(dataDir, "outputDuplicateDefinedName.xlsx"));
```

## **コンソール出力**

提供された[サンプルエクセルファイル](sampleDuplicateDefinedName.xlsx)を使用して上記のコードを実行した際のコンソール出力は次のとおりです。

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
