---
title: Excel を OFD 形式に変換する
linktitle: Excel を OFD 形式に変換する
description: Aspose.Cells for Node.js via Java は、Excel ワークブックを OFD（Open Fixed-layout Document）形式に変換することをサポートするスプレッドシートライブラリです。この記事では、Excel コンテンツを作成して OFD としてエクスポートする方法、および Aspose.Cells を使用して既存の Excel ファイルを OFD に変換する方法について説明します。
keywords: Aspose.Cells, Node.js via Java ライブラリ, スプレッドシート, Excel から OFD, OFD 変換, SaveFormat.Ofd, 固定レイアウトドキュメント, ワークブックのエクスポート
type: docs
weight: 195
url: /ja/nodejs-java/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、`SaveFormat.Ofd` 列挙値を使用して、Excel ワークブックを OFD（Open Fixed-layout Document）形式に直接変換することをサポートしています。生成される OFD ドキュメントは、ワークブックの表示レイアウト、コンテンツ、結合セル、列幅、行高、フォント、色、罫線、および数値形式を保持します。これにより Aspose.Cells は、アーカイブ、印刷、規制当局への提出、政府提出ワークフローなど、固定レイアウトの出力が必要な用途に適しています。

{{% /alert %}}
## **はじめに**
OFD（Open Fixed-layout Document）は、固定されたページベースのレイアウトでデジタルドキュメントを表現するための中国国家標準（GB/T 33190-2016）です。これは、ソースドキュメントの視覚的な外観が作成時とまったく同様に保持されなければならないユースケースにおいて、PDF と同様の役割を果たします。OFD は、中華人民共和国における政府提出書類、規制当局への届出、電子請求書、長期アーカイブで広く採用されています。

Excel ワークブックを OFD に変換することは、スプレッドシートのコンテンツを編集可能なスプレッドシートとしてではなく、読み取り専用でレイアウトが固定された成果物として配布する必要があるシナリオで一般的に求められる要件です。例としては、最終化された請求書を顧客に送付する、四半期財務報告をアーカイブする、規制当局に予算スプレッドシートを提出する、といったものがあります。Aspose.Cells はこの要件に `SaveFormat.Ofd` 列挙値で対応しており、中間変換ステップを必要とせずにワークブックを直接 OFD に書き込みます。OFD 出力は、ワークブックに設定されたセルの値、結合範囲、フォント、色、罫線、数値形式、およびページ設定オプションを保持します。

{{% alert color="primary" %}}

Aspose.Cells によって生成される OFD 出力は、ソースワークブックの表示レイアウトを保持します。これには、セルのコンテンツ、結合セル、列幅、および行高が含まれます。フォント、色、罫線、配置、数値形式などのセル書式設定も、固定レイアウトの出力に反映されます。ワークシートに設定された用紙サイズ、向き、印刷領域などのページ設定オプションは、生成される OFD ドキュメントのレイアウトに影響します。

{{% /alert %}}
## **Excel ワークブックを作成して OFD として保存する**
Aspose.Cells を使用すると、ワークブックをプログラムで構築し、データを入力してから、`SaveFormat.Ofd` 列挙値を使用して直接 OFD 形式に保存できます。次の例では、請求書をゼロから作成します。会社のロゴ、ヘッダー情報、請求先セクション、明細項目、および計算された合計を追加し、その後ワークブックを OFD ドキュメントとしてエクスポートします。
### **ロゴ付きの請求書の作成**
この例では、ロゴ画像を上部左側の領域に挿入し、会社名と連絡先情報を入力し、結合セルにわたって「INVOICE」タイトルを追加し、請求書番号と日付を記録し、請求先のクライアントを記載し、説明、数量、単価、合計の列を含む明細項目テーブルを構築し、セルの数式を使用して小計、税金、総合計を計算することで、請求書ワークシートを作成します。太字のヘッダー、価格の通貨形式、罫線、列幅などの書式設定は、`Style` および `Font` オブジェクトを使用して適用されます。最後に、ワークブックは `SaveFormat.Ofd` を使用して `.ofd` 拡張子で保存されます。

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
## **既存の Excel ファイルを OFD に変換する**
Aspose.Cells は、ディスクから既存の Excel ワークブックを読み込み、それを直接 OFD 形式にエクスポートすることもできます。これは、バッチ変換パイプライン、アーカイブワークフロー、およびソースワークブックが別のツールで作成され、固定レイアウトの成果物として再出力するだけでよいシナリオで役立ちます。次の例では、既存の `.xlsx` ワークブックを読み込み、そのセルからデータを読み取り、オプションのページ設定調整を適用し、結果を OFD ドキュメントとして保存します。

```javascript
const AsposeCells = require("aspose.cells");

const dataDir = "C:\\Examples\\";

// ディスクから既存のExcelブックを開く
const workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");

// (1) ファイルが読み込まれたことを確認するために、選択したセルから値を読み取って表示する
const firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Worksheetsコレクションを反復処理して利用可能なシートを列挙する
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    const ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}

// (3) オプションで変換を反映するためにタイムスタンプセルを更新する
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));

// データブロックの先頭にサマリーヘッダー行を追加する
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));

// (4) ワークシートにPageSetupプロパティを設定する
const pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) オプションでOFD出力の印刷範囲を設定する
const lastRow = firstSheet.getCells().getMaxDataRow();
const lastCol = firstSheet.getCells().getMaxDataColumn();
const lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
const printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);

// (6) ブックをOFDファイルとして保存する
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");

function formatDate(date) {
    const pad = (n) => n.toString().padStart(2, '0');
    return date.getFullYear() + "-" + pad(date.getMonth() + 1) + "-" + pad(date.getDate()) + " " + pad(date.getHours()) + ":" + pad(date.getMinutes()) + ":" + pad(date.getSeconds());
}
```

## **関連記事**
- [Excel ファイルを複数のファイルに分割する](/cells/ja/nodejs-java/splitting-excel-files-into-multiple-files/)
- [セルへの画像の挿入](/cells/ja/nodejs-java/inserting-an-image-into-a-cell/)
- [DBF ファイルの読み取りと書き込み](/cells/ja/nodejs-java/dbf/)
- [Aspose.Cells for Node.js via Java におけるスパークラインから画像と HTML への変換](/cells/ja/nodejs-java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="javascript" >}}