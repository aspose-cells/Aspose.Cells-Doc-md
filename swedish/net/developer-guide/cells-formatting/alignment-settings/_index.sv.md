---
title: Justeringsinställningar
description: I Aspose.Cells biblioteket kan du använda celljusteringsinställningar för att justera layouten och visningen av text. Genom att justera inställningar som horisontell justering, vertikal justering och textradbrytning har du mer kontroll över hur text flödar i celler. Detta dokument ger dig detaljerade steg och kodexempel för att snabbt lära dig hur du använder Aspose.Cells för celljusteringsinställningar.
keywords: Aspose.Cells, celljustering, horisontell justering, vertikal justering, textombrytning
type: docs
weight: 20
url: /sv/net/cells-alignment-settings/
---

## **Konfigurera justeringsinställningar**

### **Justeringsinställningar i Microsoft Excel**

Alla som har använt Microsoft Excel för att formatera celler kommer att vara bekanta med justeringsinställningarna i Microsoft Excel.

Som du kan se från figuren ovan, finns det olika typer av justeringsalternativ:

- Textjustering (horisontell & vertikal)
- Indrag.
- Orientering.
- Textkontroll.
- Textriktning.

Alla dessa justeringsinställningar stöds fullt ut av Aspose.Cells och diskuteras mer detaljerat nedan.

### **Justeringsinställningar i Aspose.Cells**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som tillåter åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassen. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) klassen.

Aspose.Cells tillhandahåller [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) och [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) metoder för klassen [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) som används för att få och ställa in en cells formatering. Klassen [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) tillhandahåller användbara egenskaper för att konfigurera justeringsinställningar.

Välj vilken som helst textjusteringstyp med hjälp av uppräkningen [**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype). De fördefinierade textjusteringstyperna i uppräkningen [**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) är:

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

Du kan också tillämpa inställningen för rättfärdigad distribution med hjälp av egenskapen [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed).

{{% /alert %}}

#### **Horisontell justering**

Använd [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objektets [**HorizontalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment) egenskap för att justera texten horisontellt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

#### **Vertikal justering**

Liknande horisontell justering, använd [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objektets [**VerticalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment) egenskap för att justera texten vertikalt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

#### **Indrag**

Det är möjligt att ange indelningsnivån för texten i en cell med [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objektets [**IndentLevel**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel) egenskap.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

#### **Orientering**

Ange orienteringen (rotationen) för texten i en cell med [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objektets [**RotationAngle**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle) egenskap.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

#### **Textkontroll**

I följande avsnitt diskuteras hur man kontrollerar text genom att ställa in textbrytning, krympa till passa och andra formateringsalternativ.

##### **Textindrag**

Att rada text i en cell gör det lättare att läsa: cellens höjd justeras för att passa all text istället för att klippa av den eller få den att rinna över i intilliggande celler. Ange textombrytning på eller av med [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objektets [**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) egenskap.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##### **Krympa passande**

Ett alternativ för att rada text i ett fält är att krympa textstorleken för att passa en cells dimensioner. Detta görs genom att ställa in [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objektets [**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) egenskap till **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

##### **Sammanfoga celler**

Liksom Microsoft Excel stöder Aspose.Cells att sammanfoga flera celler till en. Aspose.Cells tillhandahåller två tillvägagångssätt för denna uppgift. Ett sätt är att anropa [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samlingen [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) metod. [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) metoden tar följande parametrar för att sammanfoga cellerna:

- Första rad: den första raden från vilken sammanfogningen ska börja.
- Första kolumn: den första kolumnen från vilken sammanfogningen ska börja.
- Antal rader: antalet rader att sammanfoga.
- Antal kolumner: antalet kolumner att sammanfoga.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

Det andra sättet är att först anropa [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samlingen [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) metod för att skapa en räckvidd av celler som ska sammanfogas. [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) metoden tar samma parametrar som [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) metoden som diskuterades ovan och returnerar ett [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) objekt. [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) objektet tillhandahåller också en [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) metod som sammanfogar den angivna räckvidden i [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) objektet.

##### **Textriktning**

Det är möjligt att ställa in läsordningen för text i celler. Läsordningen är den visuella ordningen där tecken, ord osv. visas. Till exempel är engelska ett vänster-till-höger-språk medan arabiska är ett höger-till-vänster-språk.

Läsordningen ställs in med [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objektets [**TextDirection**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) egenskap. Aspose.Cells tillhandahåller fördefinierade textriktningstyper i [**TextDirectionType**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype) uppräkning.

|**Textriktningstyper**|**Beskrivning**|
| :- | :- |
|Context| Läsordningen som är konsekvent med språket för det första inmatade tecknet
|LeftToRight|Vänster till höger-läsordning
|RightToLeft|Höger till vänster-läsordning

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

## **Fortsatta ämnen**
- [Ändra cellers justering och behåll befintlig formatering](/cells/sv/net/change-cells-alignment-and-keep-existing-formatting/)
- [Radbrytningar och textindrag](/cells/sv/net/line-breaks-and-text-wrapping/)

