---
title: OpenXmlのSheet.SheetIdプロパティをAspose.Cells for Node.js via C++を用いて利用する
linktitle: Aspose.Cellsを使用したOpenXmlのSheet.SheetIdプロパティを利用する
type: docs
weight: 200
url: /ja/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: この記事では、Excel操作のAspose.Cells for Node.js via C++を使用してOpenXmlのSheet.SheetIdプロパティをプログラム的に利用する方法を示します。
keywords: openxmlノード.jsのシートIDプロパティ（C++経由）、C++のノード.jsのシートID Excelワークシート
---

## **可能な使用シナリオ**

*Sheet.SheetId*プロパティは*DocumentFormat.OpenXml.Spreadsheet*モジュール内で利用可能で、OpenXmlの一部です。このプロパティとその値は、以下のスクリーンショットのように*workbook.xml*内で確認できます。Aspose.Cellsは、これと同等のプロパティを[**Worksheet.getTabId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTabId--)として提供します。

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **OpenXmlのSheet.SheetIdプロパティをAspose.Cells for Node.js via C++を使用して利用する**

次のサンプルコードは、[サンプルExcelファイル](51740716.xlsx)をロードし、そのシートまたはタブIDを読み取り、それに新しいタブIDを割り当てて[出力Excelファイル](51740717.xlsx)として保存します。以下に示すコードのコンソール出力も参照してください。

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSheetId.xlsx");

// Load source Excel file
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Print its Sheet or Tab Id on console
console.log("Sheet or Tab Id: " + ws.getTabId());

// Change Sheet or Tab Id
ws.setTabId(358);

// Save the workbook
wb.save("outputSheetId.xlsx");
```

## **コンソール出力**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
