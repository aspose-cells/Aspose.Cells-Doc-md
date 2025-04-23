---
title: 罫線設定
description: PythonでAspose.Cells for Python via .NETライブラリを使用して、セルの枠線のスタイルと色を設定する方法。枠線の幅、スタイル、色を調整することで、セルの見た目をより細かく制御できます。
keywords: Aspose.Cells for Python via .NET、セル枠設定、Pythonの枠線幅、枠線スタイル、枠線色
type: docs
weight: 40
url: /ja/python-net/cells-border-settings/
---

## **セルにボーダーを追加する**

Microsoft Excelでは、ユーザーが罫線を追加することでセルのフォーマットを指定できます。追加する罫線の種類は、追加される位置に依存します。たとえば、上部の罫線はセルの上部に追加される罫線です。Aspose.Cellsでは、開発者はMicrosoft Excelと同じ柔軟な方法で罫線を追加し、外見をカスタマイズできます。

Aspose.Cells for Python via .NETを使用すると、開発者はExcelと同じ柔軟な方法で枠線を追加およびカスタマイズできます。

### **セルにボーダーを追加する**

Aspose.Cells for Python via .NETは、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを提供します。このクラスはMicrosoft Excelファイルを表します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクション内の各アイテムは[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスのオブジェクトを表します。

Aspose.Cells for Python via .NETは、[**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style)メソッドを[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスに提供します。この[**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style)メソッドはセルの書式スタイルを設定するために使用されます。[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)クラスはセルに枠線を追加するためのプロパティを提供します。

#### **セルに罫線を追加**

開発者は、[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)オブジェクトの[**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders)コレクションを使用してセルに罫線を追加できます。罫線のタイプは、[**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders)列挙型で事前に定義されています。

**境界の列挙**

|**境界タイプ**|**説明**|
| :- | :- |
|BOTTOM_BORDER|下境界線|
|DIAGONAL_DOWN|左上から右下へ向かう斜め線|
|DIAGONAL_UP|左下から右上へ向かう斜め線|
|LEFT_BORDER|左側の境界線|
|RIGHT_BORDER|右側の境界線|
|TOP_BORDER|上の境界線|

The [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border) object which provides two properties, [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/border/color) and [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) to set a border's line color and style respectively.

境界線の線の色を設定するには、.NET Frameworkの一部であるColor列挙型を使用して色を選択し、それをBorderオブジェクトのColorプロパティに割り当てます。

境界線の線スタイルは、[**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype)列挙体から線スタイルを選択して設定されます。

**CellBorderType列挙体**

|**線のスタイル**|**説明**|
| :- | :- |
|DASH_DOT|細い点線の線|
|DASH_DOT_DOT|細い点線の二点線|
|DASHED|破線|
|DOTTED|点線|
|DOUBLE|二重線|
|HAIR|細線|
|MEDIUM_DASH_DOT|中間の破線点線|
|MEDIUM_DASH_DOT_DOT|中間の破点線|
|MEDIUM_DASHED|中くらいの破線|
|NONE|線無し|
|MEDIUM|中程度の線|
|SLANTED_DASH_DOT|斜め中点破線付き線|
|THICK|太い線|
|THIN|細い線|
線のスタイルを選択してから、[**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border)オブジェクトの [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) プロパティにそれを割り当てます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBordersToCells-1.py" >}}

{{% alert color="primary" %}}

線のスタイルと色の両方を同時に設定する必要があります。 2つの対角線の境界線は、同じ線スタイルと色を持っている必要があります。

{{% /alert %}}

#### **セルの範囲に境界線を追加する**

1つのセルだけでなく、セルの範囲にも境界線を追加することができます。そのためには、まず[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションの[**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range)メソッドを呼び出して、セルの範囲を作成します。 このメソッドには、次のパラメータを渡します:

- 最初の行、範囲の最初の行。
- 最初の列、範囲の最初の列を表す。
- 行数、範囲内の行数。
- 列数、範囲内の列数。

[**create_range**](hhttps://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str) メソッドは、指定されたセルの範囲を含む [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) オブジェクトを返し、[**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) オブジェクトは、次のパラメータを取る [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border) メソッドを提供する。

- **境界線の種類**、[**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype) 列挙型から選択した境界線の種類。
- **線のスタイル**、[**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype) 列挙型から選択した境界線のスタイル。
- **色**、Color 列挙型から選択した線の色。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBorderstoRange-1.py" >}}

