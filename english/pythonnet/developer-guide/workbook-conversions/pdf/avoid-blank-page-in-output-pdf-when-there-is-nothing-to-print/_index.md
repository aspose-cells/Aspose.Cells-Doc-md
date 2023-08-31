---
title: Avoid Blank Page in Output PDF when there is Nothing to Print
type: docs
weight: 30
url: /python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Learn how to Avoid Blank Page in Output PDF when there is Nothing to Print with Aspose.Cells for Python via .NET API.
keywords: Python Avoid Blank Page in Output PDF when there is Nothing to Print
---

## **Possible Usage Scenarios**

When the Excel file is empty and the user saves it to PDF using Aspose.Cells for Python via .NET, it renders a blank page in output PDF. Sometimes, this default behavior is undesirable. Aspose.Cells for Python via .NET provides the [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) property to deal with this issue. If you will set it as **false**, then [**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/) will occur whenever there is nothing to print in the output PDF.

## **Avoid Blank Page in Output PDF when there is Nothing to Print**

The following sample code creates an empty workbook and then saves it as PDF after setting the [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) property as **false**. Since there is nothing to print in the output PDF, the [**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/) occurs as shown below.

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

## **Exception**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
