---
title: Spara varje kalkylblad i en separat PDF fil
type: docs
weight: 50
url: /sv/java/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}}

Aspose.Cells stöder konvertering av kalkylbladsfiler (som innehåller bilder, diagram osv.) till PDF-dokument. Aspose.Cells for Java kan fungera fristående för att konvertera en kalkylblad till PDF-dokument och du behöver inte längre använda Aspose.PDF för Java för konverteringen. Konverteringen kräver inte heller att skapa/använda temporära filer eftersom hela processen kan utföras i minnet.

{{% /alert %}}

Om du behöver spara varje kalkylblad i din mall Excel-fil för att generera olika PDF-filer kan detta enkelt uppnås. Du kan försöka ställa in ett kalkylbladindex på [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)-alternativet åt gången för att rendera till PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

Om kalkylbladet innehåller formler är det bäst att anropa metoden [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) precis innan kalkylbladet renderas till PDF. Detta säkerställer att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
