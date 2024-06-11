---
title: X轴与分类轴的区别
description: 学习如何区分Aspose.Cells for Java中的X轴和类别轴。我们的指南将帮助您了解它们的使用和属性之间的区别，以及如何根据您的需求对它们进行配置。
keywords: Aspose.Cells for Java, X轴, 类别轴, 差异, 使用, 属性, 配置。
type: docs
weight: 180
url: /zh/java/x-axis-vs-category-axis/
---

## **可能的使用场景**
X轴有不同类型。而Y轴是一个值类型轴，X轴可以是分类类型轴或值类型轴。使用值轴，数据被视为连续变化的数值数据，并且标记位于沿轴的变动点，其位置根据其数值而变化。使用分类轴，数据被视为一系列非数值文本标签，并且标记位于沿轴的一个位置，其位置根据其在序列中的位置而变化。下面的示例说明了值轴和分类轴之间的区别。
我们的示例数据如下图中的[示例表文件](sample.png)所示。第一列包含我们的X轴数据，可以视为分类或值。请注意，数字不是等间距的，也不按照数字顺序出现。

![todo:image_alt_text](sample.png)
## **处理X轴和分类轴，就像处理Microsoft Excel一样**
我们将在两种类型的图表上显示这些数据，第一个图表是XY（散点）图，X作为值轴，第二个图表是折线图，X作为分类轴。

![todo:image_alt_text](compare.png)

以下示例代码生成[输出Excel文件](XAxis.xlsx)。

## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "X-axis-vs-category-axis.java" >}}
