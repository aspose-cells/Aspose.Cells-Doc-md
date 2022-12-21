---
title: 塗りつぶし設定
type: docs
weight: 50
url: /ja/net/cells-fill-settings/
---
## **色と背景パターン**

Microsoft Excel では、セルの前景色 (アウトライン) と背景 (塗りつぶし) の色と背景パターンを設定できます。

Aspose.Cells もこれらの機能を柔軟にサポートします。このトピックでは、Aspose.Cells を使用してこれらの機能の使用方法を学習します。

### **色と背景パターンの設定**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。の各項目[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションはのオブジェクトを表します[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

の[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)を持っています[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)と[**スタイルの設定**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)セルの書式設定を取得および設定するために使用されるメソッド。の[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)クラスは、セルの前景色と背景色を設定するためのプロパティを提供します。 Aspose.Cells は[**背景の種類**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)以下に示す事前定義されたタイプの背景パターンのセットを含む列挙。

|**背景パターン**|**説明**|
|:- |:- |
|斜めクロスハッチ|斜めのクロスハッチ パターンを表します|
|斜めストライプ|斜めの縞模様を表現|
|グレー6|6.25% グレー パターンを表します|
|グレー12|12.5% グレー パターンを表します|
|グレイ25|25% グレー パターンを表します|
|グレイ50|50% グレー パターンを表します|
|グレイ75|75% グレー パターンを表します|
|横縞|横縞模様を表現|
|なし|背景なしを表します|
|逆対角ストライプ|逆斜め縞模様を表す|
|個体|ソリッドパターンを表します|
|太い対角線のクロスハッチ|太い斜めのクロスハッチ パターンを表します|
|薄い対角線のクロスハッチ|細い斜めのクロスハッチ パターンを表します|
|細い斜めストライプ|細い斜めの縞模様を表現|
|薄い水平クロスハッチ|薄い水平のクロスハッチ パターンを表します|
|薄い横縞|細い横縞模様を表現|
|薄い逆対角線ストライプ|細い逆斜めストライプパターンを表現|
|細い縦縞|細い縦縞模様を表現|
|縦ストライプ|縦縞模様を表現|

以下の例では、A1 セルの前景色が設定されていますが、A2 は縦縞の背景パターンで前景色と背景色の両方を持つように構成されています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **知っておくべき重要事項**

{{% alert color="primary" %}}

- セルの前景色または背景色を設定するには、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**前景色**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)また[**背景色**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor)プロパティ。両方のプロパティが有効になるのは、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**パターン**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)プロパティが構成されます。
- の[**前景色**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)プロパティは、セルの陰影の色を設定します。
の[**パターン**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)プロパティは、前景色または背景色に使用される背景パターンのタイプを指定します。 Aspose.Cells は列挙を提供し、[**背景の種類**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype).これには、定義済みのタイプの背景パターンのセットが含まれています。
- 選択した場合*BackgroundType.なし*からの値[**背景の種類**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)列挙、前景色は適用されません。
同様に、選択した場合、背景色は適用されません。*BackgroundType.なし*また*BackgroundType.Solid*値。
- セルのシェーディング/塗りつぶしの色を取得する場合、[**スタイル.パターン**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)は*BackgroundType.なし*, [**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)戻ります*色.空*.

{{% /alert %}}

### **グラデーション塗りつぶし効果の適用**

目的のグラデーション塗りつぶし効果をセルに適用するには、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)それに応じた方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

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
