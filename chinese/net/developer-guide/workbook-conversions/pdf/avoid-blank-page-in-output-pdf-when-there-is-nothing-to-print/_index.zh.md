---
title: 当没有可打印的内容时，避免在输出 PDF 中出现空白页
type: docs
weight: 30
url: /zh/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **可能的使用场景**

当 Excel 文件为空并且用户使用 Aspose.Cells 将其保存到 PDF 时，它会在输出 PDF 中呈现空白页。有时，这种默认行为是不可取的。 Aspose.Cells 提供了[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint)财产来处理这个问题。如果你将它设置为**错误的**， 然后[**细胞异常**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)只要输出 PDF 中没有可打印的内容，就会发生。

## **当没有可打印的内容时，避免在输出 PDF 中出现空白页**

以下示例代码创建一个空工作簿，然后在设置后将其另存为 PDF[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint)财产作为**错误的**.由于输出 PDF 中没有要打印的内容，因此[**细胞异常**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)发生如下所示。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **例外**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
