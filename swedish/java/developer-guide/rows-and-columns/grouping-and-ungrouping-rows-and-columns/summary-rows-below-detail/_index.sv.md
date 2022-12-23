---
title: Tillämpa delsumma och ändra riktning på kontursammanfattningsraderna under detalj
type: docs
weight: 100
url: /sv/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---
{{% alert color="primary" %}}

Den här artikeln kommer att förklara hur du tillämpar delsumma på data och ändrar riktningen för översiktssammanfattningsraderna nedanför detalj.

 Du kan tillämpa delsumma på data med hjälp av[**Arbetsblad.Cells.subtotal()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal(com.aspose.cells.CellArea,%20int,%20int,%20int[])) metod. Den kräver följande parametrar.

- **CellArea** Intervallet att tillämpa delsumma på
- **Grupp av** - Fältet att gruppera efter, som en nollbaserad heltalsoffset
- **Fungera** - Deltotalfunktionen.
- **Totallista** - En matris med nollbaserade fältförskjutningar, som indikerar de fält till vilka delsummorna läggs till.
- **Byta ut** - Indikerar om de nuvarande delsummorna ersätts
- **Pagebreaks** - Anger om du lägger till en sidbrytning mellan grupper
- **SammanfattningBelowData** - Indikerar om du lägger till sammanfattning under data.

 Du kan också styra riktningen för Outline**Sammanfattningsrader nedan detalj** som visas i följande skärmdump med hjälp av[**Worksheet.getOutline().SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) fast egendom. Du kan öppna den här inställningen i Microsoft Excel med**Data > Disposition > Inställningar**

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Exempel

### Skärmdumpar som jämför käll- och utdatafiler

Följande skärmdump visar källfilen för Excel som används i exempelkoden nedan som innehåller vissa data i kolumnerna A och B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Följande skärmdump visar den utgående Excel-filen som genereras av exempelkoden. Som du kan se har delsumman tillämpats på intervallet**A2:B11** och konturens riktning är sammanfattningsrader under detaljen.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### Java-kod för att tillämpa delsumma och ändra riktning för kontursammanfattningsraderna nedanför detalj

Här är exempelkoden för att uppnå utdata som visas ovan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
