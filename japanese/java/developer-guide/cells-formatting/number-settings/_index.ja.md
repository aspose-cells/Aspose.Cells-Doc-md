---
title: 番号設定
type: docs
weight: 10
url: /ja/java/cells-number-settings/
---
##  **Numbersと日付の表示形式を設定する**

Microsoft Excel の非常に強力な機能は、数値や日付の表示形式をユーザーが設定できることです。数値データを使用して、小数、通貨、パーセンテージ、分数、会計上の値などのさまざまな値を表すことができることはわかっています。これらの数値はすべて、それが表す情報の種類に応じて異なる形式で表示されます。同様に、日付や時刻を表示できる形式は数多くあります。
Aspose.Cells はこの機能をサポートしており、開発者は数値または日付の表示形式を設定できます。

##  **Microsoft Excel での表示形式の設定**

Microsoft Excel で表示形式を設定するには:

1. 任意のセルを右クリックします。
1. *形式 Cells** を選択します。任意の種類の値の表示形式を設定するためのダイアログが表示されます。

ダイアログの左側には、次のような値のカテゴリが多数あります。**一般**、**数値**、**通貨**、**会計**、**日付**、**時刻**、**パーセント、**など。Aspose.Cells はこれらの表示形式をすべてサポートしています。

##  **組み込みの数値形式の使用**

Aspose.Cells は、数値と日付の表示形式を構成するためのいくつかの組み込み数値形式を提供します。すべての組み込み数値形式には、一意の数値が与えられます。開発者は、任意の数値を[**番号**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number)の方法[**スタイル**](https://reference.aspose.com/cells/java/com.aspose.cells/style)表示形式を適用するオブジェクト。このアプローチは高速です。 Aspose.Cells でサポートされる組み込みの数値形式を以下に示します。

|**価値**|**タイプ**|**フォーマット文字列**|
| :- | :- | :- |
|0|General|一般的な|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|# ,##0
|
|4|Decimal|# ,##0.00
|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[赤]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[レッド]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|#  ?/?
|
|13|Fraction|#  */*
|
|14|Date|月/日/yyyy|
|15|Date|うーん、うん|
|16|Date|うーん|
|17|Date|うーん、うん|
|18|Time|時:分 午前/午後|
|19|Time|時:mm:s 午前/午後|
|20|Time|ふーむ|
|21|Time|時:mm:ss|
|22|Time|m/d/yy 時:mm|
|37|Currency|# ,##0;-#,##0
|
|38|Currency|# ,##0;[赤]-#,##0
|
|39|Currency|# ,##0.00;-#,##0.00
|
|40|Currency|# ,##0.00;[赤]-#,##0.00
|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|時:mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|## 0.0E+00
|
|49|Text|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

##  **カスタム数値形式の使用**

表示形式を設定するための独自のカスタマイズされた形式文字列を定義するには、[**カスタム**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)。このアプローチは、プリセット形式を使用するほど高速ではありませんが、より柔軟です。


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

を使用する場合は、[**カスタム**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)数値形式を設定するには、[**番号**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） is overridden and vice versa.

{{% /alert %}}

## **Advance topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/java/check-custom-number-format-when-setting-style-custom-property/)
- [ワークブックのカスタム数値の小数点およびグループ区切り文字を指定する](/cells/ja/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [DBNum カスタム パターン形式の指定](/cells/ja/java/specifying-dbnum-custom-pattern-formatting/)
