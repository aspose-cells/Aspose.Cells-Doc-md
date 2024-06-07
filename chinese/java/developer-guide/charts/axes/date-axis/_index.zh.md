---
title: 日期轴
description: 学习如何在Aspose.Cells for Java中管理日期轴。我们的指南将帮助您了解如何处理各种日期格式、时间刻度和刻度标签频率。
keywords: Aspose.Cells for Java, 日期轴, 管理, 日期格式, 时间刻度, 刻度标签频率。
type: docs
weight: 200
url: /zh/java/date-axis/
---

## **可能的使用场景**
当您从工作表数据创建图表时使用日期，并且日期沿图表中的水平(类别)轴绘制时，Aspose.cells会自动将类别轴更改为日期(时间刻度)轴。
日期轴以特定间隔或基本单位(如天数、月份或年份)按照时间顺序显示日期，即使工作表上的日期不是按顺序或在相同基本单位上。
默认情况下，Aspose.cells会根据工作表数据中任意两个日期之间的最小差异来确定日期轴的基本单位。例如，如果您有关于股价的数据，日期之间的最小差异为七天，Excel会将基本单位设置为天，但如果您想查看股票在更长时间内的表现，可以将基本单位更改为月或年。
## **像Microsoft Excel一样处理日期轴**
请参阅以下示例代码，创建一个新的Excel文件并将图表的值放在第一个工作表中。 
然后我们添加一个图表并设置[**Axis**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/)的类型 
为[**TimeScale**](https://reference.aspose.com/cells/java/com.aspose.cells/categorytype/#TIME-SCALE)设置基本单位为天。

![todo:image_alt_text](excel.png)

以下示例代码生成了[输出Excel文件](DateAxis.xlsx)。

## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DateAxis.java" >}}
