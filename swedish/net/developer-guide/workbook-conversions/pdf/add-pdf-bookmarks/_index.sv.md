---
title: Lägg till PDF Bokmärken
type: docs
weight: 10
url: /sv/net/add-pdf-bookmarks/
---
{{% alert color="primary" %}}

Den här artikeln innehåller information om hur du infogar PDF-bokmärken när du konverterar ett kalkylblad till PDF.

Aspose.Cells låter dig lägga till bokmärken i farten. PDF bokmärken kan drastiskt förbättra navigerbarheten för långa dokument. När du lägger till bokmärkeslänkar till PDF dokument kan du ha exakt kontroll över den exakta vy du vill ha, du är inte begränsad till att länka till en sida. Du kan ställa in den exakta vyn genom att placera målsidan och sedan skapa bokmärket.

{{% /alert %}}

Se följande exempelkod för att ta reda på hur du lägger till PDF-bokmärken. Koden genererar en enkel arbetsbok, anger PDF-bokmärken med destinationsplatser och genererar PDF-filen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddPDFBookmarks-1.cs" >}}

{{% alert color="primary" %}}

Om ditt kalkylblad har formler är det bäst att ringa[**Arbetsbok. BeräknaFormel**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) precis innan du renderar kalkylarket till formatet PDF. Om du gör det säkerställer du att de formelberoende värdena uppdateras och återges korrekt i PDF.

{{% /alert %}}
