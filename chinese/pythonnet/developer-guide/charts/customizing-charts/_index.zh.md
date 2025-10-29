---
title: 自定义图表
description: 了解如何在 Aspose.Cells for Python via .NET 中自定义图表。我们的指南将向您展示如何修改图表布局、添加和格式化数据系列、调整坐标轴，并应用各种格式选项以提升图表的外观和实用性。
keywords: Aspose.Cells for Python via .NET，图表，自定义，布局，数据系列，坐标轴，格式，外观，实用性。
type: docs
weight: 40
url: /zh/python-net/customizing-charts/
---


## **创建自定义图表**

到目前为止，在讨论图表时，我们已经看到了具有其标准格式设置的标准图表。我们只需定义数据源，设置几个属性，图表就会以其默认格式创建好。不过，Aspose.Cells for Python via .NET 的API也支持创建具有自己格式设置的自定义图表，允许开发者按照自己的喜好定制图表外观。

开发者可以在运行时使用Aspose.Cells for Python via .NET创建自定义图表。

图表由数据系列组成。在Aspose.Cells for Python via .NET中，每个数据系列由一个[**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series)对象表示，而[**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)对象作为[**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series)对象的集合。当创建自定义图表时，开发者可以自由为不同的数据系列（集合在[**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)对象中）使用不同类型的图表。

下面的示例代码演示了如何创建自定义图表。在此示例中，我们将为第一个数据系列使用柱形图，为第二个系列使用折线图。结果是，我们在工作表中添加了一个柱形图，结合了一条折线图。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreateCustomChart-1.py" >}}

{{% alert color="primary" %}}

目前，Aspose.Cells for Python via .NET只支持结合饼图、折线图、柱状图和簇状柱状图的自定义图表，但未来版本将支持更多类型的图表。

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
