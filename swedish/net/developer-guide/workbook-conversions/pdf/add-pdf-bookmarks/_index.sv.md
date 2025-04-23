---
title: Lägg till PDF bokmärken
type: docs
weight: 10
url: /sv/net/add-pdf-bookmarks/
---

{{% alert color="primary" %}}

Denna artikel ger information om hur man lägger till PDF-bokmärken när man konverterar en kalkyl till PDF.

Aspose.Cells låter dig lägga till bokmärken på språng. PDF-bokmärken kan markant förbättra navigeringen i långa dokument. När du lägger till bokmärkeslänkar till PDF-dokumentet kan du ha exakt kontroll över exakt vy du vill, du är inte begränsad till att länka till en sida. Du kan ställa in den exakta vyn genom att placera målsidan och sedan skapa bokmärket.

{{% /alert %}}

Se det följande kodexemplet för att se hur man lägger till PDF-bokmärken. Koden genererar en enkel arbetsbok, specificerar PDF-bokmärken med destinationsplatser och genererar PDF-filen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddPDFBookmarks-1.cs" >}}

{{% alert color="primary" %}}

Om din kalkylblad har formler är det bäst att anropa [**Workbook.CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) precis innan du renderar kalkylbladet i PDF-format. På så sätt säkerställs det att de formelberoende värdena uppdateras och renderas korrekt i PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
