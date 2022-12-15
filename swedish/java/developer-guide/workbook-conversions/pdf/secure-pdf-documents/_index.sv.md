---
title: Säkra PDF-dokument
type: docs
weight: 260
url: /sv/java/secure-pdf-documents/
description: Säkra PDF-filer medan du konverterar från Excel-filer. Den här artikeln visar generering av säker PDF-fil från Excel med Aspose.Cells for Java API.
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---
{{% alert color="primary" %}}

Ibland behöver utvecklare arbeta med krypterade PDF-filer. De behöver till exempel säkra dokument med användar- och ägarlösenord så att inte vem som helst kan öppna dem, eller vill begränsa om dokumentinnehållet kan skrivas ut eller extraheras.

Den här artikeln förklarar hur du skickar in PDF-säkerhetsalternativ när du sparar kalkylblad till PDF.

{{% /alert %}} 

 Aspose.Cells API:er tillhandahåller[**Pdf Säkerhetsalternativ**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSecurityOptions)klass för att arbeta med säkerheten för PDF-filformat. Exempelkoden nedan beskriver hur man skapar säkra PDF-filer med Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

 Om kalkylbladet innehåller formler är det bäst att ringa[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) precis innan du renderar den till PDF. Detta säkerställer att formelberoende värden beräknas om och att de korrekta värdena återges i PDF-filen.

{{% /alert %}}
