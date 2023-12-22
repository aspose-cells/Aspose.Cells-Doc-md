---
title: Lägg till PDF Bokmärken
type: docs
weight: 10
url: /sv/python-net/add-pdf-bookmarks/
description: Lär dig hur du lägger till pdf-bokmärken med Aspose.Cells for Python via .NET API.
keywords: Python add pdf bookmarks, add pdf book marks Pyton via NET, insert pdf bookmarks
---
{{% alert color="primary" %}}

Den här artikeln innehåller information om hur du infogar PDF-bokmärken när du konverterar ett kalkylblad till PDF.

Aspose.Cells for Python via .NET låter dig lägga till bokmärken i farten. PDF bokmärken kan drastiskt förbättra navigerbarheten för långa dokument. När du lägger till bokmärkeslänkar till PDF dokument kan du ha exakt kontroll över den exakta vy du vill ha, du är inte begränsad till att länka till en sida. Du kan ställa in den exakta vyn genom att placera målsidan och sedan skapa bokmärket.

{{% /alert %}}

Se följande exempelkod för att ta reda på hur du lägger till PDF-bokmärken. Koden genererar en enkel arbetsbok, anger PDF-bokmärken med destinationsplatser och genererar PDF-filen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AddPDFBookmarks-1.py" >}}

{{% alert color="primary" %}}

 Om ditt kalkylblad har formler är det bäst att ringa[**Workbook.calculate_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) precis innan du renderar kalkylarket till formatet PDF. Om du gör det säkerställer du att de formelberoende värdena uppdateras och återges korrekt i PDF.

{{% /alert %}}
