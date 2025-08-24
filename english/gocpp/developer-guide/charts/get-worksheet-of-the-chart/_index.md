---
title: Get Worksheet of the Chart with Golang via C++
linktitle: Get Worksheet of the Chart
description: Learn how to retrieve the worksheet associated with an Excel chart using Aspose.Cells for C++. Our guide will show you how to access the worksheet and perform operations on it to manipulate the underlying data of the chart.
keywords: Aspose.Cells for C++, Excel charts, worksheets, data manipulation, underlying data, operations.
type: docs
weight: 1000
url: /go-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Sometimes, you want to access a worksheet from a chart's reference. Aspose.Cells provides the [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/) method which returns the reference of the worksheet that contains the chart.

{{% /alert %}}

The following example shows how to use the [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/) method. The code first prints the name of the worksheet, then accesses the first chart on the worksheet. It then prints the worksheet name again, using the [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/) method.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-GetWorksheetOfTheChart.go" >}}
Below is the console output that the sample code results in. As you can see, it prints the same worksheet name both times.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}