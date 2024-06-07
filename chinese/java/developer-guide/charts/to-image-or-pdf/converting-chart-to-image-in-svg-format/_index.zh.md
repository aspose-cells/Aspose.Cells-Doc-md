---
title: 将图表转换为 SVG 格式的图像
type: docs
weight: 140
url: /zh/java/converting-chart-to-image-in-svg-format/
---

{{% alert color="primary" %}} 

可伸缩矢量图形 (SVG) 是一种基于 XML 的二维图形矢量图像格式，同时支持交互和动画。 SVG 规范是由万维网联盟 (W3C) 自 1999 年以来开发的开放标准。

SVG 图像及其行为是在 XML 文本文件中定义的。 这意味着它们可以被搜索、索引、脚本化和压缩。 作为 XML 文件，SVG 图像可以使用任何文本编辑器创建和编辑，但更常见的是使用绘图软件创建。

Aspose.Cells可以将图表保存为各种格式的图像，如BMP、JPEG、PNG、GIF、SVG等。本文解释了如何将图表保存为SVG图像。

{{% /alert %}} 

以下示例代码说明了如何使用Aspose.Cells将图表转换为SVG格式图像。该代码加载源Excel文件，然后将找到的第一个工作表上的第一个图表保存为SVG。

以下截图显示了使用示例代码创建的SVG格式转换图表图像。

**输出图像** 

![todo:image_alt_text](converting-chart-to-image-in-svg-format_1.png)

因为SVG是基于XML的格式，您还可以在文本编辑器（如记事本）中打开输出图表图像，如此截图所示。

**在文本编辑器中显示的SCG输出** 

![todo:image_alt_text](converting-chart-to-image-in-svg-format_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertCharttoImageinSVGFormat-ConvertCharttoImageinSVGFormat.java" >}}
