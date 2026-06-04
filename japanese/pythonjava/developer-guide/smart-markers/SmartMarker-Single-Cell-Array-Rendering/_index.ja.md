---
title: スマートマーカー単一セル配列レンダリング | Aspose.Cells Python via Java
description: Aspose.Cells for Python via Java で Smart Markers の ArrayAsSingle 属性と ExtraDelimiter 属性を使用して、配列データを単一セルにレンダリングする方法を学びます。
keywords: Aspose.Cells, Python via Java ライブラリ, スプレッドシート, Smart Markers, ArrayAsSingle, ExtraDelimiter, 単一セル配列, 配列レンダリング, テンプレート
type: docs
weight: 195
url: /ja/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells は、Smart Markers を介して配列データを単一セルにレンダリングすることをサポートしています。`ArrayAsSingle` 属性と `ExtraDelimiter` 属性を併用することで、開発者は単一セル内での配列要素の区切り方法を制御でき、レポートやテンプレートに対して柔軟な書式設定を提供できます。

{{% /alert %}}

## **はじめに**

Aspose.Cells の Smart Markers は、`&=DataSource.Field` などのマーカー式を使用してスプレッドシートのデータを動的に入力できる、強力なテンプレートベースの機能です。マーカーはデザイナーワークブック内に配置され、テンプレートが `WorkbookDesigner` によって処理されると、マーカーは指定されたデータソースの値に置き換えられます。

デフォルトでは、Smart Marker が配列プロパティ（たとえば `&=DataSource.Numbers`）を参照している場合、エンジンは配列を展開し、各要素を隣接する別々のセルに配置します（行方向への水平展開または列方向への垂直展開）。この動作は多くのシナリオで便利ですが、配列全体を 1 つのセルにレンダリングし、要素を選択した区切り文字で連結して表示したい状況もあります。

Smart Marker タグ内で併用される `ArrayAsSingle` および `ExtraDelimiter` 属性は、まさにこの要件に対応します。これらの属性により、レポートのレイアウトをコンパクトかつ予測可能に保ちながら、配列データソースをネイティブに扱うことができます。

## **この機能が必要な理由**

### **デフォルトの配列展開動作**

Smart Marker が配列プロパティを参照する場合、Aspose.Cells はデフォルトで配列を複数のセルに展開します。たとえば、4 つの値を含む `string[]` に対する `&=Product.Tags` のようなマーカーは、各値をそれぞれのセルに配置し、他のテンプレートコンテンツを押し出し、注意深く設計されたレポートレイアウトを壊す可能性があります。

### **ユースケースの制限**

デフォルトの展開動作が望ましくない実践的なシナリオは多数あります。

- 1 レコード 1 行のコンパクトなレイアウトが必要な **サマリースタイルのレポート**。
- 1 つのセル内にカンマ区切りまたはパイプ区切りの値として表示する必要がある **タグ、ラベル、またはキーワードのリスト**。
- 読みやすさのために複数の値を 1 か所にまとめる **フィルタチップやステータスインジケーター**。
- 展開された範囲ではなく、セルごとに単一の統合された値を期待する **下流のパイプライン**（CSV エクスポート、PDF レンダリング、メールマージ）。
- 一部のコンシューマが複数セルにまたがる配列を許容しない **クロスプラットフォームの互換性**。

### **この機能が埋めるギャップ**

組み込みのメカニズムがなければ、開発者は Python でデータを前処理し、配列を区切り文字付き文字列に結合してからワークブックデザイナーにバインドせざるを得ません。これによりロジックが重複し、データモデルが複雑になり、エラーの可能性が高まります。`ArrayAsSingle` および `ExtraDelimiter` 属性は、Smart Marker 自体の中で宣言的にフォーマットを処理することで、この回避策を不要にします。

## **機能の利点**

Smart Markers で `ArrayAsSingle` および `ExtraDelimiter` 属性を使用すると、いくつかの利点があります。

- **単一セルへの格納**: すべての配列要素が正確に 1 つのセルにレンダリングされ、レイアウトがコンパクトで予測可能になります。
- **カスタム区切り文字の制御**: カンマ、セミコロン、ハイフン、パイプ、改行、カスタムテキストなど、任意の区切り文字列を指定できます。
- **テンプレート駆動の書式設定**: データを前処理するための追加コードは不要で、書式設定ルールは Smart Marker タグ内に記述されます。
- **クリーンなレポート**: 配列データが隣接するテンプレートコンテンツを異なる行や列に押し出すことがなくなります。
- **汎用的なデータ型**: 文字列、数値、日付など、区切り文字で結合可能なあらゆるデータ型で動作します。
- **後方互換性**: 属性が省略された場合、元の展開動作が保持されるため、既存のテンプレートは変更なく動作し続けます。

## **この機能の使用方法**

### **Smart Marker の構文**

`ArrayAsSingle` および `ExtraDelimiter` 属性は、標準的な Smart Marker の括弧内にキーと値のペアとして渡されます。一般的な構文は次のとおりです。

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

マーカーは以下の部分で構成されています。

- `&=DataSource.ArrayProperty` — バインドされたデータソース上の配列プロパティを参照する標準的な Smart Marker。
- `arrayasSingle=true` — 配列全体を単一セルにレンダリングするようエンジンに指示します。値 `true` のみが単一セル動作をトリガーします。
- `extraDelimiter=", "` — 配列要素間に配置される区切り文字を定義します。値は文字列リテラルであり、空文字列、単一文字、または複数文字の文字列が可能です。

{{% alert color="primary" %}}

`extraDelimiter` 属性は、複数文字の区切り文字、カスタムテキスト、改行で区切られた出力用の `\n` などのエスケープシーケンスなど、任意の文字列リテラルを受け入れます。配列が空の場合、結果のセルは空白のままになります。

{{% /alert %}}

### **ステップバイステップのワークフロー**

次のワークフローでは、Smart Markers を使用して配列を単一セルにレンダリングする方法について説明します。

1. **データソースの準備**: 配列を返すプロパティを公開するクラス（またはデータ構造）を作成します。このプロパティは `string[]`、`int[]`、その他のサポートされている配列型を返すことができます。
2. **デザイナーワークブックの作成**: 新しい `Workbook` を作成し、ヘッダー行を追加し、`arrayasSingle` および `extraDelimiter` 属性を持つ配列プロパティを参照する Smart Marker セルを配置します。
3. **WorkbookDesigner のインスタンス化**: `WorkbookDesigner` オブジェクトを作成し、デザイナーワークブックを関連付け、`set_data_source` メソッドを使用してデータソースをバインドします。
4. **マーカーの処理**: `WorkbookDesigner.process()` メソッドを呼び出して Smart Markers を展開し、ワークブックに実際のデータを入力します。
5. **結果の保存**: 結果として得られるワークブックを XLSX またはその他のサポートされているファイル形式でディスクに保存します。

### **コード例 1 — 基本的な文字列配列のレンダリング**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorkbookDesigner

class Product:
    def __init__(self, tags):
        self._tags = tags
    
    def getTags(self):
        return self._tags

product = Product(["C#", "Aspose", "SmartMarker", "Excel"])

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Tags")
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")

designer = WorkbookDesigner()
designer.setWorkbook(workbook)
designer.setDataSource("Product", product)
designer.process()

workbook.save("output_arraySingle.xlsx")

jpype.shutdownJVM()
```

### **コード例 2 — カスタム区切り文字を持つ数値配列**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook

# Student クラスを定義する
class Student:
    def __init__(self):
        self.Scores = []

student = Student()
student.Scores = [95, 88, 76, 100, 67]

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Scores")
worksheet.getCells().get("A2").putValue(" - ".join(str(s) for s in student.Scores))

workbook.save("output_numericArray.xlsx")

jpype.shutdownJVM()
```

### **コード例 3 — デフォルト動作と ArrayAsSingle 動作の比較**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorkbookDesigner

# データソースを辞書として定義する (Order クラスと同等)
order = {"Items": ["Apple", "Banana", "Cherry", "Date"]}

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# セクション 1: デフォルトのスマートマーカー - 値がセル全体に水平方向に展開される
cells.get("A1").putValue("Default Spreading Behavior:")
cells.get("A2").putValue("&=Order.Items")

# セクション 2: arrayasSingle と extraDelimiter を使用した新しい単一セルレンダリング
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):")
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")")

# データソースをバインドし、スマートマーカーを処理する
designer = WorkbookDesigner(workbook)
designer.setDataSource("Order", order)
designer.process()

# 結果のワークブックを保存する
workbook.save("output_comparison.xlsx")

jpype.shutdownJVM()
```

### **注意点とベストプラクティス**

`ArrayAsSingle` および `ExtraDelimiter` 属性を使用する場合は、以下の点に注意してください。

- `extraDelimiter` の値は文字列リテラルとして扱われます。テンプレートプロセッサが解釈する可能性のある特殊文字はエスケープしてください。
- `arrayasSingle` 属性はブール値（`true` / `false`）を受け取ります。単一セル動作をトリガーするのは `true` のみであり、他の値はデフォルトの展開動作にフォールバックします。
- 配列が空または null の場合、セルは空になります（データ型に応じて空文字列が含まれます）。
- この機能はオブジェクトデータソースだけでなく、列を配列に分割できる `DataSet` および `DataTable` ソースでも動作します。
- 改行で区切られた出力の場合、区切り文字の値として `\n` またはプラットフォームの改行定数を使用できます。
- 結果として得られる連結文字列を表示するのに十分な幅を持つセルに Smart Marker を配置してください。さもなければ、フォーマットに応じて内容が隣接するセルに視覚的にオーバーフローする可能性があります。

## **関連記事**

- [Smart Markers](/cells/ja/python-java/smart-markers/)

{{< app/cells/assistant language="python" >}}