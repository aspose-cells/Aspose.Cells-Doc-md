---
title: ワークシート ビュー
type: docs
weight: 40
url: /ja/net/worksheet-views/
description: この記事では、C# と .NET API を使用して、Excel ブックとワークシートの改ページ プレビューを操作する方法について説明します。分割されたペイン、固定されたペイン、ズーム倍率も操作できます。
---
## **改ページプレビュー**

すべてのワークシートは、次の 2 つのモードで表示できます。

- 通常のビュー。
- 改ページのプレビュー。

標準ビューは、ワークシートの既定のビューです。改ページ プレビューは、印刷時にワークシートを表示する編集ビューです。改ページのプレビューでは、各ページにどのようなデータが表示されるかが表示されるため、印刷範囲と改ページを調整できます。 Aspose.Cells を使用すると、開発者は通常のビューまたは改ページ プレビュー モードを有効にできます。

### **表示モードの制御**

Aspose.Cells は[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Microsoft Excel ファイルを表すクラス。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。通常または改ページのプレビュー モードを有効にするには、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)財産。[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)ブール型のプロパティです。つまり、格納できるのは**真実**または**間違い**価値。

#### **通常表示を有効にする**

を設定して、ワークシートを通常のビューに設定します。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)プロパティへ**間違い**.

#### **改ページプレビューを有効にする**

を設定して、任意のワークシートを改ページ プレビューに設定します。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)プロパティへ**真実**.これにより、ワークシートが通常のビューから改ページ プレビューに切り替わります。

の使用方法を示す完全な例を以下に示します。[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)プロパティを使用して、Excel ファイルの最初のワークシートの改ページ プレビュー モードを有効にします。

book1.xls ファイルは、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラス。ビューは、最初のワークシートの改ページ プレビューに切り替えられます。[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)プロパティへ**真実**.変更されたファイルは、output.xls として保存されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **ズーム倍率**

### **Microsoft エクセルを使う**

Microsoft Excel には、ユーザーがワークシートのズームまたは倍率を設定できる機能があります。この機能は、ユーザーがワークシートの内容を小さいビューまたは大きいビューで表示するのに役立ちます。ユーザーはズーム倍率を任意の値に設定できます。

### **Aspose.Cells & ズーム倍率**

Aspose.Cells を使用すると、開発者はワークシートのズーム率を設定できます。
Aspose.Cells は[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Microsoft Excel ファイルを表すクラス。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。ワークシートのズーム倍率を設定するには、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス'[**ズーム**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom)財産。ズーム倍率は、数値 (整数) 値を[**ズーム**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom)財産。

の使用方法を示す完全な例を以下に示します。[**ズーム**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom)プロパティを使用して、Excel ファイルの最初のワークシートのズーム倍率を設定します。

book1.xls ファイルは、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラス。最初のワークシートの倍率は 75 に設定され、変更されたファイルは output.xls として保存されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **フリーズペイン**

### **Microsoft エクセルを使う**

フリーズ ウィンドウは、Microsoft Excel によって提供される機能です。ペインをフリーズすると、ワークシートをスクロールするときにデータを選択して表示したままにすることができます。

### **Aspose.Cells & フリーズペイン**

Aspose.Cells を使用すると、開発者はフリーズ ペインを実行時にワークシートに適用できます。

Aspose.Cells は[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel ファイルを表すクラス。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。

ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。フリーズ ペインを構成するには、Worksheet クラスを呼び出します。[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)方法。の[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)メソッドは次のパラメータを取ります。

- **行**、フリーズが開始されるセルの行インデックス。
- **桁**、フリーズが開始されるセルの列インデックス。
- **凍結された行**、上部ペインに表示される行の数。
- **冷凍列**、左ペインに表示される列の数

 book1.xls ファイルは、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)インスタンス化中のクラスのコンストラクターと、最初のワークシートでいくつかの行と列が固定されています。変更されたファイルは、output.xls として保存されます。

の使用方法を示す完全な例を以下に示します。[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)Excel ファイルの最初のワークシートの行と列 (行と列が 0 インデックスから始まる、4 行目と 3 列目で表される C4 から始まる) を固定するメソッド。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **ペインの分割**

同じワークシートに 2 つの異なるビューを表示するために画面を分割する必要がある場合は、ペインを分割します。 Microsoft Excel には、ワークシートの複数のコピーを表示したり、ワークシートの各ペインを個別にスクロールしたりできる非常に便利な機能、分割ペインがあります。

ペインは同時に機能します。一方を変更すると、同時に他方にも変更が反映されます。 Aspose.Cells は、ユーザーに分割ペイン機能を提供します。

### **分割ペインの適用と削除**

#### **ペインの分割**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excel ファイルを管理するためのさまざまなプロパティとメソッドが用意されています。分割ビューを実装するには、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス'[**スプリット**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split) .分割ペインを削除するには、[**削除スプリット**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)方法。

この例では、読み込まれた単純なテンプレート ファイルを使用し、分割ペインの設定機能が最初のワークシートのセルに適用されます。更新されたファイルが保存されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

上記のコードを実行すると、生成されたファイルは分割ビューになります。

#### **ペインの削除**

を使用して分割ペインを削除します[**削除スプリット**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **先行トピック**
- [ワークシートでゼロ値の表示を非表示にする](/cells/ja/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [ワークシートのタブの色を設定](/cells/ja/net/set-worksheet-tab-color/)
- [グリッド線と行の列ヘッダーの表示と非表示](/cells/ja/net/show-and-hide-gridlines-and-row-column-headers/)
- [行、列、およびスクロール バーの表示と非表示](/cells/ja/net/show-and-hide-rows-columns-and-scroll-bars/)
- [ワークシートとタブの表示と非表示](/cells/ja/net/show-and-hide-worksheets-and-tabs/)
- [ワークシートに値の代わりに数式を表示する](/cells/ja/net/show-formulas-instead-of-values-in-a-worksheet/)
- [エラー チェック オプションを使用する](/cells/ja/net/use-error-checking-options/)

