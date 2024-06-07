---
title: 将列宽设置为可伸缩单位如 em 或百分比
type: docs
weight: 130
url: /zh/java/set-column-width-to-scalable-unit-like-em-or-percent/
---

从电子表格生成 HTML 文件非常常见。“pt”定义了列的大小，在许多情况下都有效。然而，在某些情况下可能不需要固定大小。例如，如果容器面板宽度为600像素，此 HTML 页面正在显示，则如果生成的表格宽度更大，可能会出现水平滚动条。在这种情况下，可以修改固定大小为比例单位，如 em 或百分比，以获得更好的展示效果。可以使用以下示例代码，其中 [**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#WidthScalable) 设置为 **true** 以创建可伸缩宽度。

可以从以下链接下载示例源文件和输出文件：

[可伸缩列的示例.xlsx](74776596.xlsx)

[可伸缩列的输出.zip](74776597.zip)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-SetScalableColumnWidth.java" >}}
