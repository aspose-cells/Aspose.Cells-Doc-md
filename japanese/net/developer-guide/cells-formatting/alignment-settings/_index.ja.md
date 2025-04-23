---
title: 配置設定
description: Aspose.Cellsライブラリでは、セルの配置設定を使用してテキストのレイアウトと表示を調整できます。水平配置、垂直配置、テキストの折り返しなどの設定を調整することで、セル内のテキストの流れをより細かく制御できます。このドキュメントでは、Aspose.Cellsを使用したセルの配置設定の詳細な手順とサンプルコードを提供し、すばやく理解するのに役立ちます。
keywords: Aspose.Cells、セルの配置、水平配置、垂直配置、テキストの折り返し
type: docs
weight: 20
url: /ja/net/cells-alignment-settings/
---

## **配置設定の構成**

### **Microsoft Excelの配置設定**

セルの書式設定にMicrosoft Excelを使用したことがある人であれば、Microsoft Excelの配置設定に精通しているでしょう。

上記の図から分かるように、異なる種類の配置オプションがあります:

- テキストの配置（水平および垂直）
- インデント
- 方向
- テキスト コントロール。
- テキスト方向。

これらの配置設定は、Aspose.Cellsで完全にサポートされており、以下で詳しく説明します。

### **Aspose.Cellsの配置設定**

Aspose.Cellsは、Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) コレクション内の各アイテムは[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) クラスのオブジェクトを表します。

Aspose.Cellsは、[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) および[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) メソッドを提供しています。これらは[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) クラスで使用され、セルの書式設定を取得および設定します。[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) クラスには、配置設定を構成するための便利なプロパティが提供されています。

[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) 列挙型を使用して任意のテキスト配置タイプを選択します。[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) 列挙型の事前定義されたテキスト配置タイプは次のとおりです:

|**テキスト配置タイプ**|**説明**|
| :- | :- |
|Bottom| 下部のテキスト配置を表します。
|Center| 中央のテキスト配置を表します。
|CenterAcross| 横方向に中央揃えのテキスト配置を表します。
|Distributed| 分散テキスト配置を表します。
|Fill| 塗りつぶしのテキスト配置を表します。
|General| 一般的なテキスト配置を表します。
|Justify| 両端揃えのテキスト配置を表します。
|Left| 左揃えのテキスト配置を表します。
|Right| 右揃えのテキスト配置を表します。
|Top| 上部のテキスト配置を表します。
|JustifiedLow| アラビア語のテキストに対して調整されたカシダ長でテキストを配置します。
|ThaiDistributed| 特にタイ語のテキストを分散配置し、各文字を単語として扱います。

{{% alert color="primary" %}}

また、[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed) プロパティを使用して両端揃え分散設定を適用できます。

{{% /alert %}}

#### **水平配置**

[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) オブジェクトの[**HorizontalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment) プロパティを使用してテキストを水平に配置します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

#### **垂直配置**

水平配置と同様に、[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) オブジェクトの[**VerticalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment) プロパティを使用してテキストを垂直に配置します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

#### **インデント**

セル内のテキストのインデントレベルを[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) オブジェクトの[**IndentLevel**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel) プロパティで設定することができます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

#### **方向**

セル内のテキストの方向（回転）を[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) オブジェクトの[**RotationAngle**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle) プロパティで設定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

#### **テキストコントロール**

次のセクションでは、テキストの折り返し、収縮に合わせるなど、テキストの制御方法について説明します。

##### **テキストの折り返し**

セル内のテキストを折り返すと、テキストが切れたり隣接するセルに流れ出ないようになり、読みやすくなります。テキストの折り返しは、[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)の[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)プロパティを使用してオンまたはオフに設定できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##### **収縮に合わせる**

フィールド内のテキストを折り返すオプションは、セルのサイズに合わせてテキストサイズを収縮することもできます。これは、[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)の[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)プロパティを**true**に設定することで行います。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

##### **セルの結合**

Aspose.Cellsは、Microsoft Excelのように複数のセルを1つに結合する機能をサポートしています。Aspose.Cellsには、このタスクを行うための2つの方法が提供されています。1つ目は、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)の[**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)メソッドを呼び出す方法です。[**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)メソッドは、次のパラメータを取り、セルを結合します:

- 最初の行: 結合の開始行。
- 最初の列: 結合の開始列。
- 行数: 結合する行数。
- 列数: 結合する列数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

もう1つの方法は、まず[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)の[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index)メソッドを呼び出して結合するセルの範囲を作成する方法です。[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index)メソッドは、前述の[**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)メソッドと同じパラメータを取り、[**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)オブジェクトを返します。[**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)オブジェクトには、[**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)オブジェクトで指定された範囲を結合する[**Merge**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)メソッドも用意されています。

##### **テキストの方向**

セル内のテキストの読み取り順を設定することが可能です。読み取り順は、文字や単語などが表示される視覚的な順序です。たとえば、英語は左から右への言語であり、アラビア語は右から左への言語です。

読み取り順は、[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)の[**TextDirection**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection)プロパティを使用して設定されます。Aspose.Cellsは、[**TextDirectionType**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype)列挙型で事前定義されたテキストの方向タイプを提供しています。

|**テキスト方向の種類**|**説明**|
| :- | :- |
|Context|最初に入力された文字の言語と一貫した読み取り順|
|LeftToRight|左から右の読み取り順|
|RightToLeft|右から左の読み取り順|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

## **高度なトピック**
- [セルの配置を変更し、既存の書式を保持する](/cells/ja/net/change-cells-alignment-and-keep-existing-formatting/)
- [改行とテキストの折り返し](/cells/ja/net/line-breaks-and-text-wrapping/)

{{< app/cells/assistant language="csharp" >}}
