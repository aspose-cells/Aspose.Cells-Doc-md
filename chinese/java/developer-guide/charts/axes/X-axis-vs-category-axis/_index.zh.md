---
title: X轴与分类轴
description: 学习如何区分Aspose.Cells for Java中的X轴和类别轴。我们的指南将帮助您了解它们在使用和属性上的差异，并如何根据需求配置它们。
keywords: Aspose.Cells for Java, X轴, 类别轴, 差异, 使用, 属性, 配置。
type: docs
weight: 180
url: /zh/java/x-axis-vs-category-axis/
---

## **可能的使用场景**
有不同类型的X轴。而Y轴是值类型轴，X轴可以是分类类型轴或值类型轴。 使用值轴，数据被视为连续变化的数值数据，标记放置在沿轴的一点，其位置根据数值而变化。使用分类轴，数据被视为一系列非数值文本标签，标记放置在沿轴的一点，其位置根据其在序列中的位置而变化。 下面的示例说明了值轴和分类轴之间的差异。
我们的示例数据显示在下面的样本表文件中。第一列包含我们的X轴数据，可以作为类别或值进行处理。请注意，数字的间隔不相等，也不按数值顺序排列。

![todo:image_alt_text](sample.png)
## **像Microsoft Excel一样处理X轴和分类轴**
我们将在两种类型的图表上显示这些数据，第一个图表是XY(散点)图表X作为值轴，第二个图表是线图表X作为分类轴。

![todo:image_alt_text](compare.png)

以下示例代码生成了[输出Excel文件](XAxis.xlsx)。

## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "X-axis-vs-category-axis.java" >}}
