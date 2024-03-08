---
title: X 轴与 X 轴类别轴
description: 了解如何区分 X 轴和类别轴 Aspose.Cells for Java。我们的指南将帮助您了解它们的用法和属性的差异，以及如何根据您的需求配置它们。
keywords: Aspose.Cells for Java, X axis, Category axis, difference, usage, properties, configuration.
type: docs
weight: 180
url: /zh/java/x-axis-vs-category-axis/
---
##  **可能的使用场景**
轴有不同类型。 Y 轴是值类型轴，而 X 轴可以是类别类型轴或值类型轴。使用值轴，数据被视为连续变化的数值数据，并且标记被放置在沿轴的点上，该点根据其数值而变化。使用类别轴，数据被视为非数字文本标签序列，并且标记根据其在序列中的位置放置在沿轴的点处。下面的示例说明了值轴和类别轴之间的差异。
我们的样本数据显示在[示例表文件](sample.png)以下。第一列包含我们的 X 轴数据，可以将其视为类别或值。请注意，数字的间距不相等，甚至也不按数字顺序出现。

![待办事项：图像_替代_文本](sample.png)
##  **像 Microsoft Excel 一样处理 X 和类别轴**
我们将在两种类型的图表上显示这些数据，第一个图表是 XY（散点图）图表 X 作为值轴，第二个图表是折线图 X 作为类别轴。

![待办事项：图像_替代_文本](compare.png)

以下示例代码生成[输出Excel文件](XAxis.xlsx).

##  **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "X-axis-vs-category-axis.java" >}}
