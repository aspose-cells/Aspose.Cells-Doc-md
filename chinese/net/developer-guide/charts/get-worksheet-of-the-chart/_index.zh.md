---
title: 获得图表的工作表
description: 学习如何使用Aspose.Cells for .NET检索与Excel图表相关联的工作表。我们的指南将向您展示如何访问工作表并对其执行操作以操作图表的基础数据。
keywords: Aspose.Cells for .NET，Excel图表，工作表，数据操作，基础数据，操作。
type: docs
weight: 1000
url: /zh/net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

有时，您希望从图表的引用中访问工作表。Aspose.Cells提供了[**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet)属性，该属性返回包含该图表的工作表的引用。

{{% /alert %}}

下面的示例展示了如何使用[**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet)属性。该代码首先打印出工作表的名称，然后访问工作表上的第一个图表。然后再次通过使用[**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet)属性打印出工作表名称。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetWorksheetOfTheChart-GetWorksheetOfTheChart.cs" >}}

下面是示例代码的控制台输出结果。您可以看到，它两次打印了相同的工作表名称。

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
