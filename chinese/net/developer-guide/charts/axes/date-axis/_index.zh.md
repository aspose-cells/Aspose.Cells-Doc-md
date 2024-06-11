---
title: 日期轴
description: 学习如何在Aspose.Cells for .NET中管理日期轴。我们的指南将帮助您了解如何使用各种日期格式、时间刻度和刻度标签频率。
keywords: Aspose.Cells for .NET，日期轴，管理，日期格式，时间刻度，刻度标签频率。
type: docs
weight: 200
url: /zh/net/date-axis/
---

## **可能的使用场景**
当您从工作表数据创建图表并使用日期时，日期会沿图表中的水平（类别）轴绘制，并且Aspose.Cells会自动将类别轴更改为日期（时间刻度）轴。
日期轴以特定间隔或基本单位（例如天数、月份或年份）按年代顺序显示日期，即使工作表上的日期不是按顺序或基本单位相同。
默认情况下，Aspose.Cells会根据工作表数据中任意两个日期之间的最小差异确定日期轴的基本单位。例如，如果您拥有股价数据，日期之间的最小差异为七天，Excel会将基本单位设置为天数，但是如果您想要查看股票在较长时间内的表现，可以将基本单位更改为月份或年份。
## **处理日期轴就像处理Microsoft Excel一样**
请参阅以下样本代码，创建一个新的Excel文件并在第一个工作表中放置图表的值。 
然后，我们添加一个图表并设置[**Axis**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis)的类型 
到[**TimeScale**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/categorytype/)，然后将基本单位设置为天数。

![todo:image_alt_text](excel.png)
## **示例代码**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DateAxis.cs" >}}
