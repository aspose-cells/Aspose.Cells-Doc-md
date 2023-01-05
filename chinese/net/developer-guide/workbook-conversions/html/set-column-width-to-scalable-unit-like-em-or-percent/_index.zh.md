---
title: 将列宽设置为可缩放单位，如 em 或百分比
type: docs
weight: 130
url: /zh/net/set-column-width-to-scalable-unit-like-em-or-percent/
---
从电子表格生成 HTML 文件非常常见。列的大小以“pt”定义，这在许多情况下都有效。但是，可能存在不需要此固定大小的情况。例如，如果显示此 HTML 页面的容器面板宽度为 600 像素。在这种情况下，如果生成的表格宽度更大，您可能会得到一个水平滚动条。要求将此固定大小更改为可缩放的单位，如 em 或 percent，以获得更好的显示效果。以下示例代码可用于[**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/widthscalable)被设置为**真的**用于创建可缩放宽度。

示例源文件和输出文件可以从以下链接下载：

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetScalableColumnWidth-1.cs" >}}
