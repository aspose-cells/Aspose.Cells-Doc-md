---
title: 使用 DrawObjectEventHandler 类在呈现为 PDF 时获取 DrawObject 和 Bound
type: docs
weight: 70
url: /zh/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **可能的使用场景**

 Aspose.Cells 提供抽象类[**绘图对象事件处理器**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)它有一个[**画（）**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)方法。用户可以实施[**绘图对象事件处理器**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)并利用[**画（）**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)获取方法[**绘图对象**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)和绑定，同时将 Excel 渲染为 PDF 或图像。下面简单介绍一下参数[**画（）**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)方法。

- 绘制对象：[**绘图对象**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)将在渲染时初始化并返回

- x：左边[**绘图对象**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- y：顶部[**绘图对象**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- 宽度：宽度[**绘图对象**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- 高度：高度[**绘图对象**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

如果您将 Excel 文件渲染为 PDF，那么您可以使用[**绘图对象事件处理器**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)类[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler).同样，如果您将 Excel 文件渲染为图像，您可以使用[**绘图对象事件处理器**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)类[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## **使用 DrawObjectEventHandler 类在渲染到 Pdf 时获取 DrawObject 和 Bound**

请参阅以下示例代码。它加载了[示例 Excel 文件](64716821.xlsx)并将其另存为[输出PDF](64716822.pdf).在呈现为 PDF 时，它利用[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler)财产和捕获[**绘图对象**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)现有单元格和对象的边界，例如图像等。如果[**绘图对象**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)type 是 Cell，它打印它的 Bound 和 StringValue。如果[**绘图对象**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)类型是图像，它打印它的绑定和形状名称。请查看下面给出的示例代码的控制台输出以获得更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **控制台输出**

{{< highlight "java" >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
