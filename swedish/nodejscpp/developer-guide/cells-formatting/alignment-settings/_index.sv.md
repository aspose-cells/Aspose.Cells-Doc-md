---
title: Justeringsinställningar
linktitle: Justeringsinställningar
description: I Aspose.Cells biblioteket kan du använda celljusteringsinställningar för att justera layouten och visningen av text med Node.js via C++. Detta dokument ger detaljerade steg och exempel på kod för att använda Aspose.Cells för celljustering.
keywords: Aspose.Cells, celljustering, horisontell justering, vertikal justering, textomslag Node.js via C++
type: docs
weight: 20
url: /sv/nodejs-cpp/cells-alignment-settings/
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

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen tillhandahåller en [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassen.

Aspose.Cells tillhandahåller [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) och [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)-metoder för [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassen som används för att hämta och ställa in cellformat. [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-klassen ger användbara egenskaper för att konfigurera justeringsinställningar.

Välj vilken textjusteringstyp som helst med hjälp av [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype)-uppräkningslistan. De fördefinierade textjusteringstyperna i [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype)-uppräkningslistan är:

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

Du kan också tillämpa det justerade fördelade inställningen med hjälp av [**Style.setIsJustifyDistributed(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsJustifyDistributed-boolean-)-metoden.

{{% /alert %}}

#### **Horisontell justering**

Använd [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektets [**setHorizontalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setHorizontalAlignment-textalignmenttype-)-metod för att justera texten horisontellt.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-HorizontalAlignment.js" >}}



#### **Vertikal justering**

Liknande horisontell justering, använd [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektets [**setVerticalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setVerticalAlignment-textalignmenttype-)-metod för att justera texten vertikalt.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-VerticalAlignment.js" >}}


#### **Indrag**

Det är möjligt att ställa in indentationsnivån för texten i en cell med hjälp av [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektets [**setIndentLevel**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIndentLevel-number-)-metod.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Indentation.js" >}}



#### **Orientering**

Ställ in orienteringen (rotation) av texten i en cell med hjälp av [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektets [**setRotationAngle**](https://reference.aspose.com/cells/nodejs-cpp/style/#setRotationAngle-number-)-metod.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Orientation.js" >}}

#### **Textkontroll**

I följande avsnitt diskuteras hur man kontrollerar text genom att ställa in textbrytning, krympa till passa och andra formateringsalternativ.

##### **Textindrag**

Omslag av text i en cell gör det lättare att läsa: cellens höjd anpassar sig för att passa all text, istället för att klippa av den eller spilla över i angränsande celler. Aktivera eller inaktivera textomslag med hjälp av [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektets [**setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-)-metod.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapText.js" >}}


##### **Krympa passande**

Ett alternativ för textomslag i ett fält är att krympa teckenstorleken för att passa cellens dimensioner. Detta görs genom att ställa in [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektets [**setShrinkToFit(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setShrinkToFit-boolean-)-metod till **true**.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ShrinkToFit.js" >}}


##### **Sammanfoga celler**

Liksom Microsoft Excel, stöder Aspose.Cells att slå samman flera celler till en. Aspose.Cells erbjuder två tillvägagångssätt för detta. Ett sätt är att anropa [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-)-metod. [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-)-metoden tar följande parametrar för att slå samman cellerna:

- Första rad: den första raden från vilken sammanfogningen ska börja.
- Första kolumn: den första kolumnen från vilken sammanfogningen ska börja.
- Antal rader: antalet rader att sammanfoga.
- Antal kolumner: antalet kolumner att sammanfoga.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-MergeCells.js" >}}


Det andra sättet är att först anropa [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-)-metod för att skapa ett område av celler att slå samman. [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-)-metoden tar samma uppsättning parametrar som den ovan diskuterade [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-)-metoden och returnerar ett [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)-objekt. [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)-objektet tillhandahåller också en [**merge**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--)-metod som slår samman det angivna området i [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)-objektet.

##### **Textriktning**

Det är möjligt att ställa in läsordningen för text i celler. Läsordningen är den visuella ordningen där tecken, ord osv. visas. Till exempel är engelska ett vänster-till-höger-språk medan arabiska är ett höger-till-vänster-språk.

Läsordningen ställs in med [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektets [**TextDirection**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTextDirection-textdirectiontype-)-egenskap. Aspose.Cells tillhandahåller fördefinierade textriktningstyper i [**TextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/textdirectiontype)-uppräkningslistan.

|**Textriktningstyper**|**Beskrivning**|
| :- | :- |
|Context| Läsordningen som är konsekvent med språket för det första inmatade tecknet
|LeftToRight|Vänster till höger-läsordning
|RightToLeft|Höger till vänster-läsordning

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-TextDirection.js" >}}


## **Fortsatta ämnen**
- [Ändra cellers justering och behåll befintlig formatering](/cells/sv/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Radbrytningar och textindrag](/cells/sv/nodejs-cpp/line-breaks-and-text-wrapping/)

{{< app/cells/assistant language="nodejs-cpp" >}}
