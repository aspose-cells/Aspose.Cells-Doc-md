---
title: Cell 同时读取多个线程中的值
linktitle: 多线程
type: docs
weight: 1800
url: /zh/net/reading-cell-values-in-multiple-threads-simultaneously/
---
{{% alert color="primary" %}}

需要同时读取多个线程中的单元格值是一个常见的需求。本文介绍了如何为此目的使用 Aspose.Cells。

{{% /alert %}}

要同时读取多个线程中的单元格值，请设置[**工作表.Cells.多线程读取**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading)至**真的**.如果不这样做，您可能会得到错误的单元格值。

以下代码：

1. 创建工作簿。
1. 添加工作表。
1. 使用字符串值填充工作表。
1. 然后它创建两个同时从随机单元格中读取值的线程。
如果读取的值正确，则不会发生任何事情。如果读取的值不正确，则会显示一条消息。

如果您评论此行：

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
