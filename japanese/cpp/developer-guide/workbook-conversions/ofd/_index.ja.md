---
title: Excel を OFD 形式に変換する
linktitle: Excel を OFD 形式に変換する
description: Aspose.Cells は、スプレッドシートファイルを扱うための C++ ライブラリであり、Excel ワークブックを OFD（Open Fixed-layout Document）形式に変換することをサポートしています。この記事では、Excel コンテンツを作成して OFD としてエクスポートする方法、および Aspose.Cells を使用して既存の Excel ファイルを OFD に変換する方法について説明します。
keywords: Aspose.Cells, C++ ライブラリ, スプレッドシート, Excel から OFD, OFD 変換, SaveFormat.Ofd, 固定レイアウトドキュメント, ワークブックのエクスポート
type: docs
weight: 195
url: /ja/cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、`SaveFormat.Ofd` 列挙値を使用して Excel ワークブックを OFD（Open Fixed-layout Document）形式に直接変換することをサポートしています。生成された OFD ドキュメントは、ワークブックの表示レイアウト、内容、結合セル、列幅、行の高さ、フォント、色、罫線、および数値形式を保持します。このため、Aspose.Cells は、固定レイアウトの出力が必要なアーカイブ、印刷、規制当局への提出、政府機関への申請ワークフローに適しています。

{{% /alert %}}
## **はじめに**
OFD（Open Fixed-layout Document）は、固定されたページベースのレイアウトでデジタル文書を表現するための中国の国家标准（GB/T 33190-2016）です。これは、ソース文書の視覚的な外観を正確に保持する必要があるユースケースにおいて、PDF と同様の役割を果たします。OFD は中華人民共和国における政府機関への提出、規制当局への申請、電子請求書、長期アーカイブに広く採用されています。

Excel ワークブックを OFD に変換することは、スプレッドシートの内容を編集可能なスプレッドシートとしてではなく、読み取り専用のレイアウトが固定された成果物として配布する必要があるシナリオで一般的な要件です。例としては、確定した請求書を顧客に送付する場合、四半期財務報告をアーカイブする場合、規制当局に予算スプレッドシートを提出する場合などがあります。Aspose.Cells はこの要件に `SaveFormat.Ofd` 列挙値で対応しており、中間変換ステップを必要とせずにワークブックを直接 OFD に書き込みます。OFD 出力は、セル値、結合範囲、フォント、色、罫線、数値形式、およびワークブックに設定されたページ設定オプションを保持します。

{{% alert color="primary" %}}

Aspose.Cells によって生成された OFD 出力は、ソースワークブックの表示レイアウトを保持します。これには、セル内容、結合セル、列幅、行の高さが含まれます。フォント、色、罫線、配置、数値形式などのセル書式も、固定レイアウト出力でレンダリングされます。用紙サイズ、向き、印刷領域など、ワークシートに設定されたページ設定オプションは、生成される OFD ドキュメントのレイアウトに影響します。

{{% /alert %}}
## **Excel ワークブックを作成して OFD として保存する**
Aspose.Cells を使用すると、ワークブックをプログラムで構築し、データを入力してから、`SaveFormat.Ofd` 列挙を使用して OFD 形式に直接保存できます。次の例では、請求書をゼロから作成します。会社ロゴ、ヘッダー情報、請求先セクション、明細項目、計算された合計を追加し、ワークブックを OFD ドキュメントとしてエクスポートします。
### **ロゴ付き請求書の作成**
この例では、ロゴ画像を左上の領域に挿入し、会社名と連絡先を入力し、結合セルに「INVOICE」タイトルを追加し、請求書番号と日付を記録し、請求先クライアントをリストし、説明、数量、単価、合計の各列を含む明細項目テーブルを作成し、セルの数式を使用して小計、税、総合計を計算することで、請求書ワークシートを構築します。太字のヘッダー、価格の通貨形式、罫線、列幅などの書式設定は、`Style` および `Font` オブジェクトを使用して適用されます。最後に、ワークブックは `SaveFormat.Ofd` を使用して `.ofd` 拡張子で保存されます。

```cpp
// Aspose.Cells for C++ のサンプル
// Aspose.Cells 26.6.0（以降）と C++17（以降）対応コンパイラでコンパイル

#include "Aspose.Cells.h"
#include <string>
#include <ctime>

using namespace Aspose::Cells;

int main()
{
    // Aspose.Cells を初期化
    Aspose::Cells::Startup();

    // リソースおよび出力用ディレクトリ
    const char16_t* dataDir = u"C:\\Temp\\";

    // 新しいワークブックを作成
    Workbook workbook;

    // 最初のワークシートを取得
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // 列幅を設定
    cells.SetColumnWidth(0, 5.0);
    cells.SetColumnWidth(1, 35.0);
    cells.SetColumnWidth(2, 12.0);
    cells.SetColumnWidth(3, 15.0);
    cells.SetColumnWidth(4, 15.0);
    cells.SetColumnWidth(5, 5.0);

    // 会社ロゴを挿入
    worksheet.GetPictures().Add(1, 1, U16String(dataDir) + u"logo.png");

    // 会社名と連絡先情報
    cells.Get(u"B3").PutValue(u"Acme Corporation");
    cells.Get(u"B4").PutValue(u"123 Business Street");
    cells.Get(u"B5").PutValue(u"City, State 12345");
    cells.Get(u"B6").PutValue(u"Phone: (555) 123-4567");

    // INVOICE タイトル - セルを結合
    cells.Merge(7, 1, 2, 4);
    Cell titleCell = cells.Get(u"B8");
    titleCell.PutValue(u"INVOICE");

    Style titleStyle = workbook.CreateStyle();
    titleStyle.GetFont().SetIsBold(true);
    titleStyle.GetFont().SetSize(20);
    titleStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    titleCell.SetStyle(titleStyle);

    // 請求書番号と日付
    cells.Get(u"B11").PutValue(u"Invoice Number:");
    cells.Get(u"C11").PutValue(u"INV-2024-001");
    cells.Get(u"B12").PutValue(u"Date:");

    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char dateBuffer[11];
    std::strftime(dateBuffer, sizeof(dateBuffer), "%Y-%m-%d", now);
    cells.Get(u"C12").PutValue(U16String(dateBuffer));

    // 請求先セクション
    cells.Get(u"B14").PutValue(u"Bill To:");
    cells.Get(u"B15").PutValue(u"Client Name");
    cells.Get(u"B16").PutValue(u"Client Address");
    cells.Get(u"B17").PutValue(u"Client City, State");

    // 明細項目のヘッダー
    Cell headerDesc = cells.Get(u"B19");
    Cell headerQty = cells.Get(u"C19");
    Cell headerPrice = cells.Get(u"D19");
    Cell headerTotal = cells.Get(u"E19");

    headerDesc.PutValue(u"Description");
    headerQty.PutValue(u"Quantity");
    headerPrice.PutValue(u"Unit Price");
    headerTotal.PutValue(u"Total");

    Style headerStyle = workbook.CreateStyle();
    headerStyle.GetFont().SetIsBold(true);
    headerStyle.GetFont().SetColor(Color::White());
    headerStyle.SetForegroundColor(Color{0, 0, 128});
    headerStyle.SetPattern(BackgroundType::Solid);
    headerStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    headerStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    headerDesc.SetStyle(headerStyle);
    headerQty.SetStyle(headerStyle);
    headerPrice.SetStyle(headerStyle);
    headerTotal.SetStyle(headerStyle);

    // 罫線付き通貨スタイル
    Style currencyStyle = workbook.CreateStyle();
    currencyStyle.SetCustom(u"\"$\"#,##0.00");
    currencyStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // 説明・数量セル用のシンプルな罫線スタイル
    Style borderStyle = workbook.CreateStyle();
    borderStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // 明細項目の行
    struct LineItem { const char16_t* desc; int qty; double price; };
    LineItem lineItems[] = {
        {u"Product A - Widget", 2, 50.00},
        {u"Product B - Gadget", 3, 75.00},
        {u"Product C - Service", 1, 100.00}
    };

    for (int i = 0; i < 3; i++)
    {
        int row = 20 + i;
        Cell descCell = cells.Get(row, 1);
        Cell qtyCell = cells.Get(row, 2);
        Cell priceCell = cells.Get(row, 3);
        Cell totalCell = cells.Get(row, 4);

        descCell.PutValue(lineItems[i].desc);
        qtyCell.PutValue(lineItems[i].qty);
        priceCell.PutValue(lineItems[i].price);

        std::string formula = "C" + std::to_string(row) + "*D" + std::to_string(row);
        totalCell.SetFormula(U16String(formula.c_str()));

        descCell.SetStyle(borderStyle);
        qtyCell.SetStyle(borderStyle);
        priceCell.SetStyle(currencyStyle);
        totalCell.SetStyle(currencyStyle);
    }

    // 小計、税、総合計
    cells.Get(u"B24").PutValue(u"Subtotal:");
    Cell subtotalCell = cells.Get(u"E24");
    subtotalCell.SetFormula(u"SUM(E20:E22)");

    cells.Get(u"B25").PutValue(u"Tax (10%):");
    Cell taxCell = cells.Get(u"E25");
    taxCell.SetFormula(u"E24*0.1");

    cells.Get(u"B26").PutValue(u"Grand Total:");
    Cell grandTotalCell = cells.Get(u"E26");
    grandTotalCell.SetFormula(u"E24+E25");

    // 合計値用の太字＋通貨スタイル
    Style totalStyle = workbook.CreateStyle();
    totalStyle.GetFont().SetIsBold(true);
    totalStyle.SetCustom(u"\"$\"#,##0.00");

    subtotalCell.SetStyle(totalStyle);
    taxCell.SetStyle(totalStyle);
    grandTotalCell.SetStyle(totalStyle);

    // 合計ラベル用の太字スタイル
    Style boldStyle = workbook.CreateStyle();
    boldStyle.GetFont().SetIsBold(true);

    cells.Get(u"B24").SetStyle(boldStyle);
    cells.Get(u"B25").SetStyle(boldStyle);
    cells.Get(u"B26").SetStyle(boldStyle);

    // ワークブックを OFD ファイルとして保存
    workbook.Save(U16String(dataDir) + u"Invoice.ofd", SaveFormat::Ofd);

    // Aspose.Cells のリソースを解放
    Aspose::Cells::Cleanup();

    return 0;
}
```
## **既存の Excel ファイルを OFD に変換する**
Aspose.Cells は、ディスクから既存の Excel ワークブックを読み込み、OFD 形式に直接エクスポートすることもできます。これは、バッチ変換パイプライン、アーカイブワークフロー、ソースワークブックが別のツールで作成され、固定レイアウトの成果物として再出力するだけでよいシナリオで役立ちます。次の例では、既存の `.xlsx` ワークブックを読み込み、そのセルからデータを読み取り、オプションのページ設定調整を適用し、結果を OFD ドキュメントとして保存します。

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <iostream>
#include <ctime>

using namespace Aspose::Cells;

std::string GetCurrentTimestamp() {
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char buffer[20];
    std::strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", now);
    return std::string(buffer);
}

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "C:\\Examples\\";

    // ディスクから既存のExcelブックを開きます
    Workbook workbook(U16String((dataDir + "SampleBook.xlsx").c_str()));

    // (1) ファイルが読み込まれたことを確認するために、選択したセルの値を読み取って表示します
    Worksheet firstSheet = workbook.GetWorksheets().Get(0);
    U16String sheetName = firstSheet.GetName();
    Cell a1 = firstSheet.GetCells().Get(u"A1");
    Cell b1 = firstSheet.GetCells().Get(u"B1");
    Cell c1 = firstSheet.GetCells().Get(u"C1");

    std::cout << "First sheet name: " << sheetName.ToUtf8() << std::endl;
    std::cout << "Cell A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell B1: " << b1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell C1: " << c1.GetStringValue().ToUtf8() << std::endl;

    // (2) Worksheetsコレクションを反復処理して利用可能なシートを列挙します
    std::cout << "\nAvailable worksheets:" << std::endl;
    WorksheetCollection sheets = workbook.GetWorksheets();
    int sheetCount = sheets.GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet ws = sheets.Get(i);
        U16String wsName = ws.GetName();
        std::cout << "  [" << i << "] " << wsName.ToUtf8() << std::endl;
    }

    // (3) オプションでタイムスタンプセルを更新して変換を反映します
    std::string timestamp1 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A1").PutValue(U16String(("Converted on: " + timestamp1).c_str()));

    // データブロックの先頭にサマリーヘッダー行を追加します
    firstSheet.GetCells().InsertRow(0);
    firstSheet.GetCells().Get(u"A1").PutValue(u"Conversion Summary");

    std::string timestamp2 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A2").PutValue(U16String(("Generated: " + timestamp2).c_str()));

    // (4) ワークシートにPageSetupプロパティを設定します
    PageSetup pageSetup = firstSheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    pageSetup.SetFitToPagesTall(1);
    pageSetup.SetFitToPagesWide(1);

    // (5) オプションでOFD出力の印刷範囲を設定します
    int lastRow = firstSheet.GetCells().GetMaxDataRow();
    int lastCol = firstSheet.GetCells().GetMaxDataColumn();
    U16String lastColLetter = CellsHelper::ColumnIndexToName(lastCol);
    std::string printArea = "A1:" + lastColLetter.ToUtf8() + std::to_string(lastRow + 1);
    firstSheet.GetPageSetup().SetPrintArea(U16String(printArea.c_str()));
    std::cout << "\nPrint area set to: " << printArea << std::endl;

    // (6) ワークブックをOFDファイルとして保存します
    workbook.Save(U16String((dataDir + "SampleBook.ofd").c_str()), SaveFormat::Ofd);
    std::cout << "\nFile successfully converted to OFD format: " << dataDir << "SampleBook.ofd" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **関連記事**
- [Excel ファイルを複数のファイルに分割する](/cells/ja/cpp/splitting-excel-files-into-multiple-files/)
- [セルに画像を挿入する](/cells/ja/cpp/inserting-an-image-into-a-cell/)
- [DBF ファイルの読み取りと書き込み](/cells/ja/cpp/dbf/)
- [Aspose.Cells for C++ でスパークラインを画像と HTML に変換する](/cells/ja/cpp/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="cpp" >}}
