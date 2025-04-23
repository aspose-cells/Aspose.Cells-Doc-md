---
title: 数字设置
description: Aspose.Cells 是一个用Python编写的电子表格文件处理库，支持多种单元格数字设置。本文将介绍如何使用Aspose.Cells库管理单元格的数字设置，以便用户根据需要调整表格中的数字格式。
keywords: Aspose.Cells，Python库，电子表格，单元格数字设置，格式化，管理，数字和日期格式
type: docs
weight: 10
url: /zh/python-net/cells-number-settings/
---

## **如何设置数字和日期的显示格式**

Microsoft Excel的一个非常强大的特性是它允许用户设置数字值和日期的显示格式。我们知道，数字数据可以用来表示不同的值，包括小数、货币、百分比、分数或会计值等。所有这些数值根据表示的信息类型以不同的格式显示。类似地，日期或时间可以以多种格式显示。
Aspose.Cells for Python via .NET支持此功能，允许开发人员为数字或日期设置任何显示格式。

### **如何在Microsoft Excel中设置显示格式**

在Microsoft Excel中设置显示格式：

1. 右键单击任何单元格。
1. 选择**设置单元格格式**。将会出现一个对话框，用于设置任何类型值的显示格式。

在对话框左侧，有许多类别的值，如**常规**、**数字**、**货币**、**会计**、**日期**、**时间**、**百分比**等。Aspose.Cells for Python via .NET支持所有这些显示格式。

Aspose.Cells for Python via .NET提供了[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类，代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类提供一个[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)集合，集合中的每个项目代表一个[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)类的对象。

Aspose.Cells for Python via .NET为[**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style)和[**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style)方法提供支持，用于[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)类。这些方法用于获取和设置单元格的格式。[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)类提供一些有用的属性，用于处理数字和日期的显示格式。

### **如何使用内置数字格式**

Aspose.Cells for Python via .NET提供一些内置的数字格式，用于配置数字和日期的显示格式。这些内置数字格式可以通过使用[**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number)属性应用于[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)对象。所有内置数字格式都赋予了唯一的数字值。开发人员可以将任何期望的数字值赋予[**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number)属性，从而应用显示格式。这种方法速度快。Aspose.Cells支持的内置数字格式如下所列。

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingBuiltInNumberFormats-1.py" >}}

### **如何使用自定义数字格式**

要为设置显示格式定义自定义的格式字符串，请使用[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)对象的[**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom)属性。这种方法不像使用预设格式那样快，但它更灵活。


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCustomNumber-1.py" >}}

{{% alert color="primary" %}}

如果使用[**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom)属性设置数字格式，则会覆盖之前使用[**number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number)属性设置的格式，反之亦然。

{{% /alert %}}

## **高级主题**
- [在设置Style.Custom属性时检查自定义数字格式](/cells/zh/python-net/check-custom-number-format-when-setting-style-custom-property/)
- [支持的数字格式列表](/cells/zh/python-net/list-of-supported-number-formats/)
- [呈现自定义日期格式模式g和ge mm dd](/cells/zh/python-net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [为工作簿指定自定义数值小数和分组分隔符](/cells/zh/python-net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [指定DBNum自定义模式格式化](/cells/zh/python-net/specifying-dbnum-custom-pattern-formatting/)

