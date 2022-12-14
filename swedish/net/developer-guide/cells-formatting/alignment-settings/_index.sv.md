---
title: Justeringsinställningar
type: docs
weight: 20
url: /sv/net/cells-alignment-settings/
---
## **Konfigurera justeringsinställningar**

### **Justeringsinställningar i Microsoft Excel**

Alla som har använt Microsoft Excel för att formatera celler kommer att känna till justeringsinställningarna i Microsoft Excel.

Som du kan se från ovanstående figur finns det olika typer av justeringsalternativ:

- Textjustering (horisontell och vertikal)
- Indrag.
- Orientering.
- Textkontroll.
- Textriktning.

Alla dessa justeringsinställningar stöds fullt ut av Aspose.Cells och diskuteras mer i detalj nedan.

### **Justeringsinställningar i Aspose.Cells**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samling. Varje objekt i[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samlingen representerar ett föremål för[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)klass.

 Aspose.Cells tillhandahåller[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) och[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) metoder för[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) klass som används för att hämta och ställa in en cells formatering. De[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)klass tillhandahåller användbara egenskaper för att konfigurera justeringsinställningar.

 Välj valfri textjusteringstyp med hjälp av[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) uppräkning. De fördefinierade textjusteringstyperna i[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)uppräkning är:

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
|Höger|Representerar höger textjustering|
|Topp|Representerar topptextjustering|
|JustifiedLow|Justerar texten med en justerad kashida-längd för arabisk text.|
|ThaiDistribuerat|Distribuerar thailändsk text speciellt, eftersom varje tecken behandlas som ett ord.|

{{% alert color="primary" %}}

 Du kan också använda inställningen för att motivera distribuerad med hjälp av[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed) fast egendom.

{{% /alert %}}

#### **Horisontell linjering**

 Använd[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt[**Horisontell linjering**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment)egenskap för att justera texten horisontellt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

#### **Vertikal inriktning**

 I likhet med horisontell justering, använd[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt[**Vertical Alignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment)egenskap för att justera texten vertikalt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

#### **Indrag**

 Det är möjligt att ställa in indragsnivån för texten i en cell med[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt[**IndentLevel**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel)fast egendom.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

#### **Orientering**

 Ställ in orienteringen (rotationen) för texten i en cell med[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt[**Rotations vinkel**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle)fast egendom.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

#### **Textkontroll**

Följande avsnitt diskuterar hur man kontrollerar text genom att ställa in textbrytning, krympa för att passa och andra formateringsalternativ.

##### **Radbrytande text**

 Radbrytning av text i en cell gör det lättare att läsa: cellens höjd justeras för att passa all text, istället för att klippa av den eller spilla över i intilliggande celler. Slå på eller av textbrytning med[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)fast egendom.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##### **Krymper för att passa**

 Ett alternativ för att radbryta text i ett fält är att krympa textstorleken så att den passar en cells dimensioner. Detta görs genom att ställa in[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) egendom till**Sann**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

##### **Slår ihop Cells**

 Liksom Microsoft Excel stöder Aspose.Cells sammanslagning av flera celler till en. Aspose.Cells ger två tillvägagångssätt för denna uppgift. Ett sätt är att ringa till[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samlingens[**Sammanfoga**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) metod. De[**Sammanfoga**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)Metoden använder följande parametrar för att slå samman cellerna:

- Första raden: den första raden varifrån man ska börja sammanfoga.
- Första kolumnen: den första kolumnen varifrån sammanslagningen ska börja.
- Antal rader: antalet rader som ska sammanfogas.
- Antal kolumner: antalet kolumner som ska sammanfogas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

 Det andra sättet är att först ringa till[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samlingens[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) metod för att skapa ett område av cellerna som ska slås samman. De[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) metoden tar samma uppsättning parametrar som den för[**Sammanfoga**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) metod som diskuterats ovan och returnerar en[**Räckvidd**](https://reference.aspose.com/cells/net/aspose.cells/range) objekt. De[**Räckvidd**](https://reference.aspose.com/cells/net/aspose.cells/range) objekt ger också en[**Sammanfoga**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) metod som slår samman intervallet som anges i[**Räckvidd**](https://reference.aspose.com/cells/net/aspose.cells/range)objekt.

##### **Textriktning**

Det är möjligt att ställa in läsordningen för text i celler. Läsordningen är den visuella ordning i vilken tecken, ord etc. visas. Till exempel är engelska ett språk från vänster till höger medan arabiska är ett språk från höger till vänster.

 Läsordningen ställs in med[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt[**TextDirection**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) fast egendom. Aspose.Cells tillhandahåller fördefinierade textriktningstyper i[**TextDirectionType**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype)uppräkning.

|**Textriktningstyper**|**Beskrivning**|
|:- |:- |
|Sammanhang|Läsordningen överensstämmer med språket för det först inmatade tecknet|
|Vänster till höger|Vänster till höger läsordning|
|Höger till vänster|Läsordning från höger till vänster|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

## **Förhandsämnen**
- [Ändra Cells Justering och behåll befintlig formatering](/cells/sv/net/change-cells-alignment-and-keep-existing-formatting/)
- [Radbrytningar och textbrytning](/cells/sv/net/line-breaks-and-text-wrapping/)

