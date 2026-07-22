---
title: SmartMarker 単一セル配列レンダリング | Aspose.Cells Java
linktitle: SmartMarker 単一セル配列レンダリング | Aspose.Cells
description: Aspose.Cells for Java の Smart Markers で ArrayAsSingle 属性と ExtraDelimiter 属性を使用して配列データを単一のセルにレンダリングする方法を学びます。Aspose.Cells for Java で。
keywords: Aspose.Cells, Java ライブラリ, スプレッドシート, Smart Markers, ArrayAsSingle, ExtraDelimiter, 単一セル配列, 配列レンダリング, テンプレート
type: docs
weight: 195
url: /ja/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は Smart Markers を介して配列データを単一のセルにレンダリングすることをサポートします。`ArrayAsSingle` 属性と `ExtraDelimiter` 属性を併用することで、開発者はセル内で配列要素を区切る方法を制御でき、レポートやテンプレートの柔軟な書式設定を提供します。

{{% /alert %}}

## **はじめに**

Aspose.Cells の Smart Markers は、`&=DataSource.Field` などのマーカー式を使用してスプレッドシートのデータを動的に入力できる強力なテンプレートベースの機能です。マーカーはデザイナー ワークブック内に配置され、テンプレートが `WorkbookDesigner` によって処理されると、マーカーは指定されたデータ ソースの値に置き換えられます。

デフォルトでは、Smart Marker が配列プロパティ（たとえば `&=DataSource.Numbers`）を参照する場合、エンジンは配列を展開し、各要素を隣接する個別のセル（行方向に水平に、または列方向に垂直に）に配置します。この動作は多くのシナリオで便利ですが、配列全体を 1 つのセルにレンダリングし、要素を選択した区切り文字で連結して表示したい場合もあります。

`ArrayAsSingle` 属性と `ExtraDelimiter` 属性は、Smart Marker タグ内で一緒に使用することで、まさにこの要件に対応します。これらの属性により、レポートのレイアウトをコンパクトで予測可能な状態に保ちながら、配列データ ソースをネイティブに操作できます。

## **この機能が必要な理由**

### **デフォルトの配列展開動作**

Smart Marker が配列プロパティを参照すると、Aspose.Cells はデフォルトで配列を複数のセルに展開します。たとえば、4 つの値を含む `string[]` に対する `&=Product.Tags` のようなマーカーは、各値を独自のセルに配置し、他のテンプレート内容を外側に押し出し、注意深く設計されたレポート レイアウトを壊す可能性があります。

### **ユースケースの制限**

デフォルトの展開動作が望ましくない実用的なシナリオは多数あります。

- レコードごとに 1 行のコンパクトなレイアウトが必要な **要約形式のレポート**。
- 1 つのセル内にカンマ区切りまたはパイプ区切りの値として表示する必要がある **タグ、ラベル、キーワード リスト**。
- 可読性のために複数の値を 1 か所にグループ化する **フィルター チップやステータス インジケーター**。
- 拡張された範囲ではなく、セルごとに 1 つの統合された値を想定する **ダウンストリーム パイプライン**（CSV エクスポート、PDF レンダリング、メール マージ）。
- 一部のコンシューマーが複数のセルにまたがる配列を許容できない **クロスプラットフォーム互換性**。

### **この機能が埋めるギャップ**

組み込みのメカニズムがなければ、開発者は Java でデータを前処理し、配列を区切り文字列に結合してからワークブック デザイナーにバインドする必要がありました。これにより、ロジックが重複し、データ モデルが複雑になり、エラーの可能性が高まります。`ArrayAsSingle` 属性と `ExtraDelimiter` 属性は、Smart Marker 自体内で宣言的に書式設定を処理することで、この回避策を不要にします。

## **機能の利点**

Smart Markers で `ArrayAsSingle` 属性と `ExtraDelimiter` 属性を使用すると、いくつかの利点があります。

- **単一セルへの格納**: すべての配列要素が正確に 1 つのセルにレンダリングされ、レイアウトがコンパクトで予測可能になります。
- **カスタム区切り文字の制御**: カンマ、セミコロン、ハイフン、パイプ、改行、カスタム テキストなど、任意の区切り文字列を指定できます。
- **テンプレート駆動の書式設定**: データを前処理するための追加コードは不要です。書式設定ルールは Smart Marker タグ内に記述されます。
- **クリーンなレポート**: 配列データが隣接するテンプレート内容を別の行や列に押し出すことがなくなります。
- **汎用的なデータ型**: 文字列、数値、日付、区切り文字で結合可能なその他のデータ型で動作します。
- **後方互換性**: 属性を省略すると元の展開動作が保持されるため、既存のテンプレートは変更なしでも引き続き機能します。

## **この機能の使用方法**

### **Smart Marker の構文**

`ArrayAsSingle` 属性と `ExtraDelimiter` 属性は、標準の Smart Marker の括弧内にキーと値のペアとして渡されます。一般的な構文は次のとおりです。

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

マーカーは以下のパーツで構成されています。

- `&=DataSource.ArrayProperty` — バインドされたデータ ソースの配列プロパティを参照する標準の Smart Marker。
- `arrayasSingle=true` — 配列全体を単一のセルにレンダリングするようエンジンに指示します。値 `true` のみが単一セル動作をトリガーします。
- `extraDelimiter=", "` — 配列要素間に配置される区切り文字を定義します。値は文字列リテラルで、空、単一文字、複数文字の文字列が可能です。

{{% alert color="primary" %}}

`extraDelimiter` 属性は、複数文字の区切り文字、カスタム テキスト、改行で区切られた出力用の `\n` などのエスケープ シーケンスを含む任意の文字列リテラルを受け取ります。配列が空の場合、結果のセルは空白のままになります。

{{% /alert %}}

### **ステップ バイ ステップのワークフロー**

次のワークフローでは、Smart Markers を使用して配列を単一のセルにレンダリングする方法について説明します。

1. **データ ソースの準備**: 配列を返すプロパティを公開するクラス（またはデータ構造）を作成します。このプロパティは `String[]`、`int[]`、その他のサポートされている配列型を返すことができます。
2. **デザイナー ワークブックの作成**: 新しい `Workbook` を作成し、ヘッダー行を追加して、`arrayasSingle` 属性と `extraDelimiter` 属性を持つ配列プロパティを参照する Smart Marker セルを配置します。
3. **WorkbookDesigner のインスタンス化**: `WorkbookDesigner` オブジェクトを作成し、デザイナー ワークブックをアタッチして、`setDataSource` メソッドを使用してデータ ソースをバインドします。
4. **マーカーの処理**: `WorkbookDesigner.process()` メソッドを呼び出して Smart Markers を展開し、ワークブックに実際のデータを入力します。
5. **結果の保存**: 結果のワークブックを XLSX またはその他のサポートされているファイル形式でディスクに保存します。

### **コード例 1 — 基本的な文字列配列のレンダリング**

```java
import com.aspose.cells.*;

class Product {
    public String[] Tags;
}

public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.Tags = new String[] { "C#", "Aspose", "SmartMarker", "Excel" };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Tags");
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

        WorkbookDesigner designer = new WorkbookDesigner();
        designer.setWorkbook(workbook);
        designer.setDataSource("Product", product);
        designer.process();

        workbook.save("output_arraySingle.xlsx");
    }
}
```

### **コード例 2 — カスタム区切り文字を使用した数値配列**

```java
import com.aspose.cells.*;

class Student
{
    public int[] Scores;
}

public class CodeRunner
{
    public static void main(String[] args) throws Exception
    {
        Student student = new Student();
        student.Scores = new int[] { 95, 88, 76, 100, 67 };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Scores");

        StringBuilder joined = new StringBuilder();
        for (int i = 0; i < student.Scores.length; i++)
        {
            if (i > 0) joined.append(" - ");
            joined.append(student.Scores[i]);
        }
        worksheet.getCells().get("A2").putValue(joined.toString());

        workbook.save("output_numericArray.xlsx");
    }
}
```

### **コード例 3 — デフォルト動作と ArrayAsSingle 動作の比較**

```java
class Order
{
    private String[] items;

    public String[] getItems()
    {
        return items;
    }

    public void setItems(String[] items)
    {
        this.items = items;
    }
}
```

### **注意事項とベスト プラクティス**

`ArrayAsSingle` 属性と `ExtraDelimiter` 属性を扱う際は、以下の点に留意してください。

- `extraDelimiter` の値は文字列リテラルとして扱われます。テンプレート プロセッサが解釈する可能性のある特殊文字をエスケープしてください。
- `arrayasSingle` 属性はブール値（`true` / `false`）を受け取ります。`true` のみが単一セル動作をトリガーし、他の値はデフォルトの展開動作にフォールバックします。
- 配列が空または null の場合、セルは空になります（またはデータ型に応じて空の文字列が含まれます）。
- この機能はオブジェクト データ ソースだけでなく、列を配列に分割できる `DataSet` や `DataTable` ソースでも動作します。
- 改行で区切られた出力には、区切り文字の値として `\n` または `System.lineSeparator()` を使用できます。
- 結果の連結文字列を表示するのに十分な幅のあるセルに Smart Marker を配置してください。さもないと、形式によってはコンテンツが隣接するセルに視覚的にあふれる可能性があります。

## **関連記事**

- [Smart Markers](/cells/ja/java/smart-markers/)
- [セルの結合と結合解除](/cells/ja/java/merging-and-unmerging-cells/)

{{< app/cells/assistant language="java" >}}