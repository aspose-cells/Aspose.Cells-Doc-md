---
title: 日期轴
type: docs
weight: 200
url: /zh/net/date-axis/
---
## **可能的使用场景**
当您从使用日期的工作表数据创建图表并且日期沿图表中的水平（类别）轴绘制时，Aspose.cells 会自动将类别轴更改为日期（时间刻度）轴。
日期轴按特定时间间隔或基本单位（例如天数、月数或年数）按时间顺序显示日期，即使工作表上的日期不按顺序或使用相同的基本单位也是如此。
默认情况下，Aspose.cells 根据工作表数据中任意两个日期之间的最小差异确定日期轴的基本单位。例如，如果您有股票价格数据，其中日期之间的最小差异为 7 天，Excel 将基本单位设置为天，但如果您想查看股票在过去一段时间内的表现，您可以将基本单位更改为月或年更长的时间。
## **像 Microsoft Excel 一样处理日期轴**
请查看以下创建新 Excel 文件并将图表值放入第一个工作表的示例代码。
然后我们添加一个图表并设置图表的类型[**轴**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis) 
至[**时标**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/categorytype/)然后将基本单位设置为天。

![待办事项：图像_替代_文本](excel.png)
## **示例代码**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DateAxis.cs" >}}
