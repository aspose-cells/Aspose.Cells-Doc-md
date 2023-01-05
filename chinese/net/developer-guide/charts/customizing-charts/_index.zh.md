---
title: 自定义图表
type: docs
weight: 40
url: /zh/net/customizing-charts/
---
{{% alert color="primary" %}}

## **创建自定义图表**

到目前为止，当我们讨论图表时，我们已经查看了具有标准格式设置的标准图表。我们只定义数据源，设置一些属性，并使用默认格式设置创建图表。但 Aspose.Cells API 还支持创建自定义图表，允许开发人员使用自己的格式设置创建图表。

开发人员可以使用 Aspose.Cells 在运行时创建自定义图表。

图表由数据系列组成。 Aspose.Cells 中的每个数据系列都由一个[**系列**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)对象而[**系列合集**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)对象作为集合[**系列**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)对象。在创建自定义图表时，开发人员可以自由地为不同的数据系列（收集在[**系列合集**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)目的）。

下面的示例代码演示了如何创建自定义图表。在此示例中，我们将为第一个数据系列使用柱形图，为第二个系列使用折线图。结果是我们向工作表添加了一个柱形图和一个折线图。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

目前 Aspose.Cells 仅支持组合饼图、折线图、柱形图和柱形堆栈图的自定义图表，但未来版本将支持更多图表。

{{% /alert %}}
