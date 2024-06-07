---
title: 在使用DrawObjectEventHandler类呈现为PDF时获取DrawObject和Bound
type: docs
weight: 70
url: /zh/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **可能的使用场景**

Aspose.Cells提供了一个抽象类[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)，其中有一个[**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)方法。用户可以实现[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)并利用[**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)方法获取Excel到PDF或图像的[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)和Bound。下面简要描述了[**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)方法的参数。

- drawObject: 当呈现时会初始化并返回[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- x: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)的左边界

- y: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)的顶部边界

- 宽度: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)的宽度

- 高度: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)的高度

如果您将Excel文件呈现为PDF，则可以使用[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)类和[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler)。同样，如果您将Excel文件呈现为图像，则可以使用[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)类和[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler)。

## **在使用DrawObjectEventHandler类呈现为PDF时获取DrawObject和Bound**

请参阅以下示例代码。它加载[示例Excel文件](64716821.xlsx)并将其另存为[输出PDF](64716822.pdf)。在呈现为PDF时，它利用[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler)属性并捕获现有单元格和对象（如图像等）的[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)和Bound。如果[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)类型是单元格，它会打印其Bound和StringValue。如果[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)类型是图像，则会打印其Bound和形状名称。请查看下面给出的示例代码的控制台输出以获取更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **控制台输出**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
