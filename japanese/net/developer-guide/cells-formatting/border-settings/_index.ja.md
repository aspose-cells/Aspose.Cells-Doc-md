---
title: ボーダー設定
type: docs
weight: 40
url: /ja/net/cells-border-settings/
---
## **Cells に罫線を追加する**

Microsoft Excel では、ユーザーは罫線を追加してセルの書式を設定できます。境界線の種類は、追加する場所によって異なります。たとえば、上罫線は、セルの上端に追加される罫線です。ユーザーは、境界線のスタイルと色を変更することもできます。

Aspose.Cells を使用すると、開発者は Microsoft Excel と同じように柔軟な方法で境界線を追加し、外観をカスタマイズできます。

### **Cells に罫線を追加する**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供する[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。の各項目[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションはのオブジェクトを表します[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

Aspose.Cells は[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)のメソッド[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。の[**スタイルの設定**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)メソッドは、セルの書式設定スタイルを設定するために使用されます。の[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)クラスは、セルに境界線を追加するためのプロパティを提供します。

#### **Cell にボーダーを追加する**

開発者は、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**国境**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)コレクション。ボーダー タイプはインデックスとして渡されます。[**国境**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)コレクション。すべての境界線の種類は、[**ボーダータイプ**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)列挙。

**ボーダー列挙**

|**境界線の種類**|**説明**|
|:- |:- |
|BottomBorder|下の境界線|
|斜め下|左上から右下への対角線|
|斜め上|左下から右上への対角線|
|左ボーダー|左の境界線|
|右ボーダー|右の境界線|
|上枠|上の境界線|

の[**国境**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)コレクションにはすべての境界線が格納されます。の各境界線[**国境**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)コレクションは[**国境**](https://reference.aspose.com/cells/net/aspose.cells/border) つのプロパティを提供するオブジェクト、[**色**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color)と[**線種**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)ボーダーの線の色とスタイルをそれぞれ設定します。

境界線の色を設定するには、Color 列挙体 (.NET フレームワークの一部) を使用して色を選択し、それを Border オブジェクトの Color プロパティに割り当てます。

ボーダーの線のスタイルは、[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)列挙。

**CellBorderType 列挙体**

|**線種**|**説明**|
|:- |:- |
|ダッシュドット|細い一点鎖線|
|ダッシュドットドット|細い一点鎖線|
|破線|破線|
|点在|点線|
|ダブル|二重線|
|髪|生え際|
|中破線|中一点鎖線|
|ミディアムダッシュドットドット|中一点鎖線|
|中破線|中破線|
|なし|行なし|
|中くらい|ミディアムライン|
|斜めダッシュドット|斜め中一点鎖線|
|厚い|太線|
|薄い|細い線|
ライン スタイルの 1 つを選択し、それを[**国境**](https://reference.aspose.com/cells/net/aspose.cells/border)オブジェクトの[**線種**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

線のスタイルと色の両方を同時に設定する必要があります。 2 つの対角線の境界線は、同じ線種と色にする必要があります。

{{% /alert %}}

#### **Cells の範囲に境界線を追加する**

単一のセルだけでなく、セルの範囲に罫線を追加することもできます。これを行うには、まず、を呼び出してセルの範囲を作成します。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの[**作成範囲**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1)方法。次のパラメータを取ります。

- 最初の行、範囲の最初の行。
- 最初の列は、範囲の最初の列を表します。
- 行数、範囲内の行数。
- 列数、範囲内の列数。

の[**作成範囲**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1)メソッドは[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range)指定されたセル範囲を含むオブジェクト。の[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range)オブジェクトは[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)次のパラメーターを使用して、セル範囲に境界線を追加するメソッド:

- **ボーダータイプ**から選択された境界線タイプ[**ボーダータイプ**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)列挙。
- **線種**から選択された境界線のスタイル[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)列挙。
- **色**Color 列挙体から選択された線の色。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}

## **色とパレット**

パレットは、画像の作成に使用できる色の数です。プレゼンテーションで標準化されたパレットを使用すると、ユーザーは一貫した外観を作成できます。各 Microsoft Excel (97-2003) ファイルには、グラフのセル、フォント、グリッド線、グラフィック オブジェクト、塗りつぶし、線に適用できる 56 色のパレットがあります。

Aspose.Cells では、パレットの既存の色だけでなく、カスタム カラーも使用できます。カスタム カラーを使用する前に、まずパレットに追加します。

このトピックでは、カスタム カラーをパレットに追加する方法について説明します。

### **パレットへのカスタム カラーの追加**

Aspose.Cells は Microsoft Excel の 56 色パレットをサポートします。パレットで定義されていないカスタム カラーを使用するには、そのカラーをパレットに追加します。

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスは[**チェンジパレット**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette)次のパラメーターを使用してカスタム カラーを追加し、パレットを変更するメソッド:

- カスタム カラー、追加するカスタム カラー。
- インデックス、カスタム色が置き換えるパレット内の色のインデックス。 0 から 55 の間である必要があります。

次の例では、カスタム カラー (Orchid) をフォントに適用する前にパレットに追加しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

パレットには 56 色しかありません。カスタム カラーをパレットに追加すると、パレットが変更され、以前の色でフォーマットされたファイル内のすべての要素が変更されます。そのため、パレットを変更する際は十分ご注意ください。さらに、XLSX またはその他の高度な MS Excel (2007/2010 または 2013) ファイル形式にはそのような制限がないため、これは XLS (Excel 97 - 2003) ファイル形式のみの制限です。

{{% /alert %}}


