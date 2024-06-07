---
title: Aspose.Cells 8.1.2中的公共API更改
type: docs
weight: 70
url: /zh/java/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

此文档描述了从版本8.1.1到8.1.2的Aspose.Cells API的更改，这可能会引起模块/应用程序开发人员的兴趣。它不仅包括新的和更新的公共方法，还描述了Aspose.Cells背后的行为中的任何更改。

{{% /alert %}} 
## **添加了警告支持，如果发生字体替换**
使用Aspose.Cells for Java 8.1.2版本，添加了WarningInfo和WarningType类，IWarningCallback接口，以及SaveOptions.WarningCallback和ImageOrPrintOptions.WarningCallback属性，以允许开发人员在将电子表格转换为图片、XPS和PDF格式时接收警告。 

{{% alert color="primary" %}} 

请查看[在渲染电子表格时获取字体替换警告](http://aspose.com/docs/display/cellsjava/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File)的详细文章了解更多信息。

{{% /alert %}}
## **删除过时的PdfSaveOptions.ChartImageType属性**
Aspose.Cells for Java 8.1.2版本已从公共API中移除了过时的PdfSaveOptions.ChartImageType属性。
