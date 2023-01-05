---
title: 号码设置
type: docs
weight: 10
url: /zh/net/cells-number-settings/
---
## **设置Numbers和日期的显示格式**

Microsoft Excel的一个非常强大的功能是它允许用户设置数值和日期的显示格式。我们知道，数值数据可以用来表示不同的数值，包括小数、货币、百分比、分数或会计数值等。所有这些数值都根据其表示的信息类型以不同的格式显示。同样，日期或时间的显示格式也有很多种。
Aspose.Cells 支持此功能并允许开发人员为数字或日期设置任何显示格式。

### **在 Microsoft Excel 中设置显示格式**

在 Microsoft Excel 中设置显示格式：

1. 右键单击任何单元格。
1. 选择**格式 Cells**.将出现一个对话框，用于设置任何一种值的显示格式。

在对话框的左侧，有许多类别的值，例如**一般的**, **数字**, **货币**, **会计**, **日期**, **时间**, **百分比，**等 Aspose.Cells 支持所有这些显示格式。

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。中的每一项[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合代表一个对象[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级。

Aspose.Cells提供[**获取样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)和[**设置样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)的方法[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级。这些方法用于获取和设置单元格的格式。这[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)类提供了一些有用的属性来处理数字和日期的显示格式。

### **使用内置数字格式**

 Aspose.Cells 提供了一些内置的数字格式来配置数字和日期的显示格式。这些内置的数字格式可以通过使用[**数字**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)的财产[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)目的。所有内置数字格式都被赋予唯一的数值。开发人员可以为[**数字**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)的财产[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象应用显示格式。这种方法很快。下面列出了 Aspose.Cells 支持的内置数字格式。

|**价值**|**类型**|**格式化字符串**|
|:- |:- |:- |
|0|一般的|一般的|
|1|十进制|0|
|2|十进制|0.00|
|3|十进制|# ,##0
|
|4|十进制|# ,##0.00
|
|5|货币|$#,##0;$-#,##0|
|6|货币|$#,##0;[红色]$-#,##0|
|7|货币|$#,##0.00;$-#,##0.00|
|8|货币|$#,##0.00;[红色]$-#,##0.00|
|9|百分比|0%|
|10|百分比|0.00%|
|11|科学的|0.00E+00|
|12|分数|# ?/?
|
|13|分数|# */*
|
|14|日期|月/日/年|
|15|日期|d-mmm-yy|
|16|日期|嗯嗯|
|17|日期|嗯嗯|
|18|时间|高：毫米上午/下午|
|19|时间|h:mm:ss 上午/下午|
|20|时间|唔|
|21|时间|时：分：秒|
|22|时间|米/日/年 高：毫米|
|37|货币|# ,##0;-#,##0
|
|38|货币|# ,##0;[红色]-#,##0
|
|39|货币|# ,##0.00;-#,##0.00
|
|40|货币|# ,##0.00;[红色]-#,##0.00
|
|41|会计|_ * #,##0_ ;_ * "_ ;_ @_|
|42|会计|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|会计|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|会计|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|时间|毫米：不锈钢|
|46|时间|时：毫米：秒|
|47|时间|毫米：ss.0|
|48|科学的|## 0.0E+00
|
|49|文本|@|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

### **使用自定义数字格式**

要定义您自己的自定义格式字符串以设置显示格式，请使用[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**风俗**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)财产。这种方法不如使用预设格式快，但更灵活。


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

如果您使用[**风俗**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)属性设置数字格式，任何以前的格式设置使用[**数字**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)属性被覆盖，反之亦然。

{{% /alert %}}

## **推进主题**
- [设置 Style.Custom 属性时检查自定义数字格式](/cells/zh/net/check-custom-number-format-when-setting-style-custom-property/)
- [支持的数字格式列表](/cells/zh/net/list-of-supported-number-formats/)
- [呈现自定义日期格式模式 g 和 ge mm dd](/cells/zh/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [为工作簿指定自定义数字小数和组分隔符](/cells/zh/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [指定 DBNum 自定义模式格式](/cells/zh/net/specifying-dbnum-custom-pattern-formatting/)
