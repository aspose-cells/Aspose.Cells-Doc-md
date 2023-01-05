---
title: アライメント設定
type: docs
weight: 20
url: /ja/java/cells-alignment-settings/
---
## **配置設定の構成**

## **Microsoft Excelでの配置設定**

Microsoft Excel を使用してセルをフォーマットしたことがある人は、Microsoft Excel の配置設定に慣れているでしょう。

上の図からわかるように、さまざまな種類の配置オプションがあります。

- テキストの配置 (水平および垂直)
- インデント。
- オリエンテーション。
- テキスト コントロール。
- テキスト方向。

これらの配置設定はすべて Aspose.Cells で完全にサポートされており、以下で詳しく説明します。

## **Aspose.Cellsのアライメント設定**

Aspose.Cells提供[**GetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle)と[**スタイルの設定**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle)のメソッド[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)セルのフォーマットを取得および設定するために使用されるクラス。の[**スタイル**](https://reference.aspose.com/cells/java/com.aspose.cells/style)クラスは、配置設定を構成するための便利なプロパティを提供します。

を使用して、任意のテキスト配置タイプを選択します。[**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype)列挙。で定義済みのテキスト配置タイプ[**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype)列挙は次のとおりです。

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

を使用して正当化分散設定を適用することもできます。[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed)財産。

{{% /alert %}}

## **水平方向、垂直方向の配置とインデント**

使用[**HorizontalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment)テキストを水平方向に揃えるプロパティ[**VerticalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment)テキストを垂直方向に配置するプロパティ。
セル内のテキストのインデント レベルを設定することができます。[**インデントレベル**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel)財産
tt は、水平方向の配置が左または右の場合にのみ有効です。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **オリエンテーション**

でセル内のテキストの向き (回転) を設定します。[**回転角度**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle)財産。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **テキスト コントロール**

次のセクションでは、テキストの折り返し、サイズに合わせて縮小、およびその他の書式設定オプションを設定して、テキストを制御する方法について説明します。

### **テキストの折り返し**

セル内でテキストを折り返すと、読みやすくなります。セルの高さは、テキストが切り取られたり、隣接するセルにあふれたりするのではなく、すべてのテキストに合わせて調整されます。でテキストの折り返しをオンまたはオフに設定します[**IsTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)財産。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **縮小してフィット**

フィールド内のテキストを折り返すオプションの 1 つは、セルの寸法に合わせてテキスト サイズを縮小することです。これは、[**縮小して合わせる**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit)財産。に**真実**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **合併 Cells**

 Microsoft Excel と同様に、Aspose.Cells は複数のセルを 1 つに結合することをサポートしています。 Aspose.Cells は、このタスクに対する 2 つのアプローチを提供します。 1 つの方法は、[**マージ**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)） 方法。このメソッドは、次のパラメーターを使用してセルをマージします。

- 最初の行: マージを開始する最初の行。
- 最初の列: マージを開始する最初の列。
- 行数: 結合する行数。
- 列数: マージする列の数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **テキスト方向**

セル内のテキストの読み上げ順序を設定することができます。読み順とは、文字や単語などが表示される視覚的な順序です。たとえば、英語は左から右への言語ですが、アラビア語は右から左への言語です。

読み上げ順序は[**テキスト方向**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection)財産。 Aspose.Cells は、[**TextDirectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection)列挙。

|**テキストの方向の種類**|**説明**|
|:- |:- |
|コンテクスト|最初に入力された文字の言語と一致する読み順|
|左から右へ|左から右の読み順|
|右から左に|右から左の読み順|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **先行トピック**
- [Cells の配置を変更し、既存の書式を維持する](/cells/ja/java/change-cells-alignment-and-keep-existing-formatting/)
- [改行とテキストの折り返し](/cells/ja/java/line-breaks-and-text-wrapping/)
