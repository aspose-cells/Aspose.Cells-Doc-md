---
title: 当没有要打印的内容时输出空白页
type: docs
weight: 90
url: /zh/net/output-blank-page-when-there-is-nothing-to-print/
---

## **可能的使用场景**

如果工作表为空，则 Aspose.Cells 在导出工作表为图像时不会打印任何内容。您可以在此使用 [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) 属性进行更改。将其设置为 **true**，将会打印空白页。

## **当没有要打印的内容时输出空白页**

以下示例代码创建了一个空工作簿，其中包含一个空工作表，并在将 [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) 属性设置为 **true** 后，将空工作表渲染为图像。因此，生成了一个空白页面，因为没有内容可以打印，您可以在下面的图像中看到。

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.cs" >}}
