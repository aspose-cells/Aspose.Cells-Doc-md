---
title: 同时读取多个线程中的 Cell 值
linktitle: 多线程
type: docs
weight: 1100
url: /zh/java/reading-cell-values-in-multiple-threads-simultaneously/
description: 了解如何使用 Aspose.Cells for Java API 同时读取多个线程中的 Cell 值。
keywords: Java Read Cell Values in Multiple Threads Simultaneously, Multiple Threads for Aspose.Cells for Java APIs.
---
{{% alert color="primary" %}}

需要同时读取多个线程中的单元格值是一种常见的需求。本文介绍了如何使用 Aspose.Cells 来实现此目的。

{{% /alert %}}

##  **如何使用 Aspose.Cells for Java 在多个线程中同时读取 Cell 值**

要同时读取多个线程中的单元格值，请设置[**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading)为*真**。如果不这样做，您可能会得到错误的单元格值。请注意，多线程不支持某些功能，例如格式化单元格值。因此，MultiThreadReading 只能让您访问单元格的原始数据。在多线程环境中，如果您尝试获取单元格的格式化值，例如通过 Cell.getStringValue() 获取数值，您可能会得到意外的结果或异常。

下面的代码：

1. 创建工作簿。
1. 添加工作表。
1. 使用字符串值填充工作表。
1. 然后，它创建两个线程，同时从随机单元读取值。
如果读取的值正确，则不会发生任何情况。如果读取的值不正确，则会显示一条消息。

如果你评论这一行：

{{< highlight "java" >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

然后显示以下消息：

{{< highlight "java" >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

否则，程序运行时不会显示任何消息，这意味着从单元格读取的所有值都是正确的。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
