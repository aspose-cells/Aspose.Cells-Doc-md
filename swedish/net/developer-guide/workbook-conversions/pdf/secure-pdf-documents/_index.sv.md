---
title: Säkra PDF dokument
type: docs
weight: 120
url: /sv/net/secure-pdf-documents/
---

{{% alert color="primary" %}}

Ibland behöver utvecklare arbeta med krypterade PDF-filer. Till exempel:

- Säkra dokumenten med ägar- och användarlösenord så att inte vem som helst kan öppna dem.
- Ange begränsningar eller behörigheter för dokumentet efter att dokumentet har öppnats. t.ex. begränsa om dokumentinnehållet kan skrivas ut eller extraheras.

Den här artikeln förklarar hur man skickar in PDF-säkerhetsalternativ när man sparar kalkylblad till PDF.

{{% /alert %}}

Aspose.Cells tillhandahåller [**PdfSecurityOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) för att arbeta med säkerhet. Du kan ställa in ägar- och användarlösenord vid sparning till PDF. Ägarlösenordet eller användarlösenordet kommer att krävas för att öppna den krypterade PDF-filen för visning.

- Användarlösenordet kan vara null eller en tom sträng, i så fall kommer inget lösenord att krävas från användaren vid öppning av PDF-dokumentet.
- Öppning av PDF-dokumentet med det korrekta ägarlösenordet tillåter fullständig åtkomst (utan några angivna åtkomstbegränsningar) till dokumentet.
- Öppning av PDF-dokumentet med det korrekta användarlösenordet (eller öppnande av ett dokument som inte har ett användarlösenord) tillåter begränsad åtkomst enligt de angivna behörigheterna.

Exempelkoden nedan beskriver hur du säkrar PDF:er med Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

Om kalkylbladet innehåller formler är det bäst att anropa [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) precis innan det renderas till PDF. Detta ser till att formelberoende värden omberäknas och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
