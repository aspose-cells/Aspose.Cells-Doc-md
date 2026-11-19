---
title: ヘッダーとフッターのスマートマーカー | Aspose.Cells for Python via Java
linktitle: ヘッダー・フッターのスマートマーカー | Aspose.Cells
description: ダブル角括弧構文と WorkbookDesigner.setEnableHeaderFooterMarkers スイッチを使用して、表形式の行または JSON データ ソースからページヘッダーとフッターに Smart Marker プレースホルダーを配置し、データ URI で画像をバインドできます。Aspose.Cells for Python via Java。
keywords: Aspose.Cells, Aspose.Cells for Python via Java, スマートマーカー, ヘッダー, フッター, ヘッダー フッターマーカー, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, ICellsDataTable, カスタム データテーブル, データ バインディング, 画像, データ URI, Python via Java
type: docs
weight: 196
url: /ja/python-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
ページのヘッダーやフッターには、レポートのタイトル、期間、作成者、部門などのメタデータが含まれることが一般的です。この情報がワークブックにデータを投入する際に使用するデータ ソースにすでに存在している場合、手動で繰り返し入力すると不必要な重複が生じます。  
従来のスマートマーカー構文 `&=Source.Field` はワークシート本体のセルで処理されます。`PageSetup.setHeader` または `PageSetup.setFooter` を使用してヘッダーやフッターに従来のマーカーを配置した場合、`WorkbookDesigner.process()` が走査するワークシートのセル グリッドの一部ではないため、文字列はそのままリテラルテキストとして残ります。  
**Aspose.Cells for Python via Java 26.11** 以降、デフォルトで `False` の `WorkbookDesigner.setEnableHeaderFooterMarkers` スイッチを `True` に設定して `process()` を呼び出すと、ヘッダーおよびフッターのセクション文字列に記述された `<<Source.Field>>` プレースホルダーが解決されます。ヘッダーとフッターのプレースホルダーは本体のマーカーと同じデータ ソースを使用します。  
各ヘッダーとフッターにはアドレス指定可能な 3 つのセクションがあります:
- セクション `0` は左側セクションです。
- セクション `1` は中央セクションです。
- セクション `2` は右側セクションです。
`PageSetup.setHeader(int section, str value)` と `PageSetup.setFooter(int section, str value)` を使用してこれらのセクションに文字列を書き込みます。処理後は `PageSetup.getHeader(int section)` と `PageSetup.getFooter(int section)` で完成したテキストを取得できます。

{{% alert color="primary" %}}
`<<Source.Field>>` のようなプレースホルダーはフィールドの値をテキストとしてセクション文字列に挿入します。画像は `(picture)` サフィックスとデータ URI の値でバインドされます。
{{% /alert %}}

## **カスタム データテーブルでヘッダー/フッターマーカーを有効にする**
**Aspose.Cells for Python via Java 26.11** でカスタム表形式データ ソースを使用してヘッダーとフッターのプレースホルダーを解決する手順は次のとおりです。
1. `Workbook` を作成し、`workbook.getWorksheets().get(0)` を使用してインデックス `0` の最初の `Worksheet` を取得します。
2. `worksheet.getPageSetup().setHeader(section, value)` および `worksheet.getPageSetup().setFooter(section, value)` を使用して、目的のヘッダーおよびフッター セクションに `<<Source.Field>>` プレースホルダーを書き込みます。
3. `ICellsDataTable` を実装する小さなクラスを定義し、列名、行数、および `beforeFirst()`, `next()`, `get()` を持つカーソルで表形式の行データを提供します。そして、プレースホルダーで使用されるプレフィックスと一致するソース名を使用します。例として、`node` というソース名は `<<node.Name>>` のようなプレースホルダーに対応します。単純な Python クラスや辞書のリストはこのプラットフォームではバインドされません。`ICellsDataTable` の実装がカスタムオブジェクト データソースとなります。
4. ワークブック用に `WorkbookDesigner` を作成します。
5. 処理前に `designer.setEnableHeaderFooterMarkers(True)` を呼び出します。
6. `designer.setDataSource("node", table)` でテーブルとソース名を紐付けます。
7. `designer.process()` を呼び出します。
8. 処理後、プレースホルダーはヘッダーやフッターのテキストから削除されます。完了したセクション文字列は `worksheet.getPageSetup().getHeader(section)` および `worksheet.getPageSetup().getFooter(section)` で取得できます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name", "Author"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>")
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
print("Footer: " + worksheet.getPageSetup().getFooter(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
jpype.shutdownJVM()
```

## **JSON データ ソースを使用する**
レポート データがすでに JSON 形式で利用可能な場合、カスタム `ICellsDataTable` の代わりに JSON を使用できます。`designer.setJsonDataSource(name, json)` を呼び出してソースを紐付けます。  
`name` 引数は表形式データで使用したソース名と同じ役割を持ちます。例として、`node` という名前は `<<node.Company>>` や `<<node.Title>>` のプレースホルダーに対応します。  
`setJsonDataSource` に行データを直接渡します:
- 行の配列（1 つまたは複数の行オブジェクトを含む JSON 配列）をサポートします。
- 単一の行オブジェクトも直接渡すことができます。
- `{"rows":[...]}` のように名前付きトップレベルキーで行をラップしないでください。このラッパーはこのワークフローが期待する行指向の入力形式ではありません。  
1 回の `process()` 呼び出しで同じ JSON ソースが両方のマーカー形式を生成できます。ワークシート本体セルの従来 `&=` マーカーとヘッダー/フッターの `<<>>` プレースホルダーの両方を解決できますが、ヘッダーとフッターのプレースホルダーを解決するには依然として `setEnableHeaderFooterMarkers` を有効にする必要があります。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>")
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>")
worksheet.getCells().get("A1").putValue("&=node.Company")
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setJsonDataSource(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.getPageSetup().getHeader(0))
print("Right: " + worksheet.getPageSetup().getHeader(2))
print("Body: " + worksheet.getCells().get("A1").getStringValue())
workbook.save("HeaderFooterJsonMarkers.xlsx")
jpype.shutdownJVM()
```

## **スイッチとマルチ行データ ソースのセマンティクス**
ヘッダーとフッターマーカーの設定はデフォルトで `False` です。`designer.setEnableHeaderFooterMarkers(True)` はヘッダーとフッターの `<<Source.Field>>` プレースホルダーのみを制御します。スイッチがオフのときは、`process()` は従来の `&=` 本体マーカーは解決しますが、ヘッダーまたはフッターの `<<Source.Field>>` プレースホルダーはリテラルテキストのままです。  
ヘッダーまたはフッターのセクションは 1 つの文字列であり、繰り返し帯ではありません。データ ソースに複数行が含まれている場合、最初の行がヘッダーとフッターの値を提供します。解決後、これらの値は通常のヘッダーまたはフッターテキストとなり、`workbook.save(...)` 後にワークブックに残り、保存されたワークブックを再度ロードしたときにも存在します。  
以下の例では、同じ複数行の表形式データ ソースを使用して 2 つのワークブックを作成し、マーカーが無効の場合と有効の場合の動作を比較します。`plainDesigner` はプレースホルダーを変更せずに残し、`enabledDesigner` は最初の行を使用してプレースホルダーを解決します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
table = NodeTable([
    ("First Row",),
    ("Second Row",),
])
# Without the switch the placeholder stays literal text
plain_workbook = Workbook()
plain_sheet = plain_workbook.getWorksheets().get(0)
plain_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
plain_designer = WorkbookDesigner(plain_workbook)
plain_designer.setDataSource("node", table)
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = Workbook()
enabled_sheet = enabled_workbook.getWorksheets().get(0)
enabled_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
enabled_designer = WorkbookDesigner(enabled_workbook)
enabled_designer.setEnableHeaderFooterMarkers(True)
enabled_designer.setDataSource("node", table)
enabled_designer.process()
print("Without switch: " + plain_sheet.getPageSetup().getHeader(1))
print("With switch: " + enabled_sheet.getPageSetup().getHeader(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
jpype.shutdownJVM()
```

## **ヘッダーまたはフッターに画像をバインドする**
`(picture)` サフィックスは画像をヘッダーまたはフッターのセクションにバインドします。画像を表示したい場所に `<<node.logo(picture)>>` と記述し、フィールド値としてデータ URI を提供します。プレフィックスは `data:image/png;base64,` で、続くのは画像バイトの Base64 テキストです。デコードされた画像は `byte[]` 配列として扱われます。`data:` プレフィックスなしの純粋な Base64 文字列だけでは画像は埋め込まれません。  
`process()` 後:
1. プレースホルダーは `&G` に置き換えられます。これはヘッダーおよびフッターの標準画像コードです。マーカーがセクション文字列内のコードになるため、`Logo: <<node.logo(picture)>>` のような長いテキストの中に配置できます。
2. 画像バイトはワークブック内のメディアパートとして埋め込まれ、該当シートのヘッダー/フッタードローイング層に添付されるため、印刷時にヘッダーやフッターとともに画像が出力されます。

```python
import base64
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["logo"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    image_bytes = image_file.read()
logo_data = "data:image/png;base64," + base64.b64encode(image_bytes).decode("ascii")
table = NodeTable([(logo_data,)])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
jpype.shutdownJVM()
```

印刷時に表示される `&G` は、Excel がヘッダーをレンダリングする際に解釈する画像コードです。`logo.png` のバイトが `HeaderFooterPicture.xlsx` に格納され、コードの代わりに画像が印刷されます。  
ヘッダーとフッターのスマートマーカーを使用するには、`setHeader` と `setFooter` を使って左・中央・右のヘッダーまたはフッター セクションに `<<Source.Field>>` プレースホルダーを書き込みます。`process()` の前に `designer.setEnableHeaderFooterMarkers(True)` を呼び出し、カスタム `ICellsDataTable` 実装を使用した `designer.setDataSource("node", table)` または `designer.setJsonDataSource(name, json)` のいずれかで値を供給します。完了したセクションは `getHeader` と `getFooter` で取得できます。同一のデータ ソースで本体マーカーとヘッダー/フッターのプレースホルダーを同時に処理できます。画像をセクションにバインドするには、データ URI の値とともに `(picture)` サフィックスを付加します。

## 関連記事
- [SmartMarker シングルセル配列レンダリング](/cells/ja/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python" >}}