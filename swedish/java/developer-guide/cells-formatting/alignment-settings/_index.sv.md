---
title: Justeringsinställningar
type: docs
weight: 20
url: /sv/java/cells-alignment-settings/
---
## **Konfigurera justeringsinställningar**

## **Justeringsinställningar i Microsoft Excel**

Alla som har använt Microsoft Excel för att formatera celler kommer att känna till justeringsinställningarna i Microsoft Excel.

Som du kan se från ovanstående figur finns det olika typer av justeringsalternativ:

- Textjustering (horisontell och vertikal)
- Indrag.
- Orientering.
- Textkontroll.
- Textriktning.

Alla dessa justeringsinställningar stöds fullt ut av Aspose.Cells och diskuteras mer i detalj nedan.

## **Justeringsinställningar i Aspose.Cells**

 Aspose.Cells tillhandahåller[**GetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) och[**SetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle) metoder för[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) klass som används för att hämta och ställa in en cells formatering. De[**Stil**](https://reference.aspose.com/cells/java/com.aspose.cells/style)klass tillhandahåller användbara egenskaper för att konfigurera justeringsinställningar.

 Välj valfri textjusteringstyp med hjälp av[**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) uppräkning. De fördefinierade textjusteringstyperna i[**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype)uppräkning är:

|**Typer av textjustering**|**Beskrivning**|
|:- |:- |
|Botten|Representerar nedre textjustering|
|Centrum|Representerar centrerad textjustering|
|CenterAcross|Representerar mitten över textjusteringen|
|Distribuerad|Representerar distribuerad textjustering|
|Fylla|Representerar fyllningstextjustering|
|Allmän|Representerar allmän textjustering|
|Rättfärdiga|Representerar justera textjustering|
|Vänster|Representerar vänster textjustering|
|Rätt|Representerar höger textjustering|
|Topp|Representerar topptextjustering|
|JustifiedLow|Justerar texten med en justerad kashida-längd för arabisk text.|
|ThaiDistribuerat|Distribuerar thailändsk text speciellt, eftersom varje tecken behandlas som ett ord.|

{{% alert color="primary" %}}

 Du kan också använda inställningen för att motivera distribuerad med hjälp av[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed) fast egendom.

{{% /alert %}}

## **Horisontell, vertikal inriktning och indrag**

 Använd[**Horisontell linjering**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment) egenskap för att justera texten horisontellt och[**Vertical Alignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment)egenskap för att justera texten vertikalt.
 Det är möjligt att ställa in indragsnivån för texten i en cell med[**IndentLevel**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel) fast egendom
och tt påverkar endast när horisontell justering är vänster eller höger.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **Orientering**

 Ställ in orienteringen (rotationen) för texten i en cell med[**Rotations vinkel**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle)fast egendom.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **Textkontroll**

Följande avsnitt diskuterar hur man kontrollerar text genom att ställa in textbrytning, krympa för att passa och andra formateringsalternativ.

### **Radbrytande text**

 Radbrytning av text i en cell gör det lättare att läsa: cellens höjd justeras för att passa all text, istället för att klippa av den eller spilla över i intilliggande celler. Slå på eller av textbrytning med[**IsTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)fast egendom.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **Krymper för att passa**

 Ett alternativ för att radbryta text i ett fält är att krympa textstorleken så att den passar en cells dimensioner. Detta görs genom att ställa in[**Krymp för att passa**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit) fast egendom. till**Sann**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **Slår ihop Cells**

 Liksom Microsoft Excel stöder Aspose.Cells sammanslagning av flera celler till en. Aspose.Cells ger två tillvägagångssätt för denna uppgift. Ett sätt är att ringa till[**Sammanfoga**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) metod. Metoden använder följande parametrar för att slå samman cellerna:

- Första raden: den första raden varifrån man ska börja sammanfoga.
- Första kolumnen: den första kolumnen varifrån sammanslagningen ska börja.
- Antal rader: antalet rader som ska sammanfogas.
- Antal kolumner: antalet kolumner som ska sammanfogas.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **Textriktning**

Det är möjligt att ställa in läsordningen för text i celler. Läsordningen är den visuella ordning i vilken tecken, ord etc. visas. Till exempel är engelska ett språk från vänster till höger medan arabiska är ett språk från höger till vänster.

 Läsordningen ställs in med[**TextDirection**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection) fast egendom. Aspose.Cells tillhandahåller fördefinierade textriktningstyper i[**TextDirectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection)uppräkning.

|**Textriktningstyper**|**Beskrivning**|
|:- |:- |
|Sammanhang|Läsordningen överensstämmer med språket för det först inmatade tecknet|
|Vänster till höger|Vänster till höger läsordning|
|Höger till vänster|Läsordning från höger till vänster|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **Förhandsämnen**
- [Ändra Cells Justering och behåll befintlig formatering](/cells/sv/java/change-cells-alignment-and-keep-existing-formatting/)
- [Radbrytningar och textbrytning](/cells/sv/java/line-breaks-and-text-wrapping/)
