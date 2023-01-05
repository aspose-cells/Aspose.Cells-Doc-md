---
title: 使用 DrawObjectEventHandler 类渲染到 PDF 时获取 DrawObject 和 Bound
type: docs
weight: 60
url: /zh/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **可能的使用场景**

Aspose.Cells 提供抽象类[**绘图对象事件处理器**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)它有一个[**画（）**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)） 方法。用户可以实施[**绘图对象事件处理器**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)并利用[**画（）**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)方法获取[**绘图对象**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)和**边界**在将 Excel 渲染为 PDF 或图像时。下面简单介绍一下参数[**画（）**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)） 方法。

- 绘制对象：[**绘图对象**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)将在渲染时初始化并返回

- x：左边[**绘图对象**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- y：顶部[**绘图对象**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- 宽度：宽度[**绘图对象**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- 高度：高度[**绘图对象**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

如果您将 Excel 文件渲染到 PDF，那么您可以利用[**绘图对象事件处理器**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)类[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler).同样，如果您将 Excel 文件渲染为图像，您可以使用[**绘图对象事件处理器**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)类[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler).

## **使用 DrawObjectEventHandler 类在渲染到 Pdf 时获取 DrawObject 和 Bound**

请参阅以下示例代码。它加载了[示例 Excel 文件](64716843.xlsx)并将其另存为[输出 PDF](64716842.pdf).在渲染到 PDF 时，它利用[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler)财产和捕获[**绘图对象**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)和**边界**现有的单元格和对象，例如图像等。如果 drawObject 类型是 Cell，它会打印其 Bound 和 StringValue。如果 drawObject 类型是 Image，它会打印它的 Bound 和 Shape Name。请查看下面给出的示例代码的控制台输出以获得更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **控制台输出**

{{< highlight "java" >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
