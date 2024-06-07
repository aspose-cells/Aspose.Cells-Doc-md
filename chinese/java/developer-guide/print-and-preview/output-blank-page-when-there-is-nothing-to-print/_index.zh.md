---
title: 当没有打印内容时输出空白页
type: docs
weight: 80
url: /zh/java/output-blank-page-when-there-is-nothing-to-print/
---

## **可能的使用场景**

如果工作表为空，则在将工作表导出为图像时，Aspose.Cells不会打印任何内容。 您可以通过使用 [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint) 属性来更改这种行为。 当将其设置为**true**时，它将打印空白页。

## **当没有内容可打印时输出空白页**

以下示例代码创建了一个空工作簿，其中包含一个空工作表，并在将 [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint) 属性设置为**true**后呈现了空工作表的图像。 结果，它生成了空白页，因为没有要打印的内容，您可以如下所示。

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
