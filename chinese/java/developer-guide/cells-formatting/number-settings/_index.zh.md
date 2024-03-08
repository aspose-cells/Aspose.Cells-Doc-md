---
title: 号码设置
type: docs
weight: 10
url: /zh/java/cells-number-settings/
---
##  **设置Numbers和日期的显示格式**

Microsoft Excel的一个非常强大的功能是它允许用户设置数值和日期的显示格式。我们知道，数值数据可以用来表示不同的值，包括小数、货币、百分比、分数或会计值等。所有这些数值根据其表示的信息类型以不同的格式显示。同样，日期或时间的显示格式也有多种。
Aspose.Cells 支持此功能，并允许开发人员设置数字或日期的任何显示格式。

##  **在 Microsoft Excel 中设置显示格式**

要在 Microsoft Excel 中设置显示格式：

1. 右键单击任意单元格。
1. 选择*格式 Cells**。将出现一个对话框，用于设置任何类型值的显示格式。

在对话框的左侧，有许多类别的值，例如**一般**、**数字**、**货币**、**会计**、**日期**、**时间**、**百分比、**等。Aspose.Cells 支持所有这些显示格式。

##  **使用内置数字格式**

Aspose.Cells提供了一些内置的数字格式来配置数字和日期的显示格式。所有内置数字格式都被赋予唯一的数值。开发人员可以将任何所需的数值分配给[**数字**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number)的方法[**风格**](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象来应用显示格式。这种方法很快。下面列出了 Aspose.Cells 支持的内置号码格式。

|**价值**|**类型**|**格式化字符串**|
| :- | :- | :- |
|0|General|一般的|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|# ,##0
|
|4|Decimal|# ,##0.00
|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[红色]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[红色]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|#  ?/?
|
|13|Fraction|#  */*
|
|14|Date|月/日/年|
|15|Date|d-mmm-yy|
|16|Date|d-mmm|
|17|Date|嗯-年|
|18|Time|小时:毫米 上午/下午|
|19|Time|时:分:秒 上午/下午|
|20|Time|唔|
|21|Time|时:分:秒|
|22|Time|月/日/年 时:毫米|
|37|Currency|# ,##0;-#,##0
|
|38|Currency|# ,##0;[红色]-#,##0
|
|39|Currency|# ,##0.00;-#,##0.00
|
|40|Currency|# ,##0.00;[红色]-#,##0.00
|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|毫米：SS|
|46|Time|时:分:秒|
|47|Time|毫米：SS.0|
|48|Scientific|## 0.0E+00
|
|49|Text|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

##  **使用自定义数字格式**

要定义您自己的自定义格式字符串来设置显示格式，请使用[**风俗**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)。这种方法不如使用预设格式那么快，但更灵活。


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

如果您使用[**风俗**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)设置数字格式，使用之前设置的任何格式[**数字**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） is overridden and vice versa.

{{% /alert %}}

## **Advance topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/java/check-custom-number-format-when-setting-style-custom-property/)
- [为工作簿指定自定义数字小数点和组分隔符](/cells/zh/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [指定 DBNum 自定义模式格式](/cells/zh/java/specifying-dbnum-custom-pattern-formatting/)
