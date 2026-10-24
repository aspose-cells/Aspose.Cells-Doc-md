---
title: SmartMarker の単一セル配列レンダリング | Aspose.Cells for Node.js via Java
linktitle: SmartMarker の単一セル配列レンダリング | Aspose.Cells for Node.js via Java
description: Aspose.Cells for Node.js via Java のスマートマーカーで ArrayAsSingle および ExtraDelimiter 属性を使用して、配列データを単一セルにレンダリングする方法を学びます。
keywords: Aspose.Cells, Node.js via Java ライブラリ, スプレッドシート, スマートマーカー, ArrayAsSingle, ExtraDelimiter, 単一セル配列, 配列レンダリング, テンプレート
type: docs
weight: 195
url: /ja/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、スマートマーカーを使用して配列データを単一セルにレンダリングできます。`ArrayAsSingle` 属性を `ExtraDelimiter` 属性とともに使用することで、開発者は単一セル内で配列要素を区切る方法を制御し、レポートやテンプレートに柔軟な書式を設定できます。
{{% /alert %}}

## **Introduction**
Aspose.Cells のスマートマーカーは、`&=DataSource.Field` などのマーカー式を使用して、スプレッドシートのデータを動的に設定できる、強力なテンプレートベースの機能です。マーカーをデザイナー用ワークブックに配置し、テンプレートを `WorkbookDesigner` で処理すると、マーカーは提供されたデータソースの値に置き換えられます。
既定では、スマートマーカーが配列プロパティ（たとえば `&=DataSource.Numbers`）を参照すると、エンジンは配列を展開し、各要素を行方向または列方向に、隣接する別々のセルへ配置します。この動作は多くのシナリオで便利です。しかし、配列全体を 1 つのセルにレンダリングし、要素を連結して任意の区切り文字で区切りたい場合があります。
`ArrayAsSingle` と `ExtraDelimiter` の属性は、スマートマーカータグ内で一緒に使用することで、この要件に正確に応えます。配列データソースとネイティブに連携しながら、レポートレイアウトをコンパクトで予測可能な状態に保つことができます。

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
スマートマーカーが配列プロパティを参照すると、Aspose.Cells は既定で配列を複数のセルに展開します。たとえば、4 つの値を含む `string[]` に対して `&=Product.Tags` のようなマーカーを使用すると、各値が独自のセルに配置され、他のテンプレートコンテンツが外側に押し出され、慎重に設計されたレポートレイアウトが壊れる可能性があります。

### **Use Case Limitations**
既定の展開動作が望ましくない実用的なシナリオは多数あります。
- **サマリー形式のレポート**: レコードごとに 1 行のコンパクトなレイアウトが必要な場合。
- **タグ、ラベル、またはキーワードのリスト**: 1 つのセル内にカンマ区切りまたはパイプ区切りの値として表示する必要がある場合。
- **フィルターチップまたはステータスインジケーター**: 可読性のため複数の値を 1 か所にまとめたい場合。
- **後続のパイプライン**（CSV エクスポート、PDF レンダリング、メールマージ）: 展開された範囲ではなく、セルごとに 1 つの統合された値を必要とする場合。
- **クロスプラットフォーム互換性**: 一部のコンシューマーが複数セルにまたがる配列を許容できない場合。

### **The Gap It Fills**
組み込みのメカニズムがなければ、開発者は JavaScript でデータを前処理し、ワークブックデザイナーにバインドする前に配列を区切り文字付き文字列に結合せざるを得ません。これによりロジックが重複し、データモデルが複雑になり、エラー発生の可能性が高まります。`ArrayAsSingle` と `ExtraDelimiter` の属性は、スマートマーカー内で書式を宣言的に処理することで、この回避策を不要にします。

## **Feature Benefits**
スマートマーカーで `ArrayAsSingle` と `ExtraDelimiter` の属性を使用すると、いくつかの利点が得られます。
- **単一セルへの集約**: すべての配列要素がちょうど 1 つのセルにレンダリングされ、レイアウトをコンパクトで予測可能な状態に保ちます。
- **カスタム区切り文字の制御**: カンマ、セミコロン、ハイフン、パイプ、改行、または任意のカスタムテキストなど、お好みの区切り文字列を指定できます。
- **テンプレート駆動の書式設定**: データを前処理するための追加コードは不要です。書式設定ルールはスマートマーカータグ内に記述されます。
- **より整洁なレポート**: 配列データによって隣接するテンプレートコンテンツが別の行や列へ押し出されることがなくなります。
- **柔軟なデータ型**: 文字列、数値、日付など、区切り文字で結合できるあらゆるデータ型を使用できます。
- **後方互換性**: 属性を省略した場合は元の展開動作が維持されるため、既存のテンプレートは変更を加えずに引き続き動作します。

## **How to Use This Feature**

### **Smart Marker Syntax**
`ArrayAsSingle` と `ExtraDelimiter` の属性は、標準のスマートマーカーの括弧内にキーと値のペアとして渡されます。一般的な構文は次のとおりです。

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

マーカーは次の要素で構成されます。
- `&=DataSource.ArrayProperty` — バインドされたデータソース上の配列プロパティを参照する標準のスマートマーカー。
- `arrayasSingle=true` — エンジンに配列全体を単一セルにレンダリングするよう指示します。値 `true` の場合のみ、単一セル動作が有効になります。
- `extraDelimiter=", "` — 配列要素の間に配置される区切り文字を定義します。値は文字列リテラルであり、空の文字列、1 文字、または複数文字の文字列にできます。

{{% alert color="primary" %}}
`extraDelimiter` 属性は、複数文字の区切り文字、カスタムテキスト、改行区切りの出力のための `\n` などのエスケープシーケンスなど、任意の文字列リテラルを受け入れます。配列が空の場合、結果のセルは空白のままになります。
{{% /alert %}}

### **Step-by-Step Workflow**
次のワークフローは、スマートマーカーを使用して配列を単一セルにレンダリングする方法を説明します。
1. **データソースを準備する**: 配列を返すプロパティを公開するクラス（またはデータ構造）を作成します。プロパティは `string[]`、`int[]`、その他サポートされている配列型を返すことができます。
2. **デザイナー用ワークブックを作成する**: 新しい `Workbook` を作成し、ヘッダー行を追加して、`arrayasSingle` と `extraDelimiter` 属性を備えた配列プロパティを参照するスマートマーカーのセルを配置します。
3. **WorkbookDesigner をインスタンス化する**: `WorkbookDesigner` オブジェクトを作成し、デザイナー用ワークブックをそれに設定し、`setDataSource` メソッドを使用してデータソースをバインドします。
4. **マーカーを処理する**: `workbookDesigner.process()` メソッドを呼び出してスマートマーカーを展開し、ワークブックに実際のデータを入力します。
5. **結果を保存する**: 結果のワークブックを、XLSX またはサポートされているその他のファイル形式でディスクに保存します。

### **Code Example 1 — Basic String Array Rendering**

```javascript
const AsposeCells = require("aspose.cells");
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

### **Code Example 2 — Numeric Array with Custom Delimiter**

```javascript
const AsposeCells = require("aspose.cells");
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

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

```javascript
const AsposeCells = require("aspose.cells");
function main() {
    const order = {
        Items: ["Apple", "Banana", "Cherry", "Date"]
    };
    const workbook = new AsposeCells.Workbook();
    const sheet = workbook.getWorksheets().get(0);
    const cells = sheet.getCells();
    // セクション 1: 既定のスマートマーカー - 値がセル横向に展開されます
    cells.get("A1").putValue("Default Spreading Behavior:");
    cells.get("A2").putValue("&=Order.Items");
    // セクション 2: arrayasSingle と extraDelimiter を使用した新しい単一セルレンダリング
    cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):");
    cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");
    // データソースをバインドしてスマートマーカーを処理
    const designer = new AsposeCells.WorkbookDesigner(workbook);
    designer.setDataSource("Order", order);
    designer.process();
    // 結果のワークブックを保存
    workbook.save("output_comparison.xlsx");
}
main();
```

### **Notes & Best Practices**
`ArrayAsSingle` と `ExtraDelimiter` の属性を扱うときは、次の点に注意してください。
- `extraDelimiter` の値は文字列リテラルとして扱われます。テンプレートプロセッサーが解釈する可能性がある特殊文字はエスケープしてください。
- `arrayasSingle` 属性はブール値 (`true` / `false`) を受け取ります。`true` の場合のみ単一セル動作が有効になり、それ以外の値の場合は既定の展開動作に戻ります。
- 配列が空または `null` の場合、セルは空のままです（データ型によっては空の文字列になります）。
- この機能は、オブジェクトデータソースと、列を配列に分割できる `DataSet` および `DataTable` ソースでも動作します。
- 改行区切りの出力には、区切り文字の値として `\n` を使用できます。
- スマートマーカーを、結果の連結文字列を表示できる幅が十分なセルに配置してください。それ以外の場合、書式に応じてコンテンツが隣接するセルに視覚的にあふれる可能性があります。

{{< app/cells/assistant language="nodejs-java" >}}