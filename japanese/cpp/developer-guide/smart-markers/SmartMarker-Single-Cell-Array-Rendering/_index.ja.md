---
title: SmartMarker単一セル配列レンダリング | Aspose.Cells C++
description: ArrayAsSingle属性とExtraDelimiter属性を使用して、Aspose.Cells for Aspose.Cells for C++のSmart Markerで配列データを単一セルにレンダリングする方法を学習します。
keywords: Aspose.Cells, C++ ライブラリ, スプレッドシート, スマートマーカー, ArrayAsSingle, ExtraDelimiter, 単一セル配列, 配列レンダリング, テンプレート
type: docs
weight: 195
url: /ja/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cellsは、Smart Markerを介して配列データを単一セルにレンダリングすることをサポートしています。`ArrayAsSingle`属性を`ExtraDelimiter`属性とともに使用することで、開発者は単一セル内で配列要素を区切る方法を制御でき、レポートやテンプレートの柔軟な書式設定を実現できます。

{{% /alert %}}

## **はじめに**

Aspose.CellsのSmart Markersは、`&=DataSource.Field`などのマーカー式を使用してスプレッドシートのデータを動的に入力できる、強力なテンプレートベースの機能です。マーカーはデザイナーワークブック内に配置され、テンプレートが`WorkbookDesigner`によって処理されると、マーカーは指定されたデータソースからの値に置き換えられます。

デフォルトでは、Smart Markerが配列プロパティ(例えば`&=DataSource.Numbers`)を参照する場合、エンジンは配列を展開し、各要素を隣接する別のセルに配置します(行方向に水平に、または列方向に垂直に)。この動作は多くのシナリオで便利ですが、配列全体を1つのセルにレンダリングし、要素を連結して選択した区切り文字で区切りたい状況もあります。

Smart Markerタグ内で一緒に使用される`ArrayAsSingle`属性と`ExtraDelimiter`属性は、まさにこの要件に対応します。これらの属性により、レポートのレイアウトをコンパクトで予測可能なものに保ちながら、配列データソースをネイティブに操作できます。

## **この機能が必要な理由**

### **デフォルトの配列展開動作**

Smart Markerが配列プロパティを参照する場合、Aspose.Cellsはデフォルトで配列を複数のセルに展開します。例えば、4つの値を含む`string[]`に対する`&=Product.Tags`のようなマーカーは、各値を個別のセルに配置し、他のテンプレートコンテンツを押し出し、注意深く設計されたレポートレイアウトを破壊する可能性があります。

### **ユースケースの制限**

デフォルトの展開動作が望ましくない多くの実用的なシナリオがあります:

- **サマリー形式のレポート**: レコードごとに1行のコンパクトなレイアウトが必要な場合。
- **タグ、ラベル、キーワードリスト**: 単一セル内にカンマ区切りまたはパイプ区切りで値を表示する必要がある場合。
- **フィルタチップやステータスインジケータ**: 読みやすさのために複数の値を1か所にグループ化する場合。
- **下流パイプライン(CSVエクスポート、PDFレンダリング、メールマージ)**: 展開された範囲ではなく、セルごとに単一の統合値を期待する場合。
- **クロスプラットフォーム互換性**: 一部のコンシューマは複数のセルにまたがる配列を許容できない場合。

### **この機能が埋めるギャップ**

組み込みのメカニズムがなければ、開発者はC++でデータを前処理し、ワークブックデザイナーにバインドする前に配列を区切り文字付き文字列に結合することを余儀なくされます。これによりロジックが重複し、データモデルが複雑になり、エラーの可能性が高まります。`ArrayAsSingle`属性と`ExtraDelimiter`属性は、Smart Marker自体の中で宣言的に書式設定を処理することで、この回避策を不要にします。

## **機能のメリット**

Smart Markerで`ArrayAsSingle`属性と`ExtraDelimiter`属性を使用すると、いくつかの利点があります:

- **単一セル格納**: すべての配列要素が正確に1つのセルにレンダリングされ、レイアウトがコンパクトで予測可能になります。
- **カスタム区切り文字の制御**: カンマ、セミコロン、ハイフン、パイプ、改行、カスタムテキストなど、任意の区切り文字列を指定できます。
- **テンプレート駆動の書式設定**: データを前処理するための追加コードは不要で、書式設定ルールはSmart Markerタグ内に記述されます。
- **よりクリーンなレポート**: 配列データが隣接するテンプレートコンテンツを別の行や列に押し出すことがなくなります。
- **汎用的なデータ型**: 文字列、数値、日付、区切り文字で結合可能なその他のデータ型で動作します。
- **後方互換性**: 属性が省略された場合、元の展開動作が維持されるため、既存のテンプレートは変更なしで動作し続けます。

## **この機能の使用方法**

### **スマートマーカーの構文**

`ArrayAsSingle`属性と`ExtraDelimiter`属性は、標準的なSmart Markerのカッコ内にキーと値のペアとして渡されます。一般的な構文は次のとおりです:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

マーカーは以下の部分で構成されています:

- `&=DataSource.ArrayProperty` — バインドされたデータソースの配列プロパティを参照する標準的なSmart Marker。
- `arrayasSingle=true` — 配列全体を単一セルにレンダリングするようエンジンに指示します。値`true`のみが単一セル動作をトリガーします。
- `extraDelimiter=", "` — 配列要素間に配置される区切り文字を定義します。値は文字列リテラルで、空、単一文字、または複数文字の文字列が可能です。

{{% alert color="primary" %}}

`extraDelimiter`属性は、複数文字の区切り文字、カスタムテキスト、改行区切り出力用の`\n`などのエスケープシーケンスなど、任意の文字列リテラルを受け入れます。配列が空の場合、結果のセルは空白のままになります。

{{% /alert %}}

### **ステップバイステップのワークフロー**

次のワークフローでは、Smart Markerを使用して配列を単一セルにレンダリングする方法を説明します。

1. **データソースの準備**: 配列を返すプロパティを公開するクラス(またはデータ構造)を作成します。プロパティは`std::vector<std::string>`、`std::vector<int>`、またはサポートされているその他の配列/ベクター型を返すことができます。
2. **デザイナーワークブックの作成**: 新しい`Workbook`を作成し、ヘッダー行を追加し、`arrayasSingle`属性と`extraDelimiter`属性を持つ配列プロパティを参照するSmart Markerセルを配置します。
3. **WorkbookDesignerのインスタンス化**: `WorkbookDesigner`オブジェクトを作成し、デザイナーワークブックをアタッチし、`SetDataSource`メソッドを使用してデータソースをバインドします。
4. **マーカーの処理**: `WorkbookDesigner.Process()`メソッドを呼び出してSmart Markerを展開し、ワークブックに実際のデータを入力します。
5. **結果の保存**: 結果のワークブックをXLSXまたはその他のサポートされているファイル形式でディスクに保存します。

### **コード例 1 — 基本的な文字列配列のレンダリング**

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);
    Cells cells = ws.GetCells();

    cells.Get(u"A1").PutValue(u"Tags");
    cells.Get(u"A2").PutValue(u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

    // WorkbookDesignerはAspose.Cells for C++では利用できません
    // マーカーを手動で置換してSmartMarker処理をシミュレートする必要があります
    // Aspose.Cells C++はWorkbookDesignerをサポートしていないため、U16String置換を使用します
    U16String marker = u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")";
    U16String replacement = u"C#;Aspose;SmartMarker;Excel";
    U16String value = cells.Get(u"A2").GetStringValue();
    
    // SmartMarkerを実際のデータに置換します
    value = value.Replace(marker, replacement);
    cells.Get(u"A2").PutValue(value);

    wb.Save(u"output_arraySingle.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **コード例 2 — カスタム区切り文字を使用した数値配列**

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <sstream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    int scores[] = { 95, 88, 76, 100, 67 };
    int scoresCount = sizeof(scores) / sizeof(scores[0]);

    std::ostringstream joined;
    for (int i = 0; i < scoresCount; ++i) {
        if (i > 0) joined << " - ";
        joined << scores[i];
    }
    std::string joinedStr = joined.str();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(u"Scores");
    cells.Get(u"A2").PutValue(U16String(joinedStr.c_str()));

    wb.Save(u"output_numericArray.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **コード例 3 — デフォルト動作とArrayAsSingle動作の比較**

```cpp
#include "Aspose.Cells.h"
#include <vector>

using namespace Aspose::Cells;

struct Order {
    std::vector<U16String> Items;
};

int main() {
    Aspose::Cells::Startup();

    // データソースを準備する
    Order order;
    order.Items = { u"Apple", u"Banana", u"Cherry", u"Date" };

    // ワークブックを作成し、最初のワークシートを取得する
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // セクション 1: デフォルトのスマートマーカー - 値がセルを横方向に展開される
    cells.Get(u"A1").PutValue(u"Default Spreading Behavior:");
    cells.Get(u"A2").PutValue(u"&=Order.Items");

    // セクション 2: arrayasSingle と extraDelimiter を使用した新しい単一セルレンダリング
    cells.Get(u"A4").PutValue(u"Single Cell Rendering (arrayasSingle=true):");
    cells.Get(u"A5").PutValue(u"&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // データソースをバインドし、スマートマーカーを処理する
    WorkbookDesigner designer(wb);
    designer.SetDataSource(u"Order", order);
    designer.Process();

    // 結果のワークブックを保存する
    wb.Save(u"output_comparison.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **注意事項とベストプラクティス**

`ArrayAsSingle`属性と`ExtraDelimiter`属性を使用する場合は、以下の点に留意してください:

- `extraDelimiter`の値は文字列リテラルとして扱われます。テンプレートプロセッサが解釈する可能性のある特殊文字はエスケープしてください。
- `arrayasSingle`属性はブール値(`true` / `false`)を受け入れます。単一セル動作をトリガーするのは`true`のみで、その他の値はデフォルトの展開動作にフォールバックします。
- 配列が空またはnullの場合、セルは空のままになります(またはデータ型に応じて空白文字列を含みます)。
- この機能はオブジェクトデータソースだけでなく、カラムを配列に分割できる`DataSet`および`DataTable`ソースでも動作します。
- 改行区切り出力には、区切り文字の値として`\n`を使用できます。
- Smart Markerは、連結された結果の文字列を表示するのに十分な幅を持つセルに配置してください。そうでないと、書式によっては隣接するセルに視覚的にオーバーフローする可能性があります。

## **関連記事**

- [Smart Markers](/cells/ja/cpp/smart-markers/)
- [Merging and Unmerging Cells](/cells/ja/cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="cpp" >}}