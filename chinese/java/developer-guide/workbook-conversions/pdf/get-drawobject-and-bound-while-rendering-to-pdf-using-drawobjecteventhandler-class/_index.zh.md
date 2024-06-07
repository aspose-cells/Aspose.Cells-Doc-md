---
title: 在使用DrawObjectEventHandler类呈现为PDF时获取DrawObject和Bound
type: docs
weight: 60
url: /zh/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **可能的使用场景**

Aspose.Cells 提供一个抽象类 [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)，其中有一个 [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float) 方法。用户可以实现 [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) 并利用 [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float) 方法获得 [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) 和 **Bound**，在将 Excel 呈现为 PDF 或图像时。以下是  [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float) 方法的参数的简要说明。

- drawObject: 当呈现时将初始化并返回 [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- x: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)的左边界

- y: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)的顶部边界

- 宽度: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)的宽度

- 高度: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)的高度

如果您将 Excel 文件呈现为 PDF，则可以使用 [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) 类与 [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler)。同样，如果将 Excel 文件呈现为图像，则可以使用 [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) 类与 [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler)。

## **在使用DrawObjectEventHandler类呈现为PDF时获取DrawObject和Bound**

请参阅以下示例代码。它加载了[示例 Excel 文件](64716843.xlsx) 并将其另存为 [输出 PDF](64716842.pdf)。在呈现为 PDF 时，利用了 [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler) 属性，并捕获了现有单元格和对象（如图像等）的 [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) 和 **Bound**。如果 drawObject 类型为 Cell，则打印其 Bound 和 StringValue。如果 drawObject 类型为 Image，则打印其 Bound 和 Shape Name。请查看下面给出的示例代码的控制台输出以获取更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **控制台输出**

{{< highlight java >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
