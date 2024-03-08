---
title: 日期轴
description: 了解如何管理日期轴 Aspose.Cells for Java。我们的指南将帮助您了解如何使用各种日期格式、时间刻度和刻度标签频率。
keywords: Aspose.Cells for Java, date axis, manage, date formats, time scales, tick label frequencies.
type: docs
weight: 200
url: /zh/java/date-axis/
---
##  **可能的使用场景**
当您从使用日期的工作表数据创建图表，并且日期沿图表中的水平（类别）轴绘制时，Aspose.cells 会自动将类别轴更改为日期（时间刻度）轴。
日期轴以特定间隔或基本单位（例如天数、月数或年数）按时间顺序显示日期，即使工作表上的日期不按顺序排列或采用相同的基本单位也是如此。
默认情况下，Aspose.cells 根据工作表数据中任意两个日期之间的最小差异确定日期轴的基本单位。例如，如果您的股票价格数据中日期之间的最小差异为 7 天，Excel 将基本单位设置为天，但如果您想查看股票在过去一段时间内的表现，则可以将基本单位更改为月或年。较长一段时间。
##  **像 Microsoft Excel 一样处理日期轴**
请参阅以下示例代码，该代码创建一个新的 Excel 文件并将图表的值放入第一个工作表中。
然后我们添加一个图表并设置图表的类型[**轴**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/) 
到[**时间刻度**](https://reference.aspose.com/cells/java/com.aspose.cells/categorytype/#TIME-SCALE)然后将基本单位设置为天。

![待办事项：图像_替代_文本](excel.png)

以下示例代码生成[输出Excel文件](DateAxis.xlsx).

##  **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DateAxis.java" >}}
