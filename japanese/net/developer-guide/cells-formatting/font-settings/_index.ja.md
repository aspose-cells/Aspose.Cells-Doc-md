---
title: フォント設定
type: docs
weight: 30
url: /ja/net/cells-font-settings/
---
{{% alert color="primary" %}}

テキストのルック アンド フィールは、フォント設定を変更することで制御できます。フォント設定には、フォントの名前、スタイル、サイズ、色、およびその他の効果が含まれる場合があります。 Microsoft Excel と同様に、Aspose.Cells もセルのフォント設定の構成をサポートしています。

{{% /alert %}}

## **フォント設定の構成**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の各項目[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションはのオブジェクトを表します[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

Aspose.Cells は[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス'[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)と[**スタイルの設定**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)セルの書式設定スタイルを取得および設定するために使用されるメソッド。の[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)クラスは、フォント設定を構成するためのプロパティを提供します。

### **フォント名の設定**

開発者は、セル内のテキストに任意のフォントを適用できます。[**スタイル.フォント**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[名前](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **フォント スタイルを太字に設定する**

開発者は、設定することでテキストを太字にすることができます[**スタイル.フォント**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**太字**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold)プロパティへ**真実**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **フォントサイズの設定**

でフォントサイズを設定します[**スタイル.フォント**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**サイズ**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **フォントの色の設定**

使用[**スタイル.フォント**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**色**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)フォントの色を設定するプロパティ。 Color 列挙体 (.NET フレームワークの一部) から任意の色を選択し、[**色**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **フォントの下線タイプの設定**

使用[**スタイル.フォント**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**下線**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)テキストに下線を引くプロパティ。 Aspose.Cells は、さまざまな定義済みフォントの下線タイプを[**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype)列挙。

|**フォントの下線の種類**|**説明**|
|:- |:- |
|会計|単一の会計下線|
|ダブル|二重下線|
|二重会計|二重会計下線|
|なし|下線なし|
|独身|一重下線|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **打ち消し効果の設定**

を設定して取り消し線を適用する[**スタイル.フォント**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**は三振**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)プロパティへ**真実**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **下付き効果の設定**

を設定して添え字を適用する[**スタイル.フォント**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript)プロパティへ**真実**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **フォントに上付き文字効果を設定する**

開発者は、設定することにより、フォントに上付き文字効果を適用できます。[**上付き文字**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript)のプロパティ[**スタイル.フォント**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)異議を唱える**真実**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **先行トピック**
- [フォントに上付きおよび下付き効果を適用する](/cells/ja/net/apply-superscript-and-subscript-effects-on-fonts/)
- [スプレッドシートまたはワークブックで使用されているフォントのリストを取得する](/cells/ja/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

