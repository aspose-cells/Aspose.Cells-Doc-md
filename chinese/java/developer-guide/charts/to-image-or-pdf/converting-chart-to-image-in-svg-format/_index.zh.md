---
title: 将图表转换为SVG格式的图像
type: docs
weight: 140
url: /zh/java/converting-chart-to-image-in-svg-format/
---

{{% alert color="primary" %}} 

可缩放矢量图形（SVG）是一种基于XML的二维图形格式，还支持交互和动画。SVG规范是由万维网联盟（W3C）自1999年以来制定的开放标准。

SVG图像及其行为是在XML文本文件中定义的。这意味着它们可以被搜索、索引、编写脚本和压缩。作为XML文件，SVG图像可以使用任何文本编辑器创建和编辑，但更常见的是使用绘图软件创建。

Aspose.Cells可以将图表保存为BMP、JPEG、PNG、GIF、SVG等各种格式的图像。本文介绍如何将图表保存为SVG图像。

{{% /alert %}} 

以下示例代码解释了如何使用Aspose.Cells将图表转换为SVG格式图像。该代码加载源Excel文件，然后将第一个工作表上找到的第一个图表保存为SVG。

下面的截图显示了使用示例代码创建的SVG格式转换图表图像。

**输出图像** 

![todo:image_alt_text](converting-chart-to-image-in-svg-format_1.png)

由于SVG是基于XML的格式，因此您也可以像在此截图中显示的那样在诸如记事本之类的文本编辑器中打开输出图表图像。

**在文本编辑器中的SCG输出** 

![todo:image_alt_text](converting-chart-to-image-in-svg-format_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertCharttoImageinSVGFormat-ConvertCharttoImageinSVGFormat.java" >}}
