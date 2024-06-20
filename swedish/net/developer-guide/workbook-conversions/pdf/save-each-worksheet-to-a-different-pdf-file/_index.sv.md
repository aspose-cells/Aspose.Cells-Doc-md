---
title: Spara varje kalkylblad i en separat PDF fil
type: docs
weight: 130
url: /sv/net/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}} 

Aspose.Cells stöder att konvertera XLS-filer (som innehåller bilder, diagram osv.) till PDF-dokument. Aspose.Cells for .NET kan arbeta oberoende för att konvertera ett kalkylblad till PDF och du behöver inte använda Aspose.PDF for .NET för konverteringen. Konverteringen kräver inte att programvaran skapar eller använder några tillfälliga filer eftersom hela processen kan göras i minnet.

{{% /alert %}} 
## **Spara varje arbetsblad i en separat PDF-fil**
Om du behöver spara varje kalkylblad i din mall-Excel-fil för att generera olika PDF-filer kan du enkelt uppnå detta. Du kan försöka ställa in ett kalkylbladsindex till [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)-alternativet i taget för att rendera till PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
