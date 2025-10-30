---
title: Tillämpa delsumma och ändra riktning på sammanfattning av sammanfattningsrader nedanför detaljer
type: docs
weight: 100
url: /sv/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Lär dig hur du tillämpar subtotal och ändrar riktningen för översiktsammanfattningen av rader under detaljer med hjälp av Aspose.Cells för Python via .NET API.
keywords: Python Excel bibliotek, Tillämpa subtotal, Lägg till subtotal, ändra riktningen för översiktsammanfattning av rader under detaljer, ändra riktningen för översiktsammanfattning av kolumner till höger om detaljer, Skapa subtotal och ändra riktningen för översiktsammanfattning av rader under detaljer
---

{{% alert color="primary" %}}

Denna artikel förklarar hur du tillämpar delsumma på data och ändrar riktningen på sammanfattningsrader under detaljerna.

Du kan tillämpa delsumma på data med hjälp av [**Worksheet.cells.subtotal()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list-bool-bool-bool) metoden. Den tar följande parametrar.

- **ca** - Intervallet att tillämpa subtotal på
- **group_by** - Fältet att gruppera efter, som en nollbaserad heltalsförskjutning
- **function** - Subtotalfunktionen
- **total_list** - En array med nollbaserade fältavvikelser, som anger fälten till vilka subtotals läggs till
- **replace** - Indikerar om du ska byta ut nuvarande subtotals
- **page_breaks** - Indikerar om du ska lägga till sidbrytningar mellan grupper
- **summary_below_data** - Indikerar om du ska lägga till sammanfattning nedanför datan

Du kan också styra riktningen för översiktsrader under detaljer som visas i följande skärmbild med hjälp av Worksheet.Outline.SummaryRowBelow-egenskapen. Du kan öppna denna inställning i Microsoft Excel med **Data > Översikt > Inställningar**

![todo:image_alt_text](1.png)

{{% /alert %}}

## **Bilder på käll- och utmatningsfiler**

Följande skärmbild visar den ursprungliga Excel-filen som används i den kodexempel nedan som innehåller några data i kolumnerna A och B.

![todo:image_alt_text](2.png)

Följande skärmbild visar den genererade Excel-filen som skapats av provkoden. Som du kan se har subtotalen tillämpats på intervall A2:B11 och riktningen på översikten är sammanfattningar av rader under detaljer.

![todo:image_alt_text](3.png)

## **Python-kod för att tillämpa subtotal och ändra riktningen på översiktsammnafattning av rader**

Här är kodexempel för att uppnå utdata som visas ovan.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyingSubtotalChangeSummaryDirection-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
