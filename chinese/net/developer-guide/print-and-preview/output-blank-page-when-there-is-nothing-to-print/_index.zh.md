---
title: 无内容打印时输出空白页
type: docs
weight: 90
url: /zh/net/output-blank-page-when-there-is-nothing-to-print/
---
## **可能的使用场景**

如果工作表为空，则在将工作表导出为图像时 Aspose.Cells 将不会打印任何内容。您可以使用更改此行为[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint)财产。什么时候设置**真的**，它将打印空白页。

## **无内容打印时输出空白页**

以下示例代码创建一个空工作簿，其中包含一个空工作表，并在设置后将空工作表呈现为图像[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint)财产作为**真的**.因此，它会生成空白页，因为您可以在下图中看到没有要打印的内容。

![待办事项：图片_替代_文本](output-blank-page-when-there-is-nothing-to-print_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.cs" >}}
