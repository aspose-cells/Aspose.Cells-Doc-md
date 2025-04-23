---
title: X轴与分类轴的区别
description: 学习如何区分 Aspose.Cells for Python via .NET 中的 X 轴和类别轴。我们的指南将帮助你理解它们的用法和属性差异，以及如何根据需要进行配置。
keywords: Aspose.Cells for Python via .NET，X 轴，类别轴，区别，用途，属性，配置。
type: docs
weight: 180
url: /zh/python-net/X-axis-vs-category-axis/
---

## **可能的使用场景**
X轴有不同类型。而Y轴是一个值类型轴，X轴可以是分类类型轴或值类型轴。使用值轴，数据被视为连续变化的数值数据，并且标记位于沿轴的变动点，其位置根据其数值而变化。使用分类轴，数据被视为一系列非数值文本标签，并且标记位于沿轴的一个位置，其位置根据其在序列中的位置而变化。下面的示例说明了值轴和分类轴之间的区别。
我们的示例数据如下图中的[示例表文件](sample.png)所示。第一列包含我们的X轴数据，可以视为分类或值。请注意，数字不是等间距的，也不按照数字顺序出现。

![todo:image_alt_text](sample.png)

## **处理X轴和分类轴，就像处理Microsoft Excel一样**
我们将在两种类型的图表上显示这些数据，第一个图表是XY（散点）图，X作为值轴，第二个图表是折线图，X作为分类轴。

![todo:image_alt_text](compare.png)
## **示例代码**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-X-axis-vs-category-axis.py" >}}
