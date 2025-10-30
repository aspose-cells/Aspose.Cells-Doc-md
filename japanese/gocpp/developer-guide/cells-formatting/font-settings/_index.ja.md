---
title: GolangをC++経由で使用したフォント設定
linktitle: フォント設定
type: docs
weight: 30
url: /ja/go-cpp/cells-font-settings/
description: Aspose.Cellsは、スプレッドシートファイルを操作するC++ライブラリです。セルのフォント設定をサポートし、フォントのスタイルやプロパティをカスタマイズできます。この記事では、Aspose.Cellsライブラリを使用してセルのフォント設定を行う方法を示します。
keywords: Aspose.Cells、Cells、フォント設定、スタイル、プロパティ
---

{{% alert color="primary" %}}

テキストの見た目はフォント設定を変更することで制御できます。フォント設定には、フォント名、スタイル、サイズ、色、その他効果が含まれます。Microsoft Excelと同様に、Aspose.Cellsもセルのフォント設定をサポートしています。

{{% /alert %}}

## **フォント設定の構成**

Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)クラスにはExcelファイル内の各ワークシートへのアクセスを許可する[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションが含まれます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)コレクションを提供します。[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)コレクション内の各アイテムは[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスのオブジェクトを表します。

Aspose.Cellsは、[**Cell**](https://reference.aspose.com/cells/go-cpp/cell/)クラスの[**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/)および[**SetStyle**](https://reference.aspose.com/cells/go-cpp/cell/setstyle/)メソッドを提供しており、セルの書式設定スタイルの取得と設定に使用されます。[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)クラスはフォント設定を構成するためのプロパティを提供します。

### **フォント名の設定**

開発者は、[**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/)オブジェクトの[GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/)プロパティを使用して任意のフォントをセル内のテキストに適用できます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings.go" >}}
### **太字にフォントスタイルを設定する**

開発者は、[**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/)オブジェクトの[**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/)プロパティを**true**に設定することでテキストを太字にすることができます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-1.go" >}}
### **フォントサイズの設定**

[**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/)オブジェクトの[**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/)プロパティでフォントサイズを設定します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-2.go" >}}
### **フォントの色の設定**

[**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/)オブジェクトの[**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/)プロパティを使用してフォントの色を設定します。Color列挙体（C++フレームワークの一部）から任意の色を選択し、[**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/)プロパティに割り当ててください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-3.go" >}}
### **フォントの下線タイプの設定**

[**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/)オブジェクトの[**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/)プロパティを使用してテキストに下線を付けます。Aspose.Cellsでは、[**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/)列挙型でさまざまな予め定義されたフォントの下線タイプを提供しています。

|**フォントの下線の種類**|**説明**|
| :- | :- |
|Accounting|単一のアカウンティング下線
|Double|ダブル下線
|DoubleAccounting|ダブルアカウンティング下線
|None|下線なし
|Single|単一の下線

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-4.go" >}}
### **取り消し線の効果の設定**

[**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/)オブジェクトの[**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/)プロパティを**true**に設定することで取り消し線を適用します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-5.go" >}}
### **下付き文字の効果の設定**

[**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/)オブジェクトの[**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/)プロパティを**true**に設定することで下付き文字を適用します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-6.go" >}}
### **フォントの上付き文字効果の設定**

開発者は、[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)オブジェクトの[**IsSuperscript**](https://reference.aspose.com/cells/go-cpp/font/issuperscript/)プロパティを**true**に設定することで、フォントに上付き文字効果を適用できます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-7.go" >}}
## **高度なトピック**
- [フォントに上付き文字および下付き文字効果を適用する](/cells/ja/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [スプレッドシートまたはブックで使用されているフォントのリストを取得する](/cells/ja/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
