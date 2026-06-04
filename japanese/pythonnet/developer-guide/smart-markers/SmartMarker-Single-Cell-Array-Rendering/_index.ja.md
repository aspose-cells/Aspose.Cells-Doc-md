---
title: SmartMarker 単一セル配列レンダリング | Aspose.Cells for Python via .NET
description: Aspose.Cells for Python via .NET の Smart Markers で、ArrayAsSingle 属性と ExtraDelimiter 属性を使用して配列データを単一セルにレンダリングする方法を学びます。
keywords: Aspose.Cells, Python via .NET ライブラリ, スプレッドシート, Smart Markers, ArrayAsSingle, ExtraDelimiter, 単一セル配列, 配列レンダリング, テンプレート
type: docs
weight: 195
url: /ja/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells は、Smart Markers を介して配列データを単一セルにレンダリングすることをサポートしています。`ArrayAsSingle` 属性と `ExtraDelimiter` 属性を併用することで、開発者は単一セル内での配列要素の区切り方法を制御でき、レポートやテンプレートに柔軟な書式設定を提供できます。

{{% /alert %}}

## **はじめに**

Aspose.Cells の Smart Markers は、`&=DataSource.Field` などのマーカー式を使用してスプレッドシートのデータを動的に入力できる、強力なテンプレートベースの機能です。マーカーはデザイナー ワークブック内に配置され、`WorkbookDesigner` によってテンプレートが処理されると、マーカーは指定されたデータソースの値に置き換えられます。

デフォルトでは、Smart Marker が配列プロパティ（たとえば `&=DataSource.Numbers`）を参照する場合、エンジンは配列を展開し、各要素を隣接する別のセルに配置します（行方向に水平に、または列方向に垂直に）。この動作は多くのシナリオで便利ですが、配列全体を 1 つのセルにレンダリングし、要素を選択した区切り文字で連結して表示したい状況もあります。

Smart Marker タグ内で併用される `ArrayAsSingle` 属性と `ExtraDelimiter` 属性は、まさにこの要件に対応します。これらの属性により、配列データソースをネイティブに扱いながら、レポートレイアウトをコンパクトで予測可能な状態に保つことができます。

## **この機能が必要な理由**

### **デフォルトの配列展開動作**

Smart Marker が配列プロパティを参照する場合、Aspose.Cells はデフォルトで配列を複数のセルに展開します。たとえば、4 つの値を含む `string[]` に対する `&=Product.Tags` のようなマーカーは、各値を独自のセルに配置し、他のテンプレートコンテンツを押し出し、慎重に設計されたレポートレイアウトを壊す可能性があります。

### **ユースケースの制限**

デフォルトの展開動作が望ましくない実用的なシナリオは多数あります。

- レコードごとに 1 行のコンパクトなレイアウトを必要とする**サマリー形式のレポート**。
- 1 つのセル内にカンマ区切りまたはパイプ区切りの値として表示する必要がある**タグ、ラベル、またはキーワードのリスト**。
- 読みやすさのために複数の値を 1 か所にグループ化する**フィルタチップやステータスインジケーター**。
- 展開された範囲ではなく、セルごとに単一の統合された値を期待する**ダウンストリームパイプライン**（CSV エクスポート、PDF レンダリング、メールマージ）。
- 一部のコンシューマーが複数のセルにまたがる配列を許容できない場合の**クロスプラットフォーム互換性**。

### **この機能が埋めるギャップ**

組み込みのメカニズムがなければ、開発者は Python でデータを前処理し、ワークブックデザイナーにバインドする前に配列を区切り文字列に結合することを強制されます。これによりロジックが重複し、データモデルが複雑になり、エラーの可能性が高まります。`ArrayAsSingle` 属性と `ExtraDelimiter` 属性は、Smart Marker 自体の中で宣言的に書式設定を処理することで、この回避策を不要にします。

## **機能のメリット**

Smart Markers で `ArrayAsSingle` 属性と `ExtraDelimiter` 属性を使用すると、いくつかの利点があります。

- **単一セル格納**：すべての配列要素が正確に 1 つのセルにレンダリングされ、レイアウトがコンパクトで予測可能になります。
- **カスタム区切り文字の制御**：カンマ、セミコロン、ハイフン、パイプ、改行、カスタムテキストなど、任意の区切り文字列を指定できます。
- **テンプレート駆動の書式設定**：データを前処理するための追加コードは不要で、書式設定ルールは Smart Marker タグ内に記述されます。
- **よりクリーンなレポート**：配列データが隣接するテンプレートコンテンツを別の行や列に押し出すことがなくなります。
- **多様なデータ型**：文字列、数値、日付、その他区切り文字で結合可能なあらゆるデータ型で動作します。
- **後方互換性**：属性を省略した場合、元の展開動作が保持されるため、既存のテンプレートは変更されず動作し続けます。

## **この機能の使用方法**

### **Smart Marker の構文**

`ArrayAsSingle` 属性と `ExtraDelimiter` 属性は、標準の Smart Marker の括弧内にキーと値のペアとして渡されます。一般的な構文は次のとおりです。

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

マーカーは以下の部分で構成されています。

- `&=DataSource.ArrayProperty` — バインドされたデータソースの配列プロパティを参照する標準の Smart Marker。
- `arrayasSingle=true` — 配列全体を 1 つのセルにレンダリングするようエンジンに指示します。値 `true` のみが単一セル動作をトリガーします。
- `extraDelimiter=", "` — 配列要素間に配置される区切り文字を定義します。値は文字列リテラルであり、空文字列、単一文字、または複数文字の文字列が可能です。

{{% alert color="primary" %}}

`extraDelimiter` 属性は、複数文字の区切り文字、カスタムテキスト、改行区切りの出力用の `\n` などのエスケープシーケンスを含む、任意の文字列リテラルを受け入れます。配列が空の場合、結果のセルは空白のままになります。

{{% /alert %}}

### **ステップバイステップのワークフロー**

以下のワークフローは、Smart Markers を使用して配列を単一セルにレンダリングする方法を説明しています。

1. **データソースの準備**：配列を返すプロパティを公開するクラス（またはデータ構造）を作成します。プロパティは `list[str]`、`list[int]`、またはその他のサポートされている配列型を返すことができます。
2. **デザイナー ワークブックの作成**：新しい `Workbook` を作成し、ヘッダー行を追加し、配列プロパティを参照する `arrayasSingle` 属性と `extraDelimiter` 属性を持つ Smart Marker セルを配置します。
3. **WorkbookDesigner のインスタンス化**：`WorkbookDesigner` オブジェクトを作成し、デザイナー ワークブックをアタッチし、`set_data_source` メソッドを使用してデータソースをバインドします。
4. **マーカーの処理**：`WorkbookDesigner.process()` メソッドを呼び出して、Smart Markers を展開し、ワークブックに実際のデータを入力します。
5. **結果の保存**：結果のワークブックを XLSX またはその他のサポートされているファイル形式でディスクに保存します。

### **コード例 1 — 基本的な文字列配列のレンダリング**

```python
class Product:
    def __init__(self):
        self.Tags = []

product = Product()
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"]

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Tags")
worksheet.cells["A2"].put_value("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")

designer = ac.WorkbookDesigner()
designer.workbook = workbook
designer.set_data_source("Product", product)
designer.process()

workbook.save("output_arraySingle.xlsx")
```

### **コード例 2 — カスタム区切り文字を使用した数値配列**

```python
class Student:
    def __init__(self):
        self.scores = []


student = Student()
student.scores = [95, 88, 76, 100, 67]

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Scores")
worksheet.cells["A2"].put_value(" - ".join(str(s) for s in student.scores))

workbook.save("output_numericArray.xlsx")
```

### **コード例 3 — デフォルト動作と ArrayAsSingle 動作の比較**

```python
class Order:
    def __init__(self, items):
        self._items = items

    @property
    def Items(self):
        return self._items

    @Items.setter
    def Items(self, value):
        self._items = value

order = Order(["Apple", "Banana", "Cherry", "Date"])

workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# セクション 1: デフォルトのスマートマーカー - 値がセル全体に水平方向に展開される
cells["A1"].put_value("Default Spreading Behavior:")
cells["A2"].put_value("&=Order.Items")

# セクション 2: arrayasSingle と extraDelimiter を使用した新しい単一セルレンダリング
cells["A4"].put_value("Single Cell Rendering (arrayasSingle=true):")
cells["A5"].put_value('&=Order.Items(arrayasSingle=true, extraDelimiter="; ")')

# データソースをバインドし、スマートマーカーを処理する
designer = ac.WorkbookDesigner(workbook)
designer.set_data_source("Order", order)
designer.process()

# 結果のワークブックを保存する
workbook.save("output_comparison.xlsx")
```

### **注意事項とベストプラクティス**

`ArrayAsSingle` 属性と `ExtraDelimiter` 属性を操作する際は、以下の点に注意してください。

- `extraDelimiter` の値は文字列リテラルとして扱われます。テンプレートプロセッサが解釈する可能性のある特殊文字はエスケープしてください。
- `arrayasSingle` 属性はブール値（`True` / `False`）を受け入れます。`True` のみが単一セル動作をトリガーし、それ以外の値はデフォルトの展開動作にフォールバックします。
- 配列が空または null の場合、セルは空のままになります（データ型に応じて空文字列を含む場合もあります）。
- この機能はオブジェクトデータソースだけでなく、列を配列に分割できる `DataSet` および `DataTable` ソースとも連携します。
- 改行区切りの出力には、区切り文字の値として `\n` または `os.linesep` を使用できます。
- 結果の連結文字列を表示するのに十分な幅を持つセルに Smart Marker を配置してください。そうでない場合、形式によってはコンテンツが隣接するセルに視覚的にオーバーフローする可能性があります。

## **関連記事**

- [Smart Markers](/cells/ja/python-net/smart-markers/)
- [セルの結合と結合解除](/cells/ja/python-net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="python" >}}