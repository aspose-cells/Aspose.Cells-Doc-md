---
title: Excel を OFD 形式に変換
linktitle: Excel を OFD 形式に変換
description: Aspose.Cells for Python via Java は、スプレッドシートファイルを操作するためのライブラリであり、Excel ワークブックを OFD (Open Fixed-layout Document) 形式に変換することをサポートしています。この記事では、Excel コンテンツを作成し OFD としてエクスポートする方法、ならびに Aspose.Cells for Python via Java を使用して既存の Excel ファイルを OFD に変換する方法について説明します。
keywords: Aspose.Cells, Python via Java ライブラリ, スプレッドシート, Excel から OFD へ, OFD 変換, SaveFormat.Ofd, 固定レイアウトドキュメント, ワークブックのエクスポート
type: docs
weight: 195
url: /ja/python-java/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via Java は、`SaveFormat.Ofd` 列挙値を使用して、Excel ワークブックを OFD (Open Fixed-layout Document) 形式に直接変換することをサポートしています。生成された OFD ドキュメントは、ワークブックの表示レイアウト、内容、結合セル、列幅、行の高さ、フォント、色、罫線、および表示形式を保持します。このため、Aspose.Cells for Python via Java は、固定レイアウトの出力が必要なアーカイブ、印刷、規制当局への提出、政府への申請のワークフローに適しています。

{{% /alert %}}
## **はじめに**
OFD (Open Fixed-layout Document) は、デジタル文書を固定のページベースのレイアウトで表現するための中国国家標準 (GB/T 33190-2016) です。ソース文書の視覚的な外観を正確に保持する必要があるユースケースにおいて、PDF と同様の役割を果たします。OFD は中華人民共和国における政府への提出、規制当局への届出、電子請求書、長期アーカイブで広く採用されています。

Excel ワークブックを OFD に変換することは、スプレッドシートの内容を編集可能なスプレッドシートとしてではなく、読み取り専用でレイアウトが固定された成果物として配布する必要があるシナリオで一般的な要件です。例えば、最終化された請求書を顧客に送付する、四半期財務報告をアーカイブする、予算スプレッドシートを規制当局に提出するなどの例があります。Aspose.Cells for Python via Java は、中間の変換ステップを必要とせず、ワークブックを直接 OFD に書き出す `SaveFormat.Ofd` 列挙値によって、この要件に対応します。OFD 出力は、セル値、結合範囲、フォント、色、罫線、表示形式、およびワークブックに設定されたページ設定オプションを保持します。

{{% alert color="primary" %}}

Aspose.Cells for Python via Java によって生成された OFD 出力は、ソースワークブックの表示レイアウト (セルの内容、結合セル、列幅、行の高さなど) を保持します。フォント、色、罫線、配置、表示形式などのセル書式設定も、固定レイアウトの出力にレンダリングされます。ワークシートに設定された用紙サイズ、向き、印刷領域などのページ設定オプションは、生成される OFD ドキュメントのレイアウトに影響します。

{{% /alert %}}
## **Excel ワークブックの作成と OFD としての保存**
Aspose.Cells for Python via Java を使用すると、ワークブックをプログラムで構築し、データを入力してから、`SaveFormat.Ofd` 列挙を使用して OFD 形式に直接保存できます。次の例では、請求書をゼロから作成します。会社のロゴ、ヘッダー情報、請求先セクション、明細項目、および計算された合計を追加し、ワークブックを OFD ドキュメントとしてエクスポートします。
### **ロゴ付き請求書の作成**
この例では、ロゴ画像を左上の領域に挿入し、会社名と連絡先情報を入力し、結合セルにわたって「INVOICE」というタイトルを追加し、請求書番号と日付を記録し、請求先クライアントを記載し、説明、数量、単価、合計の列を含む明細項目の表を作成し、セルの数式を使用して小計、税、総合計を計算します。太字のヘッダー、価格の通貨形式、罫線、列幅などの書式設定は、`Style` および `Font` オブジェクトを使用して適用されます。最後に、ワークブックは `SaveFormat.Ofd` を使用して `.ofd` 拡張子で保存されます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style, Cell, TextAlignmentType, BorderType, CellBorderType, Color

dataDir = "/tmp/"

# 新しいワークブックを作成
workbook = Workbook()

# 最初のワークシートを取得
worksheet = workbook.getWorksheets().get(0)

# 列幅を設定
worksheet.getCells().setColumnWidth(0, 5)
worksheet.getCells().setColumnWidth(1, 35)
worksheet.getCells().setColumnWidth(2, 12)
worksheet.getCells().setColumnWidth(3, 15)
worksheet.getCells().setColumnWidth(4, 15)
worksheet.getCells().setColumnWidth(5, 5)

# 会社のロゴを挿入
worksheet.getPictures().add(1, 1, dataDir + "logo.png")

# 会社名と連絡先情報
worksheet.getCells().get("B3").putValue("Acme Corporation")
worksheet.getCells().get("B4").putValue("123 Business Street")
worksheet.getCells().get("B5").putValue("City, State 12345")
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567")

# INVOICEタイトル - セルを結合
worksheet.getCells().merge(7, 1, 2, 4)
titleCell = worksheet.getCells().get("B8")
titleCell.putValue("INVOICE")

titleStyle = workbook.createStyle()
titleStyle.getFont().setBold(True)
titleStyle.getFont().setSize(20)
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER)
titleCell.setStyle(titleStyle)

# 請求書番号と日付
worksheet.getCells().get("B11").putValue("Invoice Number:")
worksheet.getCells().get("C11").putValue("INV-2024-001")
worksheet.getCells().get("B12").putValue("Date:")
worksheet.getCells().get("C12").putValue(datetime.datetime.now().strftime("%Y-%m-%d"))

# 請求先セクション
worksheet.getCells().get("B14").putValue("Bill To:")
worksheet.getCells().get("B15").putValue("Client Name")
worksheet.getCells().get("B16").putValue("Client Address")
worksheet.getCells().get("B17").putValue("Client City, State")

# 明細項目のヘッダー
headerDesc = worksheet.getCells().get("B19")
headerQty = worksheet.getCells().get("C19")
headerPrice = worksheet.getCells().get("D19")
headerTotal = worksheet.getCells().get("E19")

headerDesc.putValue("Description")
headerQty.putValue("Quantity")
headerPrice.putValue("Unit Price")
headerTotal.putValue("Total")

headerStyle = workbook.createStyle()
headerStyle.getFont().setBold(True)
headerStyle.getFont().setColor(Color.getWhite())
headerStyle.setBackgroundColor(Color.getNavy())
headerStyle.setHorizontalAlignment(TextAlignmentType.CENTER)
headerStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

headerDesc.setStyle(headerStyle)
headerQty.setStyle(headerStyle)
headerPrice.setStyle(headerStyle)
headerTotal.setStyle(headerStyle)

# 罫線付きの通貨スタイル
currencyStyle = workbook.createStyle()
currencyStyle.setCustom("\"$\"#,##0.00")
currencyStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# 説明/数量セル用のシンプルな罫線スタイル
borderStyle = workbook.createStyle()
borderStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# 明細項目の行
lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]

for i in range(len(lineItems)):
    row = 20 + i
    descCell = worksheet.getCells().get(row, 1)
    qtyCell = worksheet.getCells().get(row, 2)
    priceCell = worksheet.getCells().get(row, 3)
    totalCell = worksheet.getCells().get(row, 4)

    descCell.putValue(lineItems[i][0])
    qtyCell.putValue(lineItems[i][1])
    priceCell.putValue(lineItems[i][2])
    totalCell.setFormula("C" + str(row) + "*D" + str(row))

    descCell.setStyle(borderStyle)
    qtyCell.setStyle(borderStyle)
    priceCell.setStyle(currencyStyle)
    totalCell.setStyle(currencyStyle)

# 小計、税、総合計
worksheet.getCells().get("B24").putValue("Subtotal:")
subtotalCell = worksheet.getCells().get("E24")
subtotalCell.setFormula("SUM(E20:E22)")

worksheet.getCells().get("B25").putValue("Tax (10%):")
taxCell = worksheet.getCells().get("E25")
taxCell.setFormula("E24*0.1")

worksheet.getCells().get("B26").putValue("Grand Total:")
grandTotalCell = worksheet.getCells().get("E26")
grandTotalCell.setFormula("E24+E25")

# 合計値用の太字+通貨スタイル
totalStyle = workbook.createStyle()
totalStyle.getFont().setBold(True)
totalStyle.setCustom("\"$\"#,##0.00")

subtotalCell.setStyle(totalStyle)
taxCell.setStyle(totalStyle)
grandTotalCell.setStyle(totalStyle)

# 合計ラベル用の太字スタイル
boldStyle = workbook.createStyle()
boldStyle.getFont().setBold(True)

worksheet.getCells().get("B24").setStyle(boldStyle)
worksheet.getCells().get("B25").setStyle(boldStyle)
worksheet.getCells().get("B26").setStyle(boldStyle)

# ワークブックをOFDファイルとして保存
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd)

jpype.shutdownJVM()
```
## **既存の Excel ファイルを OFD に変換する**
Aspose.Cells for Python via Java は、ディスクから既存の Excel ワークブックを読み込み、OFD 形式に直接エクスポートすることもできます。これは、バッチ変換パイプライン、アーカイブワークフロー、ソースワークブックが別のツールで作成され、固定レイアウトの成果物として再発行するだけでよいシナリオで役立ちます。次の例では、既存の `.xlsx` ワークブックを読み込み、そのセルからデータを読み取り、オプションのページ設定調整を適用し、結果を OFD ドキュメントとして保存します。

```python
from datetime import datetime
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PageOrientationType, PaperSizeType, CellsHelper

dataDir = "C:\\Examples\\"

# ディスクから既存の Excel ブックを開きます
workbook = Workbook(dataDir + "SampleBook.xlsx")

# (1) ファイルが読み込まれたことを確認するために、選択したセルから値を読み取って表示します
firstSheet = workbook.getWorksheets().get(0)
print("First sheet name: " + firstSheet.getName())
print("Cell A1: " + firstSheet.getCells().get("A1").getStringValue())
print("Cell B1: " + firstSheet.getCells().get("B1").getStringValue())
print("Cell C1: " + firstSheet.getCells().get("C1").getStringValue())

# (2) Worksheets コレクションを反復処理して利用可能なシートを列挙します
print("\nAvailable worksheets:")
for i in range(workbook.getWorksheets().getCount()):
    ws = workbook.getWorksheets().get(i)
    print("  [" + str(i) + "] " + ws.getName())

# (3) 必要に応じて、変換を反映するタイムスタンプセルを更新します
firstSheet.getCells().get("A1").putValue("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# データブロックの先頭にサマリーヘッダー行を追加します
firstSheet.getCells().insertRow(0)
firstSheet.getCells().get("A1").putValue("Conversion Summary")
firstSheet.getCells().get("A2").putValue("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# (4) ワークシートの PageSetup プロパティを設定します
pageSetup = firstSheet.getPageSetup()
pageSetup.setOrientation(PageOrientationType.LANDSCAPE)
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4)
pageSetup.setFitToPagesTall(1)
pageSetup.setFitToPagesWide(1)

# (5) 必要に応じて、OFD 出力の印刷範囲を設定します
lastRow = firstSheet.getCells().getMaxDataRow()
lastCol = firstSheet.getCells().getMaxDataColumn()
lastColLetter = CellsHelper.columnIndexToName(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.getPageSetup().setPrintArea(printArea)
print("\nPrint area set to: " + printArea)

# (6) ブックを OFD ファイルとして保存します
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")

jpype.shutdownJVM()
```

## **関連記事**
- [Excel ファイルを複数のファイルに分割する](/cells/ja/python-java/splitting-excel-files-into-multiple-files/)
- [セルへの画像の挿入](/cells/ja/python-java/inserting-an-image-into-a-cell/)
- [DBF ファイルの読み取りと書き込み](/cells/ja/python-java/dbf/)
- [Aspose.Cells for Python via Java でスパークラインを画像と HTML に変換する](/cells/ja/python-java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="python" >}}