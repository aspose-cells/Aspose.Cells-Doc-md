---
title: 在使用DrawObjectEventHandler类呈现到PDF时获取绘图对象和边界
type: docs
weight: 70
url: /zh/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **可能的使用场景**

Aspose.Cells提供了一个抽象类 [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)，其中有一个 [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) 方法。用户可以实现 [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) 并利用 [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) 方法来获取渲染Excel为PDF或图像时的 [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) 和 Bound。以下是对 [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) 方法参数的简要描述。

- drawObject: 在呈现时会初始化并返回 [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- x：[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)的左边界

- y：[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)的顶部

- width：[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)的宽度

- height：[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)的高度

如果要将Excel文件呈现为PDF，则可以利用 [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) 类结合 [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler)。同样，如果要将Excel文件呈现为图像，则可以利用 [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) 类结合 [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler)。

## **在使用DrawObjectEventHandler类呈现PDF时获取绘图对象和边界**

请参阅以下示例代码。它加载 [示例Excel文件](64716821.xlsx) 并将其保存为 [输出PDF](64716822.pdf)。在呈现为PDF时，它利用 [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) 属性来捕获现有单元格和对象（例如图像等）的 [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) 和 Bound。如果 [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) 类型是单元格，则打印其 Bound 和 StringValue。如果 [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) 类型是图像，则打印其 Bound 和形状名称。请参见下方所提供的示例代码的控制台输出以获取更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **控制台输出**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
