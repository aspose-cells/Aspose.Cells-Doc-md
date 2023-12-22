---
title: 创建和自定义图表
type: docs
weight: 10
url: /zh/cpp/creating-and-customizing-charts/
---
##  **可能的使用场景**

图表是信息的直观显示。 Aspose.Cells 允许开发人员像 Microsoft Excel 一样可视化图表中的信息。以图表形式呈现信息始终有助于决策者快速、及时地做出决策。使用图表而不是原始数字更容易快速查看数据中的比较、模式和趋势。根据电子表格中的数据在运行时创建图表是 Aspose.Cells 的有用功能之一。 Aspose.Cells 支持创建标准图表和自定义图表。下面，我们将通过示例文件展示一些示例，介绍如何使用 Aspose.Cells API 创建一些常见的 MS-Excel 图表类型。

##  **金字塔图**

执行示例代码时，金字塔图将添加到工作表中。请参阅[输出Excel文件](66519068.xlsx)以下示例代码。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

##  **折线图**

在上面的例子中，只需更改[**图表类型**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/)到**`图表类型::折线`**创建折线图。下面提供了完整的来源。执行代码时，折线图将添加到工作表中。请参阅[输出Excel文件](66519069.xlsx)以下示例代码。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

##  **气泡图**

为了创建气泡图，[**图表类型**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/)必须设置为**`图表类型_气泡`**以及一些额外的属性，例如[**设置气泡大小**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/) & [**设置X值**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/)需要进行相应设置。执行以下代码后，气泡图将添加到工作表中。请参阅[输出Excel文件](66519070.xlsx)以下示例代码。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

##  **创建自定义图表**

到目前为止，当我们讨论图表时，我们已经研究了具有自己的标准格式设置的标准图表。我们仅定义数据源，设置一些属性，然后使用默认格式设置创建图表。但 Aspose.Cells API 还支持创建自定义图表，允许开发人员使用自己的格式设置创建图表。开发人员可以使用 Aspose.Cells 在运行时创建自定义图表。

图表由一系列数据组成。创建自定义图表时，开发人员可以自由地针对不同的数据系列使用不同类型的图表。

下面的示例代码演示了如何创建自定义图表。在此示例中，我们将使用柱形图表示第一个数据系列，使用折线图表示第二个数据系列。结果是我们将柱形图与折线图组合添加到工作表中。请参阅[输出Excel文件](66519071.xlsx)以下示例代码。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
