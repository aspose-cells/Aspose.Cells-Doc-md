---
title: アライメント設定
type: docs
weight: 20
url: /ja/net/cells-alignment-settings/
---
## **配置設定の構成**

### **Microsoft Excelでの配置設定**

Microsoft Excel を使用してセルをフォーマットしたことがある人は、Microsoft Excel の配置設定に慣れているでしょう。

上の図からわかるように、さまざまな種類の配置オプションがあります。

- テキストの配置 (水平および垂直)
- インデント。
- オリエンテーション。
- テキスト コントロール。
- テキスト方向。

これらの配置設定はすべて Aspose.Cells で完全にサポートされており、以下で詳しく説明します。

### **Aspose.Cellsのアライメント設定**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の各項目[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションはのオブジェクトを表します[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

Aspose.Cells提供[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)と[**スタイルの設定**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)のメソッド[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)セルのフォーマットを取得および設定するために使用されるクラス。の[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)クラスは、配置設定を構成するための便利なプロパティを提供します。

を使用して、任意のテキスト配置タイプを選択します。[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)列挙。で定義済みのテキスト配置タイプ[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)列挙は次のとおりです。

|**テキスト配置タイプ**|**説明**|
|:- |:- |
|下|下のテキストの配置を表します|
|中心|テキストの中央揃えを表します|
|センターアクロス|テキストの中央揃えを表します|
|分散|分散されたテキストの配置を表します|
|塗りつぶし|塗りつぶしテキストの配置を表します|
|全般的|一般的なテキストの配置を表します|
|正当化する|テキストの両端揃えを表します|
|左|テキストの左揃えを表します|
|右|テキストの右揃えを表します|
|上|テキストの上揃えを表します|
|JustifiedLow|アラビア語テキストの kashida の長さを調整して、テキストを揃えます。|
|タイ語分散|各文字が単語として扱われるため、特にタイ語のテキストを配布します。|

{{% alert color="primary" %}}

を使用して正当化分散設定を適用することもできます。[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed)財産。

{{% /alert %}}

#### **水平方向の配置**

使用[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**HorizontalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment)テキストを水平方向に揃えるプロパティ。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

#### **垂直方向の配置**

水平方向の配置と同様に、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**VerticalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment)テキストを垂直方向に配置するプロパティ。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

#### **インデント**

セル内のテキストのインデント レベルを設定することができます。[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**インデントレベル**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

#### **オリエンテーション**

でセル内のテキストの向き (回転) を設定します。[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**回転角度**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

#### **テキスト コントロール**

次のセクションでは、テキストの折り返し、サイズに合わせて縮小、およびその他の書式設定オプションを設定して、テキストを制御する方法について説明します。

##### **テキストの折り返し**

セル内でテキストを折り返すと、読みやすくなります。セルの高さは、テキストが切り取られたり、隣接するセルにあふれたりするのではなく、すべてのテキストに合わせて調整されます。でテキストの折り返しをオンまたはオフに設定します[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##### **縮小してフィット**

フィールド内のテキストを折り返すオプションの 1 つは、セルの寸法に合わせてテキスト サイズを縮小することです。これは、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)プロパティへ**真実**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

##### **合併 Cells**

 Microsoft Excel と同様に、Aspose.Cells は複数のセルを 1 つに結合することをサポートしています。 Aspose.Cells は、このタスクに対する 2 つのアプローチを提供します。 1 つの方法は、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**マージ**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)方法。の[**マージ**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)メソッドは、次のパラメーターを使用してセルをマージします。

- 最初の行: マージを開始する最初の行。
- 最初の列: マージを開始する最初の列。
- 行数: 結合する行数。
- 列数: マージする列の数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

もう 1 つの方法は、最初に[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**作成範囲**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index)メソッドを使用して、結合するセルの範囲を作成します。の[**作成範囲**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index)メソッドは、[**マージ**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)上記のメソッドは、[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range)物体。の[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range)オブジェクトも提供します[**マージ**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)で指定した範囲をマージするメソッド[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range)物体。

##### **テキスト方向**

セル内のテキストの読み上げ順序を設定することができます。読み順とは、文字や単語などが表示される視覚的な順序です。たとえば、英語は左から右への言語ですが、アラビア語は右から左への言語です。

読み上げ順序は[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**テキスト方向**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection)財産。 Aspose.Cells は、[**TextDirectionType**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype)列挙。

|**テキストの方向の種類**|**説明**|
|:- |:- |
|コンテクスト|最初に入力された文字の言語と一致する読み順|
|左から右へ|左から右の読み順|
|右から左に|右から左の読み順|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

## **先行トピック**
- [Cells の配置を変更し、既存の書式を維持する](/cells/ja/net/change-cells-alignment-and-keep-existing-formatting/)
- [改行とテキストの折り返し](/cells/ja/net/line-breaks-and-text-wrapping/)

