---
title: ExcelをOFD形式に変換
linktitle: ExcelをOFD形式に変換
description: Aspose.Cellsは、スプレッドシートファイルを扱うためのJavaライブラリで、ExcelワークブックをOFD（Open Fixed-layout Document）形式に変換することをサポートします。この記事では、Aspose.Cellsを使用してExcelコンテンツを作成してOFDとしてエクスポートする方法と、既存のExcelファイルをOFDに変換する方法について説明します。
keywords: Aspose.Cells, Java library, spreadsheet, Excel to OFD, OFD conversion, SaveFormat.Ofd, fixed-layout document, workbook export
type: docs
weight: 195
url: /ja/java/converting-excel-to-ofd-format/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cellsは、`SaveFormat.Ofd`列挙値を使用して、ExcelワークブックをOFD（Open Fixed-layout Document）形式に直接変換することをサポートします。生成されたOFDドキュメントは、ワークブックの表示レイアウト、コンテンツ、結合セル、列幅、行の高さ、フォント、色、罫線、および数値形式を保持します。このため、Aspose.Cellsは、固定レイアウト出力を必要とするアーカイブ、印刷、規制当局への提出、政府への提出ワークフローに適しています。

{{% /alert %}}
## **はじめに**
OFD（Open Fixed-layout Document）は、固定されたページベースのレイアウトでデジタルドキュメントを表現するための中国国家标准（GB/T 33190-2016）です。ソースドキュメントの視覚的な外観が作成時と正確に同じ状態で保持されなければならない使用ケースにおいて、PDFと同様の役割を果たします。OFDは、政府への提出書類、規制当局への申請、電子請求書、および中華人民共和国での長期アーカイブで広く採用されています。

ExcelワークブックのOFDへの変換は、スプレッドシートのコンテンツを編集可能なスプレッドシートではなく、読み取り専用のレイアウトロックされた成果物として配布する必要があるシナリオで一般的な要件です。例としては、完成した請求書を顧客に発送する、四半期財務報告書をアーカイブする、または予算スプレッドシートを規制当局に提出するなどが挙げられます。Aspose.Cellsは、中間変換ステップを必要とせずにワークブックを直接OFDに書き出す`SaveFormat.Ofd`列挙値を通じて、この要件に対応しています。OFD出力は、セル値、結合範囲、フォント、色、罫線、数値形式、およびワークブックで構成されたページ設定オプションを保持します。

{{% alert color="primary" %}}

Aspose.Cellsによって生成されたOFD出力は、ソースワークブックの表示レイアウトを保持します。これには、セルコンテンツ、結合セル、列幅、行の高さが含まれます。フォント、色、罫線、配置、数値形式などのセル書式設定も、固定レイアウト出力でレンダリングされます。用紙サイズ、向き、印刷領域など、ワークシートで構成されたページ設定オプションは、結果として得られるOFDドキュメントのレイアウトに影響します。

{{% /alert %}}
## **Excelワークブックの作成とOFDとしての保存**
Aspose.Cellsを使用すると、プログラムによってワークブックを構築し、データを入力してから、`SaveFormat.Ofd`列挙値を使用してOFD形式に直接保存できます。次の例では、ゼロから請求書を作成します。会社のロゴ、ヘッダー情報、請求先セクション、明細項目、および計算された合計を追加し、ワークブックをOFDドキュメントにエクスポートします。
### **ロゴ付きの請求書の作成**
この例では、ロゴ画像を左上の領域に挿入し、会社名と連絡先情報を入力し、結合セルにわたって「INVOICE」タイトルを追加し、請求書番号と日付を記録し、請求先クライアントをリストし、説明、数量、単価、合計列を含む明細項目テーブルを作成し、セル数式を使用して小計、税金、総合計を計算することで、請求書ワークシートを構築します。太字のヘッダー、価格の通貨形式、罫線、列幅などの書式設定は、`Style`オブジェクトと`Font`オブジェクトを使用して適用されます。最後に、ワークブックは`SaveFormat.Ofd`を使用して`.ofd`拡張子で保存されます。

```java
import com.aspose.cells.*;
import java.text.SimpleDateFormat;
import java.util.Date;

String dataDir = "C:\\Temp\\";

// 新しいワークブックを作成
Workbook workbook = new Workbook();

// 最初のワークシートを取得
Worksheet worksheet = workbook.getWorksheets().get(0);

// 列幅を設定
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);

// 会社ロゴを挿入
worksheet.getPictures().add(1, 1, dataDir + "logo.png");

// 会社名と連絡先情報
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");

// 請求書タイトル - セルを結合
worksheet.getCells().merge(7, 1, 2, 4);
Cell titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

Style titleStyle = workbook.createStyle();
titleStyle.getFont().setBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);

// 請求書番号と日付
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new SimpleDateFormat("yyyy-MM-dd").format(new Date()));

// 請求先セクション
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// 明細項目のヘッダー
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

// 罫線付き通貨スタイル
Style currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

// 説明/数量セル用のシンプルな罫線スタイル
Style borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

// 明細項目の行
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

// 小計、税金、総合計
worksheet.getCells().get("B24").putValue("Subtotal:");
Cell subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
Cell taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
Cell grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// 合計値用の太字+通貨スタイル
Style totalStyle = workbook.createStyle();
totalStyle.getFont().setBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// 合計ラベル用の太字スタイル
Style boldStyle = workbook.createStyle();
boldStyle.getFont().setBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// ワークブックをOFDファイルとして保存
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```
## **既存のExcelファイルのOFDへの変換**
Aspose.Cellsは、ディスクから既存のExcelワークブックを読み込み、OFD形式に直接エクスポートすることもできます。これは、バッチ変換パイプライン、アーカイブワークフロー、およびソースワークブックが別のツールによって生成され、固定レイアウト成果物として再発行するだけでよいシナリオで役立ちます。次の例では、既存の`.xlsx`ワークブックを読み込み、そのセルからデータを読み取り、オプションのページ設定調整を適用し、結果をOFDドキュメントとして保存します。

```java
import com.aspose.cells.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

String dataDir = "C:\\Examples\\";

// ディスクから既存の Excel ブックを開く
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");

// (1) 選択したセルから値を読み取って表示し、ファイルが読み込まれたことを確認する
Worksheet firstSheet = workbook.getWorksheets().get(0);
System.out.println("First sheet name: " + firstSheet.getName());
System.out.println("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
System.out.println("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
System.out.println("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Worksheets コレクションを反復処理して利用可能なシートを列挙する
System.out.println("\nAvailable worksheets:");
for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet ws = workbook.getWorksheets().get(i);
    System.out.println("  [" + i + "] " + ws.getName());
}

// (3) オプションでタイムスタンプ セルを更新して変換を反映する
String timestamp1 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A1").putValue("Converted on: " + timestamp1);

// データ ブロックの先頭にサマリー ヘッダー行を追加する
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");

String timestamp2 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A2").putValue("Generated: " + timestamp2);

// (4) ワークシートに PageSetup プロパティを設定する
PageSetup pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(PageOrientationType.LANDSCAPE);
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) オプションで OFD 出力の印刷範囲を設定する
int lastRow = firstSheet.getCells().getMaxDataRow();
int lastCol = firstSheet.getCells().getMaxDataColumn();
String lastColLetter = CellsHelper.columnIndexToName(lastCol);
String printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
System.out.println("\nPrint area set to: " + printArea);

// (6) ブックを OFD ファイルとして保存する
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
System.out.println("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **関連記事**
- [Excelファイルを複数のファイルに分割](/cells/ja/java/splitting-excel-files-into-multiple-files/)
- [セルに画像を挿入](/cells/ja/java/inserting-an-image-into-a-cell/)
- [DBFファイルの読み取りと書き込み](/cells/ja/java/dbf/)
- [Aspose.Cells for Javaでスパークラインを画像とHTMLに変換](/cells/ja/java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="java" >}}