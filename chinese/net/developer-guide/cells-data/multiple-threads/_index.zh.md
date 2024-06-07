---
title: 同时读取多个线程中的单元格值
linktitle: Multiple Threads
type: docs
weight: 1800
url: /zh/net/reading-cell-values-in-multiple-threads-simultaneously/
description: 学习如何通过Aspose.Cells for .NET API同时读取多个线程中的单元格值。
keywords: 同时在多个线程中读取单元格值，使用Aspose.Cells C#多线程，同时在多个线程中读取数据
---

{{% alert color="primary" %}}

在多个线程中需要同时读取单元格值是一个常见的需求。本文解释了如何使用Aspose.Cells实现此目的。

{{% /alert %}}

要同时在多个线程中读取单元格值，请将[**Worksheet.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading)设置为**true**。如果不这样做，则可能会获得错误的单元格值。

以下代码：

1. 创建一个工作簿。
1. 添加一个工作表。
1. 用字符串值填充工作表。
1. 然后创建两个同时从随机单元格读取值的线程。
   如果读取的值是正确的，什么也不会发生。如果读取的值不正确，则会显示一条消息。

如果您取消此行的注释：

{{< highlight java >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

然后将显示以下消息：

{{< highlight java >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

否则，程序将在不显示任何消息的情况下运行，这意味着从单元格读取的所有值都是正确的。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
