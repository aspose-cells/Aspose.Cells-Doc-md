---
title: Node.jsとC++を用いてシートがダイアログシートかどうかを判定する方法
linktitle: ワークシートがダイアログシートであるかを検索する
type: docs
weight: 90
url: /ja/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/
description: この記事では、Aspose.Cells for Node.js via C++を用いてExcelシートがダイアログシートかどうかをプログラム的に判定する方法とサンプルコードを提供します。
keywords: ExcelシートのダイアログタイプをNode.jsとC++で見つける
---

## **可能な使用シナリオ**

ダイアログシートは古い形式のシートで、ダイアログボックスを含みます。例えば、Microsoft Excelの古いバージョン（例：2003）で挿入されたものです。新しいバージョン（例：Microsoft Excel 2016）でもVBAを使って挿入可能です。

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Aspose.Cells for Node.js via C++が提供する[**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--)プロパティを使用してシートがダイアログシートかどうかを確認できます。これが列挙値[**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype)を返す場合、そのシートはダイアログシートです。

## **ワークシートがダイアログシートであるかを検索する**

次のサンプルコードは、ダイアログシートを含むサンプルExcelファイル（64716820.xlsx）を読み込み、[**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--)プロパティを確認し、それを[**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype)と比較してメッセージを出力します。詳細は以下のコンソール出力を参照してください。

## **サンプルコード**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFindIfWorksheetIsDialogSheet.xlsx");

// Load Excel file containing Dialog Sheet
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Find if the sheet type is dialog and print the message
if (ws.getType() === AsposeCells.SheetType.Dialog) {
console.log("Worksheet is a Dialog Sheet.");
}
```

## **コンソール出力**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
