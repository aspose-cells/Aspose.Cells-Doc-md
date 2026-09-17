---
title: ExcelをOFD形式に変換
description: Aspose.Cells for Python via .NETは、ExcelワークブックをOFD (Open Fixed-layout Document)形式に変換することをサポートするスプレッドシート処理ライブラリです。本記事では、Excelコンテンツを作成してOFDとしてエクスポートする方法、およびAspose.Cellsを使用して既存のExcelファイルをOFDに変換する方法について説明します。
linktitle: OFD
keywords: Aspose.Cells, Python via .NET ライブラリ, スプレッドシート, ExcelからOFD, OFD変換, SaveFormat.Ofd, 固定レイアウトドキュメント, ワークブックエクスポート
type: docs
weight: 195
url: /ja/python-net/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cellsは、`SaveFormat.Ofd`列挙値を使用して、Excelワークブックを直接OFD (Open Fixed-layout Document)形式に変換することをサポートします。生成されたOFDドキュメントは、ワークブックの表示レイアウト、内容、結合セル、列幅、行の高さ、フォント、色、罫線、および数値形式を保持します。これにより、Aspose.Cellsは固定レイアウトの出力を必要とするアーカイブ、印刷、規制当局への提出、政府への提出のワークフローに適しています。
{{% /alert %}}

## **Introduction**
OFD (Open Fixed-layout Document)は、デジタル文書を固定されたページベースのレイアウトで表現するための中国国家標準 (GB/T 33190-2016)です。これは、ソース文書の視覚的な外観が作成されたとおりに正確に保持されなければならないユースケースにおいて、PDFと同様の役割を果たします。OFDは中華人民共和国において、政府への提出、規制当局への届出、電子請求書、長期アーカイブに広く採用されています。
ExcelワークブックをOFDに変換することは、スプレッドシートの内容が編集可能なスプレッドシートではなく、読み取り専用かつレイアウトが固定された成果物として配布されなければならないシナリオで一般的な要件です。例としては、完成した請求書を顧客に送付すること、四半期財務報告書をアーカイブすること、予算スプレッドシートを規制当局に提出することが挙げられます。Aspose.Cellsは、`SaveFormat.Ofd`列挙値を通じてこの要件に対応しており、中間変換ステップを必要とせずにワークブックを直接OFDに書き込みます。OFD出力は、セル値、結合範囲、フォント、色、罫線、数値形式、およびワークブックに設定されたページ設定オプションを保持します。

{{% alert color="primary" %}}
Aspose.Cellsによって生成されたOFD出力は、セルの内容、結合セル、列幅、行の高さを含むソースワークブックの表示レイアウトを保持します。フォント、色、罫線、配置、数値形式などのセル書式も固定レイアウト出力にレンダリングされます。用紙サイズ、印刷の向き、印刷領域など、ワークシートに設定されたページ設定オプションは、生成されるOFDドキュメントのレイアウトに影響します。

## **Creating an Excel Workbook and Saving as OFD**
Aspose.Cellsを使用すると、プログラムによってワークブックを作成し、データを入力してから、`SaveFormat.Ofd`列挙を使用してOFD形式に直接保存できます。次の例では、ゼロから請求書を作成します。会社のロゴ、ヘッダー情報、請求先セクション、明細項目、および計算された合計を追加し、ワークブックをOFDドキュメントにエクスポートします。

### **Building an Invoice with a Logo**
この例では、ロゴ画像を左上の領域に挿入し、会社名と連絡先詳細を入力し、結合セルに「INVOICE」タイトルを追加し、請求書番号と日付を記録し、請求先クライアントを列挙し、説明、数量、単価、合計列を持つ明細項目テーブルを構築し、セルの数式を使用して小計、税金、および総計を計算することで、請求書ワークシートを作成します。太字のヘッダー、価格の通貨形式、罫線、列幅などの書式設定は、`Style`および`Font`オブジェクトを使用して適用されます。最後に、ワークブックは`SaveFormat.Ofd`を使用して`.ofd`拡張子で保存されます。

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
# 会社名と連絡先情報
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
# 説明/数量セル用の罫線スタイル
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
# 小計、税、合計
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

## **Converting an Existing Excel File to OFD**
Aspose.Cellsは、ディスクから既存のExcelワークブックを読み込み、OFD形式に直接エクスポートすることもできます。これは、バッチ変換パイプライン、アーカイブワークフロー、およびソースワークブックが別のツールによって生成され、固定レイアウトの成果物として再発行されるだけでよいシナリオで役立ちます。次の例では、既存の`.xlsx`ワークブックを読み込み、そのセルからデータを読み取り、オプションのページ設定調整を適用し、結果をOFDドキュメントとして保存します。

```python
from datetime import datetime
dataDir = "C:\\Examples\\"
# ディスクから既存のExcelブックを開きます
workbook = ac.Workbook(dataDir + "SampleBook.xlsx")
# (1) ファイルが読み込まれたことを確認するために、選択したセルから値を読み取って表示します
firstSheet = workbook.worksheets[0]
print("First sheet name: " + firstSheet.name)
print("Cell A1: " + firstSheet.cells["A1"].string_value)
print("Cell B1: " + firstSheet.cells["B1"].string_value)
print("Cell C1: " + firstSheet.cells["C1"].string_value)
# (2) Worksheetsコレクションを反復処理して利用可能なシートを列挙します
print("\nAvailable worksheets:")
for i in range(workbook.worksheets.count):
    ws = workbook.worksheets[i]
    print("  [" + str(i) + "] " + ws.name)
# (3) オプションで変換を反映するようにタイムスタンプセルを更新します
firstSheet.cells["A1"].put_value("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# データブロックの先頭にサマリーヘッダー行を追加します
firstSheet.cells.insert_row(0)
firstSheet.cells["A1"].put_value("Conversion Summary")
firstSheet.cells["A2"].put_value("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# (4) ワークシートにPageSetupプロパティを設定します
pageSetup = firstSheet.page_setup
pageSetup.orientation = ac.PageOrientationType.LANDSCAPE
pageSetup.paper_size = ac.PaperSizeType.PAPER_A4
pageSetup.fit_to_pages_tall = 1
pageSetup.fit_to_pages_wide = 1
# (5) オプションでOFD出力の印刷範囲を設定します
lastRow = firstSheet.cells.max_data_row
lastCol = firstSheet.cells.max_data_column
lastColLetter = ac.CellsHelper.column_index_to_name(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.page_setup.print_area = printArea
print("\nPrint area set to: " + printArea)
# (6) ワークブックをOFDファイルとして保存します
workbook.save(dataDir + "SampleBook.ofd", ac.SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")
```

## **Related Articles**
- [Splitting Excel Files into Multiple Files](/cells/ja/python-net/splitting-excel-files-into-multiple-files/)
- [Inserting an Image into a Cell](/cells/ja/python-net/inserting-an-image-into-a-cell/)
- [Reading and Writing DBF Files](/cells/ja/python-net/dbf/)
{{% /alert %}}

{{< app/cells/assistant language="python" >}}