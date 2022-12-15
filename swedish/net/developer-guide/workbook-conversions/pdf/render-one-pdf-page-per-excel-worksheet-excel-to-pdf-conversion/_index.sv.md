---
title: Återge en PDF-sida per Excel-arbetsblad - Excel till PDF-konvertering
type: docs
weight: 100
url: /sv/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}} 

När du arbetar med stora Microsoft Excel-filer (till exempel en arbetsbok som har många ark, var och en med 50 kolumner och 300 eller fler rader med data), kanske du vill att PDF-utdata ska visa en sida per kalkylblad, oavsett storleken på kalkylbladet . Detta skulle innebära att varje sida sannolikt har en radikalt olika sidstorlek. Detta kan uppnås genom att använda Aspose.Cells for .NET.

{{% /alert %}} 

Se följande exempelkod som konverterar en Excel-fil med flera kalkylblad till PDF.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

 Om[OnePagePerSheet](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet) alternativet är inställt på**Sann**, kommer allt arkinnehåll att renderas till en PDF-sida.

{{% /alert %}} {{% alert color="primary" %}} 

 Om ditt kalkylblad innehåller formler är det bäst att ringa[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)precis innan du renderar kalkylarket till PDF. Detta säkerställer att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF-filen.

{{% /alert %}}
