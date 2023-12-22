---
title: 当没有任何内容可打印时，避免输出中出现空白页 PDF
type: docs
weight: 30
url: /zh/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: 了解当 Aspose.Cells for Python via .NET API 没有任何内容可打印时，如何避免输出 PDF 中出现空白页。
keywords: Python Avoid Blank Page in Output PDF when there is Nothing to Print
---
##  **可能的使用场景**

当 Excel 文件为空并且用户使用 Aspose.Cells for Python via .NET 将其保存到 PDF 时，它会在输出 PDF 中呈现空白页面。有时，这种默认行为是不可取的。 Aspose.Cells for Python via .NET 提供[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)财产来处理这个问题。如果您将其设置为 *false**，那么[**细胞异常**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)每当输出 PDF 中没有任何内容可打印时就会发生。

##  **当没有任何内容可打印时，避免输出中出现空白页 PDF**

以下示例代码创建一个空工作簿，然后在设置后将其另存为 PDF[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)属性为 *false**。由于输出 PDF 中没有任何内容可打印，因此[**细胞异常**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)发生如下所示。

##  **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

##  **例外**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
