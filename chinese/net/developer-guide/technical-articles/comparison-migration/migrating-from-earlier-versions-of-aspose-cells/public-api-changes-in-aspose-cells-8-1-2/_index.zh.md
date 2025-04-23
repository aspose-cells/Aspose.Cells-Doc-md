---
title: Aspose.Cells 8.1.2中的公共API更改
type: docs
weight: 60
url: /zh/net/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

本文档描述了Aspose.Cells API从版本8.1.1到8.1.2的更改，可能对模块/应用程序开发人员感兴趣。文档不仅包括新的和更新的公共方法，还包括对Aspose.Cells背后的任何行为更改的描述。

{{% /alert %}} 
## **在发生字体替代时添加了警告支持**
使用Aspose.Cells for .NET 8.1.2，添加了WarningInfo，WarningType类，IWarningCallback接口和SaveOptions.WarningCallback，ImageOrPrintOptions.WarningCallback属性，以便让用户在将电子表格转换为图像或PDF格式时接收警告信息。 

{{% alert color="primary" %}} 

请查看有关[在呈现电子表格时接收字体替换警告](http://aspose.com/docs/display/cellsnet/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File)的详细文章。

{{% /alert %}}
## **删除了过时的PdfSaveOptions.ChartImageType属性**
Aspose.Cells for .NET 8.1.2已从公共API中移除了过时的PdfSaveOptions.ChartImageType属性。
{{< app/cells/assistant language="csharp" >}}
