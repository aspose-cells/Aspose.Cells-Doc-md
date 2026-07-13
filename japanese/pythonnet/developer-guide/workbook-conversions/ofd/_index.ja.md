---
title: Excel を OFD 形式に変換
linktitle: Excel を OFD 形式に変換
description: Aspose.Cells for Python via .NET は、Excel ワークブックを OFD（Open Fixed-layout Document）形式に変換することをサポートするスプレッドシート処理ライブラリです。この記事では、Excel コンテンツを作成して OFD としてエクスポートする方法、および Aspose.Cells を使用して既存の Excel ファイルを OFD に変換する方法について説明します。
keywords: Aspose.Cells, Python via .NET ライブラリ, スプレッドシート, Excel から OFD へ, OFD 変換, SaveFormat.Ofd, 固定レイアウトドキュメント, ワークブックのエクスポート
type: docs
weight: 195
url: /ja/python-net/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、`SaveFormat.Ofd` 列挙値を使用して、Excel ワークブックを OFD（Open Fixed-layout Document）形式に直接変換することをサポートしています。生成される OFD ドキュメントは、ワークブックの表示レイアウト、コンテンツ、結合セル、列幅、行の高さ、フォント、色、罫線、および数値形式を保持します。これにより、Aspose.Cells は、固定レイアウトの出力が必要なアーカイブ、印刷、規制当局への届出、政府への提出などのワークフローに適しています。

{{% /alert %}}
## **はじめに**
OFD（Open Fixed-layout Document）は、固定されたページベースのレイアウトでデジタル文書を表現するための中国の国家標準規格（GB/T 33190-2016）です。ソース文書の視覚的な外観を正確に保持する必要があるユースケースにおいて、PDF と同様の役割を果たします。OFD は中華人民共和国における政府への提出、規制当局への届出、電子請求、長期アーカイブに広く採用されています。

Excel ワークブックを OFD に変換することは、スプレッドシートの内容を編集可能なスプレッドシートとしてではなく、読み取り専用でレイアウトが固定された成果物として配布する必要があるシナリオで一般的な要件です。例としては、完成した請求書を顧客に送付する、四半期財務報告をアーカイブする、予算スプレッドシートを規制当局に提出する、といったケースが挙げられます。Aspose.Cells は、中間の変換ステップを必要とせずにワークブックを直接 OFD に書き出す `SaveFormat.Ofd` 列挙値を通じて、この要件に対応しています。OFD 出力は、セル値、結合範囲、フォント、色、罫線、数値形式、およびワークブックに設定されたページ設定オプションを保持します。

{{% alert color="primary" %}}

Aspose.Cells によって生成される OFD 出力は、ソースワークブックの表示レイアウトを保持します。これには、セルコンテンツ、結合セル、列幅、行の高さが含まれます。フォント、色、罫線、配置、数値形式などのセル書式設定も、固定レイアウト出力にレンダリングされます。用紙サイズ、向き、印刷領域など、ワークシートに設定されたページ設定オプションは、生成される OFD ドキュメントのレイアウトに影響します。

{{% /alert %}}
## **Excel ワークブックの作成と OFD としての保存**
Aspose.Cells を使用すると、ワークブックをプログラムで構築し、データを入力してから、`SaveFormat.Ofd` 列挙を使用して OFD 形式に直接保存できます。以下の例では、請求書を最初から作成します。会社のロゴ、ヘッダー情報、請求先セクション、明細項目、計算された合計を追加し、ワークブックを OFD ドキュメントとしてエクスポートします。
### **ロゴ付き請求書の作成**
この例では、ロゴ画像を上部左側の領域に挿入し、会社名と連絡先情報を入力し、結合セルをまたぐ「INVOICE」タイトルを追加し、請求書番号と日付を記録し、請求先のクライアントを記載し、説明、数量、単価、合計の各列を含む明細項目テーブルを作成し、セルの数式を使用して小計、税金、総合計を計算することで、請求書ワークシートを構築します。太字のヘッダー、価格の通貨形式、罫線、列幅などの書式設定は、`Style` および `Font` オブジェクトを使用して適用されます。最後に、ワークブックは `SaveFormat.Ofd` を使用して `.ofd` 拡張子で保存されます。

```python
from datetime import datetime

data_dir = "C:\\Temp\\"

# 新しいワークブックを作成
workbook = ac.Workbook()

# 最初のワークシートを取得
worksheet = workbook.worksheets[0]

# 列幅を設定
worksheet.cells.set_column_width(0, 5)
worksheet.cells.set_column_width(1, 35)
worksheet.cells.set_column_width(2, 12)
worksheet.cells.set_column_width(3, 15)
worksheet.cells.set_column_width(4, 15)
worksheet.cells.set_column_width(5, 5)

# 会社ロゴを挿入
worksheet.pictures.add(1, 1, data_dir + "logo.png")

# 会社名と連絡先詳細
worksheet.cells["B3"].put_value("Acme Corporation")
worksheet.cells["B4"].put_value("123 Business Street")
worksheet.cells["B5"].put_value("City, State 12345")
worksheet.cells["B6"].put_value("Phone: (555) 123-4567")

# INVOICEタイトル - セルを結合
worksheet.cells.merge(7, 1, 2, 4)
title_cell = worksheet.cells["B8"]
title_cell.put_value("INVOICE")

title_style = workbook.create_style()
title_style.font.is_bold = True
title_style.font.size = 20
title_style.horizontal_alignment = ac.TextAlignmentType.CENTER
title_cell.set_style(title_style)

# 請求書番号と日付
worksheet.cells["B11"].put_value("Invoice Number:")
worksheet.cells["C11"].put_value("INV-2024-001")
worksheet.cells["B12"].put_value("Date:")
worksheet.cells["C12"].put_value(datetime.now().strftime("%Y-%m-%d"))

# 請求先セクション
worksheet.cells["B14"].put_value("Bill To:")
worksheet.cells["B15"].put_value("Client Name")
worksheet.cells["B16"].put_value("Client Address")
worksheet.cells["B17"].put_value("Client City, State")

# 明細項目のヘッダー
header_desc = worksheet.cells["B19"]
header_qty = worksheet.cells["C19"]
header_price = worksheet.cells["D19"]
header_total = worksheet.cells["E19"]

header_desc.put_value("Description")
header_qty.put_value("Quantity")
header_price.put_value("Unit Price")
header_total.put_value("Total")

header_style = workbook.create_style()
header_style.font.is_bold = True
header_style.font.color = drawing.Color.white
header_style.background_color = drawing.Color.navy
header_style.horizontal_alignment = ac.TextAlignmentType.CENTER
header_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

header_desc.set_style(header_style)
header_qty.set_style(header_style)
header_price.set_style(header_style)
header_total.set_style(header_style)

# 罫線付き通貨スタイル
currency_style = workbook.create_style()
currency_style.custom = "\"$\"#,##0.00"
currency_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# 説明/数量セル用のシンプルな罫線スタイル
border_style = workbook.create_style()
border_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# 明細項目の行
line_items = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]

for i in range(len(line_items)):
    row = 20 + i
    desc_cell = worksheet.cells[row, 1]
    qty_cell = worksheet.cells[row, 2]
    price_cell = worksheet.cells[row, 3]
    total_cell = worksheet.cells[row, 4]

    desc_cell.put_value(line_items[i][0])
    qty_cell.put_value(line_items[i][1])
    price_cell.put_value(line_items[i][2])
    total_cell.formula = "C" + str(row) + "*D" + str(row)

    desc_cell.set_style(border_style)
    qty_cell.set_style(border_style)
    price_cell.set_style(currency_style)
    total_cell.set_style(currency_style)

# 小計、税金、合計
worksheet.cells["B24"].put_value("Subtotal:")
subtotal_cell = worksheet.cells["E24"]
subtotal_cell.formula = "SUM(E20:E22)"

worksheet.cells["B25"].put_value("Tax (10%):")
tax_cell = worksheet.cells["E25"]
tax_cell.formula = "E24*0.1"

worksheet.cells["B26"].put_value("Grand Total:")
grand_total_cell = worksheet.cells["E26"]
grand_total_cell.formula = "E24+E25"

# 合計値用の太字+通貨スタイル
total_style = workbook.create_style()
total_style.font.is_bold = True
total_style.custom = "\"$\"#,##0.00"

subtotal_cell.set_style(total_style)
tax_cell.set_style(total_style)
grand_total_cell.set_style(total_style)

# 合計ラベル用の太字スタイル
bold_style = workbook.create_style()
bold_style.font.is_bold = True

worksheet.cells["B24"].set_style(bold_style)
worksheet.cells["B25"].set_style(bold_style)
worksheet.cells["B26"].set_style(bold_style)

# ワークブックをOFDファイルとして保存
workbook.save(data_dir + "Invoice.ofd", ac.SaveFormat.Ofd)
```
## **既存の Excel ファイルを OFD に変換する**
Aspose.Cells は、ディスクから既存の Excel ワークブックを読み込み、それを OFD 形式に直接エクスポートすることもできます。これは、バッチ変換パイプライン、アーカイブワークフロー、ソースワークブックが他のツールによって作成され、固定レイアウトの成果物として再出力するだけでよいシナリオで役立ちます。以下の例では、既存の `.xlsx` ワークブックを読み込み、そのセルからデータを読み取り、オプションでページ設定を調整し、結果を OFD ドキュメントとして保存します。

```python
from datetime import datetime

dataDir = "C:\\Examples\\"

# ディスクから既存の Excel ブックを開きます
workbook = ac.Workbook(dataDir + "SampleBook.xlsx")

# (1) ファイルが読み込まれたことを確認するため、選択したセルから値を読み取って表示します
firstSheet = workbook.worksheets[0]
print("First sheet name: " + firstSheet.name)
print("Cell A1: " + firstSheet.cells["A1"].string_value)
print("Cell B1: " + firstSheet.cells["B1"].string_value)
print("Cell C1: " + firstSheet.cells["C1"].string_value)

# (2) Worksheets コレクションを反復処理して利用可能なシートを列挙します
print("\nAvailable worksheets:")
for i in range(workbook.worksheets.count):
    ws = workbook.worksheets[i]
    print("  [" + str(i) + "] " + ws.name)

# (3) 任意で変換を反映するタイムスタンプ セルを更新します
firstSheet.cells["A1"].put_value("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# データ ブロックの先頭にサマリー ヘッダー行を追加します
firstSheet.cells.insert_row(0)
firstSheet.cells["A1"].put_value("Conversion Summary")
firstSheet.cells["A2"].put_value("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# (4) ワークシートの PageSetup プロパティを設定します
pageSetup = firstSheet.page_setup
pageSetup.orientation = ac.PageOrientationType.LANDSCAPE
pageSetup.paper_size = ac.PaperSizeType.PAPER_A4
pageSetup.fit_to_pages_tall = 1
pageSetup.fit_to_pages_wide = 1

# (5) 任意で OFD 出力の印刷範囲を設定します
lastRow = firstSheet.cells.max_data_row
lastCol = firstSheet.cells.max_data_column
lastColLetter = ac.CellsHelper.column_index_to_name(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.page_setup.print_area = printArea
print("\nPrint area set to: " + printArea)

# (6) ブックを OFD ファイルとして保存します
workbook.save(dataDir + "SampleBook.ofd", ac.SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")
```

## **関連記事**
- [Excel ファイルを複数のファイルに分割する](/cells/ja/python-net/splitting-excel-files-into-multiple-files/)
- [セルへの画像の挿入](/cells/ja/python-net/inserting-an-image-into-a-cell/)
- [DBF ファイルの読み取りと書き込み](/cells/ja/python-net/dbf/)
- [Aspose.Cells for Python via .NET でスパークラインを画像と HTML に変換する](/cells/ja/python-net/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="python" >}}