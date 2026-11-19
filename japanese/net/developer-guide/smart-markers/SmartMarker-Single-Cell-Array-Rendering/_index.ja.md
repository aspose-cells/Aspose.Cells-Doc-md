---
title: SmartMarker 単一セル配列レンダリング | Aspose.Cells .NET
description: Aspose.Cells for .NET の arrayassingle および arraydelimiter Smart Marker 属性を使用して、配列データを1つのセルにレンダリングする方法を学びます。
linktitle: SmartMarker 単一セル配列レンダリング | Aspose.Cells
url: /ja/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, .NET ライブラリ, スプレッドシート, スマートマーカー, arrayassingle, arraydelimiter, 単一セル配列, 配列レンダリング, テンプレート
type: docs
weight: 195
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、Smart Marker を通じて配列データソースを1つのセルにレンダリングできます。`arrayassingle` 属性は既定の要素ごとの展開を無効にし、`arraydelimiter` 属性は結合された要素の間に配置する区切り文字を選択します。デフォルトはカンマですが、指定した任意の1文字、または引用符で囲んだ複数文字の文字列を使用できます。
{{% /alert %}}

## **はじめに**

Aspose.Cells の Smart Marker は、`&=DataSource.Field` などのマーカー式を使用して、スプレッドシートのデータを動的に設定するテンプレートベースの機能です。マーカーをデザイナー用ワークブックに配置し、テンプレートを `WorkbookDesigner` で処理すると、マーカーは指定したデータソースの値に置き換えられます。
既定では、Smart Marker が配列プロパティを参照する場合（例: 4つの値を持つ `string[]` にバインドされた `&=Product.Tags`）、エンジンは配列を展開し、各要素を個別のセルに配置します。値はマーカーの下にある列に沿って垂直方向に広がります。この動作は多くのシナリオで便利ですが、配列全体を1つのセルにレンダリングし、要素を連結して任意の区切り文字で区切りたい場合もあります。
`arrayassingle` と `arraydelimiter` 属性は、Smart Marker の括弧内に `name:value` 形式で記述すると、この要件に正確に対応します。レポートレイアウトをコンパクトかつ予測可能な状態に保ちながら、配列データソースをネイティブに扱えます。

## **この機能が必要な理由**

### **既定の配列展開動作**

Smart Marker が配列プロパティを参照すると、Aspose.Cells は既定で配列を複数セルに展開します。たとえば、4つの値を含む `string[]` に対して `&=Product.Tags` のようなマーカーを使用すると、各値がマーカーの下の個別のセルに配置されます。これにより他のテンプレートコンテンツが押し広げられ、慎重に設計したレポートレイアウトが崩れる可能性があります。

### **ユースケース上の制約**

既定の展開動作が望ましくない実際のシナリオは多数あります。
- **サマリー形式のレポート**: 1レコードにつき1行のコンパクトなレイアウトが必要な場合。
- **タグ、ラベル、キーワードのリスト**: 単一セル内でカンマ区切りまたはパイプ区切りの値として表示する必要がある場合。
- **フィルターチップまたはステータス表示**: 可読性のため、複数の値を1か所にまとめる場合。
- **後続処理パイプライン**（CSV エクスポート、PDF レンダリング、メールマージ）: 展開された範囲ではなく、セルごとに1つの統合された値を必要とする場合。
- **クロスプラットフォーム互換性**: 一部の利用者が複数セルにまたがる配列を扱えない場合。

### **この機能が埋めるギャップ**

組み込み.mechanismがない場合、開発者は C# または VB.NET でデータを事前処理し、配列を区切り文字付き文字列に結合してから `WorkbookDesigner` にバインドする必要がありました。これではロジックが複製され、データモデルが複雑になり、エラーの発生確率も高まります。`arrayassingle` と `arraydelimiter` 属性は、Smart Marker 内|formatを宣言的に処理するため、この回避策が不要になります。

## **機能の利点**

Smart Marker で `arrayassingle` と `arraydelimiter` 属性を使用すると、次の利点があります。
- **単一セルへの格納**: すべての配列要素が厳密に1つのセルにレンダリングされ、レイアウトをコンパクトかつ予測可能な状態に保てます。
- **区切り文字のカスタマイズ**: 既定のカンマ、セミコロン、ハイフン、パイプ、または `" | "` のような引用符で囲んだ複数文字の文字列など、任意の区切り文字を指定できます。
- **テンプレート駆動の書式設定**: データを事前処理するための追加コードは不要です。書式設定規則は Smart Marker タグ内に記述されます。
- **よりクリーンなレポート**: 配列データによって、隣接するテンプレートコンテンツが異なる行や列に押し広げられることがなくなります。
- **多様なデータ型**: オブジェクトデータソースの文字列配列と数値配列で動作します。
- **後方互換性**: 属性を省略すると従来の展開動作が維持されるため、既存のテンプレートは変更 없이引き続き動作します。

## **この機能の使用方法**

### **Smart Marker の構文**

`arrayassingle` と `arraydelimiter` 属性は、標準の Smart Marker の括弧内で Aspose.Cells の `name:value` 属性文法を使用します。一般的な構文は次のとおりです。

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

マーカーは次の要素で構成されます。
- `&=DataSource.ArrayProperty` — バインドされたデータソース上の配列プロパティを参照する標準の Smart Marker です。
- `arrayassingle:true` — 要素を展開する代わりに、配列全体を1つのセルにレンダリングするようエンジンに指示します。
- `arraydelimiter:;` — 省略可能な属性で、配列要素間に配置される区切り文字を定義します。省略した場合はカンマが使用されます。

{{% alert color="warning" %}}
属性は `name:value` 形式（等号ではなくコロン）で記述し、複数の属性は**スペースなし**でカンマ区切りにします。カンマの後のスペースにより、解析される値が1文字分ずれます。`(arrayassingle:true, arraydelimiter:;)` の場合、誤った区切り文字 `:;` で結合され、`;` にはなりません。
{{% /alert %}}

### **区切り文字の形式**

- 1文字の区切り文字は、コロンの直後に直接記述します: `arraydelimiter:;`、`arraydelimiter:-`、`arraydelimiter:*`。
- 複数文字の区切り文字は、二重引用符で囲んで記述します: `arraydelimiter:" | "`、`arraydelimiter:" - "`。

### **段階的な手順**

Smart Marker を使用して配列を1つのセルにレンダリングする方法を、次の手順で説明します。
1. **データソースを準備します**: `string[]` や `int[]` などの配列を返すプロパティを持つクラスを作成し、そのクラスの `List<T>` をバインドして、エンジンが1行につき1件のレコードを読み取れるようにします。
2. **デザイナー用ワークブックを作成します**: 新しい `Workbook` を作成し、ヘッダー行を追加します。次に、配列プロパティを参照し、`arrayassingle` 属性を指定した Smart Marker セルを追加します。カスタム区切り文字が必要な場合は `arraydelimiter` も指定します。
3. **`WorkbookDesigner` をインスタンス化します**: ワークブックを対象に `WorkbookDesigner` を作成し、`SetDataSource` でデータソースをバインドします。
4. **マーカーを処理します**: `WorkbookDesigner.Process()` メソッドを呼び出し、Smart Marker を展開して実際のデータでワークブックを設定します。
5. **結果を保存します**: 結果のワークブックを XLSX、またはその他のサポートされているファイル形式でディスクに保存します。

### **コード例1 — 基本的な文字列配列のレンダリング**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Product
    {
        public string[] Tags { get; set; }
    }

    static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Product", new List<Product> { product });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-single.xlsx");
    }
}
```

この例では、配列全体を結合した値を出力します。4つのタグは、既定のカンマで区切られ、1つのセルに配置されます。

```
C#,Aspose,SmartMarker,Excel
```

### **コード例2 — カスタム区切り文字 specifying 数値配列**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Student
    {
        public int[] Scores { get; set; }
    }

    static void Main()
    {
        Student student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Scores");
        // arraydelimiter:- joins the numbers with a hyphen
        worksheet.Cells["A2"].PutValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Student", new List<Student> { student });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-numeric.xlsx");
    }
}
```

数値配列は文字列配列と同じように結合され、各要素は単純な数値テキストとして保持されます。

```
95-88-76-100-67
```

### **コード例3 — 既定の動作と単一セルレンダリングの比較**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Order
    {
        public string[] Items { get; set; }
    }

    static void Main()
    {
        Order order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        Cells cells = sheet.Cells;
        // Column B: default marker — values spread vertically down the column
        cells["B1"].PutValue("Default");
        cells["B2"].PutValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells["C1"].PutValue("Single cell");
        cells["C2"].PutValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", new List<Order> { order });
        designer.Process();
        for (int row = 1; row <= 5; row++)
        {
            string b = cells[row, 1].StringValue;
            string c = cells[row, 2].StringValue;
            if (!string.IsNullOrEmpty(b) || !string.IsNullOrEmpty(c))
                Console.WriteLine($"B{row + 1}=[{b}]  C{row + 1}=[{c}]");
        }
        workbook.Save("output-array-comparison.xlsx");
    }
}
```

既定のマーカーは B 列で要素ごとに1つのセルを設定しますが、`arrayassingle` マーカーは同じ配列を C 列の1つのセルにまとめます。

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **注記とベストプラクティス**

`arrayassingle` と `arraydelimiter` 属性を使用する場合は、次の点に注意してください。
- 属性値は `name:value` 形式です。`arrayassingle=true` のような等号形式は認識されず、警告なく既定の展開動作にフォールバックします。
- 複数の属性は、スペースなしでカンマ区切りにします。カンマの後のスペースにより、区切り文字の値が1文字分ずれます（上の警告を参照してください）。
- `arraydelimiter` の値は、コロンの直後に直接記述した1文字、または二重引用符で囲んだ複数文字の文字列にできます。
- `arraydelimiter` を省略すると、要素はカンマで結合されます。
- データソースでは、エンジンがレコードを列挙できるようにする必要があります。要素の型が配列プロパティを公開する `List<T>`（またはその他のコレクション）をバインドしてください。単一オブジェクトをバインドすると、本文のマーカーは未解決のままになります。
- 同じ属性を文字列配列と数値配列に使用できます。各要素は、その値の単純なテキストとしてレンダリングされます。

## 関連記事
- [Aspose.Cells for .NET でピボットテーブルにフィルターフィールドを追加する](/cells/ja/net/add-page-field-in-pivot-table/)
- [Aspose.Cells for .Net でピボットテーブルにスタイルを適用](/cells/ja/net/apply-style-to-pivot-table/)
- [ピボットテーブルのページフィールドレイアウトを変更する](/cells/ja/net/change-page-field-layout/)
- [Aspose.Cells for .NET でスパークラインを画像および HTML に変換する](/cells/ja/net/convert-sparkline-to-image-and-html/)
- [Excel を OFD 形式に変換する](/cells/ja/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}