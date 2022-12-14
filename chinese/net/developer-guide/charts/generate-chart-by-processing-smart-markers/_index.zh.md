---
title: 通过处理智能标记生成图表
type: docs
weight: 2100
url: /zh/net/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}}

Aspose.Cells API 提供[**工作簿设计器**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)使用智能标记的类，其中格式和公式放置在设计器电子表格中，然后使用[**工作簿设计器**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)类根据指定的智能标记填充数据。也可以通过处理智能标记来创建 Excel 图表，这将需要以下步骤。

- 创建设计师电子表格
- 针对指定数据源处理设计器电子表格
- 基于填充数据创建图表

{{% /alert %}}

## 创建设计师电子表格

设计器电子表格是一个简单的 Excel 文件，使用 Microsoft Excel 应用程序或 Aspose.Cells API 创建，包含视觉格式、公式和智能标记，其中的内容可以在运行时填充。

为了简单起见，我们将使用 Aspose.Cells for .NET API 创建设计器电子表格，然后针对动态创建的数据源对其进行处理以进行演示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## Processing Designer 电子表格

为了处理设计器电子表格，必须具有与设计器电子表格中使用的智能标记相对应的数据源。例如，我们创建了一个 Smart Marker 条目作为 &=Sales.Year，它表示 DataTable Sales 中的 Year 列。如果相应的列在数据源中不可用，Aspose.Cells API 将跳过对该特定智能标记的处理，因此，不会填充该特定智能标记的数据。

为了演示此用例，我们将从头开始创建数据源，并根据上一步中创建的设计器电子表格对其进行处理。但是，在实时场景中，数据可能已经可用于进一步处理，因此如果数据已经可用，您可以跳过数据源的创建。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

智能标记的处理非常简单，如以下代码片段所示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

上面的代码片段使用了现有的实例[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)第一步创建的类。如果磁盘或内存中已有设计器电子表格文件，则可以创建一个实例[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)通过加载现有的设计器电子表格来上课。

{{% /alert %}}

## 创建图表

数据到位后，我们需要做的就是根据数据源创建图表。为了使示例简单，我们将使用[**图表.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)方法，这样我们就不必进一步配置图表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
