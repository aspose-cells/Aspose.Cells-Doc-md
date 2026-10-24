---
title: Excel を OFD 形式に変換する
linktitle: Excel を OFD 形式に変換する
description: Aspose.Cells for Python via .NET は、Excel ワークブックを OFD (Open Fixed-layout Document) 形式に変換できるスプレッドシート処理ライブラリです。このبيضでは、Excel の内容を作成して OFD としてエクスポートする方法と、Aspose.Cells を使用して既存の Excel ファイルを OFD に変換する方法について説明します。
keywords: Aspose.Cells, Python via .NET ライブラリ, スプレッドシート, Excel から OFD, OFD 変換, SaveFormat.OFD, 固定レイアウトドキュメント, ワークブックのエクスポート
type: docs
weight: 195
url: /ja/python-net/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、`SaveFormat.OFD` 列挙型の値を使用して、Excel ワークブックを OFD (Open Fixed-layout Document) 形式に直接変換できます。生成される OFD ドキュメントは、ワークブックの表示レイアウト、内容、結合セル、列幅、行の高さ、フォント、色、罫線、数値形式を保持します。これにより、Aspose.Cells は、長期保存、印刷、規制当局への申請、政府機関への提出など、固定レイアウトの出力が必要なワークフローに適しています。
{{% /alert %}}

## **はじめに**
OFD (Open Fixed-layout Document) は、デジタルドキュメントを固定されたページ単位のレイアウトで表現するための中国国家标准 (GB/T 33190-2016) です。作成時の視覚的な外観をそのまま保持する必要がある用途では、PDF 类似于役割を果たします。OFD は、中華人民共和国において、政府機関への提出、規制当局への申請、電子請求書、長期保存のために広く採用されています。
Excel ワークブックを OFD に変換することは、スプレッドシートの内容を編集可能なスプレッドシートとしてではなく、読み取り専用でレイアウトが固定された成果物として配布する必要があるシナリオで一般的な要件です。例としては、確定した請求書を顧客に送信したり、四半期ごとの財務報告書をアーカイブしたり、予算スプレッドシートを規制当局に提出したりすることが挙げられます。Aspose.Cells は、中間変換ステップを必要とせずにワークブックを直接 OFD に書き込む `SaveFormat.OFD` 列挙型の値を通じてこの要件に対応します。OFD 出力は、セル値、結合範囲、フォント、色、罫線、数値形式、およびワークブックに設定されたページ設定を保持します。

{{% alert color="primary" %}}
Aspose.Cells で生成される OFD 出力は、セルの内容、結合セル、列幅、行の高さなど、ソースワークブックの表示レイアウトを保持します。フォント、色、罫線、配置、数値形式などのセル書式設定も、固定レイアウトの出力に反映されます。用紙のサイズ、印刷の向き、印刷範囲など、ワークシートに設定したページ設定は、生成される OFD ドキュメントのレイアウトに影響します。
{{% /alert %}}

## **Excel ワークブックを作成して OFD 形式で保存する**
Aspose.Cells を使用すると、プログラムで Excel ワークブックを作成し、データを入力してから、`SaveFormat.OFD` 列挙型の値を使用して OFD 形式に直接保存できます。次の例では、請求書を新規作成します。会社のロゴ、ヘッダー情報、請求先情報、明細項目、計算した合計を追加し、ワークブックを OFD ドキュメントとしてエクスポートします。

### **ロゴを含む請求書の作成**
この例では、左上の領域にロゴ画像を挿入し、会社名と連絡先を入力し、結合セルに「INVOICE」タイトルを追加し、請求書番号と日付を記録し、請求先の顧客情報を入力し、説明、数量、単価、合計列を含む明細項目テーブルを作成し、セル数式を使用して小計、税、総合計を計算することで、請求書ワークシートを構築します。太字のヘッダー、価格に適用する通貨形式、罫線、列幅などの書式設定は、`Style` および `Font` オブジェクトを使用して適用します。最後に、`SaveFormat.OFD` を使用して、ワークブックを `.ofd` 拡張子で保存します。

```python
import aspose.cells as ac
from datetime import datetime
data_dir = "C:\\Temp\\"
# 新しいワークブックを作成
workbook = ac.Workbook()
# 最初のワークシートを取得
worksheet = workbook.worksheets[0]
# 列幅を設定
worksheet.cells.set_column_width(0, 5.0)
worksheet.cells.set_column_width(1, 35.0)
worksheet.cells.set_column_width(2, 12.0)
worksheet.cells.set_column_width(3, 15.0)
worksheet.cells.set_column_width(4, 15.0)
worksheet.cells.set_column_width(5, 5.0)
# 会社のロゴを挿入
worksheet.pictures.add(1, 1, data_dir + "logo.png")
# 会社名と連絡先の詳細
worksheet.cells.get("B3").put_value("Acme Corporation")
worksheet.cells.get("B4").put_value("123 Business Street")
worksheet.cells.get("B5").put_value("City, State 12345")
worksheet.cells.get("B6").put_value("Phone: (555) 123-4567")
# INVOICEタイトル - セルを結合
worksheet.cells.merge(7, 1, 2, 4)
title_cell = worksheet.cells.get("B8")
title_cell.put_value("INVOICE")
title_style = workbook.create_style()
title_style.font.is_bold = True
title_style.font.size = 20
title_style.horizontal_alignment = ac.TextAlignmentType.CENTER
title_cell.set_style(title_style)
# 請求書番号と日付
worksheet.cells.get("B11").put_value("Invoice Number:")
worksheet.cells.get("C11").put_value("INV-2024-001")
worksheet.cells.get("B12").put_value("Date:")
worksheet.cells.get("C12").put_value(datetime.now().strftime("%Y-%m-%d"))
# 請求先セクション
worksheet.cells.get("B14").put_value("Bill To:")
worksheet.cells.get("B15").put_value("Client Name")
worksheet.cells.get("B16").put_value("Client Address")
worksheet.cells.get("B17").put_value("Client City, State")
# 明细项目的ヘッダー
header_desc = worksheet.cells.get("B19")
header_qty = worksheet.cells.get("C19")
header_price = worksheet.cells.get("D19")
header_total = worksheet.cells.get("E19")
header_desc.put_value("Description")
header_qty.put_value("Quantity")
header_price.put_value("Unit Price")
header_total.put_value("Total")
header_style = workbook.create_style()
header_style.font.is_bold = True
header_style.font.color = drawing.Color.white
header_style.background_color = drawing.Color.navy
header_style.horizontal_alignment = ac.TextAlignmentType.CENTER
header_style.borders.get(ac.BorderType.TOP_BORDER).line_style = ac.CellBorderType.THIN
header_style.borders.get(ac.BorderType.BOTTOM_BORDER).line_style = ac.CellBorderType.THIN
header_style.borders.get(ac.BorderType.LEFT_BORDER).line_style = ac.CellBorderType.THIN
header_style.borders.get(ac.BorderType.RIGHT_BORDER).line_style = ac.CellBorderType.THIN
header_desc.set_style(header_style)
header_qty.set_style(header_style)
header_price.set_style(header_style)
header_total.set_style(header_style)
# 罫線付き通貨スタイル
currency_style = workbook.create_style()
currency_style.custom = "\"$\"#,##0.00"
currency_style.borders.get(ac.BorderType.TOP_BORDER).line_style = ac.CellBorderType.THIN
currency_style.borders.get(ac.BorderType.BOTTOM_BORDER).line_style = ac.CellBorderType.THIN
currency_style.borders.get(ac.BorderType.LEFT_BORDER).line_style = ac.CellBorderType.THIN
currency_style.borders.get(ac.BorderType.RIGHT_BORDER).line_style = ac.CellBorderType.THIN
# 説明文および数量セル用の基本罫線スタイル
border_style = workbook.create_style()
border_style.borders.get(ac.BorderType.TOP_BORDER).line_style = ac.CellBorderType.THIN
border_style.borders.get(ac.BorderType.BOTTOM_BORDER).line_style = ac.CellBorderType.THIN
border_style.borders.get(ac.BorderType.LEFT_BORDER).line_style = ac.CellBorderType.THIN
border_style.borders.get(ac.BorderType.RIGHT_BORDER).line_style = ac.CellBorderType.THIN
# 明細行
line_items = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]
for i in range(len(line_items)):
    row = 20 + i
    desc_cell = worksheet.cells.get(row, 1)
    qty_cell = worksheet.cells.get(row, 2)
    price_cell = worksheet.cells.get(row, 3)
    total_cell = worksheet.cells.get(row, 4)
    desc_cell.put_value(line_items[i][0])
    qty_cell.put_value(line_items[i][1])
    price_cell.put_value(line_items[i][2])
    total_cell.formula = "C" + str(row) + "*D" + str(row)
    desc_cell.set_style(border_style)
    qty_cell.set_style(border_style)
    price_cell.set_style(currency_style)
    total_cell.set_style(currency_style)
# 小計、税金、合計
worksheet.cells.get("B24").put_value("Subtotal:")
subtotal_cell = worksheet.cells.get("E24")
subtotal_cell.formula = "SUM(E20:E22)"
worksheet.cells.get("B25").put_value("Tax (10%):")
tax_cell = worksheet.cells.get("E25")
tax_cell.formula = "E24*0.1"
worksheet.cells.get("B26").put_value("Grand Total:")
grand_total_cell = worksheet.cells.get("E26")
grand_total_cell.formula = "E24+E25"
# 合計値用の太字＋通貨スタイル
total_style = workbook.create_style()
total_style.font.is_bold = True
total_style.custom = "\"$\"#,##0.00"
subtotal_cell.set_style(total_style)
tax_cell.set_style(total_style)
grand_total_cell.set_style(total_style)
# 合計ラベルの太字スタイル
bold_style = workbook.create_style()
bold_style.font.is_bold = True
worksheet.cells.get("B24").set_style(bold_style)
worksheet.cells.get("B25").set_style(bold_style)
worksheet.cells.get("B26").set_style(bold_style)
# ワークブックをOFDファイルとして保存
workbook.save(data_dir + "Invoice.ofd", ac.SaveFormat.OFD)
```

## **既存の Excel ファイルを OFD に変換する**
Aspose.Cells は、ディスクから既存の Excel ワークブックを読み込み、OFD 形式に直接エクスポートすることもできます。これは、バッチ変換パイプライン、アーカイブワークフロー、および別のツールで作成されたソースワークブックを固定レイアウトの成果物として再出力するだけでよいシナリオで役立ちます。次の例では、既存の `.xlsx` ワークブックを読み込み、そのセルからデータを読み取り、必要に応じてページ設定を調整し、変換結果を OFD ドキュメントとして保存します。

```python
import aspose.cells as ac
from datetime import datetime
dataDir = "C:\\Examples\\"
# ディスクから既存の Excel ブックを開く
workbook = ac.Workbook(dataDir + "SampleBook.xlsx")
# (1) 選択したセルの値を読み取り、ファイルが正しく読み込まれたことを確認する
firstSheet = workbook.worksheets[0]
print("First sheet name: " + firstSheet.name)
print("Cell A1: " + firstSheet.cells.get("A1").string_value)
print("Cell B1: " + firstSheet.cells.get("B1").string_value)
print("Cell C1: " + firstSheet.cells.get("C1").string_value)
# (2) Worksheets コレクションを反復処理して、利用可能なシートを列挙する
print("\nAvailable worksheets:")
for i in range(len(workbook.worksheets)):
    ws = workbook.worksheets[i]
    print("  [" + str(i) + "] " + ws.name)
# (3) 必要に応じて、変換日時を反映させるためにタイムスタンプのセルを更新する
firstSheet.cells.get("A1").put_value("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# データブロックの先頭にサマリー見出し行を追加する
firstSheet.cells.insert_row(0)
firstSheet.cells.get("A1").put_value("Conversion Summary")
firstSheet.cells.get("A2").put_value("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# (4) ワークシートの PageSetup プロパティを構成する
pageSetup = firstSheet.page_setup
pageSetup.orientation = ac.PageOrientationType.LANDSCAPE
pageSetup.paper_size = ac.PaperSizeType.PAPER_A4
pageSetup.fit_to_pages_tall = 1
pageSetup.fit_to_pages_wide = 1
# (5) 必要に応じて、OFD 出力の印刷範囲を設定する
lastRow = firstSheet.cells.max_data_row
lastCol = firstSheet.cells.max_data_column
lastColLetter = ac.CellsHelper.column_index_to_name(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.page_setup.print_area = printArea
print("\nPrint area set to: " + printArea)
# (6) ブックを OFD ファイルとして保存する
workbook.save(dataDir + "SampleBook.ofd", ac.SaveFormat.OFD)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")
```

## **関連記事**
- [Excel ファイルを複数のファイルに分割する](/cells/ja/python-net/splitting-excel-files-into-multiple-files/)
- [セルに画像を挿入する](/cells/ja/python-net/inserting-an-image-into-a-cell/)
- [DBF ファイルの読み取りと書き込み](/cells/ja/python-net/dbf/)

{{< app/cells/assistant language="python-net" >}}