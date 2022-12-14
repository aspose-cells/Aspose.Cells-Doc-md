---
title: 公共 API Aspose.Cells 8.2.0 的变化
type: docs
weight: 80
url: /zh/java/public-api-changes-in-aspose-cells-8-2-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.1.2 到 8.2.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **为 Cells 类添加了 MultiThreadReading 属性**
在 Aspose.Cells for Java 8.2.0 中，MultiThreadReading 属性已添加到 Cells 类中，以便提供更强大的机制来同时使用多个线程读取单元格值。在多线程应用程序中将布尔类型属性设置为 true 可确保每个线程都将接收到正确的单元格值。

{{% alert color="primary" %}} 

请查看详细文章[多线程环境下同时读取Cells个值](/cells/zh/java/reading-cell-values-in-multiple-threads-simultaneously/)了解更多信息。

{{% /alert %}}
## **添加了 autoFitRows 和 autoFitColumns 方法的重载**
工作表类中添加了 autoFitRows 和 autoFitColumns 的新重载，允许开发人员在传递 AutoFitterOptions 类的实例时根据各自的范围自动调整行和列。

上述方法的签名如下：

1. autoFitRows（int startRow，int endRow，AutoFitterOptions 选项）
1. autoFitColumns（int firstColumn，int lastColumn，AutoFitterOptions 选项）

{{% alert color="primary" %}} 

请查看详细文章[自动调整行和列](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns).

{{% /alert %}}
