---
title: Lägg till PDF bokmärken
type: docs
weight: 10
url: /sv/python-net/add-pdf-bookmarks/
description: Lär dig hur du lägger till pdf bokmärken med Aspose.Cells for Python via .NET API.
keywords: Python lägger till pdf bokmärken, lägger till pdf bokmärken Pyton via NET, sätter in pdf bokmärken
---

{{% alert color="primary" %}}

Denna artikel ger information om hur man lägger till PDF-bokmärken när man konverterar en kalkyl till PDF.

Aspose.Cells for Python via .NET gör att du kan lägga till bokmärken på flygande fot. PDF-bokmärken kan dramatiskt förbättra navigeringen i långa dokument. När du lägger till bokmärkeslänkar till PDF-dokument kan du ha precis kontroll över den exakta vy du vill ha, du är inte begränsad till att länka till en sida. Du kan ställa in den exakta vyn genom att positionera målsidan och sedan skapa bokmärket.

{{% /alert %}}

Se det följande kodexemplet för att se hur man lägger till PDF-bokmärken. Koden genererar en enkel arbetsbok, specificerar PDF-bokmärken med destinationsplatser och genererar PDF-filen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AddPDFBookmarks-1.py" >}}

{{% alert color="primary" %}}

Om din kalkylblad har formler är det bäst att anropa [**Workbook.calculate_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) precis innan du renderar kalkylbladet i PDF-format. På så sätt säkerställs det att de formelberoende värdena uppdateras och renderas korrekt i PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
