---
title: Dataformatering
type: docs
weight: 80
url: /sv/java/data-formatting/
---

## **Metoder för att formatera data i celler**
Det är en allmän uppfattning att om kalkylbladsceller formateras på rätt sätt blir det lättare för användarna att läsa innehållet (data) i cellen. Det finns många sätt att formatera celler och deras innehåll. Det enklaste sättet är att formatera celler med Microsoft Excel i en WYSIWYG-miljö när du skapar en Designer Spreadsheet. Efter att designerkalkylarket är skapat kan du öppna kalkylarket med Aspose.Cells och behålla alla formatinställningar som sparats med kalkylarket. Ett annat sätt att formatera celler och deras innehåll är att använda Aspose.Cells API. I detta avsnitt beskriver vi två tillvägagångssätt för att formatera celler och deras innehåll med hjälp av Aspose.Cells API.
### **Formatering av celler**
Utvecklare kan formatera celler och deras innehåll med den flexibla API:en för Aspose.Cells. Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Microsoft Excel-fil. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen innehåller en [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) som möjliggör åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassen. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassen tillhandahåller en Cells-samling. Varje objekt i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)-samlingen representerar ett objekt av **Cell**-klassen.

Aspose.Cells tillhandahåller egenskapen [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) i [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-klassen, som används för att ställa in formatmallen för en cell. Dessutom tillhandahåller även Aspose.Cells en [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-klass som används för samma ändamål. Tillämpa olika typer av formateringsmallar på cellerna för att ställa in deras bakgrund eller förgrundsfärger, ramar, teckensnitt, horisontella och vertikala justeringar, indenteringsnivå, textriktning, rotationsvinkel och mycket mer.
#### **Använda setStyle-metoden**
När olika formateringsmallar ska tillämpas på olika celler är det bättre att använda setStyle-metoden i [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-klassen. Ett exempel ges nedan för att illustrera användningen av setStyle-metoden för att tillämpa olika formateringsinställningar på en cell.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **Använda Style-objektet**
När samma formateringsmall ska tillämpas på olika celler, använd [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-objektet.

1. Lägg till ett [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-objekt till Styles-samlingen i [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen genom att anropa createStyle-metoden i Workbook-klassen.
1. Åtkomst till det nyss tillagda Style-objektet från Styles-samlingen.
1. Ange de önskade egenskaperna för Style-objektet för att tillämpa önskade formateringsinställningar.
1. Tilldela det konfigurerade Style-objektet till Egenskapen Style för valfri cell.

Denna metod kan avsevärt förbättra effektiviteten i dina applikationer och spara minne också.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **Tillämpning av gradientfylleffekter**
För att tillämpa dina önskade gradientfylleffekter på cellen, använd Style-objektets setTwoColorGradient-metod enligt behov.
#### **Kodexempel**
Följande utdata uppnås genom att köra koden nedan. 

**Tillämpning av gradientfylleffekter** 

![todo:image_alt_text](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **Konfigurera justeringsinställningar**
Alla som har använt Microsoft Excel för att formatera celler kommer att vara bekanta med justeringsinställningarna i Microsoft Excel.

**Inställningar för justering i Microsoft Excel** 

![todo:image_alt_text](data-formatting_2.png)

Som du kan se från figuren ovan, finns det olika typer av justeringsalternativ:

- [Textjustering](/cells/sv/java/data-formatting/) (horisontell & vertikal)
- [Indrag](/cells/sv/java/data-formatting/).
- [Orientering](/cells/sv/java/data-formatting/).
- [Textkontroll](/cells/sv/java/data-formatting/).
- [Textriktning](/cells/sv/java/data-formatting/).

Alla dessa justeringsinställningar stöds fullt ut av Aspose.Cells och diskuteras mer detaljerat nedan.
### **Konfigurera justeringsinställningar**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Excelfil. Workbook-klassen innehåller en WorksheetCollection som tillåter åtkomst till varje kalkylblad i Excelfilen. Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Worksheet-klassen tillhandahåller en Cells-samling. Varje objekt i Cells-samlingen representerar ett objekt av klassen [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells tillhandahåller metoden setStyle i [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-klassen som används för en cells formatering. [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-klassen tillhandahåller användbara egenskaper för att konfigurera typsnittsinställningar.

Välj vilken som helst textjusteringstyp med hjälp av TextAlignmentType-avräkningen. De fördefinierade textjusteringstyperna i TextAlignmentType-avräkningen är:

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
{{% alert color="primary" %}} 

Du kan också tillämpa rättfärdig fördelad inställning med hjälp av metoden Style.setJustifyDistributed().

{{% /alert %}} 
#### **Horisontell justering**
Använd [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-objektets setHorizontalAlignment-metod för att justera texten horisontellt.

Följande utmatning uppnås genom att köra exempelkoden nedan:

**Justerar texten horisontellt** 

![todo:image_alt_text](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **Vertikal justering**
Använd [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) objektets setVerticalAlignment metod för att aligna texten vertikalt.

Följande utdata uppnås när VerticalAlignment är satt till center.

**Alignment av texten vertikalt** 

![todo:image_alt_text](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **Indrag**
Det är möjligt att ställa in nivån för indraget för texten i en cell genom att använda [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) objektets setIndentLevel metod.

Följande utdata uppnås när IndentLevel är satt till 2.

**Indragningsnivå justerad till 2** 

![todo:image_alt_text](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **Orientering**
Ställ in orienteringen (rotationen) av texten i en cell med [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) objektets setRotationAngle metod.

Följande utdata uppnås när rotationsvinkeln är satt till 25.

**Rotationsvinkel inställd på 25** 

![todo:image_alt_text](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **Textkontroll**
I följande avsnitt diskuteras hur man kontrollerar text genom att ställa in textbrytning, krympa till passa och andra formateringsalternativ.
#### **Textindrag**
Att linda text i en cell gör det lättare att läsa: cellens höjd justeras för att passa all text, istället för att klippa av den eller att spilla över i intilliggande celler.

Ställ in textlindning på eller av med [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-objektets setTextWrapped-metod.

Följande utdata uppnås när textlindning är aktiverad.

**Text omsluten innuti cellen** 

![todo:image_alt_text](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **Krympa passande**
Ett alternativ till att linda text i en cell är att krympa textstorleken för att passa cellens dimensioner. Detta görs genom att ställa in [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-objektets IsTextWrapped-egenskap till **true**.

Följande utdata uppnås när texten krymps för att passa cellen.

**Text krympad för att passa inom cellens gränser** 

![todo:image_alt_text](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **Sammanfoga celler**
Precis som Microsoft Excel, stöder Aspose.Cells sammanfogning av flera celler till en enda.

Följande utdata uppnås om de tre cellerna i den första raden är sammanslagna för att skapa en stor enskild cell.

**Tre celler sammanfogade för att skapa en stor cell** 

![todo:image_alt_text](data-formatting_9.png)

Använd [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)-kollektionens Merge-metod för att sammanfoga celler. Merge-metoden tar följande parametrar:

- Första rad, första raden att börja sammanfoga från.
- Första kolumn, första kolumnen att börja sammanfoga från.
- Antal rader, antalet rader att sammanfoga.
- Antal kolumner, antalet kolumner att sammanfoga.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **Textriktning**
Det är möjligt att ställa in läsordningen för text i celler. Läsordningen är den visuella ordning i vilken tecken, ord etc. visas. Till exempel är engelska ett vänster till höger-språk medan arabiska är ett höger till vänster-språk.

Läsordningen sätts med [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-objektets egenskap TextDirection. Aspose.Cells tillhandahåller fördefinierade textriktningstyper i TextDirectionType-enumerationen.

|**Textriktningstyper**|**Beskrivning**|
| :- | :- |
|Context| Läsordningen som är konsekvent med språket för det första inmatade tecknet
|LeftToRight|Vänster till höger-läsordning
|RightToLeft|Höger till vänster-läsordning






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





Följande utdata uppnås om textens läsordning är inställd på höger till vänster.

**Inställning av textens läsordning till höger till vänster** 

![todo:image_alt_text](data-formatting_10.png)
## **Formatera valda tecken i en cell**
[Hantering av typsnittsinställningar](/cells/sv/java/dealing-with-font-settings/) förklarade hur man formaterar celler men endast hur man formaterar innehållet i hela celler. Vad gör man om man vill formatera endast valda tecken?

Aspose.Cells stöder denna funktion. Detta ämne förklarar hur man använder denna funktion.
### **Formatera valda tecken**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Microsoft Excel-fil. Workbook-klassen innehåller en kalkylbladskollektion som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Worksheet-klassen tillhandahåller en Cells-kollektion. Varje objekt i Cells-kollektionen representerar ett objekt av [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-klassen.

Cell-klassen tillhandahåller characters-metoden som tar följande parametrar för att välja en rad tecken i en cell:

- **Startindex**, index för tecknet att börja urvalet från.
- **Antal tecken**, antalet tecken att välja.

I utdatafilen, i cellen A1, är ordet 'Visit' formaterat med standardtypsnittet men 'Aspose!' är fett och blått.

**Formatering av valda tecken** 

![todo:image_alt_text](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

Om du är intresserad av [formatering av en del av rik text i en [cell](/cells/sv/java/access-and-update-the-portions-of-rich-text-of-cell/), överväg att använda metoderna Cell.getCharacters & Cell.setCharacters. Cell.getCharacters-metoden används för att komma åt delarna av texten och sedan kan ändringar göras med Cell.setCharacters-metoden medan **get**-metoden returnerar en array av FontSetting-objekt som kan manipuleras för att ställa in olika egenskaper som typsnittsnamn, typsnittsfärg, fetstil etc och **set**-metoden kan användas för att tillämpa ändringarna.

{{% /alert %}} 
## **Aktivera blad och göra en aktiv cell eller välj ett område med celler i kalkylbladet**
Ibland kan det vara nödvändigt att aktivera ett specifikt kalkylblad så att det är det första som visas när någon öppnar filen i Microsoft Excel. Du kan också behöva aktivera en specifik cell på ett sätt så att rullningspanelerna rullar till den aktiva cellen så att den tydligt syns. Aspose.Cells kan utföra alla ovan nämnda uppgifter.

Ett aktivt kalkylblad är kalkylbladet du arbetar med i en arbetsbok. Namnet på fliken för det aktiva kalkylbladet är fet som standard. En aktiv cell är den markerade cellen där data matas in när man börjar skriva. Endast en cell är aktiv åt gången. Den aktiva cellen omges av en tjock ram för att synas mot de andra cellerna. Aspose.Cells tillåter också att man väljer en rad med celler i kalkylbladet.
### **Aktivera ett kalkylblad och göra en cell aktiv**
Aspose.Cells tillhandahåller en specifik API för dessa uppgifter. Till exempel är WorksheetCollection.setActiveSheetIndex-metoden användbar för att ställa in ett aktivt kalkylblad. På liknande sätt används Worksheet.setActiveCell-metoden för att ställa in och hämta en aktiv cell i ett kalkylblad.

Om du vill att de horisontella och vertikala rullningspanelerna ska rulla till rad- och kolumnindexpositionen för att ge en bra vy över de valda data när filen öppnas i Microsoft Excel, använd egenskaperna Worksheet.setFirstVisibleRow och Worksheet.setFirstVisibleColumn.

Följande exempel visar hur man aktiverar ett kalkylblad och gör en cell aktiv. Rullningspanelerna rullas för att göra den andra raden och den andra kolumnen till sin första synliga rad och kolumn.

**Ställa in B2-cell som en aktiv cell** 

![todo:image_alt_text](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **Val av ett intervall av celler i arbetsbladet**
Aspose.Cells tillhandahåller metoden Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers). Genom att ställa in den sista parametern - removeOthers - till true, tas andra cell- eller cellintervallval bort i kalkylarket.

Följande exempel visar hur man väljer en mängd celler i det aktiva arbetsbladet.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

Alla ovanstående klasser och metoder är tillgängliga med den licensierade versionen av Aspose.Cells.

{{% /alert %}} 
## **Formatering av rader och kolumner**
Att formatera rader och kolumner i en kalkyl för att ge rapporten en visuell utformning är möjligen den mest använda funktionen i Excel-applikationen. Aspose.Cells API:er tillhandahåller också denna funktionalitet genom sin datamodell genom att exponera Style-klassen som främst hanterar alla stilmässiga funktioner såsom teckensnitt och dess attribut, justering av text, bakgrund/förgrundsfärger, ramar, visningsformat för siffror & datumtexter med mera. En annan användbar klass som Aspose.Cells API:er tillhandahåller är StyleFlag som möjliggör återanvändning av Style-objektet. 

I den här artikeln kommer vi att försöka förklara hur man använder Aspose.Cells for Java API för att tillämpa formatering på rader och kolumner. 
### **Formatering av rader & kolumner**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Microsoft Excel-fil. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen innehåller en WorksheetCollection som möjliggör åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen Worksheet. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassen tillhandahåller Cells-samlingen. Cells-samlingen tillhandahåller en Rows-samling.
#### **Formatering av en rad**
Varje objekt i Rows-samlingen representerar ett Row-objekt. Row-objektet erbjuder metoden applyStyle som används för att tillämpa formatering på en rad.

För att tillämpa samma formatering på en rad, använd Style-objektet:

1. Lägg till ett Style-objekt till Workbook-klassen genom att anropa dess createStyle-metod.
1. Ställ in Style-objektets egenskaper för att tillämpa formateringsinställningarna.
1. Tilldela det konfigurerade Style-objektet till applyStyle-metoden för ett Row-objekt.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **Formatering av en kolumn**
Cells-samlingen tillhandahåller en Columns-samling. Varje objekt i Columns-samlingen representerar ett Column-objekt. Liknande Row-objektet, erbjuder Column-objektet applyStyle-metoden som används för att ställa in kolumnformatering. Använd applyStyle-metoden för Column-objektet för att formatera en kolumn på samma sätt som en rad.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **Inställning av visningsformat för siffror & datum för rader & kolumner**
Om kravet är att ställa in visningsformatet för siffror & datum för en komplett rad eller kolumn är processen mer eller mindre densamma som diskuterats ovan, dock kommer du istället för att ställa in parametrar för textinnehåll att ställa in formateringen för siffror och datum med hjälp av Style.Number eller Style.Custom. Observera att Style.Number-egenskapen är av typen heltal och avser de inbyggda siffer- och datumformaten, medan Style.Custom-egenskapen är av typen sträng och accepterar giltiga mönster.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Inställning av visningsformat för siffror och [Datum](/cells/sv/java/data-formatting/).

{{% /alert %}}
