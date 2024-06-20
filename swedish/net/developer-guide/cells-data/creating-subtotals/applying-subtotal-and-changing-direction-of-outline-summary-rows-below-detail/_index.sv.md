---
title: Tillämpa delsumma och ändra riktning på sammanfattning av sammanfattningsrader nedanför detaljer
type: docs
weight: 100
url: /sv/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Lär dig hur man tillämpar delsumma och ändrar riktning på summering underdetalj rader genom att använda API et Aspose.Cells for .NET.
keywords: Tillämpa delsumma, Lägg till delsumma, ändra riktning på summering underdetalj rader, ändra riktning på summering av summeringar underdetalj kolumner till höger om detalj, skapa delsumma och ändra riktning på summering underdetalj rader
---

{{% alert color="primary" %}}

Denna artikel förklarar hur du tillämpar delsumma på data och ändrar riktningen på sammanfattningsrader under detaljerna.

Du kan tillämpa delsumma på data med hjälp av [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) metoden. Den tar följande parametrar.

- **CellArea** - Intervallet att tillämpa delsumma på
- **GroupBy** - Fältet som ska grupperas efter, som en nollbaserad heltalsförskjutning
- **Function** - Delsummeringsfunktionen.
- **TotalList** - En matris med nollbaserade fältförskjutningar som indikerar fälten som delsummorna läggs till.
- **Replace** - Indikerar om de nuvarande delsummorna ska ersättas
- **Sidbrytningar** - Indikerar om man ska lägga till sidbrytning mellan grupper
- **SummaryBelowData** - Indikerar om en sammanfattning ska läggas till under datan.

Du kan också styra riktningen för översiktsrader under detaljer som visas i följande skärmbild med hjälp av Worksheet.Outline.SummaryRowBelow-egenskapen. Du kan öppna denna inställning i Microsoft Excel med **Data > Översikt > Inställningar**

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Bilder av käll- och utdatafiler

Följande skärmbild visar den ursprungliga Excel-filen som används i den kodexempel nedan som innehåller några data i kolumnerna A och B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Följande skärmbild visar den genererade Excel-filen som skapats av provkoden. Som du kan se har subtotalen tillämpats på intervall A2:B11 och riktningen på översikten är sammanfattningar av rader under detaljer.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## C#-kod för att tillämpa delsumma och ändra riktning av summering underdetalj- rader

Här är kodexempel för att uppnå utdata som visas ovan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
