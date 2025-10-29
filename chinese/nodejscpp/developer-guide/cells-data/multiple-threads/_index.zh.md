---
title: 同时读取多个线程中的单元格值
linktitle: 多线程
type: docs
weight: 1800
url: /zh/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: 学习如何通过Aspose.Cells for Node.js via C++ API同时在多个线程中读取单元格值。
keywords: 通过C++用Node.js在多个线程中读取单元格值，Aspose.Cells C++多线程，多个线程中读取数据
---

{{% alert color="primary" %}}

需要同时在多个线程中读取单元格值是一个常见的需求。本文解释了如何使用Aspose.Cells来实现这一目的。

{{% /alert %}}

为了在多个线程中同时读取单元格值，请将[**Cells.setMultiThreadReading(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setMultiThreadReading-boolean-)设置为**true**。否则，可能会得到错误的单元格值。

以下代码：

1. 创建一个工作簿。
1. 添加一个工作表。
1. 用字符串值填充工作表。
1. 然后创建两个同时从随机单元格中读取值的线程。
   如果读取的值是正确的，则不会发生任何事情。如果读取的值不正确，则会显示一条消息。

如果您注释掉这一行：

{{< highlight javascript >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

那么将显示以下消息：

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

否则，程序将在不显示任何消息的情况下运行，这意味着从单元格中读取的所有值都是正确的。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-multiple-threads.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
