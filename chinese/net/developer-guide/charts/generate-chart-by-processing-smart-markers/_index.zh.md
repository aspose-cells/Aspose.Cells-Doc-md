---
title: 通过处理智能标记生成图表
description: 了解如何使用 Aspose.Cells for .NET 生成带有智能标记的图表。我们的指南将向您展示如何处理智能标记及其属性，以增强图表的外观和可用性。
keywords: Aspose.Cells for .NET, chart generation, smart markers, appearance, usability, processing.
type: docs
weight: 2100
url: /zh/net/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}}

 Aspose.Cells API 提供[**工作簿设计器**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)类与智能标记一起使用，其中格式和公式放置在设计器电子表格中，然后使用[**工作簿设计器**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)类根据指定的智能标记填充数据。还可以通过处理智能标记来创建 Excel 图表，这需要执行以下步骤。

- 创建设计师电子表格
- 根据指定的数据源处理设计器电子表格
- 根据填充数据创建图表

{{% /alert %}}

## 创建设计器电子表格

设计器电子表格是使用 Microsoft Excel 应用程序或 Aspose.Cells API 创建的简单 Excel 文件，其中包含可视格式、公式和智能标记，可以在运行时填充内容。

为了简单起见，我们将使用 Aspose.Cells for .NET API 创建设计器电子表格，然后根据动态创建的数据源对其进行处理以进行演示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## 处理设计器电子表格

为了处理设计器电子表格，必须有一个与设计器电子表格中使用的智能标记相对应的数据源。例如，我们创建了一个智能标记条目 &=Sales.Year，它代表数据表 Sales 中的 Year 列。如果数据源中没有相应的列，Aspose.Cells API 将跳过该特定智能标记的处理，因此，不会填充特定智能标记的数据。

为了演示此用例，我们将从头开始创建数据源，并根据上一步中创建的设计器电子表格对其进行处理。但是，在实时场景中，数据可能已经可用于进一步处理，因此如果数据已经可用，您可以跳过数据源的创建。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

智能标记的处理非常简单，如以下代码片段所示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

上面的代码片段使用了现有的实例[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)第一步中创建的类。如果磁盘或内存上已有设计器电子表格文件，则可以创建一个实例[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)通过加载现有的设计器电子表格来类。

{{% /alert %}}

## 图表的创建

数据到位后，我们需要做的就是根据数据源创建图表。为了使示例简单，我们将使用[**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)方法，这样我们就不必进一步配置图表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
