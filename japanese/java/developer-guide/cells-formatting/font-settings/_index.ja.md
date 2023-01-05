---
title: フォント設定の扱い
linktitle: フォント設定
type: docs
weight: 20
url: /ja/java/dealing-with-font-settings/
---
{{% alert color="primary" %}} 

テキストのルック アンド フィールは、フォント設定を変更することで制御できます。これらのフォント設定には、下の図に示すように、フォントの名前、スタイル、サイズ、色、およびその他の効果が含まれる場合があります。

**Microsoft エクセルのフォント設定** 

![todo:画像_代替_文章](dealing-with-font-settings_1.png)

Microsoft Excel と同様に、Aspose.Cells もセルのフォント設定の構成をサポートしています。

{{% /alert %}} 
## **フォント設定の構成**
Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスには[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスは[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。の各項目[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションはのオブジェクトを表します[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラス。

Aspose.Cells は[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)クラス'[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ) メソッド。セルの書式を設定するために使用されます。また、オブジェクトの[スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/Style)クラスは、フォント設定を構成するためのプロパティを提供します。

この記事では、次の方法について説明します。

- [特定のフォントをテキストに適用します。](/cells/ja/java/dealing-with-font-settings/)
- [テキストを太字に設定](/cells/ja/java/dealing-with-font-settings/).
- [フォントサイズを設定する](/cells/ja/java/dealing-with-font-settings/).
- [フォントの色を設定する](/cells/ja/java/dealing-with-font-settings/).
- [テキストに下線を引く](/cells/ja/java/dealing-with-font-settings/).
- [取り消し線テキスト](/cells/ja/java/dealing-with-font-settings/).
- [テキストを下付き文字に設定](/cells/ja/java/dealing-with-font-settings/).
- [テキストを上付き文字に設定](/cells/ja/java/dealing-with-font-settings/).
### **フォント名の設定**
を使用して、セル内のテキストに特定のフォントを適用します。[フォント](https://reference.aspose.com/cells/java/com.aspose.cells/Font)オブジェクトの[セット名](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name)財産。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **フォント スタイルを太字に設定する**
を設定して、テキストを太字に設定します。[フォント](https://reference.aspose.com/cells/java/com.aspose.cells/Font)オブジェクトの[setBold](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold)プロパティへ**真実**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **フォントサイズの設定**
を使用してフォント サイズを設定します。[フォント](https://reference.aspose.com/cells/java/com.aspose.cells/Font)オブジェクトの[セットサイズ](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size)財産。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **フォントの下線タイプの設定**
でテキストに下線を引く[フォント](https://reference.aspose.com/cells/java/com.aspose.cells/Font)オブジェクトの[setUnderline](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline)財産。 Aspose.Cells は、さまざまな定義済みフォントの下線タイプを[FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType)列挙。

|**フォントの下線の種類**|**説明**|
|:- |:- |
|[なし](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|下線なし|
|[独身](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|一重下線|
|[ダブル](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|二重下線|
|[会計](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|単一の会計下線|
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|二重会計下線|
|[ダッシュ](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|破線の下線|
|[ダッシュ_ドット_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|太い一点一点下線|
|[ダッシュ_ドット_重い](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|太い一点鎖線の下線|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|太い破線の下線|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG)|長い破線の下線|
|[ダッシュ_長いです_重い](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|太い長い破線の下線|
|[DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DASH)|一点鎖線の下線|
|[ドット_ドット_ダッシュ](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|一点一点下線|
|[点在](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|点線の下線|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|太い点線の下線|
|[重い](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|太い下線|
|[波](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|波下線|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|二重波下線|
|[WAVY_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|太波下線|
|` `[言葉](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|スペース以外の文字のみに下線を引く|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **フォントの色の設定**
でフォントの色を設定します[フォント](https://reference.aspose.com/cells/java/com.aspose.cells/Font)オブジェクトの[setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color)財産。から任意の色を選択[色](https://reference.aspose.com/cells/java/com.aspose.cells/Color)列挙し、選択した色を[フォント](https://reference.aspose.com/cells/java/com.aspose.cells/Font)オブジェクトの[setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **テキストに取り消し線効果を設定する**
取り消し線テキスト[フォント](https://reference.aspose.com/cells/java/com.aspose.cells/Font)オブジェクトの[setStrikeout](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout)財産。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **添え字の設定**
を使用してテキストを上付きにします。[フォント](https://reference.aspose.com/cells/java/com.aspose.cells/Font)オブジェクトの[setSubscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript)財産。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **上付き文字の設定**
でテキストに上付き文字を適用します[フォント](https://reference.aspose.com/cells/java/com.aspose.cells/Font)オブジェクトの[set上付き文字](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript)財産。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **先行トピック**
- [フォントに上付きおよび下付き効果を適用する](/cells/ja/java/apply-superscript-and-subscript-effects-on-fonts/)
- [スプレッドシートまたはワークブックで使用されているフォントのリストを取得する](/cells/ja/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
