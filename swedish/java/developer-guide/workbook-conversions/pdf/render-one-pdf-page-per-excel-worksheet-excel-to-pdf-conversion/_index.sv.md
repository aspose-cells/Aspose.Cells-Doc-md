---
title: Rendera en PDF sida per Excel ark  Konvertering av Excel till PDF
type: docs
weight: 40
url: /sv/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

När du arbetar med stora Microsoft Excel-filer (till exempel en arbetsbok med många ark, varje med 50 kolumner och 300 eller fler rader data), kan du vilja att PDF-utdata visar en sida per arbetsblad, oavsett storleken på arbetsbladet. Detta skulle innebära att varje sida förmodligen har en radikalt annorlunda sidstorlek. Detta kan uppnås genom att använda Aspose.Cells for Java.

{{% /alert %}}

Se följande exempel på kod som konverterar en Excel-fil med flera kalkylblad till PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

Om [**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet)-alternativet är inställt på **true** renderas allt innehåll på kalkylarket till en PDF-sida. Pappersstorleken som ställts in av [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) är ogiltig, men de andra inställningarna som ställts in med [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) gäller fortfarande.

{{% /alert %}} {{% alert color="primary" %}}

Om din kalkylblad innehåller formler är det bäst att anropa metoden [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) precis innan kalkylbladet renderas till PDF. Detta säkerställer att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
