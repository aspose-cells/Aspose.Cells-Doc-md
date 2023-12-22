---
title: 同时读取多个线程中的 Cell 值
linktitle: 多线程
type: docs
weight: 1800
url: /zh/net/reading-cell-values-in-multiple-threads-simultaneously/
description: 了解如何通过 Aspose.Cells for .NET API 同时读取多个线程中的 Cell 值。
keywords: Read Cell Values in Multiple Threads Simultaneously, Aspose.Cells C# Multiple Threads, Read data in Multiple Threads
---
{{% alert color="primary" %}}

需要同时读取多个线程中的单元格值是一种常见的需求。本文介绍了如何使用 Aspose.Cells 来实现此目的。

{{% /alert %}}

要同时读取多个线程中的单元格值，请设置[**工作表.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading)为*真**。如果不这样做，您可能会得到错误的单元格值。

下面的代码：

1. 创建工作簿。
1. 添加工作表。
1. 使用字符串值填充工作表。
1. 然后，它创建两个线程，同时从随机单元读取值。
如果读取的值正确，则不会发生任何情况。如果读取的值不正确，则会显示一条消息。

如果你评论这一行：

{{< highlight "java" >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

然后显示以下消息：

{{< highlight "java" >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

否则，程序运行时不会显示任何消息，这意味着从单元格读取的所有值都是正确的。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
