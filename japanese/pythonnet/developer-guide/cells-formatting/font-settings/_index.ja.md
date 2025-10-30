---
title: フォント設定
description: Aspose.Cellsは、スプレッドシートファイルを操作するためのPythonライブラリです。セルのフォント設定を設定でき、セルのフォントスタイルやプロパティをカスタマイズできます。この記事では、Aspose.Cells for Python via .NETライブラリを使用してセルのフォント設定を設定する方法を紹介します。
keywords: Aspose.Cells for Python via .NET、セル、フォント設定、スタイル、プロパティ
type: docs
weight: 30
url: /ja/python-net/cells-font-settings/
---

{{% alert color="primary" %}}

テキストの見た目や感触は、フォント設定を変更することでコントロールできます。フォント設定には、フォント名、スタイル、サイズ、色、その他の効果が含まれることがあります。Microsoft Excelと同様に、Aspose.Cells for Python via .NETもセルのフォント設定の構成をサポートしています。

{{% /alert %}}

## **フォント設定の構成**

Aspose.Cells for Python via .NETは、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスは[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)コレクションを提供します。[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/)コレクションの各アイテムは[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスのオブジェクトを表します。

Aspose.Cellsは、[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスの[**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style)および[**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style)メソッドを提供しており、セルの書式設定スタイルの取得と設定に使用されます。[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)クラスはフォント設定を構成するためのプロパティを提供します。

### **フォント名の設定**

開発者は、[**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)オブジェクトの[**name**](https://reference.aspose.com/cells/python-net/aspose.cells/font/name/)プロパティを使用してセル内のテキストに任意のフォントを適用できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontName-1.py" >}}

### **太字にフォントスタイルを設定する**

開発者は、[**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)オブジェクトの[**is_bold**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_bold)プロパティを**true**に設定することでテキストを太字にすることができます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontStyle.py" >}}

### **フォントサイズの設定**

[**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)オブジェクトの[**size**](https://reference.aspose.com/cells/python-net/aspose.cells/font/size)プロパティでフォントサイズを設定します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontSize.py" >}}

### **フォントの色の設定**

[**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)オブジェクトの[**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color)プロパティを使用してフォントの色を設定します。.NETフレームワークの一部であるColor列挙型から任意の色を選択して[**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color)プロパティに割り当てます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontColor.py" >}}

### **フォントの下線タイプの設定**

[**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)オブジェクトの[**underline**](https://reference.aspose.com/cells/python-net/aspose.cells/font/underline)プロパティを使用してテキストに下線を引きます。Aspose.Cells for Python via .NETは、[**FontUnderlineType**](https://reference.aspose.com/cells/python-net/aspose.cells/fontunderlinetype)列挙体にさまざまな事前定義されたフォント下線タイプを提供します。

|**フォントの下線の種類**|**説明**|
| :- | :- |
|会計|単一の会計下線|
|二重|二重下線|
|二重会計|二重会計下線|
|なし|下線なし|
|シングル|単一下線|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontUnderlineType-1.py" >}}

### **取り消し線の効果の設定**

[**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)オブジェクトの[**is_strikeout**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_strikeout)プロパティを**true**に設定することで取り消し線を適用します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetStrikeout.py" >}}

### **下付き文字の効果の設定**

[**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)オブジェクトの[**is_subscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_subscript/)プロパティを**true**に設定することで下付き文字を適用します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSubscript.py" >}}

### **フォントの上付き文字効果の設定**

開発者は、[**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)オブジェクトの[**is_superscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_superscript)プロパティを**true**に設定することで、フォントに上付き文字効果を適用できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSuperscript.py" >}}

## **高度なトピック**
- [フォントに上付き文字および下付き文字効果を適用する](/cells/ja/python-net/apply-superscript-and-subscript-effects-on-fonts/)
- [スプレッドシートまたはブックで使用されているフォントのリストを取得する](/cells/ja/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)


{{< app/cells/assistant language="python-net" >}}
