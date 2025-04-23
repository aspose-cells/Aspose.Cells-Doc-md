---
title: 塗りつぶし設定
description: Aspose.Cells は、スプレッドシートファイルを操作するための .NET ライブラリです。セルの塗りつぶし設定をサポートし、ユーザーがセルの背景とスタイルをカスタマイズできます。この記事では、Aspose.Cells ライブラリを使用してセルの塗りつぶし設定を行う方法について紹介します。
keywords: Aspose.Cells、Cells、塗りつぶし設定、背景、スタイル
type: docs
weight: 50
url: /ja/net/cells-fill-settings/
---

## **色と背景パターン**

Microsoft Excel では、セルの前景（輪郭）と背景（塗りつぶし）の色、および背景パターンを設定できます。

Aspose.Cells もこれらの機能を柔軟にサポートしています。このトピックでは、Aspose.Cells を使用してこれらの機能を使用する方法について学びます。

### **色と背景パターンの設定**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション内の各項目は[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラスのオブジェクトを表します。

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) には [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) および [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) メソッドがあり、セルの書式設定を取得および設定するために使用されます。[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) クラスには、セルの前景色と背景色を設定するためのプロパティがあります。 Aspose.Cells には、以下で示される一連の事前定義された背景パターンのタイプが含まれる [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype) 列挙型があります。

|**背景パターン**|**説明**|
| :- | :- |
|DiagonalCrosshatch| 対角線のかすかな格子状のパターンを表します|
|DiagonalStripe| 対角線のストライプパターンを表します|
|Gray6| 6.25% グレーのパターンを表します|
|Gray12| 12.5% グレーのパターンを表します|
|Gray25| 25% グレーのパターンを表します|
|Gray50| 50% グレーのパターンを表します|
|Gray75| 75% グレーのパターンを表します|
|HorizontalStripe|水平ストライプパターンを表します|
|None|背景なしを表します|
|ReverseDiagonalStripe|反対角ストライプパターンを表します|
|Solid|ソリッドパターンを表します|
|ThickDiagonalCrosshatch|太い斜めクロスハッチパターンを表します|
|ThinDiagonalCrosshatch|細い斜めクロスハッチパターンを表します|
|ThinDiagonalStripe|細い斜めストライプパターンを表します|
|ThinHorizontalCrosshatch|細い水平クロスハッチパターンを表します|
|ThinHorizontalStripe|細い水平ストライプパターンを表します|
|ThinReverseDiagonalStripe|細い逆斜めストライプパターンを表します|
|ThinVerticalStripe|細い垂直ストライプパターンを表します|
|VerticalStripe|垂直ストライプパターンを表します|

以下の例では、A1セルの前景色が設定されていますが、A2は前景色と背景色の両方を垂直ストライプの背景パターンで構成するように設定されています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **重要なこと**

{{% alert color="primary" %}}

- セルの前景色または背景色を設定するには、[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) オブジェクトの [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) または [**BackgroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) プロパティを使用します。どちらのプロパティも、[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) オブジェクトの [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) プロパティが構成されている場合のみ効果があります。
- [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) プロパティはセルのシェード色を設定します。
  [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) プロパティは、前景色または背景色に使用される背景パターンの種類を指定します。Aspose.Cells は、一連の事前定義された背景パターンの種類を含む [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype) 列挙体を提供します。
- [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype) 列挙体から *BackgroundType.None* 値を選択すると、前景色は適用されません。
  同様に、*BackgroundType.None* または *BackgroundType.Solid* 値を選択すると、背景色は適用されません。
- セルのシェード／塗りつぶし色を取得する場合、[**Style.Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) が *BackgroundType.None* であれば、[**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) は *Color.Empty* を返します。

{{% /alert %}}

### **グラデーション塗りつぶし効果の適用**

セルに希望のグラデーション塗りつぶし効果を適用するには、[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) オブジェクトの [**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient) メソッドを使用してください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

## **色とパレット**

パレットとは、画像を作成するために使用可能な色の数です。プレゼンテーションで標準化されたパレットを使用することで、ユーザーは一貫した外観を作成できます。各 Microsoft Excel (97-2003) ファイルには、セル、フォント、グリッド線、グラフィックオブジェクト、塗りつぶし、およびグラフの線に適用できる 56 色のパレットがあります。

Aspose.Cells を使用すると、パレットの既存の色だけでなく、カスタム色も使用できます。カスタム色を使用する前に、まずパレットに色を追加します。

このトピックでは、パレットにカスタム色を追加する方法について説明します。

### **パレットにカスタム色を追加**

Aspose.Cells は Microsoft Excel の 56 色のパレットをサポートしています。パレットに定義されていないカスタム色を使用するには、その色をパレットに追加します。

Aspose.Cells は、Microsoft Excel ファイルを表す [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) クラスには、パレットを変更するための [**ChangePalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) メソッドがあり、カスタム色を追加するために次のパラメータを取ります:

- カスタムカラー、追加するカスタムカラー。
カスタムカラーが置き換えるパレット内の色のインデックスです。0〜55の間である必要があります。

以下の例では、カスタムカラー（Orchid）をパレットに追加し、フォントに適用する前に追加します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

パレットには56色しか保持できません。パレットにカスタムカラーを追加すると、パレットが変更され、前の色でフォーマットされたファイル内の要素が変更されます。したがって、パレットを変更する際は非常に注意してください。さらに、これはXLS（Excel 97-2003）ファイル形式の制限のみであり、XLSXまたはその他の高度なMS Excel（2007/2010または2013）ファイル形式ではこのような制限はありません。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
