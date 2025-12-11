---
title: Get Worksheet of the Chart
description: Learn how to retrieve the worksheet associated with an Excel chart using Aspose.Cells for Python via .NET. Our guide will show you how to access the worksheet and perform operations on it to manipulate the underlying data of the chart.
keywords: Aspose.Cells for Python via .NET, Excel charts, worksheets, data manipulation, underlying data, operations.
type: docs
weight: 1000
url: /python-net/get-worksheet-of-the-chart/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes you want to access the worksheet from a chart reference. Aspose.Cells for Python via .NET provides the [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet) property, which returns a reference to the worksheet that contains the chart.

{{% /alert %}}

The following example shows how to use the [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet) property. The code first prints the name of the worksheet, then accesses the first chart on the worksheet. It then prints the worksheet name again, using the [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet) property.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-GetWorksheetOfTheChart.py" >}}

Below is the console output that the sample code produces. As you can see, it prints the same worksheet name both times.

{{< highlight java >}}
Sheet Name: Portfolio

Chart's Sheet Name: Portfolio
{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
