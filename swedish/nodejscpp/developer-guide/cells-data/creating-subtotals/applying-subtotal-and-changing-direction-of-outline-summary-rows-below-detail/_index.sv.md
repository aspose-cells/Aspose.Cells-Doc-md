---
title: Tillämpa delsumma och ändra riktning på sammanfattning av sammanfattningsrader nedanför detaljer
type: docs
weight: 100
url: /sv/nodejs-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Lär dig hur man tillämpar subtotal och ändrar riktningen på outline summeringsrader under detaljer genom att använda API et Aspose.Cells for Node.js via C++.
keywords: Tillämpa delsumma, Lägg till delsumma, ändra riktning på summering underdetalj rader, ändra riktning på summering av summeringar underdetalj kolumner till höger om detalj, skapa delsumma och ändra riktning på summering underdetalj rader
---

{{% alert color="primary" %}}

Denna artikel förklarar hur du tillämpar delsumma på data och ändrar riktningen på sammanfattningsrader under detaljerna.

Du kan tillämpa delsumma på data med hjälp av [**Worksheet.getCells().subtotal()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-boolean-boolean-boolean-) metoden. Den tar följande parametrar.

- **CellArea** - Intervallet att tillämpa delsumma på
- **GroupBy** - Fältet som ska grupperas efter, som en nollbaserad heltalsförskjutning
- **Function** - Delsummeringsfunktionen.
- **TotalList** - En matris med nollbaserade fältförskjutningar som indikerar fälten som delsummorna läggs till.
- **Replace** - Indikerar om de nuvarande delsummorna ska ersättas
- **Sidbrytningar** - Indikerar om man ska lägga till sidbrytning mellan grupper
- **SummaryBelowData** - Indikerar om en sammanfattning ska läggas till under datan.

Du kan också styra riktningen för översiktsrader under detaljer som visas i följande skärmbild med hjälp av Worksheet.Outline.SummaryRowBelow-egenskapen. Du kan öppna denna inställning i Microsoft Excel med **Data > Översikt > Inställningar**

![todo:image_alt_text](1.png)

{{% /alert %}}

## Bilder av käll- och utdatafiler

Följande skärmbild visar den ursprungliga Excel-filen som används i den kodexempel nedan som innehåller några data i kolumnerna A och B.

![todo:image_alt_text](2.png)

Följande skärmbild visar den genererade Excel-filen som skapats av provkoden. Som du kan se har subtotalen tillämpats på intervall A2:B11 och riktningen på översikten är sammanfattningar av rader under detaljer.

![todo:image_alt_text](3.png)

## Node.js för att tillämpa subtotal och ändra riktningen på outline-summeringsrader

Här är kodexempel för att uppnå utdata som visas ovan.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-ApplyingSubtotalChangeSummaryDirection-1.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
