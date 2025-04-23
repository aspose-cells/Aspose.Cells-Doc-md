---
title: Säkra PDF dokument
type: docs
weight: 260
url: /sv/java/secure-pdf-documents/
description: Säkra PDF filer vid konvertering från Excel filer. Den här artikeln visar generering av säker PDF fil från Excel med Aspose.Cells for Java API.
keywords: säkra pdf dokument java, säkra pdf dokument, excel till säker pdf, excel till säker pdf java, konvertera excel till säker pdf, konvertera excel till säker pdf java, konvertera excel till lösenordsskyddad pdf, konvertera excel till lösenordsskyddad pdf java, excel till lösenordsskyddad pdf java, excel till lösenordsskyddad pdf
---

{{% alert color="primary" %}}

Ibland behöver utvecklare arbeta med krypterade PDF-filer. Till exempel:

- Säkra dokumenten med ägar- och användarlösenord så att inte vem som helst kan öppna dem.
- Ange begränsningar eller behörigheter för dokumentet efter att dokumentet har öppnats. t.ex. begränsa om dokumentinnehållet kan skrivas ut eller extraheras.

Den här artikeln förklarar hur man skickar in PDF-säkerhetsalternativ när man sparar kalkylblad till PDF.

{{% /alert %}}

Aspose.Cells tillhandahåller [**PdfSecurityOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/) för att arbeta med säkerhet. Du kan ställa in ägar- och användarlösenord vid sparning till PDF. Ägarlösenordet eller användarlösenordet kommer att krävas för att öppna den krypterade PDF-filen för visning.

- Användarlösenordet kan vara null eller en tom sträng, i så fall kommer inget lösenord att krävas från användaren vid öppning av PDF-dokumentet.
- Öppning av PDF-dokumentet med det korrekta ägarlösenordet tillåter fullständig åtkomst (utan några angivna åtkomstbegränsningar) till dokumentet.
- Öppning av PDF-dokumentet med det korrekta användarlösenordet (eller öppnande av ett dokument som inte har ett användarlösenord) tillåter begränsad åtkomst enligt de angivna behörigheterna.

Den följande exempelkoden beskriver hur man skapar säkra PDF-filer med Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

Om kalkylbladet innehåller formler, är det bäst att anropa [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) strax innan man renderar det till PDF. Detta säkerställer att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
