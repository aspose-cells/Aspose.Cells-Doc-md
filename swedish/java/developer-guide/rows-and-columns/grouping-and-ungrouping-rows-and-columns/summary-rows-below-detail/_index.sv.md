---
title: Tillämpa delsumma och ändra riktning på sammanfattning av sammanfattningsrader nedanför detaljer
type: docs
weight: 100
url: /sv/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---

{{% alert color="primary" %}}

Denna artikel förklarar hur du tillämpar delsumma på data och ändrar riktningen på sammanfattningsrader under detaljerna.

Du kan tillämpa delsumma på data med hjälp av [**Worksheet.Cells.subtotal()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal(com.aspose.cells.CellArea,%20int,%20int,%20int[])) metoden. Den tar följande parametrar.

- **CellArea** - Intervallet att tillämpa delsumma på
- **GroupBy** - Fältet som ska grupperas efter, som en nollbaserad heltalsförskjutning
- **Function** - Delsummeringsfunktionen.
- **TotalList** - En matris med nollbaserade fältförskjutningar som indikerar fälten som delsummorna läggs till.
- **Replace** - Indikerar om de nuvarande delsummorna ska ersättas
- **PageBreaks** - Indikerar om en sidbrytning ska läggas till mellan grupperna
- **SummaryBelowData** - Indikerar om en sammanfattning ska läggas till under datan.

Du kan också kontrollera riktningen på **Sammanfattningsrader nedanför detaljer** som visas i följande skärmbild med hjälp av egenskapen [**Worksheet.getOutline().SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow). Du kan öppna denna inställning i Microsoft Excel genom att använda **Data > Summering > Inställningar**

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Exempel

### Skärmbilder som jämför käll- och utdatafiler

Följande skärmbild visar den ursprungliga Excel-filen som används i den kodexempel nedan som innehåller några data i kolumnerna A och B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Följande skärmbild visar den genererade Excel-filen som utdata av kodexemplet. Som du kan se har delsumma tillämpats på intervallet **A2:B11** och riktningen på sammanfattningen är sammanfattningsrader nedanför detaljerna.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### Java-kod för att tillämpa delsumma och ändra riktning på sammanfattning av sammanfattande rader nedanför detaljerne

Här är kodexempel för att uppnå utdata som visas ovan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
