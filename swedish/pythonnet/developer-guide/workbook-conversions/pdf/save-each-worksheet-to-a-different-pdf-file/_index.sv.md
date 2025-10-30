---
title: Spara varje kalkylblad i en separat PDF fil
type: docs
weight: 130
url: /sv/python-net/save-each-worksheet-to-a-different-pdf-file/
description: Lär dig hur man Sparar varje kalkylark till en annan PDF fil med Aspose.Cells for Python via .NET API.
keywords: Python Sparar aktivt kalkylark till PDF, Sparar alla kalkylark till PDF, Sparar angivna kalkylark till PDF
---

{{% alert color="primary" %}} 

Aspose.Cells för Python via .NET stödjer konvertering av XLS-filer (som innehåller bilder, diagram osv.) till PDF-dokument. Aspose.Cells för Python via .NET kan arbeta självständigt för att konvertera en kalkylblad till PDF och du behöver inte använda Aspose.PDF för .NET för konverteringen. Konverteringen kräver inte att programvaran skapar eller använder några tillfälliga filer eftersom hela processen kan göras i minnet.

{{% /alert %}} 
## **Spara varje arbetsblad i en separat PDF-fil**
Om du behöver spara varje kalkylblad i din mall-Excel-fil för att generera olika PDF-filer kan du enkelt uppnå detta. Du kan försöka ställa in ett kalkylbladsindex till [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)-alternativet i taget för att rendera till PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
