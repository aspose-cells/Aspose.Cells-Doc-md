---
title: 塗りつぶし設定
description: Aspose.Cellsは、スプレッドシートファイルを操作するためのPythonライブラリです。セルの塗りつぶし設定を行うことができ、セルの背景やスタイルをカスタマイズできます。この記事では、Aspose.Cells for Python via .NETライブラリを使用してセルの塗りつぶし設定を行う方法を紹介します。
keywords: Aspose.Cells for Python via .NET、セル、塗りつぶし設定、背景、スタイル
type: docs
weight: 50
url: /ja/python-net/cells-fill-settings/
---

## **色と背景パターン**

Microsoft Excel では、セルの前景（輪郭）と背景（塗りつぶし）の色、および背景パターンを設定できます。

Aspose.Cells for Python via .NETは、これらの機能も柔軟にサポートしています。このトピックでは、Aspose.Cellsを使用してこれらの機能を使う方法を学びます。

### **色と背景パターンの設定**

Aspose.Cells for Python via .NETは、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションの各アイテムは[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスのオブジェクトを表します。

[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)はセルの書式設定を取得・設定するための[**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style)と[**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style)メソッドを持っています。[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)クラスはセルの前景色と背景色を設定するプロパティを提供します。Aspose.Cells for Python via .NETは、以下に示す背景パターンの事前定義されたタイプを含む[**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype)列挙体を提供します。

|**背景パターン**|**説明**|
| :- | :- |
|DIAGONAL_CROSSHATCH|斜交格子パターンを表します|
|DIAGONAL_STRIPE|斜線ストライプパターンを表します|
|GRAY6|6.25％のグレーパターンを表します|
|GRAY12|12.5％のグレーパターンを表します|
|GRAY25|25％のグレーパターンを表します|
|GRAY50|50％のグレーパターンを表します|
|GRAY75|75％のグレーパターンを表します|
|HORIZONTAL_STRIPE|水平ストライプパターンを表します|
|NONE|背景なしを表します|
|REVERSE_DIAGONAL_STRIPE|逆斜線ストライプパターンを表します|
|SOLID|単色パターンを表します|
|THICK_DIAGONAL_CROSSHATCH|太い斜交格子パターンを表します|
|THIN_DIAGONAL_CROSSHATCH|細い斜交格子パターンを表します|
|THIN_DIAGONAL_STRIPE|細い斜線ストライプパターンを表します|
|THIN_HORIZONTAL_CROSSHATCH|細い横格子パターンを表します|
|THIN_HORIZONTAL_STRIPE|細い横ストライプパターンを表します|
|THIN_REVERSE_DIAGONAL_STRIPE|細い逆斜線ストライプパターンを表します|
|THIN_VERTICAL_STRIPE|細い縦ストライプパターンを表します|
|VERTICAL_STRIPE|縦ストライプパターンを表します|

以下の例では、A1セルの前景色が設定されていますが、A2は前景色と背景色の両方を垂直ストライプの背景パターンで構成するように設定されています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndBackground-1.py" >}}

### **重要なこと**

{{% alert color="primary" %}}

- セルの前景色または背景色を設定するには、[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) オブジェクトの [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) または [**background_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_color) プロパティを使用します。どちらのプロパティも、[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) オブジェクトの [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) プロパティが構成されている場合のみ効果があります。
- [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) プロパティはセルのシェード色を設定します。
  [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern)プロパティは、前景色または背景色に使用される背景パターンの種類を指定します。Aspose.Cells for Python via .NETは、[**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype)という列挙体を提供し、一連の事前定義された背景パターンを含みます。
- [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype) 列挙体から *BackgroundType.None* 値を選択すると、前景色は適用されません。
  同様に、*BackgroundType.None* または *BackgroundType.Solid* 値を選択すると、背景色は適用されません。
- セルのシェード／塗りつぶし色を取得する場合、[**Style.pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) が *BackgroundType.None* であれば、[**Style.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) は *Color.Empty* を返します。

{{% /alert %}}

### **グラデーション塗りつぶし効果の適用**

セルに希望のグラデーション塗りつぶし効果を適用するには、[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) オブジェクトの [**set_two_color_gradient**](https://reference.aspose.com/cells/python-net/aspose.cells/style/set_two_color_gradient) メソッドを使用してください。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyingGradientFillEffects-1.py" >}}

## **色とパレット**

パレットとは、画像を作成するために使用可能な色の数です。プレゼンテーションで標準化されたパレットを使用することで、ユーザーは一貫した外観を作成できます。各 Microsoft Excel (97-2003) ファイルには、セル、フォント、グリッド線、グラフィックオブジェクト、塗りつぶし、およびグラフの線に適用できる 56 色のパレットがあります。

Aspose.Cells for Python via .NETを使用すれば、既存のパレットの色だけでなく、カスタムカラーも使用できます。カスタムカラーを使う前に、最初にパレットに追加してください。

このトピックでは、パレットにカスタム色を追加する方法について説明します。

### **パレットにカスタム色を追加**

Aspose.Cells for Python via .NETは、Microsoft Excelの56色パレットをサポートしています。パレットに定義されていないカスタムカラーを使用するには、その色をパレットに追加してください。

Aspose.Cells for Python via .NETは、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、次のパラメータを受け取ってパレットを変更するカスタムカラーを追加するための[**change_palette**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/change_palette)メソッドがあります：

- カスタムカラー、追加するカスタムカラー。
カスタムカラーが置き換えるパレット内の色のインデックスです。0〜55の間である必要があります。

以下の例では、カスタムカラー（Orchid）をパレットに追加し、フォントに適用する前に追加します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndPalette-1.py" >}}

{{% alert color="primary" %}}

パレットには56色しか保持できません。パレットにカスタムカラーを追加すると、パレットが変更され、前の色でフォーマットされたファイル内の要素が変更されます。したがって、パレットを変更する際は非常に注意してください。さらに、これはXLS（Excel 97-2003）ファイル形式の制限のみであり、XLSXまたはその他の高度なMS Excel（2007/2010または2013）ファイル形式ではこのような制限はありません。

{{% /alert %}}

