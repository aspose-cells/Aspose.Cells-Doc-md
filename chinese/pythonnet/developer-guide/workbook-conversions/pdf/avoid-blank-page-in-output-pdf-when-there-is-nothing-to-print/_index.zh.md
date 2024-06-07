---
title: 在输出PDF中避免空白页当没有内容需要打印时
type: docs
weight: 30
url: /zh/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: 了解如何使用Aspose.Cells for Python通过.NET API在没有要打印内容时避免输出PDF中的空白页
keywords: Python在没有要打印的内容时避免输出PDF中的空白页。当Excel文件为空且用户使用Aspose.Cells for Python 通过.NET将其保存为PDF时，输出PDF中会呈现一个空白页面。有时，此默认行为是不可取的。Aspose.Cells for Python 通过.NET提供了一个属性来处理此问题。如果将其设置为**false**，那么在输出PDF中没有要打印的内容时将会发生。
---

## **可能的使用场景**

当Excel文件为空并且用户通过.NET使用Aspose.Cells for Python将其保存为PDF时，输出PDF中会呈现空白页面。有时，这种默认行为是不希望的。Aspose.Cells通过.NET提供了[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)属性来解决此问题。如果将其设置为false，则在输出PDF中没有内容可打印时，[**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)将发生。

## **在输出PDF中避免空白页当没有内容需要打印时**

以下示例代码创建一个空的工作簿，然后在将其保存为PDF时将[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)属性设置为**false**。由于在输出PDF中没有内容需要打印，如下所示发生了[**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)。

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
