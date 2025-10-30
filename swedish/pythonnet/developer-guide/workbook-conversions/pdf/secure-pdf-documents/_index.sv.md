---
title: Säkra PDF dokument
type: docs
weight: 120
url: /sv/python-net/secure-pdf-documents/
description: Lär dig hur man passerar in PDF säkerhetsoptioner när du sparar kalkylblad till PDF med Aspose.Cells för Python via .NET API.
keywords: Python skriver säkerhetsoptioner till PDF, krypterar PDF dokument 
---

{{% alert color="primary" %}}

Ibland behöver utvecklare arbeta med krypterade PDF-filer. Till exempel:

- Säkra dokumenten med ägar- och användarlösenord så att inte vem som helst kan öppna dem.
- Ange begränsningar eller behörigheter för dokumentet efter att dokumentet har öppnats. t.ex. begränsa om dokumentinnehållet kan skrivas ut eller extraheras.

Den här artikeln förklarar hur man skickar in PDF-säkerhetsalternativ när man sparar kalkylblad till PDF.

{{% /alert %}}

Aspose.Cells för Python via .NET ger [**PdfSecurityOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) för att arbeta med säkerhet. Du kan ange ägar- och användarlösenord när du sparar till PDF. Ägarlösenordet eller användarlösenordet kommer att krävas för att öppna det krypterade PDF-dokumentet för visning.

- Användarlösenordet kan vara null eller en tom sträng, i så fall kommer inget lösenord att krävas från användaren vid öppning av PDF-dokumentet.
- Öppning av PDF-dokumentet med det korrekta ägarlösenordet tillåter fullständig åtkomst (utan några angivna åtkomstbegränsningar) till dokumentet.
- Öppning av PDF-dokumentet med det korrekta användarlösenordet (eller öppnande av ett dokument som inte har ett användarlösenord) tillåter begränsad åtkomst enligt de angivna behörigheterna.

Det exemplifierande koden nedan beskriver hur man säkrar PDF:er med Aspose.Cells för Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

Om kalkylbladet innehåller formler är det bäst att anropa [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) precis innan det renderas till PDF. Detta ser till att formelberoende värden omberäknas och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
