---
title: Aspose.Cells 8.2.0中的公共API更改
type: docs
weight: 70
url: /zh/net/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.1.2到8.2.0的Aspose.Cells API的更改，这可能会对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，还描述了Aspose.Cells在幕后行为的任何更改。

{{% /alert %}} 
## **为Cells类添加了MultiThreadReading属性**
使用Aspose.Cells for .NET 8.2.0，已向Cells类添加了MultiThreadReading属性，以提供更强大的机制同时使用多个线程读取单元值。在多线程应用程序中将Boolean类型属性设置为true可确保每个线程都会收到正确的单元值。

{{% alert color="primary" %}} 

请查看详细文章 [Simultaneously Read Cells Values in Multi-Threaded Environment](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously) 以获取更多信息。

{{% /alert %}}
## **为 AutoFitRows 和 AutoFitColumns 方法添加了重载**
已向 Worksheet 类添加了 AutoFitRows 和 AutoFitColumns 的新重载，允许开发人员根据它们各自的范围自动调整行和列的大小，同时传递 AutoFitterOptions 类的实例。 

上述方法的签名如下:

1. AutoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. AutoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

请查看详细文章 [Auto Fit Rows and Columns](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns)。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
