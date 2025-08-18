---
title: 自定义图表
description: 学习如何在Aspose.Cells for .NET中自定义图表。 我们的指南将向你展示如何修改图表布局，添加和格式化数据系列，调整轴线，并应用各种格式选项来增强图表的外观和可用性。
keywords: Aspose.Cells for .NET，图表定制，布局，数据系列，轴线，格式化，外观，可用性。
type: docs
weight: 40
url: /zh/net/customizing-charts/
---


## **创建自定义图表**

到目前为止，当我们讨论图表时，我们看了看具有其标准格式设置的标准图表。我们只定义数据源，设置几个属性，图表就会根据其默认格式设置创建。但是，Aspose.Cells API还支持创建自定义图表，允许开发人员使用自己的格式设置创建图表。

开发人员可以使用Aspose.Cells在运行时创建自定义图表。

图表由数据系列组成。在Aspose.Cells中，每个数据系列由[**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)对象表示，而[**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)对象作为[**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)对象的集合。创建自定义图表时，开发人员可以自由选择不同类型的图表用于不同的数据系列（收集在[**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)对象中）。

下面的示例代码演示了如何创建自定义图表。在此示例中，我们将为第一个数据系列使用柱形图，为第二个系列使用折线图。结果是，我们在工作表中添加了一个柱形图，结合了一条折线图。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

目前 Aspose.Cells 只支持结合饼图、折线图、柱状图和堆积柱状图的自定义图表，但未来版本将支持更多的图表类型。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
