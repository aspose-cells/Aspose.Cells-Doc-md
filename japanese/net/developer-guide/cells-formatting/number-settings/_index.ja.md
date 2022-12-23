---
title: 番号設定
type: docs
weight: 10
url: /ja/net/cells-number-settings/
---
## **Numbersと日付の表示形式を設定する**

Microsoft Excel の非常に強力な機能は、ユーザーが数値と日付の表示形式を設定できることです。数値データは、10 進数、通貨、パーセンテージ、分数、会計値などのさまざまな値を表すために使用できることがわかっています。これらの数値はすべて、表す情報の種類に応じてさまざまな形式で表示されます。同様に、日付または時刻を表示できる形式は多数あります。
Aspose.Cells はこの機能をサポートし、開発者が数値または日付の表示形式を設定できるようにします。

### **Microsoft Excel での表示形式の設定**

Microsoft Excel で表示形式を設定するには:

1. 任意のセルを右クリックします。
1. 選択する**フォーマット Cells**.任意の種類の値の表示形式を設定するために使用されるダイアログが表示されます。

ダイアログの左側には、次のような多くの値のカテゴリがあります。**全般的**, **番号**, **通貨**, **会計**, **日にち**, **時間**, **割合、**Aspose.Cells は、これらの表示形式をすべてサポートします。

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の各項目[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションはのオブジェクトを表します[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。

Aspose.Cells提供[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)と[**スタイルの設定**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)のメソッド[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。これらのメソッドは、セルの書式設定を取得および設定するために使用されます。の[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)クラスには、数値と日付の表示形式を処理するための便利なプロパティがいくつか用意されています。

### **組み込みの数値形式の使用**

 Aspose.Cells には、数値と日付の表示形式を構成するための組み込みの数値形式がいくつか用意されています。これらの組み込み数値形式は、[**番号**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)のプロパティ[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)物体。すべての組み込みの数値形式には、一意の数値が与えられます。開発者は、任意の数値を[**番号**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)のプロパティ[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)表示形式を適用するオブジェクト。このアプローチは高速です。 Aspose.Cells でサポートされている組み込みの数値形式を以下に示します。

|**価値**|**タイプ**|**フォーマット文字列**|
|:- |:- |:- |
|0|全般的|全般的|
|1|小数|0|
|2|小数|0.00|
|3|小数|# ,##0
|
|4|小数|# ,##0.00
|
|5|通貨|$#,##0;$-#,##0|
|6|通貨|$#,##0;[赤]$-#,##0|
|7|通貨|$#,##0.00;$-#,##0.00|
|8|通貨|$#,##0.00;[赤]$-#,##0.00|
|9|パーセンテージ|0%|
|10|パーセンテージ|0.00%|
|11|科学的|0.00E+00|
|12|分数|# ?/?
|
|13|分数|# */*
|
|14|日にち|月/日/年|
|15|日にち|d-mmm-yy|
|16|日にち|d-うーん|
|17|日にち|mmm-yy|
|18|時間|h:mm 午前/午後|
|19|時間|h:mm:ss AM/PM|
|20|時間|うーん|
|21|時間|時:分:秒|
|22|時間|月/日/年 時:分|
|37|通貨|# ,##0;-#,##0
|
|38|通貨|# ,##0;[赤]-#,##0
|
|39|通貨|# ,##0.00;-#,##0.00
|
|40|通貨|# ,##0.00;[赤]-#,##0.00
|
|41|会計|_ * #,##0_ ;_ * "_ ;_ @_|
|42|会計|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|会計|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|会計|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|時間|mm:ss|
|46|時間|時:分:秒|
|47|時間|mm:ss.0|
|48|科学的|## 0.0E+00
|
|49|文章|@|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

### **カスタム数値形式の使用**

表示形式を設定するために独自のカスタマイズされた形式文字列を定義するには、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトの[**カスタム**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)財産。このアプローチは、事前設定された形式を使用するほど高速ではありませんが、より柔軟です。


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

を使用する場合[**カスタム**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)プロパティを使用して数値形式を設定します。以前の形式は、[**番号**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)プロパティはオーバーライドされ、その逆も同様です。

{{% /alert %}}

## **先行トピック**
- [Style.Custom プロパティの設定時にカスタム数値形式を確認する](/cells/ja/net/check-custom-number-format-when-setting-style-custom-property/)
- [サポートされている数値形式のリスト](/cells/ja/net/list-of-supported-number-formats/)
- [カスタム日付形式パターン g および ge mm dd のレンダリング](/cells/ja/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [ワークブックのカスタム数値の小数点記号とグループ区切り記号を指定する](/cells/ja/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [DBNum カスタム パターン形式の指定](/cells/ja/net/specifying-dbnum-custom-pattern-formatting/)
