---
title: アライメント設定
description: Aspose.Cells ライブラリでは、セル配置設定を使用してテキストのレイアウトと表示を調整できます。水平方向の配置、垂直方向の配置、テキストの折り返しなどの設定を調整することで、セル内でのテキストの流れをより詳細に制御できます。このドキュメントでは、セルの配置設定に Aspose.Cells を使用する方法をすぐに理解できるように、詳細な手順とサンプル コードを提供します。
keywords: Aspose.Cells, cell alignment, horizontal alignment, vertical alignment, text wrapping
type: docs
weight: 20
url: /ja/net/cells-alignment-settings/
---
##  **アライメント設定の構成**

###  **Microsoft Excel の配置設定**

Microsoft Excel を使用してセルの書式を設定したことのある人は、Microsoft Excel の配置設定に精通しているでしょう。

上の図からわかるように、さまざまな種類の位置合わせオプションがあります。

- テキストの配置（水平および垂直）
- インデント。
- オリエンテーション。
- テキストコントロール。
- テキストの方向。

これらの位置合わせ設定はすべて Aspose.Cells で完全にサポートされており、以下で詳しく説明します。

###  **Aspose.Cells の配置設定**

Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供するのは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の各項目[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションはオブジェクトを表します[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

 Aspose.Cellsが提供します[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)そして[**スタイルの設定**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)のためのメソッド[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)セルの書式設定を取得および設定するために使用されるクラス。の[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)クラスは、位置合わせ設定を構成するための便利なプロパティを提供します。

を使用して任意のテキスト配置タイプを選択します。[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)列挙。の事前定義されたテキスト配置タイプ[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)列挙は次のとおりです。

|**テキスト配置の種類**|**説明**|
| :- | :- |
|底|下部のテキストの配置を表します|
|中心|テキストの中央揃えを表します|
|センターアクロス|テキスト全体の中央揃えを表します|
|分散型|分散テキストの配置を表します|
|埋める|塗りつぶしテキストの配置を表します|
|一般的な|一般的なテキストの配置を表します|
|正当化する|テキストの位置揃えを表します|
|左|テキストの左揃えを表します|
|右|テキストの右揃えを表します|
|上|上部のテキストの配置を表します|
|両端揃え低|アラビア語テキストの調整されたカシダ長にテキストを配置します。|
|タイ語分散型|各文字が単語として扱われるため、特にタイ語のテキストを配布します。|

{{% alert color="primary" %}}

また、[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed)財産。

{{% /alert %}}

####  **水平方向の配置**

使用[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**水平方向の配置**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment)プロパティを使用してテキストを水平に配置します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

####  **垂直方向の配置**

水平方向の配置と同様に、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**垂直配置**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment)プロパティを使用してテキストを垂直方向に配置します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

####  **インデント**

セル内のテキストのインデントレベルを設定できます。[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**インデントレベル**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

####  **オリエンテーション**

セル内のテキストの方向（回転）を設定します。[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**回転角度**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

####  **テキストコントロール**

次のセクションでは、テキストの折り返し、全体に合わせて縮小、その他の書式設定オプションを設定してテキストを制御する方法について説明します。

#####  **テキストの折り返し**

セル内でテキストを折り返すと読みやすくなります。テキストが切り取られたり、隣接するセルにはみ出したりするのではなく、すべてのテキストが収まるようにセルの高さが調整されます。テキストの折り返しをオンまたはオフに設定します。[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

#####  **ぴったりと縮む**

フィールド内のテキストを折り返すオプションとして、セルのサイズに合わせてテキスト サイズを縮小することができます。これは、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)プロパティを *true** に設定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

#####  **結合 Cells**

 Microsoft Excel と同様に、Aspose.Cells は複数のセルを 1 つに結合することをサポートしています。 Aspose.Cells では、このタスクに対する 2 つのアプローチを提供しています。 1 つの方法は、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**マージ**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)方法。の[**マージ**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)このメソッドは、セルを結合するために次のパラメーターを受け取ります。

- 最初の行: マージを開始する最初の行。
- 最初の列: マージを開始する最初の列。
- 行数: マージする行の数。
- 列数: マージする列の数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

もう 1 つの方法は、最初に[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**範囲の作成**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index)結合するセルの範囲を作成するメソッド。の[**範囲の作成**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index)メソッドは、メソッドと同じパラメータのセットを受け取ります。[**マージ**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)上で説明したメソッドは、[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range)物体。の[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range)オブジェクトはまた、[**マージ**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)で指定した範囲を結合するメソッド[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range)物体。

#####  **テキストの方向**

セル内のテキストの読み上げ順序を設定できます。読み順とは、文字や単語などが表示される視覚的な順序です。たとえば、英語は左から右へ記述する言語ですが、アラビア語は右から左へ記述する言語です。

読み上げ順序は、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**テキストの方向**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection)財産。 Aspose.Cells は、事前定義されたテキスト方向タイプを提供します。[**TextDirectionType**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype)列挙。

|**テキストの方向の種類**|**説明**|
| :- | :- |
|コンテクスト|最初に入力された文字の言語と一致する読み上げ順序|
|左から右へ|左から右へ読む順序|
|右から左に|右から左への読み取り順序|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

##  **アドバンストトピック**
- [Cells 配置を変更し、既存の書式設定を維持する](/cells/ja/net/change-cells-alignment-and-keep-existing-formatting/)
- [改行とテキストの折り返し](/cells/ja/net/line-breaks-and-text-wrapping/)

