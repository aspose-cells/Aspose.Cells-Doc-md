---
title: 同时读取多个线程中的单元格值
linktitle: Multiple Threads
type: docs
weight: 1100
url: /zh/java/reading-cell-values-in-multiple-threads-simultaneously/
description: 学习如何使用Aspose.Cells for Java API同时在多个线程中读取单元格值。
keywords: Java同时读取多个线程的单元格值，Aspose.Cells for Java API中的多线程。
---

{{% alert color="primary" %}}

在多个线程中需要同时读取单元格值是一个常见的需求。本文解释了如何使用Aspose.Cells实现此目的。

{{% /alert %}}

## **如何使用Aspose.Cells for Java同时在多个线程中读取单元格值**

要同时在多个线程中读取单元格值，请将[**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading)设置为true。如果不这样做，您可能会得到错误的单元格值。请注意，一些功能，如格式化单元格值，不支持多线程。因此，MultiThreadReading仅允许您仅访问单元格的原始数据。在多线程环境中，如果尝试获取单元格的格式化值，例如对于数值值的Cell.getStringValue()，可能会获得意外结果或异常。

以下代码：

1. 创建一个工作簿。
1. 添加一个工作表。
1. 用字符串值填充工作表。
1. 然后创建两个同时从随机单元格读取值的线程。
   如果读取的值是正确的，什么也不会发生。如果读取的值不正确，则会显示一条消息。

如果您取消此行的注释：

{{< highlight java >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

然后将显示以下消息：

{{< highlight java >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

否则，程序将在不显示任何消息的情况下运行，这意味着从单元格读取的所有值都是正确的。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
