---
title: Number Settings
type: docs
weight: 10
url: /java/cells-number-settings/
---

## **Setting Display Formats of Numbers and Dates**

A very strong feature of Microsoft Excel is that it allows users to set the display formats of numeric values and dates. We know that numeric data can be used to represent different values including decimal, currency, percentage, fraction or accounting values, etc. All these numerical values are displayed in different formats depending on the type of information it represents. Similarly, there are many formats in which a date or time can be displayed.
Aspose.Cells supports this functionality and allows developers to set any display format for a number or date.

## **Setting Display Formats in Microsoft Excel**

To set display formats in Microsoft Excel:

1. Right-click any cell.
1. Select **Format Cells**. A dialog will appear that is used to set the display formats of any kind of value.

In the left side of the dialog, there are many categories of values like **General**, **Number**, **Currency**, **Accounting**, **Date**, **Time**, **Percentage,** etc. Aspose.Cells supports all of these display formats.

## **Using Built-in Number Formats**

Aspose.Cells offers some built-in number formats to configure the display formats of the numbers and dates. All built-in number formats are given unique numeric values. Developers can assign any desired numeric value to the [**Number**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) method of the [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) object to apply the display format. This approach is fast. The built-in number formats supported by Aspose.Cells are listed below.

|**Value**|**Type**|**Format String**|
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

## **Using Custom Number Formats**

To define your own customized format string for setting the display format, use the [**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). This approach is not as fast as using pre-set formats but it is more flexible.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

If you use the [**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) to set the number format, any previous format set using the [**Number**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) is overridden and vice versa.

{{% /alert %}}

## **Advance topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/java/check-custom-number-format-when-setting-style-custom-property/)
- [Specify Custom Number Decimal and Group Separators for Workbook](/cells/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Specifying DBNum Custom Pattern Formatting](/cells/java/specifying-dbnum-custom-pattern-formatting/)
{{< app/cells/assistant language="java" >}}