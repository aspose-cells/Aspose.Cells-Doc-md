---
title: 当没有要打印的内容时输出空白页
type: docs
weight: 80
url: /zh/java/output-blank-page-when-there-is-nothing-to-print/
---

## **可能的使用场景**

如果工作表为空，则Aspose.Cells在将工作表导出为图像时不会打印任何内容。您可以通过使用[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)属性来更改此行为。当将其设置为**true**时，它将打印空白页。

## **当没有要打印的内容时输出空白页**

以下示例代码创建了一个空工作簿，其中有一个空工作表，并在设置[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint)属性为**true**后将空工作表呈现为图像。因此，它会生成空白页，因为没有要打印的内容，您可以从下面看到。

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
