---
title: Rendera en PDF sida per Excel ark  Konvertering av Excel till PDF
type: docs
weight: 100
url: /sv/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}} 

När du arbetar med stora Microsoft Excel-filer (t ex en arbetsbok med många ark, var och en med 50 kolumner och 300 eller fler rader med data), kan du vilja att PDF-utmatningen visar en sida per arbetsblad, oavsett storleken på arbetsbladet. Det skulle innebära att varje sida förmodligen har en helt annan sidstorlek. Detta kan uppnås genom att använda Aspose.Cells for .NET.

{{% /alert %}} 

Se följande exempel på kod som konverterar en Excel-fil med flera kalkylblad till PDF.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

Om [OnePagePerSheet](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet)-alternativet är inställt på **true**, kommer allt arkets innehåll att renderas till en PDF-sida.

{{% /alert %}} {{% alert color="primary" %}} 

Om din kalkylblad innehåller formler är det bäst att anropa [Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)-metoden precis innan du renderar kalkylarket till PDF. Det säkerställer att formelberoende värden beräknas om och de korrekta värdena renderas i PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
