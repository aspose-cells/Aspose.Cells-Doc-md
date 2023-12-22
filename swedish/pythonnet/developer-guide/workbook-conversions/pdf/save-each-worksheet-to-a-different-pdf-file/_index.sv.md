---
title: Spara varje kalkylblad till en annan PDF-fil
type: docs
weight: 130
url: /sv/python-net/save-each-worksheet-to-a-different-pdf-file/
description: Lär dig hur du sparar varje kalkylblad till en annan PDF-fil med Aspose.Cells for Python via .NET API.
keywords: Python Save Each Worksheet to a Different PDF File
---
{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET stöder konvertering av XLS-filer (som innehåller bilder, diagram, etc.) till PDF-dokument. Aspose.Cells for Python via .NET kan arbeta självständigt för att konvertera ett kalkylblad till PDF och du behöver inte använda Aspose.PDF for .NET för konverteringen. Konverteringen kräver inte att programvaran skapar eller använder några temporära filer eftersom hela processen kan göras i minnet.

{{% /alert %}} 
##  **Spara varje kalkylblad till en annan PDF-fil**
 Om du behöver spara varje kalkylblad i din Excel-mall för att generera olika PDF-filer, kan du enkelt uppnå detta. Du kan försöka ställa in ett arkindex till**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** alternativ åt gången att rendera till PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

 Om ditt kalkylblad innehåller formler är det bäst att ringa[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) precis innan du renderar kalkylarket till formatet PDF. Om du gör det säkerställs att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}
