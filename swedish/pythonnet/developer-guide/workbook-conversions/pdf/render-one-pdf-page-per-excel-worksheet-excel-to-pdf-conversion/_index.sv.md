---
title: Rendera en PDF sida per Excel-arbetsblad - Excel till PDF konvertering
type: docs
weight: 100
url: /sv/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Lär dig hur du renderar en PDF sida per Excel-kalkylblad samtidigt som du konverterar Excel till PDF med Aspose.Cells for Python via .NET API.
keywords: Python Render One PDF Page Per Excel Worksheet while saving file to PDF, One PDF Page Per Excel Worksheet while saving Excel to PDF using Python, Python show one page per worksheet when converting Excel to PDF
---
{{% alert color="primary" %}} 

När du arbetar med stora Microsoft Excel-filer (till exempel en arbetsbok som har många ark, var och en med 50 kolumner och 300 eller fler rader med data), kanske du vill att PDF-utdata ska visa en sida per kalkylblad, oavsett storleken på kalkylbladet . Detta skulle innebära att varje sida sannolikt har en radikalt olika sidstorlek. Detta kan uppnås genom att använda Aspose.Cells for Python via .NET API.

{{% /alert %}} 

Se följande exempelkod som konverterar en Excel-fil med flera kalkylblad till PDF.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

 Om[PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/)alternativet är satt till *true**, allt arkinnehåll renderas till en PDF sida.

{{% /alert %}} {{% alert color="primary" %}} 

 Om ditt kalkylblad innehåller formler är det bäst att ringa[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) metod precis innan kalkylarket renderas till PDF. Detta säkerställer att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}
