---
title: Aspose.Cells 8.2.0中的公共API更改
type: docs
weight: 70
url: /zh/net/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

此文档描述了从版本8.1.2到8.2.0的Aspose.Cells API的更改，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，还包括对Aspose.Cells内部行为的任何更改的描述。

{{% /alert %}} 
## **为Cells Class添加了MultiThreadReading属性**
通过Aspose.Cells for .NET 8.2.0，已在Cells类中添加了MultiThreadReading属性，以提供更强大的机制来同时使用多个线程读取单元格值。在多线程应用程序中将布尔类型属性设置为true确保每个线程将接收正确的单元格值。

{{% alert color="primary" %}} 

欲了解更多信息，请查阅[在多线程环境中同时读取单元格值](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously)的详细文章。

{{% /alert %}}
## **为AutoFitRows和AutoFitColumns方法添加了重载**
已向Worksheet类添加了AutoFitRows和AutoFitColumns的新重载，允许开发人员根据它们各自的范围自动调整行和列，并传递AutoFitterOptions类的实例。 

上述方法的签名如下:

1. AutoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. AutoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

请查阅[自动调整行和列](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns)的详细文章。

{{% /alert %}}
