---
title: 自定义图表
description: 了解如何自定义图表 Aspose.Cells for .NET。我们的指南将向您展示如何修改图表布局、添加和格式化数据系列、调整轴以及应用各种格式化选项以增强图表的外观和可用性。
keywords: Aspose.Cells for .NET, charting, customization, layouts, data series, axes, formatting, appearance, usability.
type: docs
weight: 40
url: /zh/net/customizing-charts/
---
{{% alert color="primary" %}}

##  **创建自定义图表**

到目前为止，当我们讨论图表时，我们已经研究了具有标准格式设置的标准图表。我们仅定义数据源，设置一些属性，然后使用默认格式设置创建图表。但 Aspose.Cells API 还支持创建自定义图表，允许开发人员使用自己的格式设置创建图表。

开发人员可以使用 Aspose.Cells 在运行时创建自定义图表。

图表由一系列数据组成。 Aspose.Cells中的每个数据系列都由一个表示[**系列**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)对象而[**系列合集**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)对象作为集合[**系列**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)对象。创建自定义图表时，开发人员可以自由地将不同类型的图表用于不同的数据系列（收集在[**系列合集**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)目的）。

下面的示例代码演示了如何创建自定义图表。在此示例中，我们将使用柱形图表示第一个数据系列，使用折线图表示第二个数据系列。结果是我们将柱形图与折线图组合添加到工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

目前 Aspose.Cells 仅支持组合饼图、折线图、柱形图和柱状堆栈图的自定义图表，但未来版本将支持更多图表。

{{% /alert %}}
