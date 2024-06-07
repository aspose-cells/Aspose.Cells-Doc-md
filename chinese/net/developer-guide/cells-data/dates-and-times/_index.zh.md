---
title: 如何管理日期和时间
type: docs
weight: 600
url: /zh/net/how-to-manage-dates-and-times/
description: 学习如何通过 Aspose.Cells for .NET API 管理日期和时间。
keywords: 如何管理日期和时间，1900 日期系统，1904 日期系统，设置日期和时间，获取日期和时间，管理日期和时间，在 Excel 中存储日期和时间，在单元格中显示日期和时间。
---

## **如何在Excel中存储日期和时间**
日期和时间以数字形式存储在单元格中。因此，包含日期和时间的单元格的值是数值型。指定日期和时间的数字由日期（整数部分）和时间（小数部分）组成。Cell.DoubleValue属性返回此数字。

## **如何在Aspose.Cells中显示日期和时间**
要将数字显示为日期和时间，请通过Style.Number或Style.Custom属性将所需的日期和时间格式应用于单元格。CellValue.DateTimeValue属性返回DateTime对象，该对象指定由单元格中包含的数字表示的日期和时间。
<br>
<image src="1.png" width="70%" />

## **如何在Aspose.Cells中切换两个日期系统**
MS-Excel将日期存储为称为序列值的数字。序列值是从日期系统中的第一天经过的天数。Excel支持以下日期系统用于序列值：

1. 1900日期系统。第一个日期为1900年1月1日，其序列值为1。最后一个日期为9999年12月31日，其序列值为2,958,465。此日期系统是工作簿默认使用的。
1. 1904日期系统。第一个日期为1904年1月1日，其序列值为0。最后一个日期为9999年12月31日，其序列值为2,957,003。要在工作簿中使用此日期系统，请将Workbook.Settings.Date1904属性设置为true。


此示例显示在不同日期系统中存储的相同日期的序列值是不同的。
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Datetime-1904.cs" >}}
输出结果：
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **如何在Aspose.Cells中设置DateTime值**
此示例在单元格A1和A2中设置DateTime值，设置A1的自定义格式和A2的数字格式，然后输出值类型。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Set-Datetime.cs" >}}

输出结果：
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **如何在Aspose.Cells中获取DateTime值**
此示例在单元格A1和A2中设置DateTime值，设置A1的自定义格式和A2的数字格式，检查两个单元格的数值类型，然后输出DateTime值和格式化字符串。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Get-Datetime.cs" >}}

输出结果：
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A1 DateTime Value: 11/23/2023 5:59:09 PM
A1 DateTime String Value: 11-23-23 17:59:09
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
A2 DateTime Value: 11/23/2023 5:59:09 PM
A2 DateTime String Value: 11/23/2023 17:59
```
