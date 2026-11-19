---
title: スマートマーカーの単一セル配列レンダリング | Aspose.Cells for Python via .NET
description: Aspose.Cells for Python via .NET でスマートマーカーの arrayassingle および arraydelimiter 属性を使用し、配列データを単一セルにレンダリングする方法を学びます。
linktitle: スマートマーカーの単一セル配列レンダリング | Aspose.Cells
url: /ja/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Python via .NET ライブラリ, スプレッドシート, スマートマーカー, arrayassingle, arraydelimiter, 単一セル配列, 配列レンダリング, テンプレート
type: docs
weight: 195
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、スマートマーカーを使用して配列データソースを 1 つのセルにレンダリングできます。`arrayassingle` 属性は既定の要素ごとの展開を無効にし、`arraydelimiter` 属性は結合された要素間に配置される区切り文字を選択します。デフォルトではカンマですが、指定した任意の 1 文字または引用符で囲んだ複数文字の文字列も使用できます。
{{% /alert %}}

## **はじめに**

Aspose.Cells のスマートマーカーは、`&=DataSource.Field` などのマーカー式を使用して、スプレッドシートにデータを動的に入力するテンプレートベースの機能です。マーカーはデザイナー用ワークブックに配置され、テンプレートを `WorkbookDesigner` で処理すると、指定されたデータソースの値に置き換えられます。
既定では、スマートマーカーが配列フィールドを参照する場合（たとえば、4 つの値のリストにバインドされた `&=Product.Tags`）、エンジンは配列を展開して各要素を個別のセルに配置し、値をマーカーより下の列に垂直方向に展開します。この動作は多くのシナリオで便利です。しかし、配列全体を 1 つのセルにレンダリングし、要素を連結して任意の区切り文字で分隔したい場合は、この動作が適さない場合があります。
`arrayassingle` 属性と `arraydelimiter` 属性は、スマートマーカーの括弧内に `name:value` 形式で記述します。まさにこの要件に対応しており、レポートレイアウトをコンパクトかつ予測可能な状態に保ちながら、配列データソースをネイティブに処理できます。

## **この機能が必要な理由**

### **既定の配列展開動作**

スマートマーカーが配列フィールドを参照すると、Aspose.Cells は既定で配列を複数のセルに展開します。たとえば、4 つの値を含むリストに対して `&=Product.Tags` のようなマーカーを使用すると、各値がマーカー直下の個別のセルに配置されます。これによって他のテンプレートコンテンツが押し広げられ、綿密に設計されたレポートレイアウトが崩れる可能性があります。

### **使用ケースの制約**

既定の展開動作が望ましくない実用的なシナリオは多数あります。
- **サマリー形式のレポート**: 1 レコードにつき 1 行のコンパクトなレイアウトが必要な場合。
- **タグ、ラベル、キーワードのリスト**: 1 つのセル内でカンマ区切りまたはパイプ区切りの値として表示する必要がある場合。
- **フィルターチップまたはステータスインジケーター**: 可読性のため、複数の値を 1 か所にまとめて表示する場合。
- **後続のパイプライン**（CSV エクスポート、PDF レンダリング、メールマージ）: 展開された範囲ではなく、セルごとに単一の統合値を必要とする場合。
- **クロスプラットフォーム互換性**: 一部の利用側が複数セルにまたがる配列を扱えない場合。

### **この機能が埋めるギャップ**

組み込みのメカニズムがない場合、開発者は Python でデータを前処理し、`WorkbookDesigner` にバインドする前にリストを区切り文字付き文字列へ結合しなければなりません。この方法ではロジックが重複し、データモデルが複雑になり、エラーが発生しやすくなります。`arrayassingle` 属性と `arraydelimiter` 属性は、スマートマーカー内で書式を宣言的に処理することで、この回避策を不要にします。

## **この機能の利点**

スマートマーカーで `arrayassingle` 属性と `arraydelimiter` 属性を使用すると、いくつかの利点があります。
- **単一セルへの格納**: すべての配列要素が正確に 1 つのセルにレンダリングされ、レイアウトがコンパクトかつ予測可能になります。
- **区切り文字のカスタマイズ**: 既定のカンマ、セミコロン、ハイフン、パイプ、または `" | "` のような引用符付き複数文字文字列など、任意の区切り文字を指定できます。
- **テンプレートによる書式設定**: データを前処理するための追加コードは不要です。書式ルールはスマートマーカータグ内に記述されます。
- **読みやすいレポート**: 配列データによって隣接するテンプレートコンテンツが別の行や列へ移動することがなくなります。
- **多様なデータ型**: JSON 行として提供される文字列リストと数値リストで動作します。
- **後方互換性**: 属性を省略すると元の展開動作が保持されるため、既存のテンプレートは変更なしで引き続き動作します。

## **この機能の使用方法**

### **スマートマーカーの構文**

`arrayassingle` 属性と `arraydelimiter` 属性は、標準スマートマーカーの括弧内で Aspose.Cells の `name:value` 属性文法を使用します。一般的な構文は次のとおりです。

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

マーカーは次の要素で構成されます。
- `&=DataSource.ArrayField` — バインドされたデータソースの配列フィールドを参照する標準スマートマーカー。
- `arrayassingle:true` — 要素を展開する代わりに、配列全体を単一セルにレンダリングするようエンジンに指示します。
- `arraydelimiter:;` — 省略可能。配列要素間に配置される区切り文字を定義します。省略した場合はカンマを使用します。

{{% alert color="warning" %}}
属性は `name:value` 形式（等号ではなくコロン）で記述し、複数の属性を**スペースを入れずに**カンマで区切ります。カンマの後のスペースによって解析された値が 1 文字分ずれます。実際に `(arrayassingle:true, arraydelimiter:;)` とすると、正しい区切り文字 `;` ではなく、誤った区切り文字 `:;` で要素が結合されます。
{{% /alert %}}

### **区切り文字の形式**

- コロンの直後に 1 文字を直接記述します: `arraydelimiter:;`、`arraydelimiter:-`、`arraydelimiter:*`。
- 複数文字の区切り文字は二重引用符で囲みます: `arraydelimiter:" | "`、`arraydelimiter:" - "`。

### **段階別の手順**

次の手順では、スマートマーカーを使用して配列を単一セルにレンダリングします。
1. **データソースを準備**: 各レコードを、フィールドが配列を保持する JSON オブジェクトとして構成します（例: `{"Tags": ["C#", "Aspose"]}`）。このプラットフォームでは、`set_data_source` に渡した通常の Python クラスインスタンス、ディクショナリ、リストは配列フィールドにバインドされません。サポートされている表形式は JSON 行です。
2. **デザイナー用ワークブックを作成**: 新しい `Workbook` を作成してヘッダー行を追加し、配列フィールドを参照する `arrayassingle` 属性付きのスマートマーカーのセルを配置します（カスタム区切り文字が必要な場合は `arraydelimiter` も指定します）。
3. **WorkbookDesigner のインスタンスを作成**: ワークブックを対象に `WorkbookDesigner` を作成し、`set_json_data_source` で JSON 行を関連付けます。
4. **マーカーを処理**: `WorkbookDesigner.process()` メソッドを呼び出して、スマートマーカーを展開し、ワークブックに実際のデータを入力します。
5. **結果を保存**: 生成したワークブックを、XLSX またはサポートされているその他のファイル形式でディスクに保存します。

### **コード例 1 — 基本的な文字列配列のレンダリング**

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Tags")
# No spaces inside the parentheses: attributes are name:value pairs
worksheet.cells.get("A2").put_value("&=Product.Tags(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-single.xlsx")
```

この例では、配列全体の結合値が出力されます。4 つのタグは、既定のカンマで区切られ、1 つのセルに入ります：

```
C#,Aspose,SmartMarker,Excel
```

### **コード例 2 — カスタム区切り文字を指定した数値配列**

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Scores")
# arraydelimiter:- joins the numbers with a hyphen
worksheet.cells.get("A2").put_value("&=Student.Scores(arrayassingle:true,arraydelimiter:-)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Student",
    '[{"Scores": [95, 88, 76, 100, 67]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-numeric.xlsx")
```

JSON の数値は文字列とまったく同じように結合され、各要素は数値をそのままのテキストとして保持されます：

```
95-88-76-100-67
```

### **コード例 3 — 既定のレンダリングと単一セルへのレンダリングの比較**

```python
import aspose.cells as ac

workbook = ac.Workbook()
cells = workbook.worksheets[0].cells
# Column B: default marker — values spread vertically down the column
cells.get("B1").put_value("Default")
cells.get("B2").put_value("&=Order.Items")
# Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").put_value("Single cell")
cells.get("C2").put_value("&=Order.Items(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]')
designer.process()
for row in range(1, 6):
    b = cells.get(row, 1).string_value or ""
    c = cells.get(row, 2).string_value or ""
    if b or c:
        print(f"B{row + 1}=[{b}]  C{row + 1}=[{c}]")
workbook.save("output-array-comparison.xlsx")
```

既定のマーカーは B 列を下方向に展開して 1 要素につき 1 セルを埋めます。一方、`arrayassingle` マーカーは同じ配列を C 列の 1 つのセルにまとめます：

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **注記とベストプラクティス**

スマートマーカーの `arrayassingle` 属性と `arraydelimiter` 属性を使用する際は、次の点に注意してください。
- 属性値には `name:value` 形式を使用します。`arrayassingle=true` のような等号形式は認識されず、警告やエラーを出さずに既定の展開動作にフォールバックします。
- 属性はカンマで区切り、スペースを入れません。カンマ後のスペースによって区切り文字の値が 1 文字分ずれます（上記の警告を参照してください）。
- `arraydelimiter` の値は、コロンの直後に直接記述した 1 文字、または二重引用符で囲んだ複数文字の文字列にできます。
- `arraydelimiter` を省略すると、要素はカンマで結合されます。
- 配列フィールドは `set_json_data_source` の行オブジェクトで指定します。このプラットフォームでは、`set_data_source` に渡した通常の Python オブジェクトとディクショナリはバインドされません。また、列が Python リストを返すカスタム `ICellsDataTable` は、要素を結合する代わりにリストのコンテナのテキスト表現をレンダリングします。
- 結合された出力では、JSON の数値は整数そのままの形式を保持します。

## 関連記事
- [Aspose.Cells for Python via .NET でピボットテーブルにフィルターフィールドを追加する](/cells/ja/python-net/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via .NET でピボットテーブルにスタイルを適用する](/cells/ja/python-net/apply-style-to-pivot-table/)
- [ピボットテーブルのページフィールドレイアウトを変更する](/cells/ja/python-net/change-page-field-layout/)
- [Aspose.Cells for Python via .NET でスパークラインを画像と HTML に変換する](/cells/ja/python-net/convert-sparkline-to-image-and-html/)
- [Excel を OFD 形式に変換する](/cells/ja/python-net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python-net" >}}