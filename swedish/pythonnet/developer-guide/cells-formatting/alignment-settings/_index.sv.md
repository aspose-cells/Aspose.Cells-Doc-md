---
title: Justeringsinställningar
description: I Aspose.Cells för Python via .NET biblioteket kan du använda celljusteringsinställningar för att justera layout och textvisning. Genom att justera inställningar som horisontell justering, vertikal justering och textbrytning, får du mer kontroll över hur texten flyter i cellerna. Detta dokument ger dig detaljerade steg och exempelkod för att snabbt förstå hur du använder Aspose.Cells för Python via .NET för celljusteringsinställningar.
keywords: Aspose.Cells för Python via .NET, celljustering, horisontell justering, vertikal justering, textbrytning
type: docs
weight: 20
url: /sv/python-net/cells-alignment-settings/
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

Alla dessa justeringsinställningar stöds fullt ut av Aspose.Cells för Python via .NET och diskuteras i mer detalj nedan.

### **Justeringar i Aspose.Cells för Python via .NET**

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) samling som ger tillgång till varje kalkylblad i filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) ger en [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) samling. Varje objekt i [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) samlingen representerar ett objekt av klassen [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells för Python via .NET tillhandahåller [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) och [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) metoder för klassen [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) som används för att få och sätta cellformattering. Klassen [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) ger användbara egenskaper för att konfigurera justeringsinställningar.

Välj vilken som helst textjusteringstyp med hjälp av uppräkningen [**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype). De fördefinierade textjusteringstyperna i uppräkningen [**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype) är:

|**Textjusteringstyper**|**Beskrivning**|
| :- | :- |
|GENERAL|Representerar generell textjustering|
|BOTTOM|Representerar botten-justering|
|CENTER|Representerar mittenjustering|
|CENTER_ACROSS|Representerar centrum över cellraden justering|
|DISTRIBUTED|Representerar distribuerad textjustering|
|FILL|Representerar fyllnadsjustering|
|JUSTIFY|Representerar justera textjustering|
|LEFT|Representerar vänsterjustering|
|RIGHT|Representerar högerjustering|
|TOP|Representerar toppjustering|
|JUSTIFIED_LOW|Justerar texten med anpassad kashida-längd för arabiska|
|THAI_DISTRIBUTED|Distribuerar thaitext särskilt, eftersom varje tecken behandlas som ett ord|

{{% alert color="primary" %}}

Du kan också tillämpa inställningen för rättfärdigad distribution med hjälp av egenskapen [**Style.is_justify_distributed**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_justify_distributed).

{{% /alert %}}

#### **Horisontell justering**

Använd [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) objektets [**horizontal_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/horizontal_alignment) egenskap för att justera texten horisontellt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.py" >}}

#### **Vertikal justering**

Liknande horisontell justering, använd [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) objektets [**vertical_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/vertical_alignment) egenskap för att justera texten vertikalt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.py" >}}

#### **Indrag**

Det är möjligt att ange indelningsnivån för texten i en cell med [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) objektets [**indent_level**](https://reference.aspose.com/cells/python-net/aspose.cells/style/indent_level) egenskap.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Indentation-1.py" >}}

#### **Orientering**

Ange orienteringen (rotationen) för texten i en cell med [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) objektets [**rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle) egenskap.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Orientation-1.py" >}}

#### **Textkontroll**

I följande avsnitt diskuteras hur man kontrollerar text genom att ställa in textbrytning, krympa till passa och andra formateringsalternativ.

##### **Textindrag**

Att rada text i en cell gör det lättare att läsa: cellens höjd justeras för att passa all text istället för att klippa av den eller få den att rinna över i intilliggande celler. Ange textombrytning på eller av med [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) objektets [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) egenskap.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

##### **Krympa passande**

Ett alternativ för att rada text i ett fält är att krympa textstorleken för att passa en cells dimensioner. Detta görs genom att ställa in [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) objektets [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) egenskap till **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.py" >}}

##### **Sammanfoga celler**

Precis som Microsoft Excel stöder Aspose.Cells för Python via .NET sammanslagning av flera celler till en. Aspose.Cells för Python via .NET erbjuder två tillvägagångssätt för detta. Ett sätt är att kalla [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) samlingen [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) metod. [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) metoden tar följande parametrar för att slå samman cellerna:

- Första rad: den första raden från vilken sammanfogningen ska börja.
- Första kolumn: den första kolumnen från vilken sammanfogningen ska börja.
- Antal rader: antalet rader att sammanfoga.
- Antal kolumner: antalet kolumner att sammanfoga.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Merging-MergingCellsInWorksheet.-1.py" >}}

Det andra sättet är att först anropa [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) samlingen [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) metod för att skapa en räckvidd av celler som ska sammanfogas. [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) metoden tar samma parametrar som [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) metoden som diskuterades ovan och returnerar ett [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) objekt. [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) objektet tillhandahåller också en [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge) metod som sammanfogar den angivna räckvidden i [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) objektet.

##### **Textriktning**

Det är möjligt att ställa in läsordningen för text i celler. Läsordningen är den visuella ordningen där tecken, ord osv. visas. Till exempel är engelska ett vänster-till-höger-språk medan arabiska är ett höger-till-vänster-språk.

 Läsordningen sätts med [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) objektets [**text_direction**](https://reference.aspose.com/cells/python-net/aspose.cells/style/text_direction) egenskap. Aspose.Cells för Python via .NET tillhandahåller fördefinierade textriktningstyper i [**TextDirectionType**](https://reference.aspose.com/cells/python-net/aspose.cells/textdirectiontype) uppräkningen.

|**Textriktningstyper**|**Beskrivning**|
| :- | :- |
|CONTEXT|Läsordningen är konsekvent med språket för den första tecknet som matas in|
|LEFT_TO_RIGHT|Läsordning från vänster till höger|
|RIGHT_TO_LEFT|Läsordning från höger till vänster|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeTextDirection-1.py" >}}

## **Fortsatta ämnen**
- [Ändra cellers justering och behåll befintlig formatering](/cells/sv/python-net/change-cells-alignment-and-keep-existing-formatting/)
- [Radbrytningar och textindrag](/cells/sv/python-net/line-breaks-and-text-wrapping/)


{{< app/cells/assistant language="python-net" >}}
