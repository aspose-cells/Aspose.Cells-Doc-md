---
title: Dataformatering
type: docs
weight: 80
url: /sv/java/data-formatting/
---
## **Metoder för att formatera data i Cells**
Det är ett vanligt faktum att om kalkylbladscellerna är korrekt formaterade så blir det lättare för användarna att läsa innehållet (data) i cellen. Det finns många sätt att formatera celler och deras innehåll. Det enklaste sättet är att formatera celler med Microsoft Excel i en WYSIWYG-miljö samtidigt som du skapar ett designerkalkylblad. Efter att designerkalkylarket har skapats kan du öppna kalkylarket med Aspose.Cells och behålla alla formatinställningar sparade med kalkylarket. Ett annat sätt att formatera celler och deras innehåll är att använda Aspose.Cells API. I det här avsnittet kommer vi att beskriva två metoder för att formatera celler och deras innehåll med hjälp av Aspose.Cells API.
### **Formatering Cells**
 Utvecklare kan formatera celler och deras innehåll med den flexibla API eller Aspose.Cells. Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) som ger åtkomst till varje kalkylblad i en Excel-fil. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass tillhandahåller en Cells-samling. Varje objekt i[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)samling representerar ett föremål för**Cell** klass.

 Aspose.Cells tillhandahåller[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) egendom i[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) klass, används för att ställa in formateringsstilen för en cell. Dessutom tillhandahåller Aspose.Cells också en[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) klass som används för att tjäna samma syfte. Använd olika typer av formateringsstilar på cellerna för att ställa in deras bakgrunds- eller förgrundsfärger, ramar, teckensnitt, horisontella och vertikala justeringar, indragsnivå, textriktning, rotationsvinkel och mycket mer.
#### **Använda setStyle-metoden**
 När du använder olika formateringsstilar på olika celler är det bättre att använda setStyle-metoden för[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) klass. Ett exempel ges nedan för att demonstrera användningen av setStyle-metoden för att tillämpa olika formateringsinställningar på en cell.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **Använda stilobjektet**
 När du använder samma formateringsstil på olika celler, använd[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) objekt.

1.  Lägg till en[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) invända mot Styles-samlingen av[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass genom att anropa createStyle-metoden för klassen Workbook.
1. Få åtkomst till det nyligen tillagda Style-objektet från Styles-samlingen.
1. Ställ in önskade egenskaper för Style-objektet för att tillämpa önskade formateringsinställningar.
1. Tilldela det konfigurerade Style-objektet till Style-egenskapen för valfri cell.

Detta tillvägagångssätt kan avsevärt förbättra effektiviteten för dina applikationer och spara minne också.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **Tillämpa övertoningsfyllningseffekter**
För att tillämpa önskade gradientfyllningseffekter på cellen, använd Style-objektets setTwoColorGradient-metod i enlighet med detta.
#### **Kodexempel**
 Följande utdata uppnås genom att exekvera koden nedan.

**Tillämpa övertoningsfyllningseffekter** 

![todo:image_alt_text](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **Konfigurera justeringsinställningar**
Alla som har använt Microsoft Excel för att formatera celler kommer att känna till justeringsinställningarna i Microsoft Excel.

**Justeringsinställningar i Microsoft Excel** 

![todo:image_alt_text](data-formatting_2.png)

Som du kan se från ovanstående figur finns det olika typer av justeringsalternativ:

- [Textjustering](/cells/sv/java/data-formatting/) (horisontell och vertikal)
- [Indrag](/cells/sv/java/data-formatting/).
- [Orientering](/cells/sv/java/data-formatting/).
- [Textkontroll](/cells/sv/java/data-formatting/).
- [Textriktning](/cells/sv/java/data-formatting/).

Alla dessa justeringsinställningar stöds fullt ut av Aspose.Cells och diskuteras mer i detalj nedan.
### **Konfigurera justeringsinställningar**
 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , som representerar en Excel-fil. Klassen Workbook innehåller en WorksheetCollection som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass.

 Klassen Worksheet tillhandahåller en Cells-samling. Varje föremål i Cells-samlingen representerar ett objekt av[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) klass.

Aspose.Cells tillhandahåller setStyle-metoden i[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) klass som används för en cells formatering. De[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) klass ger användbara egenskaper för att konfigurera teckensnittsinställningar.

Välj valfri textjusteringstyp med hjälp av uppräkningen TextAlignmentType. De fördefinierade textjusteringstyperna i TextAlignmentType-uppräkningen är:

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
{{% alert color="primary" %}} 

Du kan också tillämpa en distribuerad inställning för justera med metoden Style.setJustifyDistributed().

{{% /alert %}} 
#### **Horisontell linjering**
 Använd[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) objektets setHorizontalAlignment-metod för att justera texten horisontellt.

Följande utdata uppnås genom att exekvera exempelkoden nedan:

**Justera texten horisontellt** 

![todo:image_alt_text](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **Vertikal inriktning**
 Använd[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) objektets setVerticalAlignment-mehod för att justera texten vertikalt.

Följande utdata uppnås när VerticalAlignment är inställt på mitten.

**Justera texten vertikalt** 

![todo:image_alt_text](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **Indrag**
 Det är möjligt att ställa in indragsnivån för texten i en cell genom att använda[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) objektets setIndentLevel-metod.

Följande utdata uppnås när IndentLevel är inställt på 2.

**Indragningsnivå justerad till 2** 

![todo:image_alt_text](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **Orientering**
 Ställ in orienteringen (rotationen) för texten i en cell med[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) objektets setRotationAngle-metod.

Följande utgång uppnås när rotationsvinkeln är inställd på 25.

**Rotationsvinkel inställd på 25** 

![todo:image_alt_text](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **Textkontroll**
Följande avsnitt diskuterar hur man kontrollerar text genom att ställa in textbrytning, krympa för att passa och andra formateringsalternativ.
#### **Radbrytande text**
Radbrytning av text i en cell gör det lättare att läsa: cellens höjd justeras för att passa all text, istället för att klippa av den eller spilla över i intilliggande celler.

 Slå på eller av textbrytning med[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) objektets setTextWrapped-metod.

Följande utdata uppnås när textbrytning är aktiverad.

**Text lindad inuti cellen** 

![todo:image_alt_text](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **Krymper för att passa**
 Ett alternativ för att radbryta text i ett fält är att krympa textstorleken så att den passar en cells dimensioner. Detta görs genom att ställa in[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) objektets IsTextWrapped-egenskap till**Sann**.

Följande utdata uppnås när texten krymps för att passa cellen.

**Text krympt för att passa innanför cellens gränser** 

![todo:image_alt_text](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **Slår ihop Cells**
Liksom Microsoft Excel stöder Aspose.Cells sammanslagning av flera celler till en.

Följande utdata uppnås om de tre cellerna i den första raden slås samman för att skapa en stor enskild cell.

**Tre celler slogs samman för att skapa en stor cell** 

![todo:image_alt_text](data-formatting_9.png)

 Använd[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) samlingens Merge-metod för att slå samman celler. Sammanfogningsmetoden tar följande parametrar:

- Första raden, första raden varifrån man ska börja sammanfoga.
- Första kolumnen, den första kolumnen varifrån man ska börja slå samman.
- Antal rader, antalet rader som ska sammanfogas.
- Antal kolumner, antalet kolumner som ska sammanfogas.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **Textriktning**
Det är möjligt att ställa in läsordningen för text i celler. Läsordningen är den visuella ordning i vilken tecken, ord etc. visas. Till exempel är engelska ett språk från vänster till höger medan arabiska är ett språk från höger till vänster.

 Läsordningen ställs in med[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) objektets TextDirection-egenskap. Aspose.Cells tillhandahåller fördefinierade textriktningstyper i TextDirectionType-uppräkningen.

|**Textriktningstyper**|**Beskrivning**|
|:- |:- |
|Sammanhang|Läsordningen överensstämmer med språket för det först inmatade tecknet|
|Vänster till höger|Vänster till höger läsordning|
|Höger till vänster|Läsordning från höger till vänster|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





Följande utdata uppnås om läsordningen för texten är inställd på höger till vänster.

**Ställer in textläsordning till höger till vänster** 

![todo:image_alt_text](data-formatting_10.png)
## **Formatera valda tecken i en Cell**
[Hantera teckensnittsinställningar](/cells/sv/java/dealing-with-font-settings/)förklarade hur man formaterar celler men bara hur man formaterar innehållet i hela cellerna. Vad händer om du bara vill formatera valda tecken?

Aspose.Cells stöder den här funktionen. Det här avsnittet förklarar hur du använder den här funktionen.
### **Formatera valda tecken**
 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , som representerar en Microsoft Excel-fil. Klassen Workbook innehåller en kalkylbladssamling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass. Klassen Worksheet tillhandahåller en Cells-samling. Varje föremål i Cells-samlingen representerar ett objekt av[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) klass.

Klassen Cell tillhandahåller teckenmetod som använder följande parametrar för att välja ett teckenintervall i en cell:

- **Starta index**, indexet för tecknet att starta valet från.
- **Antal tecken**, antalet tecken att välja.

I utdatafilen, i A1"-cellen, är ordet "Besök" formaterat med standardteckensnittet men "Aspose!" är fet och blå.

**Formatera valda tecken** 

![todo:image_alt_text](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

 Om du är intresserad av[formatera en del av Rich Text i en [cell]](/cells/sv/java/access-and-update-the-portions-of-rich-text-of-cell/) , överväg att använda metoderna Cell.getCharacters & Cell.setCharacters. Metoden Cell.getCharacters ska användas för att komma åt delarna av texten och sedan kan ändringar göras med metoden Cell.setCharacters medan**skaffa sig** metod returnerar en uppsättning FontSetting-objekt som kan manipuleras för att ställa in olika egenskaper typsnittsnamn, teckensnittsfärg, fetstil etc.**uppsättning** metod kan användas för att tillämpa ändringarna.

{{% /alert %}} 
## **Aktivera ark och göra en aktiv Cell eller välj ett intervall på Cells i arbetsbladet**
Ibland kan du behöva aktivera ett specifikt kalkylblad så att det är det första som visas när någon öppnar filen i Microsoft Excel. Du kan också behöva aktivera en specifik cell på ett sådant sätt att rullningslisterna rullar till den aktiva cellen så att den syns tydligt. Aspose.Cells kan utföra alla ovan nämnda uppgifter.

Ett aktivt ark är det ark som du arbetar med i en arbetsbok. Namnet på fliken på det aktiva bladet är som standard fetstilt. En aktiv cell är samtidigt den cell som är vald och i vilken data skrivs in när du börjar skriva. Endast en cell är aktiv åt gången. Den aktiva cellen är omgiven av en tung kant för att få den att dyka upp mot de andra cellerna. Aspose.Cells låter dig också välja ett cellintervall i kalkylbladet.
### **Aktivera ett ark och göra en Cell aktiv**
Aspose.Cells tillhandahåller ett specifikt API för dessa uppgifter. Till exempel är metoden WorksheetCollection.setActiveSheetIndex användbar för att ställa in ett aktivt ark. På liknande sätt används metoden Worksheet.setActiveCell för att ställa in och få en aktiv cell i ett kalkylblad.

Om du vill att de horisontella och vertikala rullningslisterna ska rullas till rad- och kolumnindexpositionen för att ge en bra överblick över vald data när filen öppnas i Microsoft Excel, använd egenskaperna Worksheet.setFirstVisibleRow och Worksheet.setFirstVisibleColumn.

Följande exempel visar hur man aktiverar ett kalkylblad och gör en cell i det aktiv. Rullningslisterna rullas för att göra den andra raden och den andra kolumnen som deras första synliga rad och kolumn.

**Ställer in B2-cell som en aktiv cell** 

![todo:image_alt_text](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **Välj ett intervall på Cells i arbetsbladet**
Aspose.Cells tillhandahåller metoden Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers). Genom att använda den sista parametern - removeOthers - till sant, tas andra cell- eller cellområdesval i arket bort.

Följande exempel visar hur du väljer ett cellintervall i det aktiva kalkylbladet.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

Alla ovanstående klasser och metoder är tillgängliga med den licensierade versionen av Aspose.Cells.

{{% /alert %}} 
## **Formatera rader och kolumner**
Formatering av rader och kolumner i ett kalkylblad för att ge rapporten ett utseende är möjligen den mest använda funktionen i Excel-applikationen. Aspose.Cells API:er tillhandahåller också denna funktionalitet genom sin datamodell genom att exponera Style-klassen som huvudsakligen hanterar alla stilrelaterade funktioner som typsnitt och dess attribut, justering av text, bakgrunds-/förgrundsfärger, ramar, visningsformat för siffror och datum bokstaver och så vidare . En annan användbar klass som Aspose.Cells API:er tillhandahåller är StyleFlag som tillåter återanvändning av Style-objektet.

I den här artikeln kommer vi att försöka förklara hur man använder Aspose.Cells for Java API för att tillämpa formatering på rader och kolumner.
### **Formatera rader och kolumner**
 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en WorksheetCollection som ger åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen Worksheet. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass tillhandahåller samlingen Cells. Cells-kollektionen tillhandahåller en rad-samling.
#### **Formatera en rad**
Varje objekt i radsamlingen representerar ett radobjekt. Row-objektet erbjuder metoden applicationStyle som används för att tillämpa formatering på en rad.

För att tillämpa samma formatering på en rad, använd Style-objektet:

1. Lägg till ett Style-objekt till Workbook-klassen genom att anropa dess createStyle-metod.
1. Ställ in Style-objektegenskaperna för att tillämpa formateringsinställningarna.
1. Tilldela det konfigurerade Style-objektet till metoden applicationStyle för ett Row-objekt.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **Formatera en kolumn**
Cells-samlingen tillhandahåller en kolumnsamling. Varje objekt i kolumnsamlingen representerar ett kolumnobjekt. I likhet med Row-objektet erbjuder Column-objektet metoden applicationStyle som används för att ställa in kolumnformateringen. Använd metoden applicationStyle för Column-objektet för att formatera en kolumn på samma sätt som en rad.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **Ställa in visningsformat för Numbers & datum för rader och kolumner**
Om kravet är att ställa in visningsformatet för siffror och datum för en hel rad eller kolumn så är processen mer eller mindre densamma som diskuterats ovan, men istället för att ställa in parametrar för textinnehållet kommer du att ställa in formateringen för siffror och datum med Style.Number eller Style.Custom. Observera att Style.Number-egenskapen är av typen heltal och hänvisar till de inbyggda tal- och datumformaten, medan Style.Custom-egenskapen är av typen string och accepterar de giltiga mönstren.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln om[Ställa in visningsformat för Numbers och [Datum]](/cells/sv/java/data-formatting/).

{{% /alert %}}
