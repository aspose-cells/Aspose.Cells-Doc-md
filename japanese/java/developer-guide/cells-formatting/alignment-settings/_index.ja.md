---
title: 配置設定
type: docs
weight: 20
url: /ja/java/cells-alignment-settings/
---

## **配置設定の構成**

## **Microsoft Excelの配置設定**

セルの書式設定にMicrosoft Excelを使用したことがある人であれば、Microsoft Excelの配置設定に精通しているでしょう。

上記の図から分かるように、異なる種類の配置オプションがあります:

- テキストの配置（水平および垂直）
- インデント
- 方向
- テキスト コントロール。
- テキスト方向。

これらの配置設定は、Aspose.Cellsで完全にサポートされており、以下で詳しく説明します。

## **Aspose.Cellsの配置設定**

Aspose.Cellsは、[**GetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) および[**SetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle) メソッドを提供しています。これらは[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) クラスで使用され、セルの書式設定を取得および設定します。[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) クラスには、配置設定を構成するための便利なプロパティが提供されています。

[**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) 列挙型を使用して任意のテキスト配置タイプを選択します。[**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) 列挙型の事前定義されたテキスト配置タイプは次のとおりです:

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

また、[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed) プロパティを使用して両端揃え分散設定を適用できます。

{{% /alert %}}

## **水平、垂直配置、およびインデント**

テキストを水平に配置するには[**HorizontalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment)プロパティを使用し、垂直に配置するには[**VerticalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment)プロパティを使用します。
セル内のテキストのインデントレベルを設定することができます。[**IndentLevel**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel)プロパティで。 
左揃えまたは右揃えの水平配置の場合にのみ影響します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **方向**

セル内のテキストの方向（回転）を[**RotationAngle**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle)プロパティで設定します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **テキストコントロール**

次のセクションでは、テキストの折り返し、収縮に合わせるなど、テキストの制御方法について説明します。

### **テキストの折り返し**

セル内のテキストを折り返すと、セルの高さがすべてのテキストに合わせて調整されます。テキストが切り捨てられたり、隣接するセルに流れ出たりするのではなく、セル内にきれいに収まります。[**IsTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)プロパティでテキストの折り返しをオンまたはオフに設定します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **収縮に合わせる**

フィールド内のテキストを折り返すオプションとして、セルの寸法に合わせてテキストサイズを縮小することができます。これは[**ShrinkToFit**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit)プロパティを**true**に設定することで行います。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **セルの結合**

Microsoft Excelと同様に、Aspose.Cellsでは複数のセルを1つに結合することができます。Aspose.Cellsにはこのタスクを実行するための2つのアプローチがあります。1つの方法は、[**Merge**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge-int-int-int-int-)メソッドを呼び出すことです。メソッドは、以下のパラメータを取り、セルを結合します:

- 最初の行: 結合の開始行。
- 最初の列: 結合の開始列。
- 行数: 結合する行数。
- 列数: 結合する列数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **テキストの方向**

セル内のテキストの読み取り順を設定することが可能です。読み取り順は、文字や単語などが表示される視覚的な順序です。たとえば、英語は左から右への言語であり、アラビア語は右から左への言語です。

読み取り順は [**TextDirection**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection) プロパティによって設定されます。 Aspose.Cells は [**TextDirectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection) 列挙型で事前定義されたテキストの方向を提供します。

|**テキスト方向の種類**|**説明**|
| :- | :- |
|Context|最初に入力された文字の言語と一貫した読み取り順|
|LeftToRight|左から右の読み取り順|
|RightToLeft|右から左の読み取り順|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **高度なトピック**
- [セルの配置を変更し、既存の書式を保持する](/cells/ja/java/change-cells-alignment-and-keep-existing-formatting/)
- [改行とテキストの折り返し](/cells/ja/java/line-breaks-and-text-wrapping/)
{{< app/cells/assistant language="java" >}}
