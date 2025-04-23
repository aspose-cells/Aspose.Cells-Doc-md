---
title: 将列宽设置为可伸缩单位，如em或百分比
type: docs
weight: 130
url: /zh/java/set-column-width-to-scalable-unit-like-em-or-percent/
---

从电子表格生成HTML文件非常常见。列的大小定义为"pt"，在许多情况下有效。但是，可能会出现不需要固定大小的情况。例如，如果容器面板宽度为600像素，HTML页面在其中显示。这种情况下，如果生成的表格宽度较大，可能会出现水平滚动条。因此，需要将这个固定大小改为可伸缩单位，如em或百分比以获得更好的呈现。以下示例代码可用于将[**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#WidthScalable)设置为**true**以创建可伸缩宽度。

可从以下链接下载示例源文件和输出文件：

[sampleForScalableColumns.xlsx](74776596.xlsx)

[outsampleForScalableColumns.zip](74776597.zip)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-SetScalableColumnWidth.java" >}}
{{< app/cells/assistant language="java" >}}
