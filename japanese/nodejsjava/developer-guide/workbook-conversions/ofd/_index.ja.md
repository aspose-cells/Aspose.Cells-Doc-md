---
title: ExcelをOFD形式に変換する
linktitle: ExcelをOFD形式に変換する
description: Aspose.Cells for Node.js via Javaは、ExcelワークブックをOFD（Open Fixed-layout Document）形式に変換することをサポートするスプレッドシートライブラリです。この記事では、Excelコンテンツを作成してOFDとしてエクスポートする方法、およびAspose.Cellsを使用して既存のExcelファイルをOFDに変換する方法について説明します。
keywords: Aspose.Cells, Node.js via Java ライブラリ, スプレッドシート, ExcelからOFD, OFD変換, SaveFormat.Ofd, 固定レイアウトドキュメント, ワークブックエクスポート
type: docs
weight: 195
url: /ja/nodejs-java/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cellsは、`SaveFormat.Ofd`列挙値を使用して、ExcelワークブックをOFD（Open Fixed-layout Document）形式に直接変換することをサポートしています。生成されたOFDドキュメントは、ワークブックの表示レイアウト、内容、結合セル、列幅、行の高さ、フォント、色、罫線、および数値形式を保持します。このため、Aspose.Cellsは、固定レイアウトの出力を必要とするアーカイブ、印刷、規制当局への提出、政府への提出ワークフローに適しています。
{{% /alert %}}

## **Introduction**
OFD（Open Fixed-layout Document）は、固定されたページベースのレイアウトでデジタルドキュメントを表現するための中国の国家標準（GB/T 33190-2016）です。これは、ソースドキュメントの視覚的な外観が作成されたとおりに正確に保持される必要があるユースケースにおいて、PDFと同様の役割を果たします。OFDは、中華人民共和国における政府への提出、規制当局への申請、電子請求書、長期保存に広く採用されています。
ExcelワークブックをOFDに変換することは、スプレッドシートの内容を編集可能なスプレッドシートとしてではなく、読み取り専用のレイアウトロックされた成果物として配布する必要があるシナリオで一般的な要件です。例としては、最終化された請求書を顧客に送付する、四半期財務報告をアーカイブする、予算スプレッドシートを規制当局に提出するなどがあります。Aspose.Cellsは、中間変換ステップを必要とせずにワークブックを直接OFDに書き込む`SaveFormat.Ofd`列挙値によってこの要件に対応しています。OFD出力は、ワークブックに設定されたセルの値、結合範囲、フォント、色、罫線、数値形式、およびページ設定オプションを保持します。

{{% alert color="primary" %}}
Aspose.Cellsによって生成されたOFD出力は、セルの内容、結合セル、列幅、行の高さなど、ソースワークブックの表示レイアウトを保持します。フォント、色、罫線、配置、数値形式などのセル書式も、固定レイアウト出力でレンダリングされます。用紙サイズ、向き、印刷領域など、ワークシートに設定されたページ設定オプションは、生成されるOFDドキュメントのレイアウトに影響します。

## **Creating an Excel Workbook and Saving as OFD**
Aspose.Cellsを使用すると、プログラムでワークブックを構築し、データを入力してから、`SaveFormat.Ofd`列挙を使用してOFD形式に直接保存できます。次の例では、請求書をゼロから作成します。会社ロゴ、ヘッダー情報、請求先セクション、明細項目、および計算された合計を追加し、ワークブックをOFDドキュメントにエクスポートします。

### **Building an Invoice with a Logo**
この例では、左上領域にロゴ画像を挿入し、会社名と連絡先情報を入力し、結合セルをまたぐ「INVOICE」タイトルを追加し、請求書番号と日付を記録し、請求先クライアントを記載し、説明、数量、単価、合計の各列を含む明細項目テーブルを構築し、セルの数式を使用して小計、税、総合計を計算することで、請求書ワークシートを構築します。太字のヘッダー、価格の通貨形式、罫線、列幅などの書式設定は、`Style`および`Font`オブジェクトを使用して適用されます。最後に、`SaveFormat.Ofd`を使用して`.ofd`拡張子でワークブックを保存します。

```javascript
let dataDir = "C:\\Temp\\";
// Create a new Workbook
let workbook = new AsposeCells.Workbook();
// Obtain the first worksheet
let worksheet = workbook.getWorksheets().get(0);
// Set column widths
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);
// Insert company logo
worksheet.getPictures().add(1, 1, dataDir + "logo.png");
// Company name and contact details
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");
// INVOICE title - merge cells
worksheet.getCells().merge(7, 1, 2, 4);
let titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");
let titleStyle = workbook.createStyle();
titleStyle.getFont().setIsBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);
// Invoice number and date
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new Date().toISOString().slice(0, 10));
// Bill-to section
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");
// Line items header
let headerDesc = worksheet.getCells().get("B19");
let headerQty = worksheet.getCells().get("C19");
let headerPrice = worksheet.getCells().get("D19");
let headerTotal = worksheet.getCells().get("E19");
headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");
let headerStyle = workbook.createStyle();
headerStyle.getFont().setIsBold(true);
headerStyle.getFont().setColor(AsposeCells.Color.getWhite());
headerStyle.setBackgroundColor(AsposeCells.Color.getNavy());
headerStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.CENTER);
headerStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);
// Currency style with borders
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
// Plain border style for description/quantity cells
let borderStyle = workbook.createStyle();
borderStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
// Line items rows
let lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
];
for (let i = 0; i < lineItems.length; i++)
{
    let row = 20 + i;
    let descCell = worksheet.getCells().get(row, 1);
    let qtyCell = worksheet.getCells().get(row, 2);
    let priceCell = worksheet.getCells().get(row, 3);
    let totalCell = worksheet.getCells().get(row, 4);
    descCell.putValue(lineItems[i][0]);
    qtyCell.putValue(lineItems[i][1]);
    priceCell.putValue(lineItems[i][2]);
    totalCell.setFormula("C" + row + "*D" + row);
    descCell.setStyle(borderStyle);
    qtyCell.setStyle(borderStyle);
    priceCell.setStyle(currencyStyle);
    totalCell.setStyle(currencyStyle);
}
// Subtotal, tax, grand total
worksheet.getCells().get("B24").putValue("Subtotal:");
let subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");
worksheet.getCells().get("B25").putValue("Tax (10%):");
let taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");
worksheet.getCells().get("B26").putValue("Grand Total:");
let grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");
// Bold + currency style for total values
let totalStyle = workbook.createStyle();
totalStyle.getFont().setIsBold(true);
totalStyle.setCustom("\"$\"#,##0.00");
subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);
// Bold style for total labels
let boldStyle = workbook.createStyle();
boldStyle.getFont().setIsBold(true);
worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);
// Save the workbook as an OFD file
workbook.save(dataDir + "Invoice.ofd", AsposeCells.SaveFormat.Ofd);
```

## **Converting an Existing Excel File to OFD**
Aspose.Cellsは、ディスクから既存のExcelワークブックをロードし、OFD形式に直接エクスポートすることもできます。これは、バッチ変換パイプライン、アーカイブワークフロー、およびソースワークブックが別のツールで作成され、固定レイアウト成果物として再発行するだけでよいシナリオに役立ちます。次の例では、既存の`.xlsx`ワークブックをロードし、そのセルからデータを読み取り、オプションのページ設定調整を適用し、結果をOFDドキュメントとして保存します。

```javascript
const AsposeCells = require("aspose.cells");
const dataDir = "C:\\Examples\\";
// Open an existing Excel workbook from disk
const workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");
// (1) Read and display values from selected cells to confirm the file was loaded
const firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());
// (2) Iterate over the Worksheets collection to enumerate available sheets
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    const ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}
// (3) Optionally update a timestamp cell to reflect the conversion
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));
// Append a summary header row at the top of the data block
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));
// (4) Configure PageSetup properties on the worksheet
const pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);
// (5) Optionally set the print area for the OFD output
const lastRow = firstSheet.getCells().getMaxDataRow();
const lastCol = firstSheet.getCells().getMaxDataColumn();
const lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
const printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);
// (6) Save the workbook as an OFD file
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
function formatDate(date) {
    const pad = (n) => n.toString().padStart(2, '0');
    return date.getFullYear() + "-" + pad(date.getMonth() + 1) + "-" + pad(date.getDate()) + " " + pad(date.getHours()) + ":" + pad(date.getMinutes()) + ":" + pad(date.getSeconds());
}
```

## **Related Articles**
- [Excelファイルを複数のファイルに分割する](/cells/ja/nodejs-java/splitting-excel-files-into-multiple-files/)
- [セルに画像を挿入する](/cells/ja/nodejs-java/inserting-an-image-into-a-cell/)
- [DBFファイルの読み取りと書き込み](/cells/ja/nodejs-java/dbf/)
{{% /alert %}}

{{< app/cells/assistant language="javascript" >}}