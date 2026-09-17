---
title: Excel を OFD 形式に変換する
linktitle: Excel を OFD 形式に変換する
description: Aspose.Cells は、スプレッドシートファイルを扱うための C++ ライブラリであり、Excel ワークブックを OFD (Open Fixed-layout Document) 形式に変換することをサポートします。この記事では、Excel コンテンツを作成して OFD としてエクスポートする方法、および Aspose.Cells を使用して既存の Excel ファイルを OFD に変換する方法について説明します。
keywords: Aspose.Cells, C++ ライブラリ, スプレッドシート, Excel から OFD, OFD 変換, SaveFormat.Ofd, 固定レイアウトドキュメント, ワークブックのエクスポート
type: docs
weight: 195
url: /ja/cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、`SaveFormat.Ofd` 列挙値を使用して、Excel ワークブックを OFD (Open Fixed-layout Document) 形式に直接変換することをサポートします。結果として生成される OFD ドキュメントは、ワークブックの視覚的なレイアウト、コンテンツ、結合されたセル、列幅、行の高さ、フォント、色、罫線、数値形式を保持します。これにより、Aspose.Cells は固定レイアウト出力が必要なアーカイブ、印刷、規制当局への提出、政府への提出ワークフローに適しています。
{{% /alert %}}

## **Introduction**
OFD (Open Fixed-layout Document) は、固定ページベースのレイアウトでデジタルドキュメントを表現するための中国国家标准 (GB/T 33190-2016) です。ソースドキュメントの視覚的な外観が作成時とまったく同じように保持されなければならないユースケースにおいて、PDF と同様の役割を果たします。OFD は中華人民共和国において、政府への提出、規制当局への届出、電子請求書、長期アーカイブに広く採用されています。
Excel ワークブックを OFD に変換することは、スプレッドシートの内容を編集可能なスプレッドシートとしてではなく、読み取り専用でレイアウトがロックされた成果物として配布する必要があるシナリオで一般的に要求されます。例としては、完成した請求書を顧客に送付する、四半期財務報告をアーカイブする、予算スプレッドシートを規制当局に提出するといったケースが挙げられます。Aspose.Cells は `SaveFormat.Ofd` 列挙値を通じてこの要件に対応しており、中間変換ステップを必要とせずにワークブックを OFD に直接書き込みます。OFD 出力は、セル値、結合範囲、フォント、色、罫線、数値形式、ワークブックに設定されたページ設定オプションを保持します。

{{% alert color="primary" %}}
Aspose.Cells によって生成された OFD 出力は、セルコンテンツ、結合されたセル、列幅、行の高さなど、ソースワークブックの視覚的なレイアウトを保持します。フォント、色、罫線、配置、数値形式などのセル書式も固定レイアウト出力にレンダリングされます。ワークシートに設定されたページ設定オプション (用紙サイズ、向き、印刷領域など) は、結果として得られる OFD ドキュメントのレイアウトに影響します。

## **Creating an Excel Workbook and Saving as OFD**
Aspose.Cells を使用すると、プログラムによってワークブックを構築し、データを入力してから、`SaveFormat.Ofd` 列挙を使用して OFD 形式に直接保存することができます。次の例では、請求書を最初から作成します。会社ロゴ、請求先セクション、明細項目、計算された合計を追加し、ワークブックを OFD ドキュメントとしてエクスポートします。

### **Building an Invoice with a Logo**
この例では、左上領域にロゴ画像を挿入し、会社名と連絡先を入力し、結合されたセルに「INVOICE」タイトルを追加し、請求書番号と日付を記録し、請求先クライアントをリストし、説明、数量、単価、合計の各列を含む明細項目テーブルを構築し、セル数式を使用して小計、税金、総合計を計算することで、請求書ワークシートを構築します。太字のヘッダー、価格の通貨形式、罫線、列幅などの書式設定は、`Style` および `Font` オブジェクトを使用して適用されます。最後に、`SaveFormat.Ofd` を使用して、ワークブックを `.ofd` 拡張子で保存します。

```cpp
// Aspose.Cells for C++ example
// Compile with Aspose.Cells 26.6.0 (or later) and a C++17 (or later) compiler
#include "Aspose.Cells.h"
#include <string>
#include <ctime>
using namespace Aspose::Cells;
int main()
{
    // Initialize Aspose.Cells
    Aspose::Cells::Startup();
    // Directory for resources and output
    const char16_t* dataDir = u"C:\\Temp\\";
    // Create a new workbook
    Workbook workbook;
    // Obtain the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Set column widths
    cells.SetColumnWidth(0, 5.0);
    cells.SetColumnWidth(1, 35.0);
    cells.SetColumnWidth(2, 12.0);
    cells.SetColumnWidth(3, 15.0);
    cells.SetColumnWidth(4, 15.0);
    cells.SetColumnWidth(5, 5.0);
    // Insert company logo
    worksheet.GetPictures().Add(1, 1, U16String(dataDir) + u"logo.png");
    // Company name and contact details
    cells.Get(u"B3").PutValue(u"Acme Corporation");
    cells.Get(u"B4").PutValue(u"123 Business Street");
    cells.Get(u"B5").PutValue(u"City, State 12345");
    cells.Get(u"B6").PutValue(u"Phone: (555) 123-4567");
    // INVOICE title - merge cells
    cells.Merge(7, 1, 2, 4);
    Cell titleCell = cells.Get(u"B8");
    titleCell.PutValue(u"INVOICE");
    Style titleStyle = workbook.CreateStyle();
    titleStyle.GetFont().SetIsBold(true);
    titleStyle.GetFont().SetSize(20);
    titleStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    titleCell.SetStyle(titleStyle);
    // Invoice number and date
    cells.Get(u"B11").PutValue(u"Invoice Number:");
    cells.Get(u"C11").PutValue(u"INV-2024-001");
    cells.Get(u"B12").PutValue(u"Date:");
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char dateBuffer[11];
    std::strftime(dateBuffer, sizeof(dateBuffer), "%Y-%m-%d", now);
    cells.Get(u"C12").PutValue(U16String(dateBuffer));
    // Bill-to section
    cells.Get(u"B14").PutValue(u"Bill To:");
    cells.Get(u"B15").PutValue(u"Client Name");
    cells.Get(u"B16").PutValue(u"Client Address");
    cells.Get(u"B17").PutValue(u"Client City, State");
    // Line items header
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
    // Currency style with borders
    Style currencyStyle = workbook.CreateStyle();
    currencyStyle.SetCustom(u"\"$\"#,##0.00");
    currencyStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    // Plain border style for description/quantity cells
    Style borderStyle = workbook.CreateStyle();
    borderStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    // Line items rows
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
    // Subtotal, tax, grand total
    cells.Get(u"B24").PutValue(u"Subtotal:");
    Cell subtotalCell = cells.Get(u"E24");
    subtotalCell.SetFormula(u"SUM(E20:E22)");
    cells.Get(u"B25").PutValue(u"Tax (10%):");
    Cell taxCell = cells.Get(u"E25");
    taxCell.SetFormula(u"E24*0.1");
    cells.Get(u"B26").PutValue(u"Grand Total:");
    Cell grandTotalCell = cells.Get(u"E26");
    grandTotalCell.SetFormula(u"E24+E25");
    // Bold + currency style for total values
    Style totalStyle = workbook.CreateStyle();
    totalStyle.GetFont().SetIsBold(true);
    totalStyle.SetCustom(u"\"$\"#,##0.00");
    subtotalCell.SetStyle(totalStyle);
    taxCell.SetStyle(totalStyle);
    grandTotalCell.SetStyle(totalStyle);
    // Bold style for total labels
    Style boldStyle = workbook.CreateStyle();
    boldStyle.GetFont().SetIsBold(true);
    cells.Get(u"B24").SetStyle(boldStyle);
    cells.Get(u"B25").SetStyle(boldStyle);
    cells.Get(u"B26").SetStyle(boldStyle);
    // Save the workbook as an OFD file
    workbook.Save(U16String(dataDir) + u"Invoice.ofd", SaveFormat::Ofd);
    // Cleanup Aspose.Cells resources
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Converting an Existing Excel File to OFD**
Aspose.Cells は、ディスクから既存の Excel ワークブックを読み込み、それを OFD 形式に直接エクスポートすることもできます。これは、バッチ変換パイプライン、アーカイブワークフロー、ソースワークブックが別のツールで生成され、固定レイアウトの成果物として再出力するだけでよいシナリオで役立ちます。次の例では、既存の `.xlsx` ワークブックを読み込み、そのセルからデータを読み取り、オプションのページ設定調整を適用し、結果を OFD ドキュメントとして保存します。

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
    // Open an existing Excel workbook from disk
    Workbook workbook(U16String((dataDir + "SampleBook.xlsx").c_str()));
    // (1) Read and display values from selected cells to confirm the file was loaded
    Worksheet firstSheet = workbook.GetWorksheets().Get(0);
    U16String sheetName = firstSheet.GetName();
    Cell a1 = firstSheet.GetCells().Get(u"A1");
    Cell b1 = firstSheet.GetCells().Get(u"B1");
    Cell c1 = firstSheet.GetCells().Get(u"C1");
    std::cout << "First sheet name: " << sheetName.ToUtf8() << std::endl;
    std::cout << "Cell A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell B1: " << b1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell C1: " << c1.GetStringValue().ToUtf8() << std::endl;
    // (2) Iterate over the Worksheets collection to enumerate available sheets
    std::cout << "\nAvailable worksheets:" << std::endl;
    WorksheetCollection sheets = workbook.GetWorksheets();
    int sheetCount = sheets.GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet ws = sheets.Get(i);
        U16String wsName = ws.GetName();
        std::cout << "  [" << i << "] " << wsName.ToUtf8() << std::endl;
    }
    // (3) Optionally update a timestamp cell to reflect the conversion
    std::string timestamp1 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A1").PutValue(U16String(("Converted on: " + timestamp1).c_str()));
    // Append a summary header row at the top of the data block
    firstSheet.GetCells().InsertRow(0);
    firstSheet.GetCells().Get(u"A1").PutValue(u"Conversion Summary");
    std::string timestamp2 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A2").PutValue(U16String(("Generated: " + timestamp2).c_str()));
    // (4) Configure PageSetup properties on the worksheet
    PageSetup pageSetup = firstSheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    pageSetup.SetFitToPagesTall(1);
    pageSetup.SetFitToPagesWide(1);
    // (5) Optionally set the print area for the OFD output
    int lastRow = firstSheet.GetCells().GetMaxDataRow();
    int lastCol = firstSheet.GetCells().GetMaxDataColumn();
    U16String lastColLetter = CellsHelper::ColumnIndexToName(lastCol);
    std::string printArea = "A1:" + lastColLetter.ToUtf8() + std::to_string(lastRow + 1);
    firstSheet.GetPageSetup().SetPrintArea(U16String(printArea.c_str()));
    std::cout << "\nPrint area set to: " << printArea << std::endl;
    // (6) Save the workbook as an OFD file
    workbook.Save(U16String((dataDir + "SampleBook.ofd").c_str()), SaveFormat::Ofd);
    std::cout << "\nFile successfully converted to OFD format: " << dataDir << "SampleBook.ofd" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Related Articles**
- [Excel ファイルを複数のファイルに分割する](/cells/ja/cpp/splitting-excel-files-into-multiple-files/)
- [セルに画像を挿入する](/cells/ja/cpp/inserting-an-image-into-a-cell/)
- [DBF ファイルの読み取りと書き込み](/cells/ja/cpp/dbf/)
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}