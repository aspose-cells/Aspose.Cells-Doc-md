---
title: ヘッダーとフッター内のスマートマーカー | Aspose.Cells for Python via .NET
linktitle: ヘッダー・フッターのスマートマーカー | Aspose.Cells
description: Aspose.Cells for Python via .NET で、カスタム ICellsDataTable 実装または JSON データ ソースを使用し、ダブルアングルブラケット構文と WorkbookDesigner.enable_header_footer_markers スイッチでページのヘッダーおよびフッターにスマートマーカープレースホルダーを配置し、データ URI を介して画像をバインドします。
keywords: Aspose.Cells, スマートマーカー, ヘッダー, フッター, ヘッダー フッターマーカー, enable_header_footer_markers, WorkbookDesigner, PageSetup, set_header, set_footer, set_json_data_source, set_data_source, ICellsDataTable, カスタムデータテーブル, データバインディング, 画像, データ URI, Aspose.Cells for Python via .NET
type: docs
weight: 196
url: /ja/python-net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
ページのヘッダーとフッターには、レポートタイトル、報告期間、作成者、部門などのメタデータが含まれることが一般的です。これらの情報がワークブックのデータ ソースにすでに存在する場合、手動で繰り返し入力すると不要な重複が発生します。  
従来のスマートマーカー構文 `&=Source.Field` はワークシート本体のセルで処理されます。`page_setup.set_header` や `page_setup.set_footer` を使用してヘッダーやフッターに従来のマーカーを配置すると、ヘッダー/フッター文字列はセル グリッドの走査対象ではないため、文字通りのテキストとして残ります。  
**Aspose.Cells for Python via .NET 26.11** 以降、デフォルトで `False` の `workbook_designer.enable_header_footer_markers` スイッチを `True` に設定して `process()` を呼び出すと、ヘッダーとフッターの文字列内で `<<Source.Field>>` と記述されたプレースホルダーが解決されます。ヘッダーとフッターのプレースホルダーは本体マーカーと同じデータ ソースを使用します。  
各ヘッダーおよびフッターは 3 つのアドレス指定可能なセクションで構成されます。
- セクション `0` は左側セクションです。  
- セクション `1` は中央セクションです。  
- セクション `2` は右側セクションです。  
`page_setup.set_header(section, value)` と `page_setup.set_footer(section, value)` を使用して各セクションに書き込みます。処理後は `page_setup.get_header(section)` と `page_setup.get_footer(section)` で完成した文字列を取得できます。

{{% alert color="primary" %}}
`<<Source.Field>>` のようなプレースホルダーは、フィールド値をテキストとしてセクション文字列に挿入します。画像は `(picture)` サフィックスとデータ-URI 値でバインドします。
{{% /alert %}}

## **カスタム データテーブルでヘッダー/フッターマーカーを有効にする**
**Aspose.Cells for Python via .NET 26.11** でカスタム表形式データ ソースを使用してヘッダーとフッターのプレースホルダーを解決する手順は次のとおりです。
1. `Workbook` を作成し、インデックス `0` の最初の `Worksheet` を取得します。  
2. `page_setup.set_header` と `page_setup.set_footer` を使用して、目的のヘッダーおよびフッター セクションに `<<Source.Field>>` プレースホルダーを書き込みます。  
3. 小さなクラスを定義し、`ICellsDataTable` を実装して列名、行数、および `before_first()`、`next()`、`__getitem__` インデクサーを持つカーソルを提供します。プレースホルダーで使用するプレフィックスと一致するソース名を指定します。例として、ソース名 `node` は `<<node.Name>>` のようなプレースホルダーに対応します。純粋な Python クラスや辞書のリストはこのプラットフォームではバインドされません。`ICellsDataTable` 実装がカスタムオブジェクト データ ソースとなります。  
4. ワークブック用に `WorkbookDesigner` を作成します。  
5. `designer.enable_header_footer_markers` を `True` に設定してから処理を実行します。  
6. `designer.set_data_source("node", table)` でテーブルとソース名を関連付けます。  
7. `designer.process()` を呼び出します。  
8. 処理後、ヘッダーまたはフッターのテキストからプレースホルダーは除去され、完了したセクション文字列は `get_header` と `get_footer` で取得できます。

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name", "Author"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.page_setup.set_header(1, "Quarterly Report - <<node.Name>>")
worksheet.page_setup.set_footer(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
print("Footer: " + worksheet.page_setup.get_footer(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
```

## **JSON データ ソースの使用**
レポート データがすでに JSON 形式で利用可能な場合は、カスタム `ICellsDataTable` の代わりに JSON を使用できます。`workbook_designer.set_json_data_source(name, json)` を呼び出してソースを添付します。  
`name` 引数は表形式データで使用したソース名と同様の役割を果たします。例として、`node` という名前は `<<node.Company>>` や `<<node.Title>>` のプレースホルダーに対応します。  
`set_json_data_source` へ直接行データを渡します。
- 複数行オブジェクトを含む JSON 配列（例: 行オブジェクトの配列）を使用できます。  
- 単一行オブジェクトを直接渡すことも可能です。  
- `{"rows":[...]}` のように名前付きトップレベルキーでラップしないでください。このラッパーは期待される行指向の入力形状ではありません。  
1 つの JSON ソースで、同一の `process()` 呼び出し中に両方のマーカースタイルを処理できます。ワークシート本体セルの従来の `&=` マーカーとヘッダー/フッターセクションの `<<>>` プレースホルダーの両方を解決できるため、ヘッダー/フッターのプレースホルダーを解決するには `enable_header_footer_markers` を有効にしたままにする必要があります。

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.page_setup.set_header(0, "<<node.Company>>")
worksheet.page_setup.set_header(2, "Page <<node.Title>>")
worksheet.cells.get("A1").put_value("&=node.Company")
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_json_data_source(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.page_setup.get_header(0))
print("Right: " + worksheet.page_setup.get_header(2))
print("Body: " + worksheet.cells.get("A1").string_value)
# This prints:
# Left: Aspose Pty Ltd
# Right: Page Half-Year Report
# Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx")
```

## **スイッチと複数行ソースの意味**
`enable_header_footer_markers` は既定で `False` であり、ヘッダーおよびフッターの `<<Source.Field>>` プレースホルダーのみを制御します。スイッチがオフの状態でも、`process()` は従来の本体マーカー `&=` を解決しますが、ヘッダーまたはフッター内の `<<Source.Field>>` プレースホルダーは文字通りのテキストとして残ります。  
ヘッダーまたはフッターのセクションは単一の文字列であり、繰り返しバンドではありません。データ ソースに複数行が含まれる場合、最初の行がヘッダーとフッターの値を提供します。解決後、これらの値は普通のヘッダー/フッターテキストとなり、`save` 後に保存されたワークブックを再度ロードした際にも保持されます。  
以下の例は、同一の複数行表形式データソースを使用して 2 つのワークブックを作成し、スイッチが無効と有効の場合の動作を対比しています。`plain_designer` はプレースホルダーを変更せず残し、`enabled_designer` は最初の行を使用して解決します。

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
rows = [("First Row",), ("Second Row",)]
# Without the switch the placeholder stays literal text
plain_workbook = ac.Workbook()
plain_sheet = plain_workbook.worksheets[0]
plain_sheet.page_setup.set_header(1, "<<node.Name>>")
plain_designer = ac.WorkbookDesigner(plain_workbook)
plain_designer.set_data_source("node", NodeTable(rows))
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = ac.Workbook()
enabled_sheet = enabled_workbook.worksheets[0]
enabled_sheet.page_setup.set_header(1, "<<node.Name>>")
enabled_designer = ac.WorkbookDesigner(enabled_workbook)
enabled_designer.enable_header_footer_markers = True
enabled_designer.set_data_source("node", NodeTable(rows))
enabled_designer.process()
print("Without switch: " + plain_sheet.page_setup.get_header(1))
print("With switch: " + enabled_sheet.page_setup.get_header(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
```

## **ヘッダーまたはフッターに画像をバインドする**
`(picture)` サフィックスは画像をヘッダーまたはフッターのセクションにバインドします。画像を表示させたい位置に `<<node.logo(picture)>>` と記述し、フィールド値としてデータ URI を供給します。プレフィックスは `data:image/png;base64,` に続く画像バイトの Base64 テキストです。`data:` プレフィックスなしの単なる Base64 文字列では画像は埋め込まれません。  
`process()` 後の動作は次のとおりです。
1. プレースホルダーは `&G` に置換され、標準のヘッダー/フッター画像コードとなります。マーカーがセクション文字列内のコードになるため、`Logo: <<node.logo(picture)>>` のような長いテキスト中に配置可能です。  
2. 画像バイトはワークブック内のメディア パートとしてヘッダー/フッタードローイング レイヤーに添付されるため、印刷時に画像がヘッダーまたはフッターに表示されます。

```python
import aspose.cells as ac
import base64
class LogoTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["logo"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.page_setup.set_header(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    logo_data_uri = "data:image/png;base64," + base64.b64encode(image_file.read()).decode("ascii")
table = LogoTable([(logo_data_uri,)])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
```

印刷時に表示される `&G` は、Excel がヘッダーを描画する際に解釈する画像コードです。`logo.png` のバイトは `HeaderFooterPicture.xlsx` 内に格納され、コードの代わりに画像が印刷されます。  
ヘッダーとフッターのスマートマーカーを使用するには、`set_header` と `set_footer` で左・中央・右の各セクションに `<<Source.Field>>` プレースホルダーを書き込み、`WorkbookDesigner` の `enable_header_footer_markers` を `True` に設定してから `process()` を呼び出します。カスタム `ICellsDataTable` 実装を使用した `set_data_source("node", table)`、または `set_json_data_source(name, json)` で値を供給します。`get_header` と `get_footer` で完成したセクションを読み取ります。同一のデータ ソースで本文マーカーとヘッダー/フッタープレースホルダーを 1 回の処理で同時に埋め込むことができます。画像をセクションにバインドするには、データ-URI 値と共に `(picture)` サフィックスを追加します。

## 関連記事
- [SmartMarker Single Cell Array Rendering](/cells/ja/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python-net" >}}