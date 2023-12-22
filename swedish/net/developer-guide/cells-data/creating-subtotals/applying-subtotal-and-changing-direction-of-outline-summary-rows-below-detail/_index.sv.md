---
title: Tillämpa delsumma och ändra riktning på kontursammanfattningsraderna under detalj
type: docs
weight: 100
url: /sv/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Lär dig hur du tillämpar delsumma och ändrar riktning för kontursammanfattningen. Raderna nedan detalj genom att använda Aspose.Cells for .NET API.
keywords: Apply subtotal, Add subtotal, change direction of outline summary Rows below Detail, change direction of outline summary Columns to right of Detail, Create subtotal and change direction of outline summary Rows below Detail
---
{{% alert color="primary" %}}

Den här artikeln kommer att förklara hur du tillämpar delsumma på data och ändrar riktningen för översiktssammanfattningsraderna nedanför detalj.

 Du kan tillämpa delsumma på data med hjälp av[**Arbetsblad.Cells.Subtotal()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) metod. Den kräver följande parametrar.

- **CellArea** - Intervallet att tillämpa delsumma på
- **Grupp av** - Fältet att gruppera efter, som en nollbaserad heltalsoffset
- **Fungera** - Deltotalfunktionen.
- **Totallista** En matris med nollbaserade fältförskjutningar, som indikerar de fält till vilka delsummorna läggs till.
- **Byta ut** - Indikerar om de nuvarande delsummorna ersätts
- **Pagebreaks** - Anger om man lägger till sidbrytning mellan grupper
- **SammanfattningBelowData** - Indikerar om du lägger till sammanfattning under data.

 Du kan också styra riktningen för Outline**Sammanfattningsrader nedan detalj** som visas i följande skärmdump med egenskapen Worksheet.Outline.SummaryRowBelow. Du kan öppna den här inställningen i Microsoft Excel med**Data > Disposition > Inställningar**

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

##  Bilder av käll- och utdatafiler

Följande skärmdump visar källfilen för Excel som används i exempelkoden nedan som innehåller vissa data i kolumnerna A och B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Följande skärmdump visar den utgående Excel-filen som genereras av exempelkoden. Som du kan se har delsumman tillämpats på intervall A2:B11 och riktningen för konturen är sammanfattande rader under detalj.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## C# kod för att tillämpa delsumma och ändra riktningen för kontursammanfattningsrader

Här är exempelkoden för att uppnå utdata som visas ovan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
