---
title: Aspose.Cells for Java におけるスマートマーカーの単一セル配列レンダリング
description: Aspose.Cells for Java の arrayassingle および arraydelimiter スマートマーカー属性を使って、配列データを単一セルにレンダリングする方法を学びます。
linktitle: スマートマーカーの単一セル配列レンダリング | Aspose.Cells
url: /ja/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Java ライブラリ, スプレッドシート, スマートマーカー, arrayassingle, arraydelimiter, 単一セル配列, 配列レンダリング, テンプレート
type: docs
weight: 195
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells では、スマートマーカーを通じて配列データソースを単一セルにレンダリングできます。`arrayassingle` 属性は既定の要素ごとの展開を無効にし、`arraydelimiter` 属性は結合された要素の間に配置される区切り文字を選択します。デフォルトはカンマですが、指定した任意の 1 文字、または引用符で囲んだ複数文字の文字列も使用できます。
{{% /alert %}}

## **導入**

Aspose.Cells のスマートマーカーは、`&=DataSource.Field` などのマーカー式を使用して、テンプレートに基づいてスプレッドシートにデータを動的に設定する機能です。マーカーをデザイナワークブックに配置し、テンプレートを `WorkbookDesigner` で処理すると、マーカーが指定されたデータソースの値に置き換えられます。
既定では、スマートマーカーが配列プロパティを参照する場合（たとえば、4 つの値を持つ `String[]` にバインドされた `&=Product.Tags`）、エンジンは配列を展開し、各要素を個別のセルに配置して、マーカーの下の列に値を縦方向に展開します。この動作は多くのシナリオでは便利ですが、配列全体を 1 つのセルにレンダリングし、要素を連結して任意の区切り文字で区切geist in wanted cases があります。
`arrayassingle` と `arraydelimiter` 属性は、スマートマーカーの括弧内に `name:value` 形式で記述することで、この要件に正確に対応します。配列データソースをネイティブに扱いつつ、レポートレイアウトをコンパクトで予測可能な状態に保てます。

## **この機能が必要な理由**

### **既定の配列展開動作**

スマートマーカーが配列プロパティを参照すると、Aspose.Cells は既定で配列を複数のセルに展開します。たとえば、4 つの値を含む `String[]` に対して `&=Product.Tags` のようなマーカーを使用すると、各値がマーカーの下にある個別のセルに配置され、他のテンプレート内容を押し出して、慎重に設計されたレポートレイアウトを崩す可能性があります。

### **ユースケースの制限**

既定の展開動作が望ましくない実用的なシナリオは多数あります。
- **サマリー形式のレポート**: レコードごとに 1 行というコンパクトなレイアウトが必要な場合。
- **タグ、ラベル、またはキーワードのリスト**: 値をカンマ区切りまたはパイプ区切りで 1 つのセル内に表示する必要がある場合。
- **フィルター条件やステータスインジケーター**: 可読性のため複数の値を 1 か所にまとめて表示する場合。
- **後続のパイプライン**（CSV エクスポート、PDF レンダリング、メールマージ）: 展開された範囲ではなく、セルごとに 1 つの統合された値を必要とする場合。
- **クロスプラットフォームの互換性**: 一部の利用側では、複数セルにまたがる配列を扱えない場合。

### **解決される課題**

組み込みのメカニズムがない場合、開発者は Java でデータを前処理し、ワークブックデザイナーにバインドする前に配列を区切り文字付き文字列に結合不得不れませんでした。これではロジックが重複し、データモデルが複雑になり、エラーの発生率も高まります。`arrayassingle` と `arraydelimiter` 属性は、スマートマーカー自体の中で書式を宣言的に処理することで、この回避策を必要なくします。

## **機能上の利点**

スマートマーカーで `arrayassingle` と `arraydelimiter` 属性を使用すると、いくつかの利点があります。
- **単一セルへの格納**: すべての配列要素がちょうど 1 つのセルにレンダリングされ、レイアウトがコンパクトで予測可能になります。
- **区切り文字のカスタマイズ**: 既定のカンマ、セミコロン、ハイフン、パイプ、または `" | "` のような引用符で囲んだ複数文字の文字列など、任意の区切り文字を指定できます。
- **テンプレートによる書式設定**: データを前処理する追加のコードは不要で、書式設定ルールはスマートマーカータグ内に記述されます。
- **より整然としたレポート**: 配列データによって、隣接するテンプレート内容が別の行や列へ押し出されることはなくなりました。
- **柔軟なデータ型**: 文字列配列と、JavaBean データソースから文字列としてレンダリングされる数値に対応します。
- **後方互換性**: 属性を省略すると従来の展開動作が維持されるため、既存のテンプレートは変更 없이動作し続けます。

## **この機能の使用方法**

### **スマートマーカーの構文**

`arrayassingle` と `arraydelimiter` 属性は、標準のスマートマーカーの括弧内で Aspose.Cells の `name:value` 属性文法を使用します。一般的な構文は次のとおりです。

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

マーカーは次の要素で構成されます。
- `&=DataSource.ArrayProperty` — バインドされたデータソース上の配列プロパティを参照する標準のスマートマーカー。
- `arrayassingle:true` — 要素を展開するのではなく、配列全体を単一セルにレンダリングするようエンジンに指示します。
- `arraydelimiter:;` — 省略可能。配列要素の間に配置される区切り文字を定義します。省略するとカンマが使用されます。

{{% alert color="warning" %}}
属性は `name:value` 形式（等号ではなくコロン）で記述し、複数の属性は**スペースを入れずに**カンマで区切ります。カンマの後のスペースは解析される値を 1 文字ずらします。`(arrayassingle:true, arraydelimiter:;)` は、`;` ではなく誤った区切り文字 `:;` で結合してしまいます。
{{% /alert %}}

### **区切り文字の形式**

- 単一文字の場合はコロンの直後に直接記述します: `arraydelimiter:;`、`arraydelimiter:-`、`arraydelimiter:*`。
- 複数文字の区切り文字は二重引用符で囲みます: `arraydelimiter:" | "`、`arraydelimiter:" - "`。

### **手順別ワークフロー**

次のワークフローで、スマートマーカーを使用して配列を単一セルにレンダリングする方法を説明します。
1. **データソースの準備**: 配列を返すゲッター（たとえば `String[] getTags()`）を持つ `public` JavaBean クラスを作成し、JavaBean の `java.util.List` をバインドして、エンジンが 1 行につき 1 レコードを読み取れるようにします。public フィールドのみではバインドされません。エンジンは JavaBean のゲッターを読み取ります。
2. **デザイナワークブックの作成**: 新しい `Workbook` を作成し、ヘッダー行を追加して、配列プロパティを参照する `arrayassingle` 属性（必要に応じてカスタム区切り文字を指定する `arraydelimiter`）を持つスマートマーカーのセルを配置します。
3. **WorkbookDesigner のインスタンス化**: ワークブックをラップする `WorkbookDesigner` を作成し、`setDataSource` でリストをバインドします。
4. **マーカーの処理**: `WorkbookDesigner.process()` メソッドを呼び出して、スマートマーカーを展開し、ワークブックに実際のデータを設定します。
5. **結果の保存**: 生成されたワークブックを XLSX、またはその他の対応ファイル形式でディスクに保存します。

### **コード例 1 — 基本的な文字列配列のレンダリング**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    // The bean must be public and expose a getter; public fields bind nothing
    public static class Product {
        private String[] tags;
        public String[] getTags() { return tags; }
        public void setTags(String[] tags) { this.tags = tags; }
    }

    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.setTags(new String[] { "C#", "Aspose", "SmartMarker", "Excel" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Product", Arrays.asList(product));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-single.xlsx");
    }
}
```

この例では、配列全体の結合値が出力されます。4 つのタグは、既定のカンマで区切られ、1 つのセルに配置されます。

```
C#,Aspose,SmartMarker,Excel
```

### **コード例 2 — カスタム区切り文字付きの数値**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Student {
        private String[] scores;
        public String[] getScores() { return scores; }
        public void setScores(String[] scores) { this.scores = scores; }
    }

    public static void main(String[] args) throws Exception {
        Student student = new Student();
        student.setScores(new String[] { "95", "88", "76", "100", "67" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Scores");
        // arraydelimiter:- joins the values with a hyphen
        worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Student", Arrays.asList(student));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-numeric.xlsx");
    }
}
```

配列プロパティが `String[]` を返す場合、数値は文字列とまったく同じように結合されます。

```
95-88-76-100-67
```

{{% alert color="note" %}}
Java では、配列プロパティを `String[]` のままにしてください。プリミティブ型の `int[]` プロパティを単一セルに結合すると、数値ではなく配列オブジェクトの toString テキスト（たとえば `[I@1a2b3c4d`）がレンダリングされます。結合は各要素の文字列形式に対して行われるため、プリミティブ配列は不透明な 1 要素として扱われるからです。
{{% /alert %}}

### **コード例 3 — 既定の展開と単一セルレンダリングの比較**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Order {
        private String[] items;
        public String[] getItems() { return items; }
        public void setItems(String[] items) { this.items = items; }
    }

    public static void main(String[] args) throws Exception {
        Order order = new Order();
        order.setItems(new String[] { "Apple", "Banana", "Cherry", "Date" });
        Workbook workbook = new Workbook();
        Cells cells = workbook.getWorksheets().get(0).getCells();
        // Column B: default marker — values spread vertically down the column
        cells.get("B1").putValue("Default");
        cells.get("B2").putValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells.get("C1").putValue("Single cell");
        cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Order", Arrays.asList(order));
        designer.process();
        for (int row = 1; row <= 5; row++) {
            String b = cells.get(row, 1).getStringValue();
            String c = cells.get(row, 2).getStringValue();
            if (b != null && !b.isEmpty() || c != null && !c.isEmpty())
                System.out.println("B" + (row + 1) + "=[" + b + "]  C" + (row + 1) + "=[" + c + "]");
        }
        workbook.save("output-array-comparison.xlsx");
    }
}
```

既定のマーカーは列 B に要素ごとに 1 セルずつ値を設定しますが、`arrayassingle` マーカーは同じ配列を列 C の 1 つのセルにまとめます。

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **注記とベストプラクティス**

`arrayassingle` と `arraydelimiter` 属性を使用する際は、次の点に注意してください。
- 属性値は `name:value` 形式を使用します。`arrayassingle=true` のような等号形式は認識されず、既定の展開動作に静かにフォールバックします。
- 属性はカンマで区切り、スペースを入れないでください。カンマの後のスペースは区切り文字の値を 1 文字ずらします（上記の警告を参照）。
- `arraydelimiter` の値は、コロンの直後に直接記述した 1 文字、または二重引用符で囲んだ複数文字の文字列にできます。
- `arraydelimiter` を省略すると、要素はカンマで結合されます。
- 配列のゲッターを持つ public JavaBean の `java.util.List` をバインドします。単一の JavaBean オブジェクトや public フィールドのみでは、マーカーが解決されません。
- 配列プロパティは `String[]` のままにしてください。プリミティブ型の `int[]` は結合時に toString テキストがレンダリングされます（上記の注記を参照）。
- 結果として得られる連結文字列を表示できるだけの幅のあるセルにスマートマーカーを配置してください。書式に応じて、コンテンツが隣接するセルへ視覚的にオーバーフローする可能性があります。

## 関連記事
- [Aspose.Cells for Java でピボットテーブルにフィルターフィールドを追加](/cells/ja/java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Java でピボットテーブルにスタイルを適用する](/cells/ja/java/apply-style-to-pivot-table/)
- [ピボットテーブルのページフィールドレイアウトを変更する](/cells/ja/java/change-page-field-layout/)
- [Aspose.Cells for Java でスパークラインを画像と HTML に変換する](/cells/ja/java/convert-sparkline-to-image-and-html/)
- [Excel を OFD 形式に変換する](/cells/ja/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}