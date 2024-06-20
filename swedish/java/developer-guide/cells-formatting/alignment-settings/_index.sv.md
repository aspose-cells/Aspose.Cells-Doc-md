---
title: Justeringsinställningar
type: docs
weight: 20
url: /sv/java/cells-alignment-settings/
---

## **Konfigurera justeringsinställningar**

## **Justeringsinställningar i Microsoft Excel**

Alla som har använt Microsoft Excel för att formatera celler kommer att vara bekanta med justeringsinställningarna i Microsoft Excel.

Som du kan se från figuren ovan, finns det olika typer av justeringsalternativ:

- Textjustering (horisontell & vertikal)
- Indrag.
- Orientering.
- Textkontroll.
- Textriktning.

Alla dessa justeringsinställningar stöds fullt ut av Aspose.Cells och diskuteras mer detaljerat nedan.

## **Justeringsinställningar i Aspose.Cells**

Aspose.Cells tillhandahåller [**GetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) och [**SetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle) metoder för klassen [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) som används för att få och ställa in en cells formatering. Klassen [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) tillhandahåller användbara egenskaper för att konfigurera justeringsinställningar.

Välj vilken som helst textjusteringstyp med hjälp av uppräkningen [**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype). De fördefinierade textjusteringstyperna i uppräkningen [**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) är:

|**Textjusteringstyper**|**Beskrivning**|
| :- | :- |
|Bottom|Representerar bottenjustering av text|
|Center|Representerar mittenjustering av text|
|CenterAcross|Representerar mittenöverjustering av text|
|Distributed|Representerar fördelad textjustering|
|Fill|Representerar fyll textjustering|
|General|Representerar generell textjustering|
|Justify|Representerar rättfärdig textjustering|
|Left|Representerar vänsterjustering av text|
|Right|Representerar högerjustering av text|
|Top|Representerar toppjustering av text|
|JustifiedLow|Justerar texten med en justerad kashida-längd för arabisk text.|
|ThaiDistributed|Distribuerar thailändsk text särskilt, eftersom varje tecken behandlas som ett ord.|

{{% alert color="primary" %}}

Du kan också tillämpa inställningen för rättfärdigad distribution med hjälp av egenskapen [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed).

{{% /alert %}}

## **Horisontell, vertikal justering och indrag**

Använd egenskapen [**HorizontalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment) för att justera texten horisontellt och egenskapen [**VerticalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment) för att justera texten vertikalt.
Det är möjligt att ställa in indelningsnivån för texten i en cell med hjälp av egenskapen [**IndentLevel**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel) 
och det påverkar endast när horisontell justering är vänster eller höger.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **Orientering**

Ställ in orienteringen (rotationen) för texten i en cell med hjälp av egenskapen [**RotationAngle**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **Textkontroll**

I följande avsnitt diskuteras hur man kontrollerar text genom att ställa in textbrytning, krympa till passa och andra formateringsalternativ.

### **Textindrag**

Textindrag i en cell gör det lättare att läsa: cellens höjd justeras för att passa all text istället för att klippa av den eller spilla över i intilliggande celler. Aktivera eller inaktivera textindrag med egenskapen [**IsTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **Krympa passande**

Ett alternativ till att göra textindrag i en cell är att minska textstorleken för att passa en cells dimensioner. Detta görs genom att ställa in egenskapen [**ShrinkToFit**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit) till **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **Sammanfoga celler**

Precis som Microsoft Excel stöder Aspose.Cells sammanfogning av flera celler till en. Aspose.Cells tillhandahåller två metoder för detta ändamål. Ett sätt är att anropa metoden [**Merge**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)). Metoden tar följande parametrar för att sammanfoga cellerna:

- Första rad: den första raden från vilken sammanfogningen ska börja.
- Första kolumn: den första kolumnen från vilken sammanfogningen ska börja.
- Antal rader: antalet rader att sammanfoga.
- Antal kolumner: antalet kolumner att sammanfoga.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **Textriktning**

Det är möjligt att ställa in läsordningen för text i celler. Läsordningen är den visuella ordningen där tecken, ord osv. visas. Till exempel är engelska ett vänster-till-höger-språk medan arabiska är ett höger-till-vänster-språk.

Läsordningen ställs in med egenskapen [**TextDirection**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection). Aspose.Cells tillhandahåller fördefinierade typer av textriktning i uppräkningen [**TextDirectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection).

|**Textriktningstyper**|**Beskrivning**|
| :- | :- |
|Context| Läsordningen som är konsekvent med språket för det första inmatade tecknet
|LeftToRight|Vänster till höger-läsordning
|RightToLeft|Höger till vänster-läsordning

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **Fortsatta ämnen**
- [Ändra cellers justering och behåll befintlig formatering](/cells/sv/java/change-cells-alignment-and-keep-existing-formatting/)
- [Radbrytningar och textindrag](/cells/sv/java/line-breaks-and-text-wrapping/)
