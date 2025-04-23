---
title: 获取图表的工作表
description: 学习如何使用Aspose.Cells for .NET访问与Excel图表关联的工作表。我们的指南将向你展示如何访问工作表并对其进行操作，以操纵图表的基础数据。
keywords: Aspose.Cells for .NET，Excel图表，工作表，数据操作，基础数据，操作。
type: docs
weight: 1000
url: /zh/net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

有时，您可能希望从图表的引用中访问工作表。Aspose.Cells提供了[**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet)属性，该属性返回包含图表的工作表的引用。

{{% /alert %}}

以下示例显示了如何使用[**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet)属性。代码首先打印工作表的名称，然后访问工作表上的第一个图表。然后使用[**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet)属性再次打印工作表名称。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetWorksheetOfTheChart-GetWorksheetOfTheChart.cs" >}}

以下是示例代码产生的控制台输出。您可以看到，它两次打印了相同的工作表名称。

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
