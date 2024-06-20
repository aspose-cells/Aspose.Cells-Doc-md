---
title: フォント設定の取り扱い
linktitle: フォント設定
type: docs
weight: 20
url: /ja/java/dealing-with-font-settings/
---

{{% alert color="primary" %}} 

テキストの外観は、フォント設定を変更することで制御できます。 これらのフォント設定には、名前、スタイル、サイズ、色、およびその他のフォントの効果が含まれる場合があります。 下の図に示すように、これらのフォント設定を変更できます。

**Microsoft Excel のフォント設定** 

![todo:image_alt_text](dealing-with-font-settings_1.png)

Microsoft Excelと同様に、Aspose.Cellsもセルのフォント設定を構成することをサポートしています。

{{% /alert %}} 
## **フォント設定の構成**
Aspose.Cellsでは、Microsoft Excelファイルを表す [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) クラスが提供されています。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) クラスには、Excelファイル内の各ワークシートにアクセスできる [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) が含まれています。ワークシートは [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスによって表されます。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスは [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションを提供します。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクション内の各アイテムは [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) クラスのオブジェクトを表します。

Aspose.Cellsは[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) クラスの [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) メソッドを提供しており、これを使用してセルの書式設定を行います。また、 [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) クラスのオブジェクトはフォント設定を構成するためのプロパティを提供しています。

この記事では以下を紹介します：

- [- 特定のフォントをテキストに適用します。](/cells/ja/java/dealing-with-font-settings/)
- [テキストを太字に設定する](/cells/ja/java/dealing-with-font-settings/)。
- [フォントサイズを設定する](/cells/ja/java/dealing-with-font-settings/)。
- [フォントの色を設定する](/cells/ja/java/dealing-with-font-settings/)。
- [テキストに下線を引く](/cells/ja/java/dealing-with-font-settings/)。
- [テキストに取り消し線を引く](/cells/ja/java/dealing-with-font-settings/)。
- [テキストを下付きに設定する](/cells/ja/java/dealing-with-font-settings/)。
- [テキストを上付きに設定する](/cells/ja/java/dealing-with-font-settings/)。
### **フォント名の設定**
[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) オブジェクトの [setName](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name) プロパティを使用して、セル内のテキストに特定のフォントを適用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **太字にフォントスタイルを設定する**
[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) オブジェクトの [setBold](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) プロパティを **true** に設定することで、テキストを太字に設定します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **フォントサイズの設定**
[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) オブジェクトの [setSize](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size) プロパティを使用して、フォントサイズを設定します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **フォントの下線タイプの設定**
[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) オブジェクトの [setUnderline](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) プロパティを使用してテキストに下線を引きます。Aspose.Cellsでは、[FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType) 列挙型で様々な事前定義のフォント下線タイプを提供しています。

|**フォントの下線の種類**|**説明**|
| :- | :- |
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|下線なし|
|[SINGLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|一重下線|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|二重下線|
|[ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|一重財務用下線|
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|二重財務用下線|
|[DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|破線の下線|
|[DASH_DOT_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|太いダッシュ・ドット・ドット下線|
|[DASH_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|太いダッシュ・ドット下線|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|太い破線下線|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG)|長い破線下線|
|[DASH_LONG_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|太い長い破線下線|
|[DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DASH)|ダッシュ・ドット下線|
|[DOT_DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|ダッシュ・ドット・ドット下線|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|点線下線|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|太い点線下線|
|[HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|太い下線|
|[WAVE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|ウェーブ下線|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|二重ウェーブ下線|
|[WAVY_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|太いウェーブ下線|
|[WORDS](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|非空白文字の下線|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **フォントの色の設定**
[フォント](https://reference.aspose.com/cells/java/com.aspose.cells/Font)オブジェクトの[setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color)プロパティを使用してフォントの色を設定します。[Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)列挙型から任意の色を選択し、選択した色を[フォント](https://reference.aspose.com/cells/java/com.aspose.cells/Font)オブジェクトの[setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color)に割り当てます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **テキストに取り消し線効果を設定**
[フォント](https://reference.aspose.com/cells/java/com.aspose.cells/Font)オブジェクトの[setStrikeout](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout)プロパティを使用してテキストに取り消し線を設定します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **下付き文字を設定**
[フォント](https://reference.aspose.com/cells/java/com.aspose.cells/Font)オブジェクトの[setSubscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript)プロパティを使用してテキストを下付き文字にします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **上付き文字を設定**
[フォント](https://reference.aspose.com/cells/java/com.aspose.cells/Font)オブジェクトの[setSuperscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript)プロパティを使用してテキストに上付き文字を適用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **高度なトピック**
- [フォントに上付き文字および下付き文字効果を適用する](/cells/ja/java/apply-superscript-and-subscript-effects-on-fonts/)
- [スプレッドシートまたはブックで使用されているフォントのリストを取得する](/cells/ja/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
