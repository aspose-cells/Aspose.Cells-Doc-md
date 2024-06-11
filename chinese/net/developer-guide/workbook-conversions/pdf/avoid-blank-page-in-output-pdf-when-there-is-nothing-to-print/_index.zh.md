---
title: 避免输出PDF中的空白页在没有内容打印时
type: docs
weight: 30
url: /zh/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **可能的使用场景**

当Excel文件为空且用户将其保存为PDF使用Aspose.Cells时，在输出PDF中会呈现空白页。有时，这种默认行为是不希望的。Aspose.Cells提供了[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint)属性来处理此问题。如果将其设置为false，则在输出PDF中没有打印内容时将会发生[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)

## **当没有需要打印的内容时，避免在输出PDF中出现空白页**

以下示例代码创建一个空的工作簿，然后将其保存为PDF，设置[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint)属性为false后保存。由于输出PDF中没有需要打印的内容，[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)的情况如下所示。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **异常**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
