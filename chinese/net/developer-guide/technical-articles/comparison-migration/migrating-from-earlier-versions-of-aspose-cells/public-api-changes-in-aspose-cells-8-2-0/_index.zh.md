---
title: 公共 API Aspose.Cells 8.2.0 的变化
type: docs
weight: 70
url: /zh/net/public-api-changes-in-aspose-cells-8-2-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.1.2 到 8.2.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **为 Cells 类添加了 MultiThreadReading 属性**
在 Aspose.Cells for .NET 8.2.0 中，MultiThreadReading 属性已添加到 Cells 类中，以便提供更强大的机制来同时使用多个线程读取单元格值。在多线程应用程序中将布尔类型属性设置为 true 可确保每个线程都将接收到正确的单元格值。

{{% alert color="primary" %}} 

请查看详细文章[多线程环境下同时读取Cells个值](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously)想要查询更多的信息。

{{% /alert %}}
## **添加了 AutoFitRows 和 AutoFitColumns 方法的重载**
AutoFitRows 和 AutoFitColumns 的新重载已添加到 Worksheet 类，允许开发人员在传递 AutoFitterOptions 类的实例时根据各自的范围自动调整行和列。

上述方法的签名如下：

1. AutoFitRows（int startRow，int endRow，AutoFitterOptions 选项）
1. AutoFitColumns（int firstColumn，int lastColumn，AutoFitterOptions 选项）

{{% alert color="primary" %}} 

请查看详细文章[自动调整行和列](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns).

{{% /alert %}}
