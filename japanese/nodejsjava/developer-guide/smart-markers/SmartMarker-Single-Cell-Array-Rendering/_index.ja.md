---
title: スマートマーカーの単一セル配列レンダリング | Aspose.Cells for Node.js via Java
description: `arrayassingle` と `arraydelimiter` のスマートマーカー属性を使用して、Aspose.Cells for Node.js via Java で配列データを単一セルにレンダリングする方法を学びます。
linktitle: スマートマーカーの単一セル配列レンダリング | Aspose.Cells for Node.js via Java
url: /ja/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Java 経由の Node.js ライブラリ, スプレッドシート, スマートマーカー, arrayassingle, arraydelimiter, 単一セル配列, 配列レンダリング, テンプレート
type: docs
weight: 195
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、スマートマーカーを使用して配列データソースを 1 つのセルにレンダリングできます。`arrayassingle` 属性は、要素を 1 つずつ展開する既定の動作を無効にし、`arraydelimiter` 属性は、結合された要素間に配置される区切り文字を選択します。初期値はカンマですが、指定した任意の 1 文字または引用符で囲んだ複数文字の文字列も使用できます。
{{% /alert %}}

## **はじめに**

Aspose.Cells のスマートマーカーは、`&=DataSource.Field` などのマーカー式を使用して、スプレッドシートにデータを動的に設定するテンプレートベースの機能です。マーカーをデザインワークブックに配置し、テンプレートを `WorkbookDesigner` で処理すると、マーカーは指定されたデータソースの値に置き換えられます。
既定では、スマートマーカーが配列フィールドを参照する場合（例：`&=Product.Tags` が 4 つの値の配列にバインドされている場合）、エンジンは配列を展開し、各要素を個別のセルに配置して、マーカーの下の列に値を垂直方向に広げます。この動作は多くのシナリオで便利ですが、要素を連結して任意の区切り文字で区切り、配列全体を 1 つのセルにレンダリングしたい場合があります。
`arrayassingle` 属性と `arraydelimiter` 属性は、スマートマーカーの括弧内に `name:value` 形式で記述すると、まさにこの要件に対応します。配列データソースをネイティブに扱いながら、レポートレイアウトをコンパクトかつ予測可能な状態に保てます。

## **この機能が必要な理由**

### **既定の配列展開動作**

スマートマーカーが配列フィールドを参照すると、既定では Aspose.Cells が配列を複数のセルに展開します。たとえば、4 つの値を含む配列に対して `&=Product.Tags` のようなマーカーを使用すると、各値がマーカーの下の個別のセルに配置されます。これにより、他のテンプレートコンテンツが押し下げられ、慎重に設計したレポートレイアウトが崩れる可能性があります。

### **ユースケースの制限**

既定の展開動作が望ましくない実際のシナリオは多数あります。
- **要約形式のレポート**: レコードごとに 1 行のコンパクトなレイアウトが必要なものです。
- **タグ、ラベル、キーワードのリスト**: 単一セル内でカンマ区切りまたはパイプ区切りの値として表示する必要があるものです。
- **フィルターチップまたはステータス表示**: 可読性のために複数の値を 1 か所にまとめる必要があるものです。
- **後続のパイプライン**（CSV エクスポート、PDF レンダリング、メールマージ）: 展開された範囲ではなく、セルごとに 1 つの統合された値が必要なものです。
- **クロスプラットフォーム互換性**: 複数のセルにまたがる配列を許容できない利用側があります。

### **この機能が解決する課題**

組み込みのメカニズムがなければ、開発者は JavaScript でデータを前処理し、ワークブックデザイナーにバインドする前に配列を区切り文字付き文字列へ結合することを強いられます。これにより、ロジックが重複し、データモデルが複雑になり、エラーの発生率が高まります。`arrayassingle` 属性と `arraydelimiter` 属性は、スマートマーカー内で書式設定を宣言的に処理できるため、この回避策を不要にします。

## **機能の利点**

スマートマーカーで `arrayassingle` 属性と `arraydelimiter` 属性を使用すると、次の利点が得られます。
- **単一セルへの格納**: すべての配列要素をちょうど 1 つのセルにレンダリングし、レイアウトをコンパクトかつ予測可能に保ちます。
- **カスタム区切り文字の制御**: 任意の区切り文字を指定できます。初期値のカンマ、セミコロン、ハイフン、パイプ、または `" | "` のような引用符付き複数文字文字列を使用できます。
- **テンプレート駆動の書式設定**: データを前処理するために追加のコードは必要ありません。書式設定ルールはスマートマーカーのタグ内に記述されます。
- **より整洁なレポート**: 配列データによって、隣接するテンプレートコンテンツが別の行や列に押し出されることがなくなります。
- **多様なデータ型**: JSON 行として提供された文字列配列や、文字列としてレンダリングされる数値も扱えます。
- **後方互換性**: 属性を省略すると元の展開動作が維持されるため、既存のテンプレートは変更されずに動作し続けます。

## **この機能の使用方法**

### **スマートマーカーの構文**

`arrayassingle` 属性と `arraydelimiter` 属性では、標準のスマートマーカーの括弧内で Aspose.Cells の `name:value` 属性文法を使用します。一般的な構文は次のとおりです。

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

マーカーは次の要素で構成されます。
- `&=DataSource.ArrayField` — バインドされたデータソースの配列フィールドを参照する標準スマートマーカー。
- `arrayassingle:true` — 要素を展開する代わりに、配列全体を単一セルにレンダリングするようエンジンに指示します。
- `arraydelimiter:;` — 省略可。配列要素間に配置される区切り文字を定義します。省略するとカンマが使用されます。

{{% alert color="warning" %}}
属性は `name:value` 形式（等号ではなくコロン）で記述し、複数の属性は**スペースを入れずに**カンマで区切ります。カンマの後にスペースを入れると、解析された値が 1 文字分ずれます。`(arrayassingle:true, arraydelimiter:;)` では、正しい区切り文字 `;` ではなく、誤った区切り文字 `:;` で結合されます。
{{% /alert %}}

### **区切り文字の形式**

- コロンの直後に 1 文字を直接記述します：`arraydelimiter:;`、`arraydelimiter:-`、`arraydelimiter:*`。
- 複数文字の区切り文字は二重引用符で記述します：`arraydelimiter:" | "`、`arraydelimiter:" - "`。

### **段階的な手順**

次のワークフローで、スマートマーカーを使用して配列を単一セルにレンダリングする方法を説明します。
1. **データソースの準備**: 各レコードを、フィールドが配列を保持する JSON オブジェクトとして構成します。例：`{"Tags": ["C#", "Aspose"]}`。このプラットフォームでは、`setDataSource` に渡されたプレーンな JavaScript オブジェクトと配列はバインドされません。JSON 行がサポートされる表形式です。
2. **デザインワークブックの作成**: 新しい `Workbook` を作成し、ヘッダー行を追加します。次に、配列フィールドを参照し、`arrayassingle` 属性（必要に応じてカスタム区切り文字を指定する `arraydelimiter` 属性）を持つスマートマーカーのセルを配置します。
3. **WorkbookDesigner のインスタンス化**: ワークブックに対して `WorkbookDesigner` を作成し、`setJsonDataSource` を使って JSON 行を関連付けます。
4. **マーカーの処理**: `workbookDesigner.process()` メソッドを呼び出して、スマートマーカーを展開し、ワークブックに実際のデータを設定します。
5. **結果の保存**: 生成されたワークブックを XLSX またはその他のサポートされているファイル形式でディスクに保存します。

### **コード例 1 — 基本的な文字列配列のレンダリング**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Tags");
// No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-single.xlsx");
```

この例では、配列全体を結合した値が出力されます。4 つのタグは、既定のカンマで区切られ、1 つのセルに配置されます。

```
C#,Aspose,SmartMarker,Excel
```

### **コード例 2 — カスタム区切り文字を使った数値値**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Scores");
// arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-numeric.xlsx");
```

スコアの値が JSON 文字列として提供されるため、結合された出力には数値がそのまま保持されます。

```
95-88-76-100-67
```

{{% alert color="note" %}}
Java エンジンを介して渡された JSON の数値は倍精度浮動小数点数になるため、`[95, 88]` は `95.0-88.0` として結合されます。結合したセルに正確な整数のテキストを表示したい場合は、JSON 行で数値を引用符で囲んでください。
{{% /alert %}}

### **コード例 3 — 既定のレンダリングと単一セルレンダリングの比較**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const cells = workbook.getWorksheets().get(0).getCells();
// Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default");
cells.get("B2").putValue("&=Order.Items");
// Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell");
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]');
designer.process();
for (let row = 1; row <= 5; row++) {
    const b = cells.get(row, 1).getStringValue() || "";
    const c = cells.get(row, 2).getStringValue() || "";
    if (b || c) console.log(`B${row + 1}=[${b}]  C${row + 1}=[${c}]`);
}
workbook.save("output-array-comparison.xlsx");
```

既定のマーカーは列 B に各要素を 1 セルずつ縦に配置しますが、`arrayassingle` マーカーは同じ配列を列 C の 1 つのセルにまとめます。

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **注記とベストプラクティス**

`arrayassingle` 属性と `arraydelimiter` 属性を使用する際は、次の点に注意してください。
- 属性値は `name:value` 形式を使用します。`arrayassingle=true` のような等号形式は認識されず、警告なく既定の展開動作にフォールバックします。
- 属性はカンマで区切り、スペースを入れません。カンマの後のスペースによって区切り文字の値が 1 文字分ずれます（上記の警告を参照してください）。
- `arraydelimiter` の値は、コロンの直後に直接記述した 1 文字、または二重引用符で囲んだ複数文字文字列にできます。
- `arraydelimiter` を省略すると、要素はカンマで結合されます。
- 配列フィールドは `setJsonDataSource` の行オブジェクトで提供してください。このプラットフォームでは、`setDataSource` に渡されたプレーンな JavaScript オブジェクトと配列はバインドされません。
- Java エンジンを介した JSON の数値は倍精度浮動小数点数として到着します（`95` は `95.0` として結合されます）。正確な整数テキストが必要な場合は、JSON 行で数値を引用符で囲んでください。
- 結果の連結文字列を表示できる幅が十分に大きいセルにスマートマーカーを配置してください。書式に応じて、コンテンツが隣接するセルに視覚的にあふれる場合があります。

## 関連記事
- [Aspose.Cells for Node.js via Java でピボットテーブルにフィルターフィールドを追加する](/cells/ja/nodejs-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via Java でピボットテーブルにスタイルを適用する](/cells/ja/nodejs-java/apply-style-to-pivot-table/)
- [ピボットテーブルのページフィールドレイアウトを変更する](/cells/ja/nodejs-java/change-page-field-layout/)
- [Aspose.Cells for Node.js via Java でスパークラインを画像および HTML に変換する](/cells/ja/nodejs-java/convert-sparkline-to-image-and-html/)
- [Excel を OFD 形式に変換する](/cells/ja/nodejs-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="nodejs-java" >}}