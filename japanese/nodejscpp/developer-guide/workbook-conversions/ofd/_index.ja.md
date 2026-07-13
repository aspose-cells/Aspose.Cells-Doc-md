---
title: ExcelをOFD形式に変換する
linktitle: ExcelをOFD形式に変換する
description: Aspose.Cellsは、スプレッドシートファイルを扱うためのNode.jsライブラリであり、ExcelワークブックをOFD（Open Fixed-layout Document）形式に変換することをサポートしています。この記事では、Excelコンテンツを作成してOFDとしてエクスポートする方法、およびAspose.Cellsを使用して既存のExcelファイルをOFDに変換する方法について説明します。
keywords: Aspose.Cells, Node.js ライブラリ, スプレッドシート, ExcelからOFD, OFD変換, SaveFormat.Ofd, 固定レイアウトドキュメント, ワークブックのエクスポート
type: docs
weight: 195
url: /ja/nodejs-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cellsは、`SaveFormat.Ofd` 列挙値を使用して、ExcelワークブックをOFD（Open Fixed-layout Document）形式に直接変換することをサポートしています。生成されたOFDドキュメントは、ワークブックの表示レイアウト、コンテンツ、結合セル、列幅、行の高さ、フォント、色、罫線、および数値形式を保持します。これにより、Aspose.Cellsは、固定レイアウトの出力が必要なアーカイブ、印刷、規制当局への提出、政府提出などのワークフローに適しています。

{{% /alert %}}
## **はじめに**
OFD（Open Fixed-layout Document）は、固定されたページベースのレイアウトでデジタルドキュメントを表現するための中国国家標準（GB/T 33190-2016）です。これは、ソースドキュメントの視覚的な外観を作成されたとおりに正確に保持する必要があるユースケースにおいて、PDFと同様の役割を果たします。OFDは、中華人民共和国における政府への提出、規制当局への申請、電子請求書、および長期アーカイブに広く採用されています。

ExcelワークブックをOFDに変換することは、スプレッドシートコンテンツを編集可能なスプレッドシートとしてではなく、読み取り専用でレイアウトが固定された成果物として配布する必要があるシナリオで一般的な要件です。例としては、顧客への最終化された請求書の送付、四半期財務報告のアーカイブ、または予算スプレッドシートの規制当局への提出などがあります。Aspose.Cellsは、中間変換ステップを必要とせずにワークブックを直接OFDに書き込む`SaveFormat.Ofd` 列挙値を通じて、この要件に対応しています。OFD出力は、セル値、結合範囲、フォント、色、罫線、数値形式、およびワークブックに設定されたページセットアップオプションを保持します。

{{% alert color="primary" %}}

Aspose.Cellsによって生成されたOFD出力は、セルコンテンツ、結合セル、列幅、行の高さなど、ソースワークブックの表示レイアウトを保持します。フォント、色、罫線、配置、数値形式などのセル書式設定も、固定レイアウトの出力でレンダリングされます。用紙サイズ、向き、印刷領域など、ワークシートに設定されたページセットアップオプションは、結果として得られるOFDドキュメントのレイアウトに影響します。

{{% /alert %}}
## **Excelワークブックの作成とOFDとしての保存**
Aspose.Cellsを使用すると、ワークブックをプログラムで構築し、データを入力してから、`SaveFormat.Ofd` 列挙を使用してOFD形式に直接保存できます。次の例では、請求書を最初から作成します。会社のロゴ、ヘッダー情報、請求先セクション、明細項目、および計算された合計を追加し、ワークブックをOFDドキュメントにエクスポートします。
### **ロゴを含む請求書の作成**
この例では、ロゴ画像を左上の領域に挿入し、会社名と連絡先情報を入力し、結合されたセルに「INVOICE」というタイトルを追加し、請求書番号と日付を記録し、請求先クライアントを記載し、説明、数量、単価、合計の列を含む明細項目テーブルを作成し、セル数式を使用して小計、税金、総合計を計算することで、請求書ワークシートを構築します。太字のヘッダー、価格の通貨形式、罫線、列幅などの書式設定は、`Style` および `Font` オブジェクトを使用して適用されます。最後に、ワークブックは`SaveFormat.Ofd` を使用して`.ofd` 拡張子で保存されます。

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
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
titleCell.setStyle(titleStyle);

// Invoice number and date
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
let now = new Date();
let dateStr = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
worksheet.getCells().get("C12").putValue(dateStr);

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
headerStyle.getFont().setColor(AsposeCells.Color.White);
headerStyle.setBackgroundColor(AsposeCells.Color.Navy);
headerStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Currency style with borders
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

// Plain border style for description/quantity cells
let borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

// Line items rows
let lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
];

for (let i = 0; i < lineItems.length; i++) {
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
## **既存のExcelファイルをOFDに変換する**
Aspose.Cellsは、ディスクから既存のExcelワークブックをロードし、OFD形式に直接エクスポートすることもできます。これは、バッチ変換パイプライン、アーカイブワークフロー、およびソースワークブックが別のツールによって作成され、固定レイアウトの成果物として再発行されるだけのシナリオで役立ちます。次の例では、既存の`.xlsx` ワークブックをロードし、そのセルからデータを読み取り、オプションのページセットアップ調整を適用し、結果をOFDドキュメントとして保存します。

```javascript
let workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");

// (1) 選択したセルから値を読み取って表示し、ファイルが読み込まれたことを確認する
let firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Worksheets コレクションを反復処理して利用可能なシートを列挙する
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    let ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}

// (3) オプションでタイムスタンプセルを更新して変換を反映する
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));

// データブロックの先頭にサマリーヘッダー行を追加する
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));

// (4) ワークシートの PageSetup プロパティを構成する
let pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) オプションで OFD 出力の印刷範囲を設定する
let lastRow = firstSheet.getCells().getMaxDataRow();
let lastCol = firstSheet.getCells().getMaxDataColumn();
let lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
let printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);

// (6) ワークブックを OFD ファイルとして保存する
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **関連記事**
- [Excelファイルを複数のファイルに分割する](/cells/ja/nodejs-cpp/splitting-excel-files-into-multiple-files/)
- [セルに画像を挿入する](/cells/ja/nodejs-cpp/inserting-an-image-into-a-cell/)
- [DBFファイルの読み取りと書き込み](/cells/ja/nodejs-cpp/dbf/)
- [Aspose.Cells for Node.js via C++でスパークラインを画像とHTMLに変換する](/cells/ja/nodejs-cpp/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="javascript" >}}