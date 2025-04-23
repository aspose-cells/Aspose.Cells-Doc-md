---
title: Aspose.Cells 8.2.0中的公共API更改
type: docs
weight: 80
url: /zh/java/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.1.2到8.2.0的Aspose.Cells API的更改，这可能会对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，还描述了Aspose.Cells在幕后行为的任何更改。

{{% /alert %}} 
## **为Cells类添加了MultiThreadReading属性**
使用Aspose.Cells for Java 8.2.0，在Cells类中添加了MultiThreadReading属性，以提供更强大的机制同时使用多个线程读取单元格值。在多线程应用程序中将布尔类型属性设置为true，确保每个线程都会接收到正确的单元格值。

{{% alert color="primary" %}} 

请查看[同时在多线程环境中读取单元格值](/cells/zh/java/reading-cell-values-in-multiple-threads-simultaneously/)的详细文章以获取更多信息。

{{% /alert %}}
## **为autoFitRows和autoFitColumns方法添加了重载**
Worksheet类添加了autoFitRows和autoFitColumns的新重载，允许开发人员根据各自的范围自动调整行和列，同时传递AutoFitterOptions类的实例。 

上述方法的签名如下:

1. autoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. autoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

请查看[自动调整行和列](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns)的详细文章。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
