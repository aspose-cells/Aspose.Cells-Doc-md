---
title: Säkra PDF Dokument
type: docs
weight: 120
url: /sv/net/secure-pdf-documents/
---
{{% alert color="primary" %}}

Ibland måste utvecklare arbeta med krypterade PDF-filer. Till exempel:

- Säkra dokumenten med ägar- och användarlösenord så att inte vem som helst kan öppna det.
- Ange begränsningar eller behörigheter för dokumentet efter att dokumentet har öppnats. t.ex. begränsa om dokumentinnehållet kan skrivas ut eller extraheras.

Den här artikeln förklarar hur du skickar in PDF säkerhetsalternativ när du sparar kalkylark till PDF.

{{% /alert %}}

 Aspose.Cells tillhandahåller[**Pdf Säkerhetsalternativ**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/)för att arbeta med säkerhet. Du kan ställa in ägar- och användarlösenord medan du sparar till PDF. Ägarlösenordet eller användarlösenordet kommer att krävas för att öppna det krypterade PDF-dokumentet för visning.

- Användarlösenordet kan vara null eller tom sträng, i detta fall kommer inget lösenord att krävas av användaren när PDF-dokumentet öppnas.
- Att öppna dokumentet PDF med rätt ägarlösenord ger full åtkomst (utan några angivna åtkomstbegränsningar) till dokumentet.
- Att öppna PDF-dokumentet med rätt användarlösenord (eller öppna ett dokument som inte har ett användarlösenord) tillåter begränsad åtkomst som de behörigheter som anges.

Exempelkoden nedan beskriver hur du säkrar PDF-filer med Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

 Om kalkylbladet innehåller formler är det bäst att ringa[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) precis innan den renderas till PDF. Detta säkerställer att formelberoende värden beräknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}
