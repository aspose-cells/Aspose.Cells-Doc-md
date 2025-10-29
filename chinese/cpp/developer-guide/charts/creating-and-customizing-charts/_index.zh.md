---
title: 创建和定制图表
type: docs
weight: 10
url: /zh/cpp/creating-and-customizing-charts/
---

## **可能的使用场景**

图表是信息的可视化显示。 Aspose.Cells允许开发人员像Microsoft Excel一样在图表中可视化信息。通过图表呈现信息总是有助于决策者能够快速和及时地做出决策。通过图表而不是原始数字快速查看数据的比较、模式和趋势更容易。在运行时基于电子表格中的数据创建图表是Aspose.Cells的一个有用功能。 Aspose.Cells支持创建标准和定制图表。接下来，我们将展示一些使用Aspose.Cells API创建一些常见的MS-Excel图表类型的示例文件。

## **金字塔图**

执行示例代码后，金字塔图将添加到工作表中。请查看以下示例代码的输出Excel文件(66519068.xlsx)。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

## **折线图**

在上面的示例中，将[**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/)更改为** `ChartType::Line`**即可创建一幅线图。完整源代码如下。执行代码后，一幅折线图将添加到工作表中。请查看以下示例代码的输出Excel文件(66519069.xlsx)。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

## **气泡图**

为创建气泡图，[**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/)必须设置为** `ChartType_Bubble`**，同时需要相应设置一些额外属性，如[**SetBubbleSizes**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/)和[**SetXValues**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/)。执行以下代码后，气泡图将添加到工作表中。请查看以下示例代码的输出Excel文件(66519070.xlsx)。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

## **创建自定义图表**

到目前为止，当我们讨论图表时，我们看过具有自己标准格式设置的标准图表。我们只定义数据源，设置一些属性，图表将以其默认格式设置创建。但Aspose.Cells API还支持创建自定义图表，允许开发人员使用自己的格式设置创建图表。开发人员可以使用Aspose.Cells在运行时创建自定义图表。

图表由数据系列组成。当创建自定义图表时，开发人员可以自由地为不同的数据系列使用不同类型的图表。

下面的示例代码演示了如何创建自定义图表。在此示例中，我们将使用柱状图来展示第一个数据系列，并使用折线图来展示第二个系列。结果是我们在工作表中添加了一个柱状图，结合了一个折线图。请查看以下示例代码的 [输出Excel文件](66519071.xlsx)。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
