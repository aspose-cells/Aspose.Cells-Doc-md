---
title: Excel、OpenOffice、Json、Csv、Htmlファイルの読み込みと管理
linktitle: ファイルを開く
type: docs
weight: 20
url: /ja/nodejs-cpp/loading-saving-and-managing/
description: Aspose.Cellsを使えば、Node.jsを通じてC++経由でExcel、CSV、TSV、ODS、HTML、Numbers、Json、XML、Pdf、Jpg、Tiff、画像、Mht、XPSファイルを簡単に作成、開く、管理できます。
---

{{% alert color="primary" %}}

Aspose.Cellsを使えば、Excelファイルを作成、開き、データの取得やデザイナーテンプレートを使った開発速度向上などが容易に行えます。

{{% /alert %}}

## **新しいワークブックの作成**
次の例は、ゼロから新しいワークブックを作成します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const licensePath = path.join(dataDir, "Aspose.Cells.lic");

try {
// Create a License object
const license = new AsposeCells.License();

// Set the license of Aspose.Cells to avoid the evaluation limitations
license.setLicense(licensePath);
} catch (ex) {
console.log(ex.message);
}

// Instantiate a Workbook object that represents Excel file.
const wb = new AsposeCells.Workbook();

// When you create a new workbook, a default "Sheet1" is added to the workbook.
const sheet = wb.getWorksheets().get(0);

// Access the "A1" cell in the sheet.
const cell = sheet.getCells().get("A1");

// Input the "Hello World!" text into the "A1" cell
cell.putValue("Hello World!");

// Save the Excel file.
wb.save(path.join(dataDir, "MyBook_out.xlsx"));
```

## **ファイルを開くと保存する**
Aspose.Cellsを使えば、Excelファイルを開き、保存し、管理するのは簡単です。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Adding new sheet
const sheet = workbook1.getWorksheets().add("MySheet");
// Setting active sheet
workbook1.getWorksheets().setActiveSheetIndex(1);
// Setting values.
const cells = sheet.getCells();
// Setting text
cells.get("A1").putValue("Hello!");
// Setting number
cells.get("A2").putValue(1000);
// Setting Date Time
const cell = cells.get("A3");
cell.putValue(new Date());
const style = cell.getStyle();
style.setNumber(14);
cell.setStyle(style);
// Setting formula
cells.get("A4").setFormula("=SUM(A1:A3)");
// Saving the workbook to disk.
workbook1.save(path.join(dataDir, "dest.xlsx"));
```

## **上級トピック**
- [ファイルを開く異なる方法](/cells/ja/nodejs-cpp/different-ways-to-open-files/)
- [ワークブックを読み込む際に定義名をフィルタリングする](/cells/ja/nodejs-cpp/filter-defined-names-while-loading-workbook/)
- [ワークブックまたはワークシートをロードする際にオブジェクトをフィルタする](/cells/ja/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [テンプレートファイルからワークブックをロードする際にデータの種類をフィルタする](/cells/ja/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Excelファイルの読み込み中に警告を受け取る](/cells/ja/nodejs-cpp/get-warnings-while-loading-excel-file/)
- [チャートを含まないソースExcelファイルをロードする](/cells/ja/nodejs-cpp/load-source-excel-file-without-charts/)
- [ワークブック内の特定のワークシートをロードする](/cells/ja/nodejs-cpp/load-specific-worksheets-in-a-workbook/)
- [指定されたプリンタ用紙サイズでワークブックを読み込む](/cells/ja/nodejs-cpp/load-workbook-with-specified-printer-paper-size/)
- [異なるMicrosoft Excelバージョンのファイルを開く](/cells/ja/nodejs-cpp/opening-different-microsoft-excel-versions-files/)
- [異なるフォーマットのファイルを開く](/cells/ja/nodejs-cpp/opening-files-with-different-formats/)
- [大規模なデータセットを持つ大きなファイルで作業する際のメモリ使用量を最適化する](/cells/ja/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Aspose.Cellsを使用してApple Inc.が開発したNumbersスプレッドシートを読む](/cells/ja/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [時間がかかりすぎる場合はInterruptMonitorを使用して変換または読み込みを停止してください](/cells/ja/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [LightCells APIの使用](/cells/ja/nodejs-cpp/using-lightcells-api/)
- [CSVをJSONに変換](/cells/ja/nodejs-cpp/convert-csv-to-json/)
- [ExcelをJSONに変換](/cells/ja/nodejs-cpp/convert-excel-to-json/)
- [JSONをCSVに変換](/cells/ja/nodejs-cpp/convert-json-to-csv/)
- [JSONをExcelに変換](/cells/ja/nodejs-cpp/convert-json-to-excel/)
- [ExcelをHtmlに変換](/cells/ja/nodejs-cpp/convert-excel-to-html/)
{{< app/cells/assistant language="nodejs-cpp" >}}
