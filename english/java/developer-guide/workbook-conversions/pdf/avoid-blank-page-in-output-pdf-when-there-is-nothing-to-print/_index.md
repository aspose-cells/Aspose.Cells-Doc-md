---
title: Avoid Blank Page in Output PDF when there is Nothing to Print
type: docs
weight: 30
url: /java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **Possible Usage Scenarios**

When the Excel file is empty and the user saves it to PDF using Aspose.Cells, it renders a blank page in output PDF. Sometimes, this default behavior is undesirable. Aspose.Cells provides the [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) property to deal with this issue. If you will set it as **false**, then [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) will occur whenever there is nothing to print in the output PDF.

## **Avoid Blank Page in Output PDF when there is Nothing to Print**

The following sample code creates an empty workbook and then saves it as output PDF after setting the [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) property as **false**. Since there is nothing to print in the output PDF, the [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) occurs as shown below.

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **Exception**

{{< highlight java >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}