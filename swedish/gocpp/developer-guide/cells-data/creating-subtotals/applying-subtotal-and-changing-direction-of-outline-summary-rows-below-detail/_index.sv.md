---
title: Använda underavsnitt och ändra riktningen på översiktssammanfattningsrader under detaljer med Golang via C++
linktitle: Tillämpa delsumma och ändra riktning på sammanfattning av sammanfattningsrader nedanför detaljer
type: docs
weight: 100
url: /sv/go-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Lär dig hur man tillämpar subtotal och ändrar riktning på raderna för outline sammanfattning nedan detaljen med API et Aspose.Cells for C++.
keywords: Tillämpa delsumma, Lägg till delsumma, ändra riktning på summering underdetalj rader, ändra riktning på summering av summeringar underdetalj kolumner till höger om detalj, skapa delsumma och ändra riktning på summering underdetalj rader
---

{{% alert color="primary" %}}

Denna artikel förklarar hur man tillämpar Subtotal på data och ändrar riktningen på outline-sammanfattningsrader nedan detalj.

Du kan tillämpa Subtotal på data med metoden [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/go-cpp/cells/subtotal_cellarea_int_consolidationfunction_int32array/). Den tar följande parametrar:

- **CellArea** - Intervallet att tillämpa delsumma på
- **GroupBy** - Fältet som ska grupperas efter, som en nollbaserad heltalsförskjutning
- **Function** - Delsummeringsfunktionen.
- **TotalList** - En matris med nollbaserade fältförskjutningar som indikerar fälten som delsummorna läggs till.
- **Replace** - Anger om befintliga underrubriker ska ersättas
- **PageBreaks** - Anger om sidbrytningar ska läggas till mellan grupper
- **SummaryBelowData** - Anger om sammanfattning ska läggas till under data.

Du kan också kontrollera riktningen för outline **Sammanfattning under detalj** som visas i följande skärmbild med egenskapen `Worksheet.Outline.SummaryRowBelow`. Du kan öppna denna inställning i Microsoft Excel via **Data > Outline > Inställningar**.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Bilder av käll- och utdatafiler

Följande skärmbild visar den ursprungliga Excel-filen som används i den kodexempel nedan som innehåller några data i kolumnerna A och B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Följande skärmbild visar den genererade Excel-filen som skapats av provkoden. Som du kan se har subtotalen tillämpats på intervall A2:B11 och riktningen på översikten är sammanfattningar av rader under detaljer.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## C++-kod för att tillämpa subtotal och ändra riktning på outline-sammanfattningsrader

Här är kodexempel för att uppnå utdata som visas ovan.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyingSubtotalAndChangingDirectionOfOutlineSummaryRowsBelowDetail.go" >}}
