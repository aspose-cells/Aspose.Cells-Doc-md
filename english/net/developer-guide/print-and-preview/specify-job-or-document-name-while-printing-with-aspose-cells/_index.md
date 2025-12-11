---
title: Specify Job or Document Name while printing with Aspose.Cells
type: docs
weight: 270
url: /net/specify-job-or-document-name-while-printing-with-aspose-cells/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

You can specify a job or document name while printing your workbook or worksheet using the **WorkbookRender** or **SheetRender** objects. Aspose.Cells provides the `WorkbookRender.ToPrinter(printerName, jobName)` and `SheetRender.ToPrinter(printerName, jobName)` methods that you can use to specify a job or document name while printing your workbook or worksheet.

{{% /alert %}}

## Specify Job or Document Name while printing with Aspose.Cells

The sample code loads the source Excel file and then sends it to the printer by specifying the job or document name using the `WorkbookRender.ToPrinter(printerName, jobName)` and `SheetRender.ToPrinter(printerName, jobName)` methods.

## Sample Code

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SpecifyJobWhilePrinting-SpecifyJobNameWhilePrinting.cs" >}}
{{< app/cells/assistant language="csharp" >}}
