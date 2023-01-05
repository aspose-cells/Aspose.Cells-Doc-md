---
title: Spara varje kalkylblad till en annan PDF-fil
type: docs
weight: 50
url: /sv/java/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}}

Aspose.Cells stöder konvertering av kalkylbladsfiler (som innehåller bilder, diagram, etc.) till PDF dokument. Aspose.Cells for Java kan arbeta självständigt för att konvertera ett kalkylblad till PDF dokument och du behöver inte längre använda Aspose.PDF for Java för konverteringen. Konverteringen kräver inte att man skapar/använder någon temporär fil(er) också eftersom hela processen kan göras i minnet.

{{% /alert %}}

Om du behöver spara varje kalkylblad i din Excel-mall för att generera olika PDF-filer. Detta kan enkelt uppnås. Du kan försöka gömma ark i filen och göra ett ark synligt i taget baserat på vilket du skulle rendera PDF-filer.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

 Om kalkylarket innehåller formler är det bäst att anropa[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()-metoden precis innan kalkylarket renderas till PDF. Detta säkerställer att formelberoende värden räknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}
