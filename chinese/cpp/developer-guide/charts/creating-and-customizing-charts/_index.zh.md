---
title: 创建和自定义图表
type: docs
weight: 10
url: /zh/cpp/creating-and-customizing-charts/
---

## **可能的使用场景**

图表是信息的可视化显示。Aspose.Cells允许开发人员像Microsoft Excel一样在图表中可视化信息。以图表形式呈现信息总是有助于决策者及时做出快速决定。通过图表快速查看数据的比较、模式和趋势比查看原始数字更容易。在运行时基于电子表格中的数据创建图表是Aspose.Cells的有用特性之一。Aspose.Cells支持创建标准图表和自定义图表。下面，我们将展示使用Aspose.Cells API创建一些常见的MS-Excel图表类型的示例文件。

## **金字塔图**

执行示例代码时，金字塔图表将添加到工作表。请参阅以下示例代码的[输出Excel文件](66519068.xlsx)。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

## **折线图**

在上例中，将**[**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/)**简单更改为**`ChartType::Line`**将创建折线图。下面提供了完整的源代码。执行代码时，将向工作表添加一条折线图。请参阅以下示例代码的[输出Excel文件](66519069.xlsx)。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

## **气泡图**

要创建气泡图，必须将**[**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/)**设置为**`ChartType_Bubble`**，并相应设置[**SetBubbleSizes**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/)和[**SetXValues**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/)等额外属性。执行以下代码后，将在工作表中添加一个气泡图。请参阅以下示例代码的[输出Excel文件](66519070.xlsx)。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

## **创建自定义图表**

到目前为止，当我们讨论图表时，我们已经查看了具有其自己标准格式设置的标准图表。我们只定义了数据源，设置了一些属性，图表就以其默认格式设置被创建。但是，Aspose.Cells API还支持创建自定义图表，允许开发人员使用自己的格式设置创建图表。开发人员可以使用Aspose.Cells在运行时创建自定义图表。

图表由数据系列组成。在创建自定义图表时，开发人员可以自由选择不同类型的图表用于不同的数据系列。

以下示例代码演示了如何创建自定义图表。在此示例中，我们将使用柱状图和线条图作为第一系列和第二系列。结果是我们向工作表添加了一个柱状图，结合了一张折线图。请参阅以下示例代码的[输出Excel文件](66519071.xlsx)。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
