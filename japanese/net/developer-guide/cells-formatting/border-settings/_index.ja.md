---
title: 罫線設定
description: Aspose.CellsライブラリをC#で使用して、セルの罫線スタイルと色を設定する方法。罫線の幅、スタイル、色を調整することで、セルの見た目や出力をより細かく制御できます。
keywords: Aspose.Cells、セルの罫線設定、C#、罫線の幅、罫線のスタイル、罫線の色
type: docs
weight: 40
url: /ja/net/cells-border-settings/
---

## **セルにボーダーを追加する**

Microsoft Excelでは、ユーザーが罫線を追加することでセルのフォーマットを指定できます。追加する罫線の種類は、追加される位置に依存します。たとえば、上部の罫線はセルの上部に追加される罫線です。Aspose.Cellsでは、開発者はMicrosoft Excelと同じ柔軟な方法で罫線を追加し、外見をカスタマイズできます。

Aspose.Cellsを使用すると、開発者はMicrosoft Excelと同様に柔軟に罫線を追加し、見た目をカスタマイズできます。

### **セルにボーダーを追加する**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供しています。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションを提供しています。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション内の各アイテムは、[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラスのオブジェクトを表します。

Aspose.Cellsは、[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)クラスで[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)メソッドを提供しています。[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)メソッドは、セルの書式設定スタイルを設定するために使用されます。[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)クラスは、セルに罫線を追加するプロパティを提供しています。

#### **セルに罫線を追加**

開発者は、[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)コレクションを使用してセルに罫線を追加できます。罫線のタイプは、[**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)列挙型で事前に定義されています。

**境界の列挙**

|**境界タイプ**|**説明**|
| :- | :- |
|BottomBorder|下部の境界線
|DiagonalDown|左上から右下への対角線
|DiagonalUp|左下から右上への対角線
|LeftBorder|左側の境界線
|RightBorder|右側の境界線
|TopBorder|上部の境界線

The [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border) object which provides two properties, [**Color**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) and [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) to set a border's line color and style respectively.

境界線の線の色を設定するには、.NET Frameworkの一部であるColor列挙型を使用して色を選択し、それをBorderオブジェクトのColorプロパティに割り当てます。

境界線の線スタイルは、[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)列挙体から線スタイルを選択して設定されます。

**CellBorderType列挙体**

|**線のスタイル**|**説明**|
| :- | :- |
|DashDot|細い点線のような線
|DashDotDot|細い破線点線のような線
|Dashed|破線のような線
|Dotted|点線のような線
|Double|二重線
|Hair|細い線
|MediumDashDot|中くらいの点線のような線
|MediumDashDotDot|中くらいの破線点線のような線
|MediumDashed|中くらいの破線のような線
|None|線なし
|Medium|中くらいの線
|SlantedDashDot|対角の中くらいの点線のような線
|Thick|太い線
|Thin|細い線
線のスタイルを選択してから、[**Border**](https://reference.aspose.com/cells/net/aspose.cells/border)オブジェクトの [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) プロパティにそれを割り当てます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

線のスタイルと色の両方を同時に設定する必要があります。 2つの対角線の境界線は、同じ線スタイルと色を持っている必要があります。

{{% /alert %}}

#### **セルの範囲に境界線を追加する**

1つのセルだけでなく、セルの範囲にも境界線を追加することができます。そのためには、まず[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1)メソッドを呼び出して、セルの範囲を作成します。 このメソッドには、次のパラメータを渡します:

- 最初の行、範囲の最初の行。
- 最初の列、範囲の最初の列を表す。
- 行数、範囲内の行数。
- 列数、範囲内の列数。

[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) メソッドは、指定されたセルの範囲を含む [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) オブジェクトを返し、[**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) オブジェクトは、次のパラメータを取る [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) メソッドを提供する。

- **境界線の種類**、[**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) 列挙型から選択した境界線の種類。
- **線のスタイル**、[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype) 列挙型から選択した境界線のスタイル。
- **色**、Color 列挙型から選択した線の色。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
