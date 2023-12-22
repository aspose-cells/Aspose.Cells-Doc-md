---
title: Säkra PDF Dokument
type: docs
weight: 260
url: /sv/java/secure-pdf-documents/
description: Säkra PDF-filer medan du konverterar från Excel-filer. Den här artikeln visar generering av säker PDF-fil från Excel med Aspose.Cells for Java API.
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---
{{% alert color="primary" %}}

Ibland måste utvecklare arbeta med krypterade PDF-filer. Till exempel:

- Säkra dokumenten med ägar- och användarlösenord så att inte vem som helst kan öppna det.
- Ange begränsningar eller behörigheter för dokumentet efter att dokumentet har öppnats. t.ex. begränsa om dokumentinnehållet kan skrivas ut eller extraheras.

Den här artikeln förklarar hur du skickar in PDF säkerhetsalternativ när du sparar kalkylark till PDF.

{{% /alert %}}

 Aspose.Cells tillhandahåller[**Pdf Säkerhetsalternativ**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/)för att arbeta med säkerhet. Du kan ställa in ägar- och användarlösenord medan du sparar till PDF. Ägarlösenordet eller användarlösenordet kommer att krävas för att öppna det krypterade PDF-dokumentet för visning.

- Användarlösenordet kan vara null eller tom sträng, i detta fall kommer inget lösenord att krävas av användaren när PDF-dokumentet öppnas.
- Att öppna dokumentet PDF med rätt ägarlösenord ger full åtkomst (utan några angivna åtkomstbegränsningar) till dokumentet.
- Att öppna PDF-dokumentet med rätt användarlösenord (eller öppna ett dokument som inte har ett användarlösenord) tillåter begränsad åtkomst som de behörigheter som anges.

Exempelkoden nedan beskriver hur man skapar säkra PDF-filer med Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

 Om kalkylbladet innehåller formler är det bäst att ringa[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()precis innan den renderas till PDF. Detta säkerställer att formelberoende värden beräknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}
