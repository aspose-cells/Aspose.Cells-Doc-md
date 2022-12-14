---
title: 公共 API Aspose.Cells 8.1.2 的变化
type: docs
weight: 60
url: /zh/net/public-api-changes-in-aspose-cells-8-1-2/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.1.1 到 8.1.2 的更改，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **如果发生字体替换，添加了对警告的支持**
在 Aspose.Cells for .NET 8.1.2 中，添加了 WarningInfo、WarningType 类、IWarningCallback 接口和 SaveOptions.WarningCallback、ImageOrPrintOptions.WarningCallback 属性，以方便用户在将电子表格转换为图像或 PDF 格式时发生字体替换时收到警告。

{{% alert color="primary" %}} 

请查看详细文章[呈现电子表格时获取字体替换警告](http://aspose.com/docs/display/cellsnet/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File)

{{% /alert %}}
## **删除了过时的 PdfSaveOptions.ChartImageType 属性**
Aspose.Cells for .NET 8.1.2 已从公共 API 中删除过时的 PdfSaveOptions.ChartImageType 属性。
