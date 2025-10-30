---
title: Säkerställ PDF dokument med Golang via C++
linktitle: Säkra PDF dokument
type: docs
weight: 120
url: /sv/go-cpp/secure-pdf-documents/
description: Lär dig hur du säkrar PDF dokument med ägar och användarlösenord med Aspose.Cells och Golang via C++.
---

{{% alert color="primary" %}}

Ibland behöver utvecklare arbeta med krypterade PDF-filer. Till exempel:

- Säkra dokumenten med ägar- och användarlösenord så att inte vem som helst kan öppna dem.
- Ange begränsningar eller behörigheter för dokumentet efter att dokumentet har öppnats. t.ex. begränsa om dokumentinnehållet kan skrivas ut eller extraheras.

Den här artikeln förklarar hur man skickar in PDF-säkerhetsalternativ när man sparar kalkylblad till PDF.

{{% /alert %}}

Aspose.Cells tillhandahåller [**PdfSecurityOptions**](https://reference.aspose.com/cells/go-cpp/pdfsecurityoptions/) för att arbeta med säkerhet. Du kan ange ägar- och användarlösenord vid sparning till PDF. Ägarlösenord eller användarlösenord krävs för att öppna den krypterade PDF-dokumentet för visning.

- Användarlösenordet kan vara null eller en tom sträng, i så fall kommer inget lösenord att krävas från användaren vid öppning av PDF-dokumentet.
- Att öppna PDF-dokumentet med rätt ägarlösenord ger full tillgång (utan några tillgångsrestriktioner angivna) till dokumentet.
- Öppning av PDF-dokumentet med det korrekta användarlösenordet (eller öppnande av ett dokument som inte har ett användarlösenord) tillåter begränsad åtkomst enligt de angivna behörigheterna.

Exempelkoden nedan beskriver hur du säkrar PDF:er med Aspose.Cells.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SecurePdfDocuments.go" >}}
{{% alert color="primary" %}}

Om kalkbladet innehåller formler är det bäst att ringa [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) precis innan det renderas till PDF. Detta säkerställer att värden beroende av formler omberäknas och de korrekta värdena visas i PDF:en.

{{% /alert %}}
