---
title: Säkra PDF Dokument
type: docs
weight: 120
url: /sv/python-net/secure-pdf-documents/
description: Lär dig hur du skickar in PDF säkerhetsalternativ när du sparar kalkylblad till PDF med Aspose.Cells for Python via .NET API.
keywords: Python write security options to pdf, encrypt PDF document 
---
{{% alert color="primary" %}}

Ibland måste utvecklare arbeta med krypterade PDF-filer. Till exempel:

- Säkra dokumenten med ägar- och användarlösenord så att inte vem som helst kan öppna det.
- Ange begränsningar eller behörigheter för dokumentet efter att dokumentet har öppnats. t.ex. begränsa om dokumentinnehållet kan skrivas ut eller extraheras.

Den här artikeln förklarar hur du skickar in PDF säkerhetsalternativ när du sparar kalkylark till PDF.

{{% /alert %}}

 Aspose.Cells for Python via .NET tillhandahåller[**Pdf Säkerhetsalternativ**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/)för att arbeta med säkerhet. Du kan ställa in ägar- och användarlösenord medan du sparar till PDF. Ägarlösenordet eller användarlösenordet kommer att krävas för att öppna det krypterade PDF-dokumentet för visning.

- Användarlösenordet kan vara null eller tom sträng, i detta fall kommer inget lösenord att krävas av användaren när PDF-dokumentet öppnas.
- Att öppna dokumentet PDF med rätt ägarlösenord ger full åtkomst (utan några angivna åtkomstbegränsningar) till dokumentet.
- Att öppna PDF-dokumentet med rätt användarlösenord (eller öppna ett dokument som inte har ett användarlösenord) tillåter begränsad åtkomst som de behörigheter som anges.

Exempelkoden nedan beskriver hur du säkrar PDF-filer med Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

 Om kalkylbladet innehåller formler är det bäst att ringa[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) precis innan den renderas till PDF. Detta säkerställer att formelberoende värden beräknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}
