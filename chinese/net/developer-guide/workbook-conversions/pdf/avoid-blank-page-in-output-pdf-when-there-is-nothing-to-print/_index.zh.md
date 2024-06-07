---
title: 在输出PDF中避免空白页当没有内容需要打印时
type: docs
weight: 30
url: /zh/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **可能的使用场景**

当Excel文件为空且用户使用Aspose.Cells将其保存为PDF时，在输出PDF中会呈现一张空白页。有时，这种默认行为是不希望的。Aspose.Cells提供了[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint)属性来处理这个问题。如果将其设置为**false**，那么[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)将在输出PDF中没有东西需要打印时发生。

## **在输出PDF中避免空白页当没有内容需要打印时**

以下示例代码创建一个空的工作簿，然后在将其保存为PDF时将[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint)属性设置为**false**。由于在输出PDF中没有内容需要打印，如下所示发生了[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)。

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
