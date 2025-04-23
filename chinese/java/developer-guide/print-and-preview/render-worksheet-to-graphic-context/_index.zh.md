---
title: 将工作表呈现到图形上下文
type: docs
weight: 300
url: /zh/java/render-worksheet-to-graphic-context/
---

{{% alert color="primary" %}} 

Aspose.Cells现在可以将工作表渲染到图形上下文。图形上下文可以是图像文件、屏幕或打印机等。请使用以下方法将工作表渲染到图形上下文。

- SheetRender.toImage(int pageIndex, Graphics2D graphic)

{{% /alert %}} 
## **将工作表渲染到图形上下文**
以下代码演示了如何使用Aspose.Cells将工作表渲染到图形上下文。执行代码后，将打印整个工作表，并将剩余的空白区域填充为蓝色，并保存图像为**test.png**文件。您可以尝试此代码使用任何源Excel文件。还请阅读代码内的评论以便更好地理解。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RenderWorksheetToGraphicContext-ReleaseUnmanagedResources.java" >}}






{{< app/cells/assistant language="java" >}}
