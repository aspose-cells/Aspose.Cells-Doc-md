---
title: Excel を OFD 形式に変換する
linktitle: Excel を OFD 形式に変換する
description: Aspose.Cells は、スプレッドシートファイルを扱うための .NET ライブラリであり、Excel ワークブックを OFD (Open Fixed-layout Document) 形式に変換することをサポートしています。この記事では、Excel コンテンツを作成して OFD としてエクスポートする方法、および Aspose.Cells を使用して既存の Excel ファイルを OFD に変換する方法について説明します。
keywords: Aspose.Cells, .NET ライブラリ, スプレッドシート, Excel から OFD, OFD 変換, SaveFormat.Ofd, 固定レイアウトドキュメント, ワークブックのエクスポート
type: docs
weight: 195
url: /ja/net/converting-excel-to-ofd-format/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、`SaveFormat.Ofd` 列挙値を使用して、Excel ワークブックを OFD (Open Fixed-layout Document) 形式に直接変換することをサポートしています。生成される OFD ドキュメントは、ワークブックの表示レイアウト、内容、結合されたセル、列幅、行の高さ、フォント、色、罫線、および数値書式を保持します。このため、Aspose.Cells は、固定レイアウトの出力を必要とするアーカイブ、印刷、規制当局への提出、政府機関への提出などのワークフローに適しています。

{{% /alert %}}
## **はじめに**
OFD (Open Fixed-layout Document) は、固定されたページベースのレイアウトでデジタル文書を表現するための中国国家标准 (GB/T 33190-2016) です。これは、ソースドキュメントの視覚的な外観を正確に作成されたとおりに保持する必要があるユースケースにおいて、PDF と同様の役割を果たします。OFD は、中華人民共和国における政府への提出、規制当局への届出、電子請求書、長期アーカイブで広く採用されています。

Excel ワークブックを OFD に変換することは、スプレッドシートの内容が編集可能なスプレッドシートとしてではなく、読み取り専用でレイアウトが固定された成果物として配布する必要があるシナリオで一般的な要件です。例としては、確定した請求書を顧客に送付する場合、四半期財務報告をアーカイブする場合、予算スプレッドシートを規制当局に提出する場合などがあります。Aspose.Cells は、中間の変換ステップを必要とせずワークブックを直接 OFD に書き出す `SaveFormat.Ofd` 列挙値を通じて、この要件に対応します。OFD 出力は、ワークブックに設定されたセルの値、結合範囲、フォント、色、罫線、数値書式、およびページ設定オプションを保持します。

{{% alert color="primary" %}}

Aspose.Cells によって生成された OFD 出力は、ソースワークブックの表示レイアウトを保持します。これには、セルの内容、結合されたセル、列幅、行の高さが含まれます。フォント、色、罫線、配置、数値書式などのセル書式も、固定レイアウト出力にレンダリングされます。用紙サイズ、向き、印刷領域など、ワークシートに設定されたページ設定オプションは、生成される OFD ドキュメントのレイアウトに影響します。

{{% /alert %}}
## **Excel ワークブックを作成して OFD として保存する**
Aspose.Cells を使用すると、ワークブックをプログラムで構築し、データを入力してから、`SaveFormat.Ofd` 列挙を使用して OFD 形式に直接保存できます。次の例では、請求書をゼロから作成します。会社のロゴ、ヘッダー情報、請求先セクション、明細項目、計算された合計を追加し、ワークブックを OFD ドキュメントとしてエクスポートします。
### **ロゴ付き請求書の作成**
この例では、ロゴ画像を左上の領域に挿入し、会社名と連絡先を入力し、結合されたセルに「INVOICE」というタイトルを追加し、請求書番号と日付を記録し、請求先のクライアントを記載し、説明、数量、単価、合計の列を含む明細項目の表を作成し、セル数式を使用して小計、税、総合計を計算することで、請求書ワークシートを作成します。太字のヘッダー、価格の通貨書式、罫線、列幅などの書式設定は、`Style` および `Font` オブジェクトを使用して適用されます。最後に、ワークブックは `SaveFormat.Ofd` を使用して `.ofd` 拡張子で保存されます。

```csharp
using System;
using Aspose.Cells;
using System.Drawing;

string dataDir = "C:\\Temp\\";

// 新しいワークブックを作成
Workbook workbook = new Workbook();

// 最初のワークシートを取得
Worksheet worksheet = workbook.Worksheets[0];

// 列幅を設定
worksheet.Cells.SetColumnWidth(0, 5);
worksheet.Cells.SetColumnWidth(1, 35);
worksheet.Cells.SetColumnWidth(2, 12);
worksheet.Cells.SetColumnWidth(3, 15);
worksheet.Cells.SetColumnWidth(4, 15);
worksheet.Cells.SetColumnWidth(5, 5);

// 会社ロゴを挿入
worksheet.Pictures.Add(1, 1, dataDir + "logo.png");

// 会社名と連絡先情報
worksheet.Cells["B3"].PutValue("Acme Corporation");
worksheet.Cells["B4"].PutValue("123 Business Street");
worksheet.Cells["B5"].PutValue("City, State 12345");
worksheet.Cells["B6"].PutValue("Phone: (555) 123-4567");

// INVOICE タイトル - セルを結合
worksheet.Cells.Merge(7, 1, 2, 4);
Cell titleCell = worksheet.Cells["B8"];
titleCell.PutValue("INVOICE");

Style titleStyle = workbook.CreateStyle();
titleStyle.Font.IsBold = true;
titleStyle.Font.Size = 20;
titleStyle.HorizontalAlignment = TextAlignmentType.Center;
titleCell.SetStyle(titleStyle);

// 請求書番号と日付
worksheet.Cells["B11"].PutValue("Invoice Number:");
worksheet.Cells["C11"].PutValue("INV-2024-001");
worksheet.Cells["B12"].PutValue("Date:");
worksheet.Cells["C12"].PutValue(DateTime.Now.ToString("yyyy-MM-dd"));

// 請求先セクション
worksheet.Cells["B14"].PutValue("Bill To:");
worksheet.Cells["B15"].PutValue("Client Name");
worksheet.Cells["B16"].PutValue("Client Address");
worksheet.Cells["B17"].PutValue("Client City, State");

// 明細項目のヘッダー
Cell headerDesc = worksheet.Cells["B19"];
Cell headerQty = worksheet.Cells["C19"];
Cell headerPrice = worksheet.Cells["D19"];
Cell headerTotal = worksheet.Cells["E19"];

headerDesc.PutValue("Description");
headerQty.PutValue("Quantity");
headerPrice.PutValue("Unit Price");
headerTotal.PutValue("Total");

Style headerStyle = workbook.CreateStyle();
headerStyle.Font.IsBold = true;
headerStyle.Font.Color = Color.White;
headerStyle.BackgroundColor = Color.Navy;
headerStyle.HorizontalAlignment = TextAlignmentType.Center;
headerStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

headerDesc.SetStyle(headerStyle);
headerQty.SetStyle(headerStyle);
headerPrice.SetStyle(headerStyle);
headerTotal.SetStyle(headerStyle);

// 罫線付き通貨スタイル
Style currencyStyle = workbook.CreateStyle();
currencyStyle.Custom = "\"$\"#,##0.00";
currencyStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// 説明/数量セル用のシンプルな罫線スタイル
Style borderStyle = workbook.CreateStyle();
borderStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// 明細項目の行
object[,] lineItems = new object[,] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};

for (int i = 0; i < lineItems.GetLength(0); i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.Cells[row, 1];
    Cell qtyCell = worksheet.Cells[row, 2];
    Cell priceCell = worksheet.Cells[row, 3];
    Cell totalCell = worksheet.Cells[row, 4];

    descCell.PutValue(lineItems[i, 0]);
    qtyCell.PutValue(lineItems[i, 1]);
    priceCell.PutValue(lineItems[i, 2]);
    totalCell.Formula = "C" + row + "*D" + row;

    descCell.SetStyle(borderStyle);
    qtyCell.SetStyle(borderStyle);
    priceCell.SetStyle(currencyStyle);
    totalCell.SetStyle(currencyStyle);
}

// 小計、税、総合計
worksheet.Cells["B24"].PutValue("Subtotal:");
Cell subtotalCell = worksheet.Cells["E24"];
subtotalCell.Formula = "SUM(E20:E22)";

worksheet.Cells["B25"].PutValue("Tax (10%):");
Cell taxCell = worksheet.Cells["E25"];
taxCell.Formula = "E24*0.1";

worksheet.Cells["B26"].PutValue("Grand Total:");
Cell grandTotalCell = worksheet.Cells["E26"];
grandTotalCell.Formula = "E24+E25";

// 合計値用の太字＋通貨スタイル
Style totalStyle = workbook.CreateStyle();
totalStyle.Font.IsBold = true;
totalStyle.Custom = "\"$\"#,##0.00";

subtotalCell.SetStyle(totalStyle);
taxCell.SetStyle(totalStyle);
grandTotalCell.SetStyle(totalStyle);

// 合計ラベル用の太字スタイル
Style boldStyle = workbook.CreateStyle();
boldStyle.Font.IsBold = true;

worksheet.Cells["B24"].SetStyle(boldStyle);
worksheet.Cells["B25"].SetStyle(boldStyle);
worksheet.Cells["B26"].SetStyle(boldStyle);

// ワークブックをOFDファイルとして保存
workbook.Save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```
## **既存の Excel ファイルを OFD に変換する**
Aspose.Cells は、ディスクから既存の Excel ワークブックを読み込み、OFD 形式に直接エクスポートすることもできます。これは、バッチ変換パイプライン、アーカイブワークフロー、ソースワークブックが別のツールによって作成され、固定レイアウトの成果物として再出力するだけでよいシナリオで役立ちます。次の例では、既存の `.xlsx` ワークブックを読み込み、そのセルからデータを読み取り、オプションのページ設定調整を適用し、結果を OFD ドキュメントとして保存します。

```csharp
using System;
using Aspose.Cells;

string dataDir = "C:\\Examples\\";

// ディスクから既存の Excel ブックを開きます
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");

// (1) ファイルが読み込まれたことを確認するために、選択したセルから値を読み取って表示します
Worksheet firstSheet = workbook.Worksheets[0];
Console.WriteLine("First sheet name: " + firstSheet.Name);
Console.WriteLine("Cell A1: " + firstSheet.Cells["A1"].StringValue);
Console.WriteLine("Cell B1: " + firstSheet.Cells["B1"].StringValue);
Console.WriteLine("Cell C1: " + firstSheet.Cells["C1"].StringValue);

// (2) Worksheets コレクションを反復処理して利用可能なシートを列挙します
Console.WriteLine("\nAvailable worksheets:");
for (int i = 0; i < workbook.Worksheets.Count; i++)
{
    Worksheet ws = workbook.Worksheets[i];
    Console.WriteLine("  [" + i + "] " + ws.Name);
}

// (3) オプションで変換を反映するタイムスタンプ セルを更新します
firstSheet.Cells["A1"].PutValue("Converted on: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// データ ブロックの先頭にサマリー ヘッダー行を追加します
firstSheet.Cells.InsertRow(0);
firstSheet.Cells["A1"].PutValue("Conversion Summary");
firstSheet.Cells["A2"].PutValue("Generated: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// (4) ワークシートで PageSetup プロパティを構成します
PageSetup pageSetup = firstSheet.PageSetup;
pageSetup.Orientation = PageOrientationType.Landscape;
pageSetup.PaperSize = PaperSizeType.PaperA4;
pageSetup.FitToPagesTall = 1;
pageSetup.FitToPagesWide = 1;

// (5) オプションで OFD 出力の印刷範囲を設定します
int lastRow = firstSheet.Cells.MaxDataRow;
int lastCol = firstSheet.Cells.MaxDataColumn;
string lastColLetter = CellsHelper.ColumnIndexToName(lastCol);
string printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.PageSetup.PrintArea = printArea;
Console.WriteLine("\nPrint area set to: " + printArea);

// (6) ブックを OFD ファイルとして保存します
workbook.Save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
Console.WriteLine("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **関連記事**
- [Excel ファイルを複数のファイルに分割する](/cells/ja/net/splitting-excel-files-into-multiple-files/)
- [セルへの画像の挿入](/cells/ja/net/inserting-an-image-into-a-cell/)
- [DBF ファイルの読み取りと書き込み](/cells/ja/net/dbf/)
- [Aspose.Cells for .NET でのスパークラインから画像および HTML への変換](/cells/ja/net/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="csharp" >}}