---
title: 塗りつぶし設定
description: Aspose.Cells は、スプレッドシート ファイルを操作するための .NET ライブラリです。セルの塗りつぶし設定をサポートしているため、ユーザーはセルの背景とスタイルをカスタマイズできます。この記事では、Aspose.Cellsライブラリを使ってセルの塗りつぶし設定を行う方法を紹介します。
keywords: Aspose.Cells, Cells, Fill Settings, Background, Style
type: docs
weight: 50
url: /ja/net/cells-fill-settings/
---
##  **色と背景パターン**

Microsoft Excelではセルの前景色（輪郭）と背景（塗りつぶし）の色や背景パターンを設定できます。

Aspose.Cells もこれらの機能を柔軟にサポートします。このトピックでは、Aspose.Cells を使用してこれらの機能を使用する方法を学習します。

###  **色と背景パターンを設定する**

Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)これは Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供するのは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。の各項目[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションはオブジェクトを表します[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

の[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)持っています[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)そして[**スタイルの設定**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)セルの書式設定を取得および設定するために使用されるメソッド。の[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)このクラスは、セルの前景色と背景色を設定するためのプロパティを提供します。 Aspose.Cells は、[**背景の種類**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)以下に示す事前定義されたタイプの背景パターンのセットを含む列挙体。

|**背景パターン**|**説明**|
| :- | :- |
|斜めクロスハッチング|斜めのクロスハッチ パターンを表します|
|斜めストライプ|斜めストライプ模様を表現|
|グレー6|6.25%のグレーパターンを表します|
|グレー12|12.5%のグレーパターンを表します|
|グレー25|25% グレー パターンを表します|
|グレー50|50% グレー パターンを表します|
|グレー75|75% グレー パターンを表します|
|水平ストライプ|横縞模様を表現|
|なし|背景なしを表します|
|逆斜めストライプ|逆斜めストライプ柄を表現|
|固体|ベタパターンを表現します|
|太い斜めのクロスハッチング|太い斜めのクロスハッチパターンを表現します|
|薄い斜めの網目模様|細い斜めのクロスハッチ パターンを表現します|
|細い斜めストライプ|細い斜めストライプ模様を表現|
|薄い水平クロスハッチング|細い水平クロスハッチ パターンを表現します|
|細い水平ストライプ|細い横縞模様を表現|
|細い逆斜めストライプ|細い逆斜めストライプ柄を表現|
|細い垂直ストライプ|細い縦縞模様を表現|
|縦ストライプ|縦縞模様を表現|

以下の例では、A1 セルの前景色が設定されていますが、A2 は前景色と背景色の両方を持ち、縦縞の背景パターンを持つように構成されています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

###  **知っておくべき重要なこと**

{{% alert color="primary" %}}

- セルの前景色または背景色を設定するには、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**前景色**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)または[**背景色**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor)プロパティ。両方のプロパティは、次の場合にのみ有効になります。[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**パターン**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)プロパティが設定されています。
- の[**前景色**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)プロパティはセルの陰影の色を設定します。
の[**パターン**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)プロパティは、前景色または背景色に使用される背景パターンのタイプを指定します。 Aspose.Cells は列挙を提供します。[**背景の種類**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)。これには、事前定義されたタイプの背景パターンのセットが含まれています。
- 選択した場合*BackgroundType.None*からの値[**背景の種類**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)列挙の場合、前景色は適用されません。
同様に、を選択した場合、背景色は適用されません。*BackgroundType.None*または*BackgroundType.Solid*価値観。
- セルのシェーディング/塗りつぶしの色を取得するときに、[**スタイル.パターン**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)は *BackgroundType.None*、[**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) *Color.Empty* を返します。

{{% /alert %}}

###  **グラデーション塗りつぶし効果の適用**

希望のグラデーション塗りつぶし効果をセルに適用するには、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)それに応じた方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

##  **色とパレット**

パレットとは、画像の作成に使用できる色の数です。プレゼンテーションで標準化されたパレットを使用すると、ユーザーは一貫した外観を作成できます。各 Microsoft Excel (97-2003) ファイルには、グラフ内のセル、フォント、グリッド線、グラフィック オブジェクト、塗りつぶし、線に適用できる 56 色のパレットがあります。

Aspose.Cells を使用すると、パレットの既存の色だけでなく、カスタム カラーも使用できます。カスタム カラーを使用する前に、まずパレットに追加します。

このトピックでは、カスタム カラーをパレットに追加する方法について説明します。

###  **カスタムカラーをパレットに追加する**

Aspose.Cells は Microsoft Excel の 56 カラー パレットをサポートします。パレットで定義されていないカスタム カラーを使用するには、そのカラーをパレットに追加します。

Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、これは Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスが提供するのは[**パレットの変更**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette)このメソッドは次のパラメーターを受け取り、カスタム カラーを追加してパレットを変更します。

- カスタムカラー、追加するカスタムカラー。
- インデックス。カスタム カラーで置き換えられるパレット内の色のインデックス。 0 ～ 55 の間である必要があります。

以下の例では、カスタム カラー (Orchid) をフォントに適用する前にパレットに追加します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

パレットに保持できる色は 56 色のみです。カスタム カラーをパレットに追加すると、パレットが変更され、以前のカラーでフォーマットされたファイル内の要素が変更されます。したがって、パレットを変更するときは十分に注意してください。さらに、これは XLS (Excel 97 ～ 2003) ファイル形式のみの制限であり、XLSX またはその他の高度な MS Excel (2007/2010 または 2013) ファイル形式にはそのような制限はありません。

{{% /alert %}}
