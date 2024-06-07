---
title: 将列宽设置为可伸缩单位如 em 或百分比
type: docs
weight: 130
url: /zh/net/set-column-width-to-scalable-unit-like-em-or-percent/
---

从电子表格生成 HTML 文件非常常见。列的大小以 "pt" 单位定义，在许多情况下有效。然而，可能存在这种固定尺寸不需要的情况。例如，如果容器面板宽度为600px，其中显示该 HTML 页面，如果生成的表格宽度更大，则可能会出现水平滚动条。因此，建议将此固定尺寸更改为可伸缩单位如 em 或百分比以获得更好的表现。可以使用以下示例代码，其中[**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/widthscalable)设为**true**来创建可伸缩宽度。

可以从以下链接下载示例源文件和输出文件：

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetScalableColumnWidth-1.cs" >}}
