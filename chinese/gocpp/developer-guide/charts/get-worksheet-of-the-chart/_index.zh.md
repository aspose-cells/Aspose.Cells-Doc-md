---
title: 使用 Golang 通过 C++ 获取图表所在工作表
linktitle: 获取图表的工作表
description: 了解如何使用Aspose.Cells for C++检索与Excel图表关联的工作表。我们的指南将展示如何访问工作表并对其执行操作，以操作图表的底层数据。
keywords: Aspose.Cells for C++、Excel图表、工作表、数据操作、底层数据、操作。
type: docs
weight: 1000
url: /zh/go-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

有时，您希望从图表引用中访问工作表。Aspose.Cells提供了[**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/)方法，可以返回包含图表的工作表的引用。

{{% /alert %}}

以下示例展示如何使用[**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/)方法。代码首先输出工作表的名称，然后访问工作表上的第一个图表，再次打印工作表名，使用[**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/)方法。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetWorksheetOfTheChart.go" >}}
以下是示例代码产生的控制台输出。您可以看到，它两次打印了相同的工作表名称。

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
