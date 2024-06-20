---
title: 数字の設定
type: docs
weight: 10
url: /ja/java/cells-number-settings/
---

## **数字と日付の表示形式の設定**

Microsoft Excelの非常に強力な機能の1つは、ユーザーが数値値や日付の表示形式を設定できることです。数値データは10進数、通貨、パーセンテージ、分数、会計などを含むさまざまな値を表すために使用できることを知っています。すべてのこれらの数値値は、それが表す情報の種類に応じて異なる形式で表示されます。同様に、日付や時刻を表示するための多くの形式があります。
Aspose.Cellsはこの機能をサポートし、開発者が数値や日付の表示形式を設定できるようにします。

## **Microsoft Excel での表示形式の設定**

Microsoft Excelで表示形式を設定するには：

1. 任意のセルを右クリックします。
1. **セルの書式設定** を選択します。ダイアログが表示され、さまざまな種類の値の表示形式を設定するのに使用されます。

ダイアログの左側には**一般**、**数値**、**通貨**、**会計**、**日付**、**時間**、**パーセンテージ**などの値のカテゴリが多数あります。Aspose.Cellsはこれらすべての表示形式をサポートしています。

## **組み込みの数値形式を使用する**

Aspose.Cells は、数値と日付の表示形式を構成するためのいくつかの組み込み数値形式を提供しています。すべての組み込み数値形式には、固有の数値が割り当てられています。開発者は、表示形式を適用するために任意の数値を[**Number**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number)メソッドに割り当てることができます。このアプローチは高速です。Aspose.Cells がサポートする組み込み数値形式は以下の通りです。

|**値**|**タイプ**|**フォーマット文字列**|
| :- | :- | :- |
|0|General|General|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|#,##0|
|4|Decimal|#,##0.00|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Red]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Red]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|# ?/?|
|13|Fraction|# */*|
|14|Date|m/d/yyyy|
|15|Date|d-mmm-yy|
|16|Date|d-mmm|
|17|Date|mmm-yy|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|h:mm|
|21|Time|h:mm:ss|
|22|Time|m/d/yy h:mm|
|37|Currency|#,##0;-#,##0|
|38|Currency|#,##0;[Red]-#,##0|
|39|Currency|#,##0.00;-#,##0.00|
|40|Currency|#,##0.00;[Red]-#,##0.00|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|##0.0E+00|
|49|Text|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

## **カスタム数値形式を使用する**

表示形式を設定するための独自のカスタマイズされた形式文字列を定義するには、[**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)を使用します。このアプローチは事前に設定された形式を使用するよりも高速ではありませんが、柔軟性が高くなります。


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

[**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)を使用して数値形式を設定すると、以前に[**Number**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） を使用して設定された形式は上書きされ、その逆も同様です。

{{% /alert %}}

## **高度なトピック**
- [Style.Customプロパティを設定する際のカスタム数値形式を確認する](/cells/ja/java/check-custom-number-format-when-setting-style-custom-property/)
- [ブックでのカスタム数値小数点およびグループの区切りの指定](/cells/ja/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [DBNumカスタムパターンの書式設定の指定](/cells/ja/java/specifying-dbnum-custom-pattern-formatting/)
