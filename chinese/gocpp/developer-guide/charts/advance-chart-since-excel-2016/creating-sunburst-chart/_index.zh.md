---
title: 如何通过C++使用Golang创建Sunburst图表
description: 学习如何用Aspose.Cells for C++创建环状图，这是以圆圈形式呈现数据的图表。我们的指南将帮助您设置图表的各种属性和格式，包括数据标签、图例、颜色等。
keywords: Aspose.Cells for C++，环形图，创建，设置属性，数据标签，图例，格式，颜色，圆形，数据渲染。
type: docs
weight: 162
url: /zh/go-cpp/creating-sunburst-chart/
---

## **可能的使用场景**
树状图适合比较层级中的比例，但树状图在显示最大类别与每个数据点之间的层次级别方面并不理想。环形图是显示层级数据的更佳直观图表。环形图理想用于显示层级数据。每个层级由一个环或圆圈表示，最内圈代表层级的顶部。没有任何层级数据（仅一层类别）的环形图看起来类似于甜甜圈图。而具有多个层级的环形图则展示了外部环与内部环的关系。环形图在展示某一环被拆分成贡献部分方面最为有效，而另一类层级图形——树状图，更适合比较相对大小。

![todo:image_alt_text](sample.png)
## **旭日图表**
运行下面的代码后，您将会看到如下所示的旭日图表。

![todo:image_alt_text](result.png)
## **示例代码**
以下示例代码加载 [样本 Excel 文件](sunburst.xlsx) 并生成 [输出 Excel 文件](out.xlsx)。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatingSunburstChart.go" >}}
