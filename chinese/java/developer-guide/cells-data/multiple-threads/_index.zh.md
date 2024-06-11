---
title: 同时读取多个线程中的单元格值
linktitle: 多线程
type: docs
weight: 1100
url: /zh/java/reading-cell-values-in-multiple-threads-simultaneously/
description: 使用 Aspose.Cells for Java API 学习如何同时在多个线程中读取单元格值。
keywords: Java 在多个线程同时读取 Aspose.Cells for Java API 的单元格值，为 Aspose.Cells for Java APIs 使用多个线程。
---

{{% alert color="primary" %}}

需要同时在多个线程中读取单元格值是一个常见的需求。本文解释了如何使用Aspose.Cells来实现这一目的。

{{% /alert %}}

## **如何使用 Aspose.Cells for Java 在多个线程中同时读取单元格值。**

为了在多个线程中同时读取单元格值，将[**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading) 设置为**true**。如果不设置，可能会得到错误的单元格值。请注意，某些功能，比如格式化单元格值，在多线程环境下是不支持的。因此，多线程读取只能访问单元格的原始数据。在多线程环境中，如果尝试获取单元格的格式化值，比如对于数字值使用Cell.getStringValue()，可能会得到意外的结果或异常。

以下代码：

1. 创建一个工作簿。
1. 添加一个工作表。
1. 用字符串值填充工作表。
1. 然后创建两个同时从随机单元格中读取值的线程。
   如果读取的值是正确的，则不会发生任何事情。如果读取的值不正确，则会显示一条消息。

如果您注释掉这一行：

{{< highlight java >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

那么将显示以下消息：

{{< highlight java >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

否则，程序将在不显示任何消息的情况下运行，这意味着从单元格中读取的所有值都是正确的。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
