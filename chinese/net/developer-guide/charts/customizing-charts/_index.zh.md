---
title: 定制图表
description: 学习如何在Aspose.Cells for .NET 中定制图表。我们的指南将向您展示如何修改图表布局，添加和格式化数据系列，调整坐标轴，并应用各种格式选项以增强您图表的外观和可用性。
keywords: Aspose.Cells for .NET，图表，自定义，布局，数据系列，坐标轴，格式，外观，可用性。
type: docs
weight: 40
url: /zh/net/customizing-charts/
---

{{% alert color="primary" %}}

## **创建自定义图表**

到目前为止，当我们讨论图表时，我们看了标准图表，并设置了一些属性，图表便会根据其默认格式设置而创建。但Aspose.Cells APIs也支持创建允许开发人员根据其自己的格式设置创建图表的自定义图表。

开发人员可以使用Aspose.Cells在运行时创建自定义图表。

图表由数据系列组成。在Aspose.Cells中，每个数据系列由一个[**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)对象表示，而[**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)对象充当[**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)对象的集合。在创建自定义图表时，开发人员可以自由使用不同类型的图表用于不同的数据系列（在[**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)对象中收集）。

下面的示例代码演示了如何创建自定义图表。在这个示例中，我们将使用柱状图作为第一个数据系列，使用折线图作为第二个系列。结果是我们在工作表中添加了一个组合了柱状图和折线图的图表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

目前Aspose.Cells只支持组合饼状图、折线图、柱状图和堆叠柱状图的自定义图表，但在未来的发布中将支持更多图表。

{{% /alert %}}
