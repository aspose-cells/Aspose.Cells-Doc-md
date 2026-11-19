---
title: スマートマーカーによる単一セルへの配列レンダリング | Aspose.Cells Python via Java
linktitle: スマートマーカーによる単一セルへの配列レンダリング | Aspose.Cells Python via Java
description: Aspose.Cells for Python via Java の arrayassingle および arraydelimiter スマートマーカー属性を使用して、配列データを単一セルにレンダリングする方法を学びます。
keywords: Aspose.Cells, Python via Java ライブラリ, スプレッドシート, スマートマーカー, arrayassingle, arraydelimiter, 単一セル配列, 配列レンダリング, テンプレート
type: docs
weight: 195
url: /ja/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、スマートマーカーを使用して配列データソースを単一セルにレンダリングできます。`arrayassingle` 属性は既定の要素ごとの展開を無効にし、`arraydelimiter` 属性は結合した要素間に挿入する区切り文字を指定します。デフォルトはカンマですが、指定した任意の 1 文字、または引用符で囲んだ複数文字の文字列も使用できます。
{{% /alert %}}

## **はじめに**
Aspose.Cells のスマートマーカーは、`&=DataSource.Field` などのマーカー式を使用して、スプレッドシートにデータを動的に設定するテンプレートベースの機能です。マーカーをデザイナー用ワークブックに配置し、テンプレートを `WorkbookDesigner` で処理すると、マーカーは指定されたデータソースの値に置き換えられます。
既定では、スマートマーカーが配列フィールドを参照すると（たとえば、4 つの値のリストにバインドされた `&=Product.Tags`）、エンジンは配列を展開して各要素を個別のセルに配置し、値をマーカーのある列内で下方向に広げます。この動作は多くのシナリオで便利ですが、要素を連結して任意の区切り文字で区切り、配列全体を 1 つのセルにレンダリングすることがある場合です。
`arrayassingle` と `arraydelimiter` 属性は、スマートマーカーの括弧内に `name:value` 形式で記述することで、この要件に対応します。レポートレイアウトをコンパクトかつ予測可能な状態に保ちながら、配列データソースをそのまま扱えるようになります。

## **この機能が必要な理由**

### **既定の配列展開動作**
スマートマーカーが配列フィールドを参照すると、既定では Aspose.Cells が配列を複数セルに展開します。たとえば、4 つの値を含むリストに対して `&=Product.Tags` のようなマーカーを使用すると、各値がマーカーの下の個別のセルに配置されます。そのためにほかのテンプレート内容が移動し、慎重に設計されたレポートレイアウトが崩れる可能性があります。

### **ユースケースの制限**
既定の展開動作が望ましくない実際のシナリオは多数あります。
- **要約形式のレポート**: 各レコードをコンパクトな 1 行のレイアウトとして表示する必要がある場合です。
- **タグ、ラベル、キーワードのリスト**: 単一セル内でカンマ区切りまたはパイプ区切りの値として表示する必要がある場合です。
- **フィルターチップまたはステータスインジケーター**: 可読性のために複数の値を 1 か所にまとめる場合です。
- **後続パイプライン**（CSV エクスポート、PDF レンダリング、メールマージ）: 展開された範囲ではなく、セルごとに単一の統合値が必要な場合です。
- **クロスプラットフォーム互換性**: 一部の利用側が複数セルにまたがる配列を許容できない場合です。

### **解決される課題**
組み込みの仕組みがない場合、開発者は Python でデータを前処理し、ワークブックデザイナーにバインドする前に、リストを区切り文字付き文字列に結合しなければなりません。これによりロジックが重複し、データモデルが複雑になり、エラーが発生する可能性が高まります。`arrayassingle` と `arraydelimiter` 属性により、スマートマーカー内で書式設定を宣言的に処理できるため、この回避策は不要になります。

## **機能の利点**
スマートマーカーで `arrayassingle` と `arraydelimiter` 属性を使用すると、次の利点が得られます。
- **単一セルへの格納**: すべての配列要素がちょうど 1 つのセルにレンダリングされ、レイアウトがコンパクトかつ予測可能になります。
- **カスタム区切り文字の制御**: 既定のカンマ、セミコロン、ハイフン、パイプ、または `" | "` のような引用符で囲んだ複数文字の文字列など、任意の区切り文字を指定できます。
- **テンプレート駆動の書式設定**: データを前処理するための追加コードは不要です。書式設定ルールはスマートマーカータグ内に記述されます。
- **よりクリーンなレポート**: 配列データによって隣接するテンプレートコンテンツが異なる行や列へ移動することがなくなります。
- **多様なデータ型**: JSON 行として提供された文字列配列で動作し、数値を文字列として表示する場合も処理できます。
- **後方互換性**: 属性を省略すると元の展開動作が維持されるため、既存のテンプレートは変更せずに動作し続けます。

## **この機能の使用方法**

### **スマートマーカーの構文**
`arrayassingle` と `arraydelimiter` 属性は、標準のスマートマーカーの括弧内で Aspose.Cells の `name:value` 属性構文を使用します。一般的な構文は次のとおりです。

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

マーカーは次の要素で構成されます。
- `&=DataSource.ArrayField` — バインドされたデータソースの配列フィールドを参照する標準スマートマーカーです。
- `arrayassingle:true` — 要素を展開するのではなく、配列全体を単一セルにレンダリングするようエンジンに指示します。
- `arraydelimiter:;` — 省略可能です。配列要素間に配置される区切り文字を定義します。省略するとカンマが使用されます。

{{% alert color="warning" %}}
属性は `name:value` 形式（等号ではなくコロン）で記述し、複数の属性は**スペースを入れずに**カンマで区切ってください。カンマの後のスペースによって、解析される値が 1 文字分ずれます。`(arrayassingle:true, arraydelimiter:;)` の場合、正しい `;` ではなく誤った区切り文字 `:;` で要素が結合されます。
{{% /alert %}}

### **区切り文字の形式**
- 1 文字の区切り文字は、コロンの直後に直接記述します。例: `arraydelimiter:;`、`arraydelimiter:-`、`arraydelimiter:*`。
- 複数文字の区切り文字は二重引用符で囲みます。例: `arraydelimiter:" | "`、`arraydelimiter:" - "`。

### **段階的なワークフロー**
以下のワークフローでは、スマートマーカーを使用して配列を単一セルにレンダリングする方法を説明します。
1. **データソースの準備**: 各レコードを、配列を保持するフィールドを持つ JSON オブジェクトとして構成します。例: `{"Tags": ["C#", "Aspose"]}`。このプラットフォームでは、`setDataSource` に渡した通常の Python クラスインスタンスや辞書はバインドされません。サポートされる表形式は JSON 行です。
2. **デザイナー用ワークブックの作成**: 新しい `Workbook` を作成してヘッダー行を追加し、配列フィールドを参照するスマートマーカーのセルを配置します。そのマーカーに `arrayassingle` 属性を付与し、必要に応じて `arraydelimiter` も指定します。
3. **WorkbookDesigner のインスタンス化**: ワークブックをラップする `WorkbookDesigner` を作成し、JSON 行を `setJsonDataSource` で関連付けます。
4. **マーカーの処理**: `WorkbookDesigner.process()` メソッドを呼び出してスマートマーカーを展開し、ワークブックに実際のデータを設定します。
5. **結果の保存**: 生成したワークブックを XLSX またはその他のサポート対象ファイル形式でディスクに保存します。

### **コード例 1 — 基本的な文字列配列のレンダリング**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Tags")
# No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]')
designer.process()
print(worksheet.getCells().get("A2").getStringValue())
workbook.save("output-array-single.xlsx")
```

この例では、配列全体を結合した値が出力されます。4 つのタグは既定のカンマで区切られ、1 つのセルに入ります。

```
C#,Aspose,SmartMarker,Excel
```

### **コード例 2 — カスタム区切り文字付き数値の例**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Scores")
# arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]')
designer.process()
print(worksheet.getCells().get("A2").getStringValue())
workbook.save("output-array-numeric.xlsx")
```

スコアを JSON 文字列として提供すると、結合された出力には数値がそのまま保持されます。

```
95-88-76-100-67
```

{{% alert color="note" %}}
Java エンジンを介して渡された JSON の数値は倍精度浮動小数点数として受信されるため、`[95, 88]` は `95.0-88.0` として結合されます。結合したセルに正確な整数の文字列を表示したい場合は、JSON 行内で数値を引用符で囲んでください。
{{% /alert %}}

### **コード例 3 — 既定のレンダリングと単一セルレンダリングの比較**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner

workbook = Workbook()
cells = workbook.getWorksheets().get(0).getCells()
# Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default")
cells.get("B2").putValue("&=Order.Items")
# Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell")
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]')
designer.process()
for row in range(1, 6):
    b = cells.get(row, 1).getStringValue() or ""
    c = cells.get(row, 2).getStringValue() or ""
    if b or c:
        print(f"B{row + 1}=[{b}]  C{row + 1}=[{c}]")
workbook.save("output-array-comparison.xlsx")
```

既定のマーカーは列 B に要素ごとに 1 セルずつ下方向に記入しますが、`arrayassingle` マーカーは同じ配列を列 C の単一セルにまとめます。

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **注記とベストプラクティス**
`arrayassingle` と `arraydelimiter` 属性を使用するときは、次の点に注意してください。
- 属性値は `name:value` 形式を使用します。`arrayassingle=true` のような等号形式は認識されず、暗黙的に既定の展開動作にフォールバックします。
- 属性はカンマとスペースなしで区切ります。カンマの後のスペースによって区切り文字の値が 1 文字分ずれます（上記の警告を参照）。
- `arraydelimiter` の値は、コロンの直後に直接記述した 1 文字、または二重引用符で囲んだ複数文字の文字列にできます。
- `arraydelimiter` を省略すると、要素はカンマで結合されます。
- 配列フィールドは `setJsonDataSource` に渡す行オブジェクトとして提供してください。このプラットフォームでは、`setDataSource` に渡した通常の Python オブジェクトや辞書はバインドされません。
- JSON の数値は Java エンジン経由で倍精度浮動小数点数として受信されます（`95` は `95.0` として結合されます）。正確な整数の文字列が必要な場合は、JSON 行内で数値を引用符で囲んでください。
- 結果の連結文字列を表示できる幅が十分なセルにスマートマーカーを配置してください。幅が足りない場合、表示形式によっては内容を隣接セルへ視覚的にオーバーフローさせる可能性があります。

## 関連記事
- [Aspose.Cells for Python via Java でピボットテーブルにフィルターフィールドを追加する](/cells/ja/python-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via Java でピボットテーブルにスタイルを適用する](/cells/ja/python-java/apply-style-to-pivot-table/)
- [ピボットテーブルのページフィールドレイアウトを変更する](/cells/ja/python-java/change-page-field-layout/)
- [Aspose.Cells for Python via Java でスパークラインを画像および HTML に変換する](/cells/ja/python-java/convert-sparkline-to-image-and-html/)
- [Excel を OFD 形式に変換する](/cells/ja/python-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python" >}}