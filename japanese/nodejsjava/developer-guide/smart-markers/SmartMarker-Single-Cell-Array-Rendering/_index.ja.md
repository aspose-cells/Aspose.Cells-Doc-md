---
title: SmartMarker 単一セル配列レンダリング | Aspose.Cells for Node.js via Java
description: Aspose.Cells for Node.js via Java の Smart Markers で ArrayAsSingle 属性と ExtraDelimiter 属性を使用して、配列データを単一のセルにレンダリングする方法を学習します。
keywords: Aspose.Cells, Node.js via Java library, spreadsheet, Smart Markers, ArrayAsSingle, ExtraDelimiter, single cell array, array rendering, template
type: docs
weight: 195
url: /ja/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells は、Smart Markers を介して配列データを単一のセルにレンダリングすることをサポートしています。`ArrayAsSingle` 属性と `ExtraDelimiter` 属性を併用することで、開発者は単一セル内における配列要素の区切り方法を制御でき、レポートやテンプレートの柔軟な書式設定を実現できます。

{{% /alert %}}

## **はじめに**

Aspose.Cells の Smart Markers は、`&=DataSource.Field` などのマーカー式を使用してスプレッドシートのデータを動的に入力できる、強力なテンプレートベースの機能です。マーカーはデザイナー ワークブックに配置され、テンプレートが `WorkbookDesigner` によって処理されると、マーカーは指定されたデータソースからの値に置き換えられます。

デフォルトでは、Smart Marker が配列プロパティ（例：`&=DataSource.Numbers`）を参照する場合、エンジンは配列を展開し、各要素を隣接する別のセルに配置します（行方向に水平に、または列方向に垂直に）。この動作は多くのシナリオで便利ですが、配列全体を 1 つのセルにレンダリングし、要素を任意の区切り文字で連結して表示したい場合もあります。

Smart Marker タグ内で併用される `ArrayAsSingle` 属性と `ExtraDelimiter` 属性は、まさにこの要件に対応します。これらの属性により、配列データソースをネイティブに扱いながら、レポートのレイアウトをコンパクトで予測可能な状態に保つことができます。

## **この機能が必要な理由**

### **デフォルトの配列展開動作**

Smart Marker が配列プロパティを参照する場合、Aspose.Cells はデフォルトで配列を複数のセルに展開します。たとえば、`string[]` 型の 4 つの値を含む `&=Product.Tags` のようなマーカーは、各値を個別のセルに配置し、他のテンプレート内容を外側に押し出し、慎重に設計されたレポート レイアウトを壊す可能性があります。

### **ユースケースの制限**

デフォルトの展開動作が望ましくない実用的なシナリオは多数あります。

- レコードごとに 1 行のコンパクトなレイアウトが必要な**サマリースタイルのレポート**。
- 単一セル内にカンマ区切りまたはパイプ区切りの値として表示する必要がある**タグ、ラベル、キーワード リスト**。
- 可読性のために複数の値を 1 か所にまとめる**フィルター チップやステータス インジケーター**。
- 展開された範囲ではなく、セルごとに単一の統合値を期待する**ダウンストリーム パイプライン**（CSV エクスポート、PDF レンダリング、メール マージ）。
- 一部のコンシューマーが複数のセルにまたがる配列を許容できない**クロスプラットフォーム互換性**。

### **この機能が埋めるギャップ**

組み込みのメカニズムがなければ、開発者は JavaScript でデータを前処理し、配列を区切り文字付き文字列に結合してからワークブック デザイナーにバインドすることを強制されます。これによりロジックが重複し、データ モデルが複雑になり、エラーの可能性が高まります。`ArrayAsSingle` 属性と `ExtraDelimiter` 属性は、Smart Marker 内で宣言的に書式設定を処理することで、この回避策を不要にします。

## **機能の利点**

Smart Markers で `ArrayAsSingle` 属性と `ExtraDelimiter` 属性を使用すると、いくつかの利点があります。

- **単一セルへの格納**: すべての配列要素が正確に 1 つのセルにレンダリングされ、レイアウトがコンパクトで予測可能な状態を保ちます。
- **カスタム区切り文字の制御**: カンマ、セミコロン、ハイフン、パイプ、改行、カスタム テキストなど、任意の区切り文字列を指定できます。
- **テンプレート駆動の書式設定**: データを前処理するための追加コードは不要です。書式設定ルールは Smart Marker タグ内に記述されます。
- **クリーンなレポート**: 配列データが隣接するテンプレート内容を異なる行や列に押し出すことがなくなります。
- **汎用的なデータ型**: 文字列、数値、日付など、区切り文字と結合可能なあらゆるデータ型で機能します。
- **後方互換性**: 属性を省略した場合、元の展開動作が維持されるため、既存のテンプレートは変更なく動作し続けます。

## **この機能の使用方法**

### **Smart Marker の構文**

`ArrayAsSingle` 属性と `ExtraDelimiter` 属性は、標準的な Smart Marker の括弧内にキーと値のペアとして渡されます。一般的な構文は次のとおりです。

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

マーカーは以下の部分で構成されています。

- `&=DataSource.ArrayProperty` — バインドされたデータソース上の配列プロパティを参照する標準的な Smart Marker。
- `arrayasSingle=true` — 配列全体を単一のセルにレンダリングするようエンジンに指示します。値 `true` のみが単一セル動作をトリガーします。
- `extraDelimiter=", "` — 配列要素間に配置される区切り文字を定義します。値は文字列リテラルであり、空、単一文字、または複数文字の文字列が可能です。

{{% alert color="primary" %}}

`extraDelimiter` 属性は、複数文字の区切り文字、カスタム テキスト、改行区切りの出力用の `\n` などのエスケープ シーケンスを含む、任意の文字列リテラルを受け入れます。配列が空の場合、結果のセルは空白のままになります。

{{% /alert %}}

### **ステップ バイ ステップのワークフロー**

以下のワークフローでは、Smart Markers を使用して配列を単一のセルにレンダリングする方法について説明します。

1. **データソースの準備**: 配列を返すプロパティを公開するクラス（またはデータ構造）を作成します。プロパティは `string[]`、`int[]`、またはその他のサポートされる配列型を返すことができます。
2. **デザイナー ワークブックの作成**: 新しい `Workbook` を作成し、ヘッダー行を追加し、`arrayasSingle` 属性と `extraDelimiter` 属性を備えた配列プロパティを参照する Smart Marker セルを配置します。
3. **WorkbookDesigner のインスタンス化**: `WorkbookDesigner` オブジェクトを作成し、デザイナー ワークブックをアタッチして、`setDataSource` メソッドを使用してデータソースをバインドします。
4. **マーカーの処理**: `workbookDesigner.process()` メソッドを呼び出して Smart Markers を展開し、実際のデータをワークブックに設定します。
5. **結果の保存**: 結果のワークブックを XLSX またはその他のサポートされるファイル形式でディスクに保存します。

### **コード例 1 — 基本的な文字列配列のレンダリング**

```javascript
class Product {
    constructor() {
        this.Tags = null;
    }
}

const product = new Product();
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

const designer = new AsposeCells.WorkbookDesigner();
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
worksheet.getCells().get("A2").putValue(student.Scores.join(" - "));

workbook.save("output_numericArray.xlsx");
```

### **コード例 3 — デフォルト動作と ArrayAsSingle 動作の比較**

```javascript
const AsposeCells = require("aspose.cells");

function main() {
    const order = {
        Items: ["Apple", "Banana", "Cherry", "Date"]
    };

    const workbook = new AsposeCells.Workbook();
    const sheet = workbook.getWorksheets().get(0);
    const cells = sheet.getCells();

    // セクション 1: デフォルトのスマートマーカー - 値がセルに水平方向に展開される
    cells.get("A1").putValue("Default Spreading Behavior:");
    cells.get("A2").putValue("&=Order.Items");

    // セクション 2: arrayasSingle と extraDelimiter を使用した新しい単一セルレンダリング
    cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):");
    cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // データソースをバインドしてスマートマーカーを処理する
    const designer = new AsposeCells.WorkbookDesigner(workbook);
    designer.setDataSource("Order", order);
    designer.process();

    // 結果のワークブックを保存する
    workbook.save("output_comparison.xlsx");
}

main();
```

### **注意事項とベスト プラクティス**

`ArrayAsSingle` 属性と `ExtraDelimiter` 属性を使用する場合は、以下の点に注意してください。

- `extraDelimiter` の値は文字列リテラルとして扱われます。テンプレート プロセッサが解釈する可能性のある特殊文字はエスケープしてください。
- `arrayasSingle` 属性はブール値（`true` / `false`）を受け入れます。`true` のみが単一セル動作をトリガーし、他の値はデフォルトの展開動作にフォールバックします。
- 配列が空または null の場合、セルは空のままになります（またはデータ型に応じて空白文字列を含みます）。
- この機能はオブジェクト データソースだけでなく、列を配列に分割できる `DataSet` および `DataTable` ソースでも機能します。
- 改行区切りの出力には、区切り文字の値として `\n` を使用できます。
- Smart Marker は、結果の連結文字列を表示するのに十分な幅を持つセルに配置してください。そうでない場合、コンテンツは形式に応じて隣接するセルに視覚的にオーバーフローする可能性があります。



{{< app/cells/assistant language="javascript" >}}