---
title: 将工作表渲染到图形上下文
type: docs
weight: 300
url: /zh/java/render-worksheet-to-graphic-context/
---

{{% alert color="primary" %}} 

Aspose.Cells现在可以将工作表呈现为图形环境。图形环境可以是图像文件、屏幕或打印机等。请使用以下方法将工作表呈现为图形环境。

- SheetRender.toImage(int pageIndex, Graphics2D graphic)

{{% /alert %}} 
## **将工作表渲染到图形上下文**
以下代码示例说明如何使用Aspose.Cells将工作表呈现为图形环境。执行代码后，将在图形环境中打印整个工作表，并使用蓝色填充剩余的空白空间，然后将图像保存为**test.png**文件。您可以使用任何源Excel文件尝试此代码。请阅读代码内的注释，以获得更好的理解。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RenderWorksheetToGraphicContext-ReleaseUnmanagedResources.java" >}}






