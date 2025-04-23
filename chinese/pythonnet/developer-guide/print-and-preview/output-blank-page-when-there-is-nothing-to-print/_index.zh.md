---
title: 当没有要打印的内容时输出空白页
type: docs
weight: 90
url: /zh/python-net/output-blank-page-when-there-is-nothing-to-print/
---

## **可能的使用场景**

如果工作表为空，Aspose.Cells for Python via .NET 在导出为图片时不会生成任何内容。你可以使用 [**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print) 属性改变此行为。当设置为 **true** 时，将输出空白页。

## **当没有要打印的内容时输出空白页**

以下示例代码创建了一个空工作簿，其中包含一个空工作表，并在将 [**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print) 属性设置为 **true** 后，将空工作表渲染为图像。因此，生成了一个空白页面，因为没有内容可以打印，您可以在下面的图像中看到。

![todo:image_alt_text](1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-OutputBlankPageWhenThereIsNothingToPrint-1.py" >}}

