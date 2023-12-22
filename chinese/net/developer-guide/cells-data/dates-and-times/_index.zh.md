---
title: 如何管理日期和时间
type: docs
weight: 600
url: /zh/net/how-to-manage-dates-and-times/
description: 通过 Aspose.Cells for .NET API 了解如何管理日期和时间。
keywords: How to Manage Dates and Times, The 1900 date system, The 1904 date system, Set Dates and Times, Get Dates and Times, Manage Dates and Times, Store Dates and Times in Excel, Display Dates and Times in Cells.
---
##  **如何在 Excel 中存储日期和时间**
日期和时间以数字形式存储在单元格中。因此，包含日期和时间的单元格的值是数字类型。指定日期和时间的数字由日期（整数部分）和时间（小数部分）组成。 Cell.DoubleValue 属性返回此数字。

##  **如何在 Aspose.Cells 中显示日期和时间**
要将数字显示为日期和时间，请通过以下命令将所需的日期和时间格式应用于单元格[款式.编号](https://reference.aspose.com/cells/net/aspose.cells/style/number/)或者[风格.定制]()财产。 CellValue.DateTimeValue 属性返回 DateTime 对象，该对象指定由单元格中包含的数字表示的日期和时间。
<br>
<image src="1.png" width="70%" />

##  **Aspose.Cells中如何切换两个日期系统**
MS-Excel 将日期存储为称为序列值的数字。序列值是一个整数，表示从日期系统中的第一天开始经过的天数。 Excel 支持以下序列值日期系统：

1. 1900 年日期系统。第一个日期是 1900 年 1 月 1 日，其序列值为 1。最后一个日期是 9999 年 12 月 31 日，其序列值为 2,958,465。默认情况下，工作簿中使用此日期系统。
1.  1904 年的日期系统。第一个日期是 1904 年 1 月 1 日，其序列值为 0。最后一个日期是 9999 年 12 月 31 日，其序列值为 2,957,003。要在工作簿中使用此日期系统，请设置[工作簿.设置.Date1904](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/date1904/)属性为真。


这个例子说明了不同日期系统中同一日期存储的序列值是不同的。
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Datetime-1904.cs" >}}
输出结果：
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

##  **如何设置 Aspose.Cells 中的日期时间值**
此示例在单元格 A1 和 A2 中设置日期时间值，设置 A1 的自定义格式和 A2 的数字格式，然后输出值类型。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Set-Datetime.cs" >}}

输出结果：
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

##  **如何获取 Aspose.Cells 中的日期时间值**
本示例在单元格 A1 和 A2 中设置一个 DateTime 值，设置 A1 的自定义格式和 A2 的数字格式，检查两个单元格的值类型，然后输出 DateTime 值和格式化字符串。

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
