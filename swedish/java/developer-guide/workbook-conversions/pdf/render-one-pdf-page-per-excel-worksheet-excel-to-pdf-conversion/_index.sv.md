---
title: Återge en PDF-sida per Excel-arbetsblad - Excel till PDF-konvertering
type: docs
weight: 40
url: /sv/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

När du arbetar med stora Microsoft Excel-filer (till exempel en arbetsbok som har många ark, var och en med 50 kolumner och 300 eller fler rader med data), kanske du vill att PDF-utdata ska visa en sida per kalkylblad, oavsett storleken på kalkylbladet . Detta skulle innebära att varje sida sannolikt har en radikalt olika sidstorlek. Detta kan uppnås genom att använda Aspose.Cells for Java.

{{% /alert %}}

Se följande exempelkod som konverterar en Excel-fil med flera kalkylblad till PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

 Om[**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet) alternativet är inställt på**Sann** , renderas allt arkinnehåll till en PDF-sida. Pappersstorleken inställd av[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) är ogiltig, men de andra inställningarna som ställts in med[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)träder fortfarande i kraft.

{{% /alert %}} {{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler är det bäst att anropa[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) -metoden precis innan du renderar kalkylarket till PDF. Detta säkerställer att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF-filen.

{{% /alert %}}
