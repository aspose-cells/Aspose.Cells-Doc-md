---
title: Specify Job or Document Name while printing with Aspose.Cells
type: docs
weight: 270
url: /python-net/specify-job-or-document-name-while-printing-with-aspose-cells/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

You can specify a job or document name while printing your workbook or worksheet using the WorkbookRender or SheetRender objects. Aspose.Cells for Python via .NET provides the `WorkbookRender.ToPrinter(printerName, jobName)` and `SheetRender.ToPrinter(printerName, jobName)` methods that you can use to specify a job name while printing your workbook or worksheet.

{{% /alert %}}

## **Specify Job or Document Name while printing with Aspose.Cells for Python via .NET**

The sample code loads the source Excel file and then sends it to the printer by specifying the job or document name using the `WorkbookRender.ToPrinter(printerName, jobName)` and `SheetRender.ToPrinter(printerName, jobName)` methods.

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SpecifyJobNameWhilePrinting.py" >}}
{{< app/cells/assistant language="python-net" >}}
