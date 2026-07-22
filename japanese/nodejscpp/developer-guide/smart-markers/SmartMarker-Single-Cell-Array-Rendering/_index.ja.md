---
title: スマートマーカー単一セル配列レンダリング | Aspose.Cells for Node.js via C++
linktitle: スマートマーカー単一セル配列レンダリング | Aspose.Cells
description: Aspose.Cells for Node.js via C++ のスマートマーカーで ArrayAsSingle および ExtraDelimiter 属性を使用して、配列データを単一セルにレンダリングする方法を学習します。
keywords: Aspose.Cells, Node.js ライブラリ, スプレッドシート, スマートマーカー, ArrayAsSingle, ExtraDelimiter, 単一セル配列, 配列レンダリング, テンプレート
type: docs
weight: 195
url: /ja/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、スマートマーカーを介して配列データを単一セルにレンダリングすることをサポートしています。`ArrayAsSingle` 属性と `ExtraDelimiter` 属性を併用することで、開発者は単一セル内で配列要素を区切る方法を制御でき、レポートやテンプレートの柔軟な書式設定を実現します。

{{% /alert %}}

## **はじめに**

Aspose.Cells のスマートマーカーは、強力なテンプレートベースの機能であり、`&=DataSource.Field` などのマーカー式を使用してスプレッドシートのデータを動的に入力することができます。マーカーはデザイナーワークブックに配置され、テンプレートが `WorkbookDesigner` によって処理されると、マーカーは指定されたデータソースからの値に置き換えられます。

デフォルトでは、スマートマーカーが配列プロパティ（例えば `&=DataSource.Numbers`）を参照する場合、エンジンは配列を展開し、各要素を隣接する個別のセルに配置します — 行方向に水平方向に、または列方向に垂直方向に展開されます。この動作は多くのシナリオで便利ですが、配列全体を 1 つの単一セルにレンダリングし、要素を選択した区切り文字で連結して表示したい状況もあります。

スマートマーカータグ内で一緒に使用される `ArrayAsSingle` 属性と `ExtraDelimiter` 属性は、まさにこの要件に対応します。これらの属性により、配列データソースをネイティブに操作しながら、レポートレイアウトをコンパクトかつ予測可能な状態に保つことができます。

## **この機能が必要な理由**

### **デフォルトの配列展開動作**

スマートマーカーが配列プロパティを参照する場合、Aspose.Cells はデフォルトで配列を複数のセルに展開します。例えば、4 つの値を含む `string[]` に対する `&=Product.Tags` のようなマーカーは、各値を独自のセルに配置し、他のテンプレートコンテンツを押し出し、慎重に設計されたレポートレイアウトを壊す可能性があります。

### **ユースケースの制限**

デフォルトの展開動作が望ましくない実際のシナリオは多数あります。

- 1 レコードにつき 1 行のコンパクトなレイアウトが必要な**サマリースタイルのレポート**。
- 単一セル内にカンマ区切りまたはパイプ区切りの値として表示する必要がある**タグ、ラベル、またはキーワードリスト**。
- 読みやすさのために複数の値を 1 か所にグループ化する**フィルターチップまたはステータスインジケーター**。
- 展開された範囲ではなく、セルごとに 1 つの統合された値を期待する**下流のパイプライン**（CSV エクスポート、PDF レンダリング、メールマージ）。
- 一部のコンシューマーが複数のセルにまたがる配列を許容できない**クロスプラットフォーム互換性**。

### **この機能が埋めるギャップ**

組み込みのメカニズムがなければ、開発者は JavaScript でデータを前処理し、配列を区切り文字列に結合してから、ワークブックデザイナーにバインドせざるを得なくなります。これにより、ロジックが重複し、データモデルが複雑になり、エラーの可能性が高まります。`ArrayAsSingle` 属性と `ExtraDelimiter` 属性は、スマートマーカー自体の中で宣言的に書式設定を処理することで、この回避策を不要にします。

## **機能の利点**

スマートマーカーで `ArrayAsSingle` 属性と `ExtraDelimiter` 属性を使用すると、いくつかの利点があります。

- **単一セルへの格納**: すべての配列要素が正確に 1 つのセルにレンダリングされ、レイアウトがコンパクトで予測可能になります。
- **カスタム区切り文字の制御**: カンマ、セミコロン、ハイフン、パイプ、改行、または任意のカスタムテキストなど、任意の区切り文字列を指定できます。
- **テンプレート駆動の書式設定**: データを前処理するための追加コードは不要です。書式設定ルールはスマートマーカータグ内に記述されます。
- **よりクリーンなレポート**: 配列データが隣接するテンプレートコンテンツを異なる行や列に押し出すことがなくなります。
- **多様なデータ型**: 文字列、数値、日付、および区切り文字で結合可能なその他のデータ型で機能します。
- **後方互換性**: 属性が省略された場合、元の展開動作が保持されるため、既存のテンプレートは変更されず動作し続けます。

## **この機能の使用方法**

### **スマートマーカーの構文**

`ArrayAsSingle` 属性と `ExtraDelimiter` 属性は、標準的なスマートマーカーの括弧内にキーと値のペアとして渡されます。一般的な構文は次のとおりです。

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

マーカーは以下の部分で構成されています。

- `&=DataSource.ArrayProperty` — バインドされたデータソースの配列プロパティを参照する標準スマートマーカー。
- `arrayasSingle=true` — 配列全体を単一セルにレンダリングするようエンジンに指示します。値 `true` のみが単一セル動作をトリガーします。
- `extraDelimiter=", "` — 配列要素間に配置される区切り文字を定義します。値は文字列リテラルであり、空、単一文字、または複数文字の文字列が可能です。

{{% alert color="primary" %}}

`extraDelimiter` 属性は、複数文字の区切り文字、カスタムテキスト、改行で区切られた出力のための `\n` などのエスケープシーケンスなど、任意の文字列リテラルを受け入れます。配列が空の場合、結果のセルは空白のままになります。

{{% /alert %}}

### **ステップバイステップのワークフロー**

次のワークフローでは、スマートマーカーを使用して配列を単一セルにレンダリングする方法について説明します。

1. **データソースの準備**: 配列を返すプロパティを公開するクラス（またはデータ構造）を作成します。プロパティは `string[]`、`int[]`、またはその他のサポートされている配列型を返すことができます。
2. **デザイナーワークブックの作成**: 新しい `Workbook` を作成し、ヘッダー行を追加し、配列プロパティを参照する `arrayasSingle` および `extraDelimiter` 属性を持つスマートマーカーセルを配置します。
3. **WorkbookDesigner のインスタンス化**: `WorkbookDesigner` オブジェクトを作成し、デザイナーワークブックをアタッチし、`setDataSource` メソッドを使用してデータソースをバインドします。
4. **マーカーの処理**: `workbookDesigner.process()` メソッドを呼び出してスマートマーカーを展開し、ワークブックに実際のデータを入力します。
5. **結果の保存**: 結果のワークブックを XLSX またはその他のサポートされているファイル形式でディスクに保存します。

### **コード例 1 — 基本的な文字列配列のレンダリング**

```javascript
let product = {
    Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
};

let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue('&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")');

let designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Product", product);
designer.process();

workbook.save("output_arraySingle.xlsx");
```

### **コード例 2 — カスタム区切り文字を使用した数値配列**

```javascript
class Student {
    constructor() {
        this.Scores = [];
    }
}

const student = new Student();
student.Scores = [95, 88, 76, 100, 67];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Scores");
worksheet.getCells().get("A2").putValue('&=Student.Scores(arrayasSingle=true, extraDelimiter=" - ")');

let designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Student", student);
designer.process();

workbook.save("output_numericArray.xlsx");
```

### **コード例 3 — デフォルトの動作と ArrayAsSingle 動作の比較**

```javascript
var order = {
    Items: ["Apple", "Banana", "Cherry", "Date"]
};

var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// セクション 1: デフォルトのスマートマーカー - 値がセルを横方向に展開される
cells.get("A1").putValue("Default Spreading Behavior:");
cells.get("A2").putValue("&=Order.Items");

// セクション 2: arrayasSingle と extraDelimiter を使用した新しい単一セルレンダリング
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):");
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

// データソースをバインドし、スマートマーカーを処理する
var designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setDataSource("Order", order);
designer.process();

// 結果のワークブックを保存する
workbook.save("output_comparison.xlsx");
```

### **注意事項とベストプラクティス**

`ArrayAsSingle` 属性と `ExtraDelimiter` 属性を使用する場合は、以下の点に注意してください。

- `extraDelimiter` 値は文字列リテラルとして扱われます。テンプレートプロセッサが解釈する可能性のある特殊文字はエスケープしてください。
- `arrayasSingle` 属性はブール値（`true` / `false`）を受け入れます。`true` のみが単一セル動作をトリガーします。他の値はデフォルトの展開動作にフォールバックします。
- 配列が空または null の場合、セルは空のままになります（またはデータ型に応じて空白文字列を含みます）。
- この機能はオブジェクトデータソースだけでなく、列を配列に分割できる `DataSet` および `DataTable` ソースでも機能します。
- 改行で区切られた出力には、区切り文字の値として `\n` または `os.EOL` を使用できます。
- スマートマーカーは、結果として得られる連結文字列を表示するのに十分な幅を持つセルに配置してください。そうでない場合、書式によってはコンテンツが隣接するセルに視覚的にオーバーフローする可能性があります。

## **関連記事**

- [セルの結合と結合解除](/cells/ja/nodejs-cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="javascript" >}}