---
title: 通过处理智能标记生成图表
description: 学习如何使用Aspose.Cells for .NET的智能标记生成图表。我们的指南将向您展示如何处理智能标记及其属性，以增强图表的外观和可用性。
keywords: Aspose.Cells for .NET，图表生成，智能标记，外观，可用性，处理。
type: docs
weight: 2100
url: /zh/net/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}}

Aspose.Cells API提供[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)类用于处理智能标记，其中格式和公式放置在设计电子表格中，然后使用[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)类处理以根据指定的智能标记填充数据。还可以通过处理智能标记创建Excel图表，这将需要以下步骤。

- 创建设计师电子表格
- 根据指定数据源处理设计师电子表格
- 基于填充数据创建图表

{{% /alert %}}

## 创建设计师电子表格

设计师电子表格是使用Microsoft Excel应用程序或Aspose.Cells APIs创建的简单Excel文件，包含视觉格式、公式和智能标记，其中内容可以在运行时填充。

为简单起见，我们将使用Aspose.Cells for .NET API创建设计师电子表格，并稍后针对动态创建的数据源进行处理以进行演示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## 处理设计师电子表格

为了处理设计师电子表格，必须拥有与设计师电子表格中使用的智能标记对应的数据源。例如，我们已经创建了一个名为“&=Sales.Year”的智能标记条目，代表数据表销售中的年份列。如果数据源中没有相应的列，则Aspose.Cells APIs将跳过该特定智能标记的处理，结果该特定智能标记的数据将不会被填充。

为了演示这种用例，我们将从头开始创建数据源，并处理它以针对上一步创建的设计师电子表格。但是，在实际情况下，如果数据已经可用进行进一步处理，则可以跳过数据源的创建。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

如下代码片段演示了智能标记的处理非常简单。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

上述代码片段使用了第一步中创建的[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类的现有实例。如果您已经有了设计师电子表格文件保存在磁盘或内存中，可以通过加载现有设计师电子表格来创建[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类的实例。

{{% /alert %}}

## 创建图表

一旦数据就绪，我们只需要基于数据源创建一个图表。为了使示例简单，我们将使用[**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)方法，这样我们就不必进一步配置图表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
