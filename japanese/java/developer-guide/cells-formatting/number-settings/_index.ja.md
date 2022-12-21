---
title: 番号設定
type: docs
weight: 10
url: /ja/java/cells-number-settings/
---
## **数字と日付の表示形式を設定する**

Microsoft Excel の非常に強力な機能は、ユーザーが数値と日付の表示形式を設定できることです。数値データは、10 進数、通貨、パーセンテージ、分数、会計値などのさまざまな値を表すために使用できることがわかっています。これらの数値はすべて、表す情報の種類に応じてさまざまな形式で表示されます。同様に、日付または時刻を表示できる形式は多数あります。
Aspose.Cells はこの機能をサポートし、開発者が数値または日付の表示形式を設定できるようにします。

## **Microsoft Excel での表示形式の設定**

Microsoft Excel で表示形式を設定するには:

1. 任意のセルを右クリックします。
1. 選択する**フォーマット Cells**.任意の種類の値の表示形式を設定するために使用されるダイアログが表示されます。

ダイアログの左側には、次のような多くの値のカテゴリがあります。**全般的**, **番号**, **通貨**, **会計**, **日にち**, **時間**, **割合、**Aspose.Cells は、これらの表示形式をすべてサポートしています。

## **組み込みの数値形式の使用**

Aspose.Cells には、数値と日付の表示形式を構成するための組み込みの数値形式がいくつか用意されています。すべての組み込みの数値形式には、一意の数値が与えられます。開発者は、任意の数値を[**番号**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number)の方法[**スタイル**](https://reference.aspose.com/cells/java/com.aspose.cells/style)表示形式を適用するオブジェクト。このアプローチは高速です。 Aspose.Cells でサポートされている組み込みの数値形式を以下に示します。

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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

## **カスタム数値形式の使用**

表示形式を設定するために独自のカスタマイズされた形式文字列を定義するには、[**カスタム**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom).このアプローチは、事前設定された形式を使用するほど高速ではありませんが、より柔軟です。


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

を使用する場合[**カスタム**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)数値形式を設定するには、[**番号**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） is overridden and vice versa.

{{% /alert %}}

## **Advance topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/java/check-custom-number-format-when-setting-style-custom-property/)
- [ワークブックのカスタム数値の小数点記号とグループ区切り記号を指定する](/cells/ja/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [DBNum カスタム パターン形式の指定](/cells/ja/java/specifying-dbnum-custom-pattern-formatting/)
