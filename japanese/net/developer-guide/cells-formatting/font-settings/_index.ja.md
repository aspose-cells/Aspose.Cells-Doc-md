---
title: フォント設定
description: Aspose.Cells は、スプレッドシート ファイルを操作するための .NET ライブラリです。セルのフォント設定をサポートしているため、ユーザーはセルのフォント スタイルとプロパティをカスタマイズできます。この記事では、Aspose.Cellsライブラリを使ってセルのフォントを設定する方法を紹介します。
keywords: Aspose.Cells, Cells, Font Settings, Styles, Properties
type: docs
weight: 30
url: /ja/net/cells-font-settings/
---
{{% alert color="primary" %}}

テキストの外観と雰囲気は、フォント設定を変更することで制御できます。フォント設定には、フォントの名前、スタイル、サイズ、色、その他の効果が含まれる場合があります。 Microsoft Excel と同様に、Aspose.Cells もセルのフォント設定の構成をサポートしています。

{{% /alert %}}

##  **フォント設定の構成**

Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)これは Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供するのは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の各項目[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションはオブジェクトを表します[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

 Aspose.Cells は、[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス'[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)そして[**スタイルの設定**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)セルの書式設定スタイルを取得および設定するために使用されるメソッド。の[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)クラスは、フォント設定を構成するためのプロパティを提供します。

###  **フォント名の設定**

開発者は、[**スタイル.フォント**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[名前](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

###  **フォントスタイルを太字に設定する**

開発者は、[**スタイル.フォント**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**大胆です**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold)プロパティを *true** に設定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

###  **フォントサイズの設定**

でフォントサイズを設定します[**スタイル.フォント**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**サイズ**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

###  **フォントの色の設定**

使用[**スタイル.フォント**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**色**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)フォントの色を設定するプロパティ。 Color 列挙 (.NET フレームワークの一部) から任意の色を選択し、それを[**色**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

###  **フォントの下線の種類を設定する**

使用[**スタイル.フォント**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**下線**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)テキストに下線を付けるプロパティ。 Aspose.Cells は、さまざまな事前定義フォントの下線タイプを提供しています。[**フォント下線の種類**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype)列挙。

|**フォントの下線の種類**|**説明**|
| :- | :- |
|会計|会計上の単一の下線|
|ダブル|二重下線|
|二重会計|二重会計下線|
|なし|下線なし|
|シングル|単一の下線|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

###  **ストライクアウト効果の設定**

を設定して取り消し線を適用します。[**スタイル.フォント**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**は三振**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)プロパティを *true** に設定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

###  **下付き文字効果の設定**

を設定して添え字を適用します。[**スタイル.フォント**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**サブスクリプトです**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript)プロパティを *true** に設定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

###  **フォントの上付き効果を設定する**

開発者は、次の設定を行うことでフォントに上付き文字効果を適用できます。[**上付き文字です**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript)の財産[**スタイル.フォント**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトを *true** に設定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

##  **アドバンストトピック**
- [フォントに上付き文字と下付き文字の効果を適用する](/cells/ja/net/apply-superscript-and-subscript-effects-on-fonts/)
- [スプレッドシートまたはワークブックで使用されているフォントのリストを取得する](/cells/ja/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

