---
title: Säkra PDF Dokument
type: docs
weight: 120
url: /sv/net/secure-pdf-documents/
---
{{% alert color="primary" %}}

Ibland måste utvecklare arbeta med krypterade PDF-filer. De behöver till exempel säkra dokument med användar- och ägarlösenord så att inte vem som helst kan öppna dem, eller vill begränsa om dokumentinnehållet kan skrivas ut eller extraheras.

Den här artikeln förklarar hur du skickar in PDF säkerhetsalternativ när du sparar kalkylark till PDF.

{{% /alert %}}

 Aspose.Cells tillhandahåller[**Aspose.Cells.Rendering.PdfSecurity**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity) namnutrymme för att arbeta med säkerhet. Exempelkoden nedan beskriver hur du säkrar PDF-filer med Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

 Om kalkylbladet innehåller formler är det bäst att ringa[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)precis innan den renderas till PDF. Detta säkerställer att formelberoende värden beräknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}
