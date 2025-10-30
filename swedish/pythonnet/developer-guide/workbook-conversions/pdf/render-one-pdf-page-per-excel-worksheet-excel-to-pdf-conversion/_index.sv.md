---
title: Rendera en PDF sida per Excel ark  Konvertering av Excel till PDF
type: docs
weight: 100
url: /sv/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Lär dig hur man Renderar en PDF sida per Excel kalkylark när du konverterar Excel till PDF med Aspose.Cells for Python via .NET API.
keywords: Python Rendera en PDF sida per Excel kalkylark när du sparar filen till PDF, en PDF sida per Excel kalkylark när du sparar Excel till PDF med Python, Python visa en sida per arbetsblad när du konverterar Excel till PDF
---

{{% alert color="primary" %}} 

När du arbetar med stora Microsoft Excel-filer (till exempel en arbetsbok som har många ark, var och en med 50 kolumner och 300 eller fler rader med data), kan du vilja att PDF-utdatan visar en sida per kalkylblad, oavsett storlek på kalkylarket. Detta skulle innebära att varje sida troligen har en radikalt annan sidstorlek. Detta kan uppnås genom att använda Aspose.Cells for Python via .NET API.

{{% /alert %}} 

Se följande exempel på kod som konverterar en Excel-fil med flera kalkylblad till PDF.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

Om [PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/) alternativet är inställt på **true**, kommer allt arkets innehåll att renderas till en PDF-sida.

{{% /alert %}} {{% alert color="primary" %}} 

Om din kalkylblad innehåller formler är det bäst att kalla på [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) metoden precis innan du renderar kalkylbladet till PDF. Detta säkerställer att de formelberoende värdena beräknas om och att de korrekta värdena renderas i PDF:en.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
