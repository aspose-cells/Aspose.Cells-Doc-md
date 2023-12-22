---
title: 枠線の設定
description: C# の Aspose.Cells ライブラリを使用してセルの境界線のスタイルと色を設定する方法。境界線の幅、スタイル、色を調整することで、セルの外観をより詳細に制御できます。
keywords: Aspose.Cells, Cell Border Settings, C#, Border Width, Border Style, Border Color
type: docs
weight: 40
url: /ja/net/cells-border-settings/
---
##  **Cells に枠線を追加する**

Microsoft Excel では、枠線を追加してセルの書式を設定できます。境界線の種類は、追加される場所によって異なります。たとえば、上枠線はセルの上部位置に追加される枠線です。ユーザーは境界線のスタイルと色を変更することもできます。

Aspose.Cells を使用すると、開発者は Microsoft Excel と同じ柔軟な方法で枠線を追加し、その外観をカスタマイズできます。

###  **Cells に枠線を追加する**

Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)これは Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供するのは、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。の各項目[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションはオブジェクトを表します[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

 Aspose.Cells は、[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)のメソッド[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。の[**スタイルの設定**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)メソッドは、セルの書式設定スタイルを設定するために使用されます。の[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)クラスは、セルに境界線を追加するためのプロパティを提供します。

####  **Cell に枠線を追加する**

開発者は、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**国境**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)コレクション。境界線のタイプはインデックスとして渡されます。[**国境**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)コレクション。すべての境界線タイプは、[**境界線の種類**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)列挙。

**境界線の列挙**

|**枠線の種類**|**説明**|
| :- | :- |
|下の境界線|下の境界線|
|斜め下向き|左上から右下への対角線|
|斜め上|左下から右上への対角線|
|左境界線|左側の境界線|
|右境界線|右の境界線|
|トップボーダー|上の境界線|

の[**国境**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)コレクションにはすべての境界線が保存されます。それぞれの境界線[**国境**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)コレクションは、[**国境**](https://reference.aspose.com/cells/net/aspose.cells/border) つのプロパティを提供するオブジェクト、[**色**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color)そして[**線スタイル**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)境界線の線の色とスタイルをそれぞれ設定します。

境界線の線の色を設定するには、Color 列挙体 (.NET フレームワークの一部) を使用して色を選択し、それを Border オブジェクトの Color プロパティに割り当てます。

境界線の線のスタイルは、[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)列挙。

**CellBorderType 列挙体**

|**線のスタイル**|**説明**|
| :- | :- |
|ダッシュドット|細い一点鎖線|
|ダッシュドットドット|細い二点鎖線|
|破線|破線|
|点在|点線|
|ダブル|二重線|
|髪|ヘアライン|
|中ダッシュドット|中一点鎖線|
|中ダッシュドットドット|中二点鎖線|
|中破線|中破線|
|なし|線なし|
|中くらい|中線|
|斜めのダッシュドット|斜め中一点鎖線|
|厚い|太い線|
|薄い|細い線|
いずれかの線スタイルを選択し、それを[**国境**](https://reference.aspose.com/cells/net/aspose.cells/border)オブジェクトの[**線スタイル**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

線のスタイルと色の両方を同時に設定する必要があります。 2 本の斜めの境界線は同じ線種と色にする必要があります。

{{% /alert %}}

####  **Cells の範囲に枠線を追加する**

単一のセルだけでなく、セル範囲に境界線を追加することもできます。これを行うには、まず、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの[**範囲の作成**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1)方法。次のパラメータを受け取ります。

- 最初の行、範囲の最初の行。
- 最初の列は、範囲の最初の列を表します。
- Number of Rows (行数)、範囲内の行数。
- Number of Columns、範囲内の列の数。

の[**範囲の作成**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1)メソッドは[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range)指定されたセル範囲を含むオブジェクト。の[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range)オブジェクトが提供するもの[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)このメソッドは、次のパラメーターを受け取り、セル範囲に境界線を追加します。

-  *Border Type**、境界線のタイプ。[**境界線の種類**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)列挙。
-  *Line Style**、境界線のスタイル。[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)列挙。
- *Color**、[Color] 列挙から選択された線の色。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
