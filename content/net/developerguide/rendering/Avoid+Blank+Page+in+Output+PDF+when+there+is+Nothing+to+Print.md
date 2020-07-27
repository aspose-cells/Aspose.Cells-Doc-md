+++
title = "Avoid Blank Page in Output PDF when there is Nothing to Print" 
description = "" 
weight = 12090 
+++

Aspose.Cells for .NET : Avoid Blank Page in Output PDF when there is Nothing to Print  

# Aspose.Cells for .NET : Avoid Blank Page in Output PDF when there is Nothing to Print


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#AvoidBlankPageinOutputPDFwhenthereisNothingtoPrint-PossibleUsageScenarios)
*   2 [Avoid Blank Page in Output PDF when there is Nothing to Print](#AvoidBlankPageinOutputPDFwhenthereisNothingtoPrint-AvoidBlankPageinOutputPDFwhenthereisNothingtoPrint)
*   3 [Sample Code](#AvoidBlankPageinOutputPDFwhenthereisNothingtoPrint-SampleCode)
*   4 [Exception](#AvoidBlankPageinOutputPDFwhenthereisNothingtoPrint-Exception)
{{< /panel >}}
 

## Possible Usage Scenarios

When the Excel file is empty and the user saves it to PDF using Aspose.Cells, it renders a blank page in output PDF. Sometimes, this default behavior is undesirable. Aspose.Cells provides the [PdfSaveOptions.OutputBlankPageWhenNothingToPrint](https://apireference.aspose.com/net/cells/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) property to deal with this issue. If you will set it as **false**, then [CellsException](https://apireference.aspose.com/net/cells/aspose.cells/cellsexception) will occur whenever there is nothing to print in the output PDF.

## Avoid Blank Page in Output PDF when there is Nothing to Print

The following sample code creates an empty workbook and then saves it as PDF after setting the [PdfSaveOptions.OutputBlankPageWhenNothingToPrint](https://apireference.aspose.com/net/cells/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) property as **false**. Since there is nothing to print in the output PDF, the [CellsException](https://apireference.aspose.com/net/cells/aspose.cells/cellsexception) occurs as shown below.

## Sample Code

## Exception

{{< code lang="cs" >}}
Aspose.Cells.CellsException was unhandled
  HResult=-2146232832
  Message=There is nothing to output/print.
  Source=Aspose.Cells
  StackTrace:
       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)
{{< /code >}}

