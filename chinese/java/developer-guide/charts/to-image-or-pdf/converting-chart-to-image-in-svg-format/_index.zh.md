---
title: 将图表转换为 SVG 格式的图像
type: docs
weight: 140
url: /zh/java/converting-chart-to-image-in-svg-format/
---
{{% alert color="primary" %}} 

可缩放矢量图形 (SVG) 是一种基于 XML 的矢量图像格式，适用于二维图形，还支持交互性和动画。 SVG 规范是万维网联盟 (W3C) 自 1999 年以来制定的开放标准。

SVG 图像及其行为在 XML 文本文件中定义。这意味着它们可以被搜索、索引、编写脚本和压缩。作为 XML 文件，SVG 图像可以使用任何文本编辑器创建和编辑，但更常见的是使用绘图软件创建。

Aspose.Cells可以将图表保存为BMP、JPEG、PNG、GIF、SVG等多种格式的图片，本文介绍如何将图表保存为SVG图片。

{{% /alert %}} 

以下示例代码解释了如何使用 Aspose.Cells 将图表转换为 SVG 格式图像。该代码加载源 Excel 文件，然后将在第一个工作表上找到的第一个图表保存到 SVG。

以下屏幕截图显示了使用示例代码创建的 SVG 格式的转换图表图像。

**输出图像** 

![待办事项：图片_替代_文本](converting-chart-to-image-in-svg-format_1.png)

由于 SVG 是一种基于 XML 的格式，您还可以在记事本等文本编辑器中打开输出图表图像，如该屏幕截图所示。

**在文本编辑器中输出 SCG** 

![待办事项：图片_替代_文本](converting-chart-to-image-in-svg-format_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertCharttoImageinSVGFormat-ConvertCharttoImageinSVGFormat.java" >}}
