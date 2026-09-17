---
title: SmartMarker 単一セル配列レンダリング | Aspose.Cells .NET
linktitle: SmartMarker 単一セル配列レンダリング | Aspose.Cells .NET
description: Aspose.Cells for .NET の Smart Markers における ArrayAsSingle および ExtraDelimiter 属性を使用して、配列データを単一セルにレンダリングする方法を学びます。
keywords: Aspose.Cells, .NET ライブラリ, スプレッドシート, Smart Markers, ArrayAsSingle, ExtraDelimiter, 単一セル配列, 配列レンダリング, テンプレート
type: docs
weight: 195
url: /ja/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は Smart Markers 経由で配列データを単一セルにレンダリングすることをサポートしています。`ArrayAsSingle` 属性と `ExtraDelimiter` 属性を併用することで、開発者は単一セル内での配列要素の区切り方を制御でき、レポートやテンプレートの柔軟な書式設定を実現できます。
{{% /alert %}}

## **Introduction**
Aspose.Cells の Smart Markers は強力なテンプレートベースの機能であり、`&=DataSource.Field` のようなマーカー式を使用してスプレッドシートのデータを動的に入力することができます。マーカーはデザイナー ワークブック内に配置され、テンプレートが `WorkbookDesigner` によって処理されると、マーカーは指定されたデータソースからの値に置き換えられます。
デフォルトでは、Smart Marker が配列プロパティ（例えば `&=DataSource.Numbers`）を参照すると、エンジンは配列を展開し、各要素を隣接する別々のセルに配置します（行方向に水平に、または列方向に垂直に展開されます）。この動作は多くのシナリオで便利ですが、配列全体を 1 つのセルにレンダリングし、要素を連結して任意の区切り文字で区切りたい場合もあります。
Smart Marker タグ内で併用される `ArrayAsSingle` および `ExtraDelimiter` 属性は、まさにこの要件に対応します。これらの属性により、配列データソースをネイティブに扱いながら、レポートのレイアウトをコンパクトで予測可能に保つことができます。

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
Smart Marker が配列プロパティを参照すると、Aspose.Cells はデフォルトで配列を複数のセルにわたって展開します。例えば、4 つの値を含む `string[]` に対する `&=Product.Tags` のようなマーカーは、各値をそれぞれのセルに配置し、他のテンプレートコンテンツを押し出して、慎重に設計されたレポートレイアウトを破壊する可能性があります。

### **Use Case Limitations**
デフォルトの展開動作が望ましくない実用的なシナリオは数多く存在します。
- **サマリー形式のレポート** — レコードごとに 1 行のコンパクトなレイアウトが必要な場合。
- **タグ、ラベル、キーワードリスト** — 単一セル内にカンマ区切りやパイプ区切りで値を表示する必要がある場合。
- **フィルターチップやステータスインジケーター** — 読みやすさのために複数の値を 1 か所にグループ化する場合。
- **下流のパイプライン** (CSV エクスポート、PDF レンダリング、メールマージ) — 展開された範囲ではなく、セルごとに単一の統合された値を期待する場合。
- **クロスプラットフォーム互換性** — 一部のコンシューマーでは複数のセルにまたがる配列を許容できない場合。

### **The Gap It Fills**
組み込みの仕組みがなければ、開発者は C# や VB.NET でデータを前処理し、ワークブックデザイナーにバインドする前に配列を区切り文字列に結合せざるを得ません。これによりロジックが重複し、データモデルが複雑化し、エラーの可能性が増加します。`ArrayAsSingle` および `ExtraDelimiter` 属性は、Smart Marker 自体の中で宣言的に書式設定を処理することで、この回避策を不要にします。

## **Feature Benefits**
Smart Markers で `ArrayAsSingle` および `ExtraDelimiter` 属性を使用すると、いくつかの利点があります。
- **単一セル格納**：すべての配列要素が正確に 1 つのセルにレンダリングされ、レイアウトがコンパクトで予測可能になります。
- **カスタム区切り文字の制御**：カンマ、セミコロン、ハイフン、パイプ、改行、カスタムテキストなど、任意の区切り文字列を指定できます。
- **テンプレート駆動の書式設定**：データを前処理するための追加コードは不要で、書式設定ルールは Smart Marker タグ内に記述されます。
- **クリーンなレポート**：配列データが隣接するテンプレートコンテンツを異なる行や列に押し出すことがなくなります。
- **多様なデータ型**：文字列、数値、日付など、区切り文字で結合可能なあらゆるデータ型に対応します。
- **後方互換性**：属性を省略した場合、元の展開動作が保持されるため、既存のテンプレートは変更なしで動作し続けます。

## **How to Use This Feature**

### **Smart Marker Syntax**
`ArrayAsSingle` および `ExtraDelimiter` 属性は、標準の Smart Marker の括弧内にキーと値のペアとして渡されます。一般的な構文は次のとおりです。

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

マーカーは以下の部分で構成されています。
- `&=DataSource.ArrayProperty` — バインドされたデータソースの配列プロパティを参照する標準の Smart Marker。
- `arrayasSingle=true` — エンジンに対して配列全体を単一セルにレンダリングするように指示します。`true` の値のみが単一セル動作をトリガーします。
- `extraDelimiter=", "` — 配列要素間に配置される区切り文字を定義します。値は文字列リテラルであり、空、単一文字、複数文字の文字列が可能です。

{{% alert color="primary" %}}
`extraDelimiter` 属性は、複数文字の区切り文字、カスタムテキスト、改行区切り出力用の `\n` などのエスケープシーケンスを含む任意の文字列リテラルを受け入れます。配列が空の場合、結果のセルは空白のままになります。

### **Step-by-Step Workflow**
以下のワークフローでは、Smart Markers を使用して配列を単一セルにレンダリングする方法を説明します。
1. **データソースの準備**：配列を返すプロパティを公開するクラス（またはデータ構造）を作成します。プロパティは `string[]`、`int[]`、またはその他のサポートされている配列型を返すことができます。
2. **デザイナー ワークブックの作成**：新しい `Workbook` を作成し、ヘッダー行を追加し、`arrayasSingle` および `extraDelimiter` 属性を指定した配列プロパティを参照する Smart Marker セルを配置します。
3. **WorkbookDesigner のインスタンス化**：`WorkbookDesigner` オブジェクトを作成し、デザイナー ワークブックをアタッチし、`SetDataSource` メソッドを使用してデータソースをバインドします。
4. **マーカーの処理**：`WorkbookDesigner.Process()` メソッドを呼び出して Smart Markers を展開し、ワークブックに実際のデータを入力します。
5. **結果の保存**：結果のワークブックを XLSX またはその他のサポートされているファイル形式でディスクに保存します。

### **Code Example 1 — Basic String Array Rendering**

```csharp
using System;
using Aspose.Cells;
class Program
{
    public class Product
    {
        public string[] Tags { get; set; }
    }
    public static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Tags");
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");
        WorkbookDesigner designer = new WorkbookDesigner();
        designer.Workbook = workbook;
        designer.SetDataSource("Product", product);
        designer.Process();
        workbook.Save("output_arraySingle.xlsx");
    }
}
```

### **Code Example 2 — Numeric Array with Custom Delimiter**

```csharp
public class Student
{
    public int[] Scores { get; set; }
}
public class Program
{
    public static void Main()
    {
        var student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };
        var workbook = new Workbook();
        var worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Scores");
        worksheet.Cells["A2"].PutValue(string.Join(" - ", student.Scores));
        workbook.Save("output_numericArray.xlsx");
    }
}
```

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

```csharp
using System;
using Aspose.Cells;
public class Program
{
    public static void Main()
    {
        var order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };
        var workbook = new Workbook();
        var sheet = workbook.Worksheets[0];
        var cells = sheet.Cells;
        // セクション1: デフォルトのスマートマーカー - 値がセルに水平方向に展開される
        cells["A1"].PutValue("Default Spreading Behavior:");
        cells["A2"].PutValue("&=Order.Items");
        // セクション2: arrayasSingle と extraDelimiter を使用した新しい単一セルレンダリング
        cells["A4"].PutValue("Single Cell Rendering (arrayasSingle=true):");
        cells["A5"].PutValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");
        // データソースをバインドし、スマートマーカーを処理する
        var designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", order);
        designer.Process();
        // 結果のワークブックを保存する
        workbook.Save("output_comparison.xlsx");
    }
}
public class Order
{
    public string[] Items { get; set; }
}
```

### **Notes & Best Practices**
`ArrayAsSingle` および `ExtraDelimiter` 属性を使用する際は、以下の点に留意してください。
- `extraDelimiter` の値は文字列リテラルとして扱われます。テンプレートプロセッサが解釈する可能性のある特殊文字はエスケープしてください。
- `arrayasSingle` 属性はブール値（`true` / `false`）を受け入れます。`true` のみが単一セル動作をトリガーし、その他の値はデフォルトの展開動作にフォールバックします。
- 配列が空または null の場合、セルは空になります（データ型に応じて空文字列が含まれる場合もあります）。
- この機能はオブジェクトデータソースだけでなく、列を配列に分割できる `DataSet` および `DataTable` ソースでも動作します。
- 改行区切りの出力には、区切り文字の値として `\n` または `Environment.NewLine` を使用できます。
{{% /alert %}}

## Related Articles
- [Aspose.Cells for .NET でピボットテーブルにフィルターフィールドを追加する](/cells/ja/net/add-page-field-in-pivot-table/)
- [Aspose.Cells for .NET でピボットテーブルにスタイルを適用する](/cells/ja/net/apply-style-to-pivot-table/)
- [ピボットテーブルのページフィールドのレイアウトを変更する](/cells/ja/net/change-page-field-layout/)
- [Aspose.Cells for .NET でスパークラインを画像と HTML に変換する](/cells/ja/net/convert-sparkline-to-image-and-html/)
- [Excel を OFD 形式に変換する](/cells/ja/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}