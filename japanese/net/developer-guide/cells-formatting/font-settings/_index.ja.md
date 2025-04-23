---
title: フォント設定
description: Aspose.Cellsはスプレッドシートファイルを操作するための.NETライブラリです。セルのフォント設定をサポートし、ユーザーはセルのフォントスタイルとプロパティをカスタマイズできます。この記事では、Aspose.Cellsライブラリを使用してセルのフォント設定を行う方法について紹介します。
keywords: Aspose.Cells、Cells、フォント設定、スタイル、プロパティ
type: docs
weight: 30
url: /ja/net/cells-font-settings/
---

{{% alert color="primary" %}}

テキストの見た目はフォント設定を変更することでコントロールできます。フォント設定にはフォントの名前、スタイル、サイズ、色、その他の効果が含まれる場合があります。Microsoft Excelと同様に、Aspose.Cellsもセルのフォント設定をサポートしています。

{{% /alert %}}

## **フォント設定の構成**

Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスにはExcelファイル内の各ワークシートへのアクセスを許可する[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション内の各アイテムは[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラスのオブジェクトを表します。

Aspose.Cellsは、[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラスの[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)および[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)メソッドを提供しており、セルの書式設定スタイルの取得と設定に使用されます。[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)クラスはフォント設定を構成するためのプロパティを提供します。

### **フォント名の設定**

開発者は、[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[Name](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)プロパティを使用してセル内のテキストに任意のフォントを適用できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **太字にフォントスタイルを設定する**

開発者は、[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**IsBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold)プロパティを**true**に設定することでテキストを太字にすることができます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **フォントサイズの設定**

[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**Size**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)プロパティでフォントサイズを設定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **フォントの色の設定**

[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)プロパティを使用してフォントの色を設定します。.NETフレームワークの一部であるColor列挙型から任意の色を選択して[**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)プロパティに割り当てます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **フォントの下線タイプの設定**

[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**Underline**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)プロパティを使用してテキストに下線を付けます。Aspose.Cellsでは、[**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype)列挙型でさまざまな予め定義されたフォントの下線タイプを提供しています。

|**フォントの下線の種類**|**説明**|
| :- | :- |
|Accounting|単一のアカウンティング下線
|Double|ダブル下線
|DoubleAccounting|ダブルアカウンティング下線
|None|下線なし
|Single|単一の下線

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **取り消し線の効果の設定**

[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**IsStrikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)プロパティを**true**に設定することで取り消し線を適用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **下付き文字の効果の設定**

[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript)プロパティを**true**に設定することで下付き文字を適用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **フォントの上付き文字効果の設定**

開発者は、[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)オブジェクトの[**IsSuperscript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript)プロパティを**true**に設定することで、フォントに上付き文字効果を適用できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **高度なトピック**
- [フォントに上付き文字および下付き文字効果を適用する](/cells/ja/net/apply-superscript-and-subscript-effects-on-fonts/)
- [スプレッドシートまたはブックで使用されているフォントのリストを取得する](/cells/ja/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

{{< app/cells/assistant language="csharp" >}}
