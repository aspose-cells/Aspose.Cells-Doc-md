---
title: 无内容打印时输出空白页
type: docs
weight: 80
url: /zh/java/output-blank-page-when-there-is-nothing-to-print/
---
##  **可能的使用场景**

如果工作表为空，则在将工作表导出为图像时 Aspose.Cells 将不会打印任何内容。您可以使用更改此行为[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)财产。当您将其设置为 *true** 时，它将打印空白页。

##  **无内容打印时输出空白页**

以下示例代码创建一个空工作簿，其中包含一个空工作表，并在设置后将空工作表呈现为图像[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)属性为 *true**。因此，它会生成空白页，因为没有要打印的内容，如下所示。

![待办事项：image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

##  **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
