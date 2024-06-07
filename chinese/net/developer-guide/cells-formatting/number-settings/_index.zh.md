---
title: 数字设置
description: Aspose.Cells是用于处理电子表格文件的.NET库，支持很多不同的单元格数字设置。本文将介绍如何使用Aspose.Cells库来管理单元格的数字设置，以便用户可以根据需要调整电子表格中的数字格式。
keywords: Aspose.Cells,.NET库,电子表格,单元格数字设置,格式,管理,数字和日期格式
type: docs
weight: 10
url: /zh/net/cells-number-settings/
---

## **如何设置数字和日期的显示格式**

Microsoft Excel的一个非常强大的功能是允许用户设置数值和日期的显示格式。我们知道数字数据可用于表示不同值，包括十进制、货币、百分比、分数或会计值等。所有这些数字值根据其表示的信息类型以不同格式显示。类似地，日期或时间可以以许多格式显示。
Aspose.Cells支持此功能，允许开发人员为数字或日期设置任何显示格式。

### **如何在Microsoft Excel中设置显示格式**

要在Microsoft Excel中设置显示格式：

1.右键单击任何单元格。
1. 选择**格式单元格**。将会出现一个用于设置任何类型值显示格式的对话框。

在对话框的左侧，有许多值类别，如**常规**、**数字**、**货币**、**会计**、**日期**、**时间**、**百分比**等。Aspose.Cells支持所有这些显示格式。

Aspose.Cells提供一个类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。一个工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合中的每个项目表示一个[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的对象。

Aspose.Cells为该类提供了[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)和[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)方法。这些方法用于获取和设置单元格的格式。该类还为处理数字和日期的显示格式提供了一些有用的属性。

### **如何使用内置数字格式**

Aspose.Cells提供了一些内置数字格式，用于配置数字和日期的显示格式。这些内置数字格式可以通过[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**Number**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)属性应用。所有内置数字格式都有唯一的数值。开发人员可以将任何所需的数值分配给[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**Number**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)属性以应用显示格式。这种方法速度快。Aspose.Cells支持的内置数字格式如下。

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

### **如何使用自定义数字格式**

要为设置显示格式定义自己的自定义格式字符串，请使用[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)属性。 这种方法不如使用预设格式快，但更灵活。


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

如果使用[**Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)属性设置数字格式，则与使用[**Number**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)属性设置的任何先前格式都将被覆盖，反之亦然。

{{% /alert %}}

## **高级主题**
- [ 设置样式时检查自定义数字格式。自定义属性](/cells/zh/net/check-custom-number-format-when-setting-style-custom-property/)
- [支持的数字格式列表](/cells/zh/net/list-of-supported-number-formats/)
- [按照自己的日期格式模式g和ge mm dd渲染自定义日期格式](/cells/zh/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [为工作簿指定自定义数字小数点和分组分隔符](/cells/zh/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [指定DBNum自定义模式格式化](/cells/zh/net/specifying-dbnum-custom-pattern-formatting/)
