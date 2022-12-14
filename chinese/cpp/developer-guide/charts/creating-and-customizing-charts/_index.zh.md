---
title: 创建和自定义图表
type: docs
weight: 10
url: /zh/cpp/creating-and-customizing-charts/
---
## **可能的使用场景**

图表是信息的视觉显示。 Aspose.Cells 允许开发人员在图表中可视化信息，就像 Microsoft Excel 一样。在图表中呈现信息总是有助于决策者做出快速及时的决策。使用图表而不是原始数字更容易快速查看数据的比较、模式和趋势。根据电子表格中的数据在运行时创建图表是 Aspose.Cells 的有用功能之一。 Aspose.Cells 支持创建标准和自定义图表。下面，我们将展示一些示例文件，说明如何使用 Aspose.Cells API 创建一些常见的 MS-Excel 图表类型。

## **金字塔图**

执行示例代码时，金字塔图将添加到工作表中。请参阅[输出Excel文件](66519068.xlsx)以下示例代码。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart.cpp" >}}

## **折线图**

在上面的示例中，只需更改[**图表类型**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70)至[**图表类型_Line**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70ad12ff1561ab1424a0c3095b6dc07ac25)创建折线图。下面提供了完整的源代码。执行代码时，工作表中会添加一个折线图。请参阅[输出Excel文件](66519069.xlsx)以下示例代码。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart.cpp" >}}

## **气泡图**

为了创建气泡图，[**图表类型**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70)必须设置为[**ChartType_Bubble**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70a5efa533b454f9415e4497dbb2ab28b3d)和一些额外的属性，例如[**设置气泡大小**](https://reference.aspose.com/cells/cpp/class/aspose.cells.charts.i_series#a00cf890ba7ab419d31a522ab52b02e9d) & [**设置 X 值**](https://reference.aspose.com/cells/cpp/class/aspose.cells.charts.i_series#a788ff4aa51dbf9bed5327298af93a6db)需要相应地设置。执行以下代码后，气泡图将添加到工作表中。请参阅[输出Excel文件](66519070.xlsx)以下示例代码。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart.cpp" >}}

## **创建自定义图表**

到目前为止，当我们讨论图表时，我们已经了解了具有自己的标准格式设置的标准图表。我们只定义数据源，设置一些属性，并使用默认格式设置创建图表。但 Aspose.Cells API 还支持创建自定义图表，允许开发人员使用自己的格式设置创建图表。开发人员可以使用 Aspose.Cells 在运行时创建自定义图表。

图表由数据系列组成。在创建自定义图表时，开发人员可以自由地为不同的数据系列使用不同类型的图表。

下面的示例代码演示了如何创建自定义图表。在此示例中，我们将为第一个数据系列使用柱形图，为第二个系列使用折线图。结果是我们向工作表添加了一个柱形图和一个折线图。请参阅[输出Excel文件](66519071.xlsx)以下示例代码。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart.cpp" >}}
