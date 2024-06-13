---
title: 在使用DrawObjectEventHandler类呈现到PDF时获取绘图对象和边界
type: docs
weight: 60
url: /zh/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **可能的使用场景**

Aspose.Cells提供了一个抽象类[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)，其中有一个[**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float))方法。用户可以实现[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)并利用[**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float))方法来获取[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)和**Bound**，同时在将Excel渲染为PDF或图像时。以下是[**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float))方法参数的简要描述。

- drawObject: 在呈现时将初始化并返回[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- x：[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)的左边界

- y：[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)的顶部

- width：[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)的宽度

- height：[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)的高度

如果您正在将Excel文件呈现为PDF，则可以结合[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler)使用[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)类。同样，如果您将Excel文件呈现为图像，则可以结合[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler)使用[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)类。

## **在使用DrawObjectEventHandler类呈现PDF时获取绘图对象和边界**

请参考以下示例代码。它加载了示例Excel文件（64716843.xlsx）并将其另存为输出PDF（64716842.pdf）。在生成PDF时，它利用了[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler)属性并捕获了现有单元格和对象（例如图像等）的[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)和**边界**。如果drawObject类型为Cell，则打印其边界和StringValue。如果drawObject类型为Image，则打印其边界和形状名称。请参见下面提供的示例代码的控制台输出以获取更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **控制台输出**

{{< highlight java >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
