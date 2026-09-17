---
title: ExcelをOFD形式に変換
linktitle: ExcelをOFD形式に変換
description: Aspose.Cellsはスプレッドシートファイルを扱うためのJavaライブラリで、ExcelワークブックをOFD（Open Fixed-layout Document）形式に変換することをサポートしています。この記事では、Excelコンテンツを作成してOFDとしてエクスポートする方法、およびAspose.Cellsを使用して既存のExcelファイルをOFDに変換する方法について説明します。
keywords: Aspose.Cells, Javaライブラリ, スプレッドシート, ExcelからOFDへ, OFD変換, SaveFormat.Ofd, 固定レイアウトドキュメント, ワークブックのエクスポート
type: docs
weight: 195
url: /ja/java/converting-excel-to-ofd-format/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cellsは、`SaveFormat.Ofd`列挙値を使用して、ExcelワークブックをOFD（Open Fixed-layout Document）形式に直接変換することをサポートしています。結果として生成されるOFDドキュメントは、ワークブックの表示レイアウト、コンテンツ、結合セル、列幅、行の高さ、フォント、色、罫線、および数値形式を保持します。これにより、Aspose.Cellsは、固定レイアウトの出力が必要なアーカイブ、印刷、規制当局への提出、政府機関への提出のワークフローに適しています。

## **はじめに**
OFD（Open Fixed-layout Document）は、固定されたページベースのレイアウトでデジタル文書を表現するための中国国家標準（GB/T 33190-2016）です。ソースドキュメントの視覚的な外観が作成時とまったく同様に保持されなければならないユースケースにおいて、PDFと同様の役割を果たします。OFDは中華人民共和国での政府への提出、規制当局への届出、電子請求書、長期アーカイブに広く採用されています。
ExcelワークブックをOFDに変換することは、スプレッドシートのコンテンツを編集可能なスプレッドシートとしてではなく、読み取り専用でレイアウトが固定されたアーティファクトとして配布する必要があるシナリオで一般的な要件です。例としては、顧客への最終化された請求書の送付、四半期財務報告書のアーカイブ、予算スプレッドシートの規制当局への提出などが挙げられます。Aspose.Cellsはこの要件に`SaveFormat.Ofd`列挙値を通じて対応しており、中間変換ステップを必要とせずにワークブックを直接OFDに書き込みます。OFD出力は、ワークブックに設定されたセルの値、結合範囲、フォント、色、罫線、数値形式、およびページ設定オプションを保持します。

{{% alert color="primary" %}}
Aspose.Cellsによって生成されたOFD出力は、ソースワークブックの表示レイアウトを保持します。これには、セルコンテンツ、結合セル、列幅、行の高さが含まれます。フォント、色、罫線、配置、数値形式などのセル書式設定も、固定レイアウトの出力でレンダリングされます。用紙のサイズ、向き、印刷領域など、ワークシートに設定されたページ設定オプションは、結果として得られるOFDドキュメントのレイアウトに影響します。

## **Excelワークブックを作成してOFDとして保存する**
Aspose.Cellsを使用すると、プログラムでワークブックを構築し、データを入力してから、`SaveFormat.Ofd`列挙を使用してOFD形式に直接保存できます。次の例では、ゼロから請求書を作成します。会社のロゴ、ヘッダー情報、請求先セクション、明細項目、および計算された合計を追加し、ワークブックをOFDドキュメントとしてエクスポートします。

### **ロゴ付き請求書の作成**
この例では、ロゴ画像を左上の領域に挿入し、会社名と連絡先を入力し、結合セルに「INVOICE」というタイトルを追加し、請求書番号と日付を記録し、請求先のクライアントを列挙し、説明、数量、単価、合計の列を持つ明細項目テーブルを構築し、セル数式を使用して小計、税金、および総計を計算することで、請求書ワークシートを作成します。太字のヘッダー、価格の通貨形式、罫線、列幅などの書式設定は、`Style`および`Font`オブジェクトを使用して適用されます。最後に、ワークブックは`SaveFormat.Ofd`を使用して`.ofd`拡張子で保存されます。

## **既存のExcelファイルをOFDに変換する**
Aspose.Cellsは、ディスクから既存のExcelワークブックを読み込み、OFD形式に直接エクスポートすることもできます。これは、バッチ変換パイプライン、アーカイブワークフロー、およびソースワークブックが別のツールで作成され、固定レイアウトのアーティファクトとして再発行するだけでよいシナリオに役立ちます。次の例では、既存の`.xlsx`ワークブックを読み込み、そのセルからデータを読み取り、オプションのページ設定調整を適用し、結果をOFDドキュメントとして保存します。
{{% /alert %}}

{{% /alert %}}

```java
import com.aspose.cells.*;
import java.text.SimpleDateFormat;
import java.util.Date;
String dataDir = "C:\\Temp\\";
// Create a new Workbook
Workbook workbook = new Workbook();
// Obtain the first worksheet
Worksheet worksheet = workbook.getWorksheets().get(0);
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
Cell titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");
Style titleStyle = workbook.createStyle();
titleStyle.getFont().setBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);
// Invoice number and date
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new SimpleDateFormat("yyyy-MM-dd").format(new Date()));
// Bill-to section
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");
// Line items header
Cell headerDesc = worksheet.getCells().get("B19");
Cell headerQty = worksheet.getCells().get("C19");
Cell headerPrice = worksheet.getCells().get("D19");
Cell headerTotal = worksheet.getCells().get("E19");
headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");
Style headerStyle = workbook.createStyle();
headerStyle.getFont().setBold(true);
headerStyle.getFont().setColor(Color.getWhite());
headerStyle.setBackgroundColor(Color.getNavy());
headerStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
headerStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);
// Currency style with borders
Style currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
// Plain border style for description/quantity cells
Style borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
// Line items rows
Object[][] lineItems = new Object[][] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};
for (int i = 0; i < lineItems.length; i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.getCells().get(row, 1);
    Cell qtyCell = worksheet.getCells().get(row, 2);
    Cell priceCell = worksheet.getCells().get(row, 3);
    Cell totalCell = worksheet.getCells().get(row, 4);
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
Cell subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");
worksheet.getCells().get("B25").putValue("Tax (10%):");
Cell taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");
worksheet.getCells().get("B26").putValue("Grand Total:");
Cell grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");
// Bold + currency style for total values
Style totalStyle = workbook.createStyle();
totalStyle.getFont().setBold(true);
totalStyle.setCustom("\"$\"#,##0.00");
subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);
// Bold style for total labels
Style boldStyle = workbook.createStyle();
boldStyle.getFont().setBold(true);
worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);
// Save the workbook as an OFD file
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```

```java
import com.aspose.cells.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
String dataDir = "C:\\Examples\\";
// Open an existing Excel workbook from disk
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");
// (1) Read and display values from selected cells to confirm the file was loaded
Worksheet firstSheet = workbook.getWorksheets().get(0);
System.out.println("First sheet name: " + firstSheet.getName());
System.out.println("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
System.out.println("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
System.out.println("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());
// (2) Iterate over the Worksheets collection to enumerate available sheets
System.out.println("\nAvailable worksheets:");
for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet ws = workbook.getWorksheets().get(i);
    System.out.println("  [" + i + "] " + ws.getName());
}
// (3) Optionally update a timestamp cell to reflect the conversion
String timestamp1 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A1").putValue("Converted on: " + timestamp1);
// Append a summary header row at the top of the data block
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
String timestamp2 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A2").putValue("Generated: " + timestamp2);
// (4) Configure PageSetup properties on the worksheet
PageSetup pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(PageOrientationType.LANDSCAPE);
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);
// (5) Optionally set the print area for the OFD output
int lastRow = firstSheet.getCells().getMaxDataRow();
int lastCol = firstSheet.getCells().getMaxDataColumn();
String lastColLetter = CellsHelper.columnIndexToName(lastCol);
String printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
System.out.println("\nPrint area set to: " + printArea);
// (6) Save the workbook as an OFD file
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
System.out.println("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

{{< app/cells/assistant language="java" >}}