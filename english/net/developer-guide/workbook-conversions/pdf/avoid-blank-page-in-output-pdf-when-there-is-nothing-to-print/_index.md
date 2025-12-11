---  
title: Avoid Blank Page in Output PDF when there is Nothing to Print  
type: docs  
weight: 30  
url: /net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/  
ai_search_scope: cells_net  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  

When the Excel file is empty and the user saves it to PDF using Aspose.Cells, it renders a blank page in the output PDF. Sometimes, this default behavior is undesirable. Aspose.Cells provides the [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) property to deal with this issue. If you set it to **false**, then [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) will occur whenever there is nothing to print in the output PDF.  

## **Avoid Blank Page in Output PDF when there is Nothing to Print**  

The following sample code creates an empty workbook and then saves it as PDF after setting the [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) property to **false**. Since there is nothing to print in the output PDF, the [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) occurs as shown below.  

## **Sample Code**  

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}  

## **Exception**  

{{< highlight java >}}  

Aspose.Cells.CellsException was unhandled  

HResult = -2146232832  

Message = There is nothing to output/print.  

Source = Aspose.Cells  

StackTrace:  

   at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)  

{{< /highlight >}}  
{{< app/cells/assistant language="csharp" >}}
