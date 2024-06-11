---
title: 避免输出PDF中的空白页在没有内容打印时
type: docs
weight: 30
url: /zh/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: 学习如何使用Aspose.Cells for Python via .NET API在没有内容打印时避免输出PDF中的空白页。
keywords: Python在没有内容打印时避免输出PDF中的空白页
---

## **可能的使用场景**

当Excel文件为空并且用户使用Aspose.Cells for Python via .NET将其保存为PDF时，输出PDF中会呈现一个空白页。有时，这种默认行为是不希望的。Aspose.Cells for Python via .NET提供[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)属性来处理此问题。如果将其设置为**false**，那么在输出PDF中没有内容可打印时将发生[**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)。

## **当没有需要打印的内容时，避免在输出PDF中出现空白页**

以下示例代码创建一个空的工作簿，然后将其保存为PDF，设置[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)属性为false后保存。由于输出PDF中没有需要打印的内容，[**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)的情况如下所示。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

## **异常**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
