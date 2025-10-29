---
title: 获取图表的工作表
description: 学习如何使用Aspose.Cells for Python via .NET检索与Excel图表相关联的工作表。我们的指南将教你如何访问工作表并对其操作，以操作图表的底层数据。
keywords: Aspose.Cells for Python via .NET、Excel图表、工作表、数据操作、底层数据、操作。
type: docs
weight: 1000
url: /zh/python-net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

有时，你可能需要访问图表引用的工作表。Aspose.Cells for Python via .NET提供了[**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet)属性，可返回包含该图表的工作表的引用。

{{% /alert %}}

以下示例显示了如何使用[**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet)属性。代码首先打印工作表的名称，然后访问工作表上的第一个图表。然后使用[**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet)属性再次打印工作表名称。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-GetWorksheetOfTheChart.py" >}}

以下是示例代码产生的控制台输出。您可以看到，它两次打印了相同的工作表名称。

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
