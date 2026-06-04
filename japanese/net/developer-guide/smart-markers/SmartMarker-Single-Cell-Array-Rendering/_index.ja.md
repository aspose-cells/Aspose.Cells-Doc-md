---
title: SmartMarker 単一セル配列のレンダリング | Aspose.Cells .NET
description: Aspose.Cells for .NET の Smart Markers における ArrayAsSingle および ExtraDelimiter 属性を使用して、配列データを単一セルにレンダリングする方法を学習します。
keywords: Aspose.Cells, .NET ライブラリ, スプレッドシート, Smart Markers, ArrayAsSingle, ExtraDelimiter, 単一セル配列, 配列レンダリング, テンプレート
type: docs
weight: 195
url: /ja/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells は、Smart Markers を介して配列データを単一セルにレンダリングすることをサポートしています。`ArrayAsSingle` 属性と `ExtraDelimiter` 属性を併用することで、開発者は単一セル内の配列要素の区切り方法を制御でき、レポートやテンプレートの柔軟な書式設定が可能になります。

{{% /alert %}}

## **はじめに**

Aspose.Cells の Smart Markers は、`&=DataSource.Field` などのマーカー式を使用してスプレッドシートのデータを動的に入力できる、強力なテンプレートベースの機能です。マーカーはデザイナーワークブックに配置され、テンプレートが `WorkbookDesigner` によって処理されると、マーカーは指定されたデータソースからの値に置き換えられます。

デフォルトでは、Smart Marker が配列プロパティ（例えば `&=DataSource.Numbers`）を参照する場合、エンジンは配列を展開し、各要素を隣接する別々のセルに配置します — 行方向に水平に、または列方向に垂直に配置します。この動作は多くのシナリオで便利ですが、配列全体を 1 つのセルにレンダリングし、要素を連結して任意の区切り文字で区切りたい状況もあります。

Smart Marker タグ内で併用される `ArrayAsSingle` 属性と `ExtraDelimiter` 属性は、まさにこの要件に対応します。これらの属性により、レポートのレイアウトをコンパクトで予測可能な状態に保ちながら、配列データソースをネイティブに操作できます。

## **この機能が必要な理由**

### **デフォルトの配列展開動作**

Smart Marker が配列プロパティを参照する場合、Aspose.Cells はデフォルトで配列を複数のセルにわたって展開します。例えば、`string[]` 型の 4 つの値を含む `&=Product.Tags` のようなマーカーは、各値をそれぞれのセルに配置し、他のテンプレートコンテンツを押し出し、慎重に設計されたレポートレイアウトを破損させる可能性があります。

### **ユースケースの制限**

デフォルトの展開動作が望ましくない、多くの実践的なシナリオが存在します：

- レコードごとに 1 行のコンパクトなレイアウトを必要とする**サマリースタイルのレポート**。
- 単一セル内にカンマ区切りまたはパイプ区切りの値として表示する必要がある**タグ、ラベル、キーワードリスト**。
- 読みやすさのために複数の値を 1 か所にグループ化する**フィルタチップやステータスインジケーター**。
- 拡張された範囲ではなく、セルごとに単一の統合値を期待する**下流のパイプライン**（CSV エクスポート、PDF レンダリング、メールマージ）。
- 一部のコンシューマが複数のセルにまたがる配列を許容しない、**クロスプラットフォームの互換性**。

### **解消されるギャップ**

組み込みのメカニズムがなければ、開発者は C# や VB.NET でデータを前処理し、配列を区切り文字列に結合してからワークブックデザイナーにバインドすることを強いられます。これによりロジックが重複し、データモデルが複雑になり、エラーの可能性が増加します。`ArrayAsSingle` 属性と `ExtraDelimiter` 属性は、Smart Marker 自体の中で宣言的に書式設定を処理することで、この回避策を不要にします。

## **機能のメリット**

Smart Markers で `ArrayAsSingle` 属性と `ExtraDelimiter` 属性を使用すると、いくつかの利点があります：

- **単一セルへの格納**：すべての配列要素が正確に 1 つのセルにレンダリングされ、レイアウトがコンパクトで予測可能な状態に保たれます。
- **カスタム区切り文字の制御**：カンマ、セミコロン、ハイフン、パイプ、改行、カスタムテキストなど、任意の区切り文字列を指定できます。
- **テンプレート駆動の書式設定**：データを前処理するための追加コードは不要で、書式設定ルールは Smart Marker タグ内に存在します。
- **クリーンなレポート**：配列データが隣接するテンプレートコンテンツを別の行や列に押し出すことがなくなります。
- **汎用的なデータ型**：文字列、数値、日付など、区切り文字で結合可能なあらゆるデータ型で機能します。
- **後方互換性**：属性を省略した場合、元の展開動作が維持されるため、既存のテンプレートは変更されず動作し続けます。

## **この機能の使用方法**

### **Smart Marker の構文**

`ArrayAsSingle` 属性と `ExtraDelimiter` 属性は、標準の Smart Marker の括弧内にキーと値のペアとして渡されます。一般的な構文は次のとおりです：

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

マーカーは以下の部分で構成されています：

- `&=DataSource.ArrayProperty` — バインドされたデータソース上の配列プロパティを参照する標準の Smart Marker。
- `arrayasSingle=true` — 配列全体を単一セルにレンダリングするようエンジンに指示します。値 `true` のみが単一セル動作をトリガーします。
- `extraDelimiter=", "` — 配列要素間に配置される区切り文字を定義します。値は文字列リテラルであり、空文字列、単一文字、または複数文字の文字列が可能です。

{{% alert color="primary" %}}

`extraDelimiter` 属性は、複数文字の区切り文字、カスタムテキスト、改行で区切られた出力のための `\n` などのエスケープシーケンスを含む、任意の文字列リテラルを受け入れます。配列が空の場合、結果のセルは空白のままになります。

{{% /alert %}}

### **ステップバイステップのワークフロー**

以下のワークフローは、Smart Markers を使用して配列を単一セルにレンダリングする方法を説明しています。

1. **データソースの準備**：配列を返すプロパティを公開するクラス（またはデータ構造）を作成します。プロパティは `string[]`、`int[]`、またはその他のサポートされる配列型を返すことができます。
2. **デザイナーワークブックの作成**：新しい `Workbook` を作成し、ヘッダー行を追加して、`arrayasSingle` 属性と `extraDelimiter` 属性を備えた配列プロパティを参照する Smart Marker セルを配置します。
3. **WorkbookDesigner のインスタンス化**：`WorkbookDesigner` オブジェクトを作成し、デザイナーワークブックをアタッチして、`SetDataSource` メソッドを使用してデータソースをバインドします。
4. **マーカーの処理**：`WorkbookDesigner.Process()` メソッドを呼び出して、Smart Markers を展開し、実際のデータでワークブックを入力します。
5. **結果の保存**：結果のワークブックを XLSX またはその他のサポートされるファイル形式でディスクに保存します。

### **コード例 1 — 基本的な文字列配列のレンダリング**

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

### **コード例 2 — カスタム区切り文字を使用した数値配列**

```csharp
using System;
using Aspose.Cells;

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
        worksheet.Cells["A2"].PutValue("&=Student.Scores(arrayasSingle=true, extraDelimiter=\" - \")");

        var designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Student", student);
        designer.Process();

        workbook.Save("output_numericArray.xlsx");
    }
}
```

### **コード例 3 — デフォルト動作と ArrayAsSingle 動作の比較**

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

        // セクション 1: デフォルトのスマートマーカー - 値がセルに水平方向に展開される
        cells["A1"].PutValue("Default Spreading Behavior:");
        cells["A2"].PutValue("&=Order.Items");

        // セクション 2: arrayasSingleとextraDelimiterを使用した新しい単一セルレンダリング
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

### **注意事項とベストプラクティス**

`ArrayAsSingle` 属性と `ExtraDelimiter` 属性を扱う際は、以下の点に留意してください：

- `extraDelimiter` の値は文字列リテラルとして扱われます。テンプレートプロセッサが解釈する可能性のある特殊文字はエスケープしてください。
- `arrayasSingle` 属性はブール値（`true` / `false`）を受け入れます。`true` のみが単一セル動作をトリガーし、その他の値はデフォルトの展開動作にフォールバックします。
- 配列が空または null の場合、セルは空のままになります（またはデータ型に応じて空文字列が含まれます）。
- この機能はオブジェクトデータソースだけでなく、列を配列に分割できる `DataSet` および `DataTable` ソースでも機能します。
- 改行区切りの出力には、区切り値として `\n` または `Environment.NewLine` を使用できます。
- 結果の連結文字列を表示するのに十分な幅のあるセルに Smart Marker を配置してください。そうでない場合、形式によってはコンテンツが視覚的に隣接セルにオーバーフローする可能性があります。

## **関連記事**

- [Smart Markers](/cells/ja/net/smart-markers/)
- [セルの結合と結合解除](/cells/ja/net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="csharp" >}}