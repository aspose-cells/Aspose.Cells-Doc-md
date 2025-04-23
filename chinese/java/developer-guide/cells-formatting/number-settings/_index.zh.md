---
title: 数字设置
type: docs
weight: 10
url: /zh/java/cells-number-settings/
---

## **设置数字和日期的显示格式**

Microsoft Excel的一个非常强大的特性是它允许用户设置数字值和日期的显示格式。我们知道，数字数据可以用来表示不同的值，包括小数、货币、百分比、分数或会计值等。所有这些数值根据表示的信息类型以不同的格式显示。类似地，日期或时间可以以多种格式显示。
Aspose.Cells支持此功能，并允许开发人员为数字或日期设置任何显示格式。

## **在Microsoft Excel中设置显示格式**

在Microsoft Excel中设置显示格式：

1. 右键单击任何单元格。
1. 选择**设置单元格格式**。将会出现一个对话框，用于设置任何类型值的显示格式。

在对话框的左侧，有许多值类别，如**常规**、**数字**、**货币**、**会计**、**日期**、**时间**、**百分比**等。Aspose.Cells支持所有这些显示格式。

## **使用内置数字格式**

Aspose.Cells提供了一些内置的数字格式，用于配置数字和日期的显示格式。所有内置的数字格式都具有唯一的数字值。开发人员可以将任何所需的数字值分配给[**Number**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number)方法的[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象，以应用显示格式。这种方法速度快。Aspose.Cells支持的内置数字格式如下。

|**数值**|**类型**|**格式字符串**|
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

## **使用自定义数字格式**

要定义自定义格式字符串以设置显示格式，使用[**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)。这种方法不像使用预设格式那样快，但更灵活。


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

如果你使用 [**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) 设置数字格式，之前用 [**Number**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) 设置的格式将被覆盖，反之亦然。

{{% /alert %}}

## **高级主题**
- [在设置Style.Custom属性时检查自定义数字格式](/cells/zh/java/check-custom-number-format-when-setting-style-custom-property/)
- [为工作簿指定自定义数值小数和分组分隔符](/cells/zh/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [指定DBNum自定义模式格式化](/cells/zh/java/specifying-dbnum-custom-pattern-formatting/)
{{< app/cells/assistant language="java" >}}
