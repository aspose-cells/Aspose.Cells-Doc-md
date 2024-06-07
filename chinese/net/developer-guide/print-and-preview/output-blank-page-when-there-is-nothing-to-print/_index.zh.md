---
title: 当没有打印内容时输出空白页
type: docs
weight: 90
url: /zh/net/output-blank-page-when-there-is-nothing-to-print/
---

## **可能的使用场景**

如果工作表为空，则当您将工作表导出为图像时，Aspose.Cells将不打印任何内容。您可以通过使用[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint)属性来更改此行为。当您将其设置为**true**时，它将打印空白页。

## **当没有内容可打印时输出空白页**

下面的示例代码创建了一个空工作簿，其中包含一个空工作表，并在将[**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint)属性设置为**true**后将空白工作表渲染为图像。因此，由于没有内容可打印，它会生成一个空白页，如下图所示。

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.cs" >}}
