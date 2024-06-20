---
title: Siduppsättningsfunktioner
type: docs
weight: 40
url: /sv/java/page-setup-features/
---

Ibland är det nödvändigt att konfigurera siduppställningsinställningar för kalkylblad för att kontrollera utskrifter. Dessa siduppställningsinställningar erbjuder olika alternativ.

**Sidoalternativ** 

![todo:image_alt_text](page-setup-features_1.png)

Siduppställningsalternativ stöds fullt ut i Aspose.Cells. Denna artikel förklarar hur du ställer in sidoalternativ med Aspose.Cells.

## **Ställa in sidalternativ**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen Arbetsbok innehåller en samling Kalkylblad som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Klassen Kalkylblad tillhandahåller egenskapen PageSetup som används för att ställa in siduppställningsalternativ. Faktum är att PageSetup-egenskapen är ett objekt av klassen PageSetup som gör det möjligt att ställa in sidlayoutalternativ för ett utskrivet kalkylblad. Klassen PageSetup tillhandahåller olika egenskaper som används för att ställa in siduppställningsalternativ. Några av dessa egenskaper diskuteras nedan.

### **Sidorientering**

Sidorientering kan ställas in till stående eller liggande med hjälp av metoden för klassen [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) [**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation). Metoden [**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) tar [**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) uppräkningen som parameter. Medlemmarna i uppräkningen [**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) listas nedan.

|**Sidorienteringstyper**|**Beskrivning**|
| :- | :- |
|[**LIGGANDE**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|Liggande orientering|
|[**STÅENDE**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|Stående orientering|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **Skalfaktor**

Det är möjligt att minska eller förstora ett kalkylblads storlek genom att justera skalfaktorn med klassens [**setZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom) metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **Anpassa till sidor alternativ**

För att passa innehållet i kalkylbladet till ett specifikt antal sidor, använd klassens [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) och [**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) metoder. Dessa metoder används också för att skala kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **Pappersstorlek**

Ange pappersstorleken som kalkylbladen ska skrivas ut på med hjälp av klassens [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) [**PaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize). Egenskapen PaperSize accepterar en av de fördefinierade värdena i uppräkningen [**PaperSizeType**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType), listade nedan.

|**Pappersstorlekar**|**Beskrivning**|
| :- | :- |
|Paper10x14|10 in. x 14 in.|
|Paper11x17|11 in. x 17 in.|
|PaperA3|A3 (297 mm x 420 mm)|
|PaperA4|A4 (210 mm x 297 mm)|
|PaperA4Small|A4 Small (210 mm x 297 mm)|
|PaperA5|A5 (148 mm x 210 mm)|
|PaperB3|B3 (13.9 x 19.7 inches)|
|PaperB4|B4 (250 mm x 354 mm)|
|PaperB5|B5 (182 mm x 257 mm)|
|PaperBusinessCard|Business Card (90 mm x 55 mm)|
|PaperCSheet|C size sheet|
|PaperDSheet|D size sheet|
|PaperEnvelope10|Envelope #10 (4-1/8 in. x 9-1/2 in.)|
|PaperEnvelope11|Envelope #11 (4-1/2 in. x 10-3/8 in.)|
|PaperEnvelope12|Envelope #12 (4-1/2 in. x 11 in.)|
|PaperEnvelope14|Envelope #14 (5 in. x 11-1/2 in.)|
|PaperEnvelope9|Envelope #9 (3-7/8 in. x 8-7/8 in.)|
|PaperEnvelopeB4|Envelope B4 (250 mm x 353 mm)|
|PaperEnvelopeB5|Envelope B5 (176 mm x 250 mm)|
|PaperEnvelopeB6|Envelope B6 (176 mm x 125 mm)|
|PaperEnvelopeC3|Envelope C3 (324 mm x 458 mm)|
|PaperEnvelopeC4|Envelope C4 (229 mm x 324 mm)|
|PaperEnvelopeC5|Envelope C5 (162 mm x 229 mm)|
|PaperEnvelopeC6|Envelope C6 (114 mm x 162 mm)|
|PaperEnvelopeC65|Envelope C65 (114 mm x 229 mm)|
|PaperEnvelopeDL|Envelope DL (110 mm x 220 mm)|
|PaperEnvelopeItaly|Envelope Italy (110 mm x 230 mm)|
|PaperEnvelopeMonarch|Envelope Monarch (3-7/8 in. x 7-1/2 in.)|
|PaperEnvelopePersonal|Envelope (3-5/8 in. x 6-1/2 in.)|
|PaperESheet|E size sheet|
|PaperExecutive|Executive (7-1/2 in. x 10-1/2 in.)|
|PaperFanfoldLegalGerman|German Legal Fanfold (8-1/2 in. x 13 in.)|
|PaperFanfoldStdGerman|German Standard Fanfold (8-1/2 in. x 12 in.)|
|PaperFanfoldUS|U.S. Standard Fanfold (14-7/8 in. x 11 in.)|
|PaperFolio|Folio (8-1/2 in. x 13 in.)|
|PaperLedger|Ledger (17 in. x 11 in.)|
|PaperLegal|Legal (8-1/2 in. x 14 in.)|
|PaperLetter|Letter (8-1/2 in. x 11 in.)|
|PaperLetterSmall|Letter Small (8-1/2 in. x 11 in.)|
|PaperNote|Note (8-1/2 in. x 11 in.)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|PaperStatement|Statement (5-1/2 in. x 8-1/2 in.)|
|PaperTabloid|Tabloid (11 in. x 17 in.)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **Utskriftskvalitet**

Ställ in utskriftskvaliteten för de kalkylblad som ska skrivas ut med metoden för klassen [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) [**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality). Måttenheten för utskriftskvaliteten är punkter per tum (DPI).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **Första sidans nummer**

Börja numreringen av kalkylbladssidor med hjälp av klassen [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)s [**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber)-metod. Metoden setFirstPageNumber ställer in sidnumret för den första kalkylbladssidan och de följande sidorna numreras i stigande ordning.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **Ställa in marginaler**

Aspose.Cells stödjer helt Microsoft Excels siduppställningsalternativ. Utvecklare kan behöva konfigurera siduppställningsinställningarna för kalkylblad för att kontrollera utskriftsprocessen. Det här avsnittet diskuterar hur man använder Aspose.Cells för att konfigurera sidmarginaler.

**Sidmarginaler i Microsoft Excel**

![todo:image_alt_text](page-setup-features_2.png)

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Microsoft Excel-fil. Workbook-klassen innehåller kalkylbladssamlingen som möjliggör åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Kalkylbladsklassen ger egenskapen PageSetup, som används för att ställa in siduppställningsalternativ. PageSetup-attributet är ett objekt av klassen [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) som gör det möjligt att ange olika sidlayoutalternativ för ett utskriftskalkylblad. PageSetup-klassen tillhandahåller olika egenskaper och metoder som används för att ställa in siduppställningsalternativ.

### **Sidmarginaler**

Ställ in marginalerna (vänster, höger, över, under) för en sida med klassmedlemmar från [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Några av metoderna som används för att ange sidmarginaler listas nedan:

- [**setLeftMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **Centrera på sidan**

Det är möjligt att centrera något på en sida horisontellt och vertikalt. Klassen [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) har medlemmar för detta ändamål: [**setCenterHorizontally**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) och [**setCenterVertically**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **Sid- och fotmarginaler**

Ställ in sid- och fotmarginaler med medlemmar från [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) såsom [**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) och [**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **Ställa in sidhuvuden och sidfötter**

Headers och footers är avsnitten med text och bilder ovanför sidans toppmarginal eller nedanför bottenmarginalen på en sida. Det är möjligt att lägga till headers och footers till kalkylblad också. Headers och footers kan användas för att visa all slags användbar information, till exempel sidnummer, författarnamn, dokumenttitel eller datum och tid. Headers och footers hanteras också med hjälp av dialogrutan Siduppsättning.

**Dialogrutan Siduppsättning** 

![todo:image_alt_text](page-setup-features_3.png)

Aspose.Cells tillåter att lägga till headers och footers i kalkylbladen vid körning, men det rekommenderas att headers och footers ställs in manuellt i en fördesignad fil för utskrift. Du kan använda Microsoft Excel som ett grafiskt verktyg för att enkelt ställa in headers och footers för att minska utvecklingstiden. Aspose.Cells kan importera filen och behålla dessa inställningar.

För att lägga till headers och footers vid körning tillhandahåller Aspose.Cells specialklasser och några skriptkommandon för att kontrollera formateringen.

### **Skriptkommandon**

Skriptkommandon är specialkommandon som tillhandahålls av Aspose.Cells som tillåter utvecklare att formatera headers och footers.

|**Skriptkommandon**|**Beskrivning**|
| :- | :- |
|&P|Aktuellt sidnummer.|
|&G|En bild.|
|&N|Antalet sidor.|
|&D|Aktuell datum.|
|&T|Aktuell tid.|
|&A|Kalkylbladets namn.|
|&F|Filnamn utan sökväg.|
|&"\<FontName>"|Ett teckensnittsnamn. Till exempel: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Ett teckensnittsnamn med en stil. Till exempel: &"Arial,Fet"|
|&\<FontSize>|Representerar teckensnittsstorlek. Till exempel: “&14abc”. Men om detta kommando följs av ett vanligt nummer som ska skrivas ut i sidhuvudet, ska detta separeras med ett mellanslag från teckensnittsstorleken. Till exempel: “&14 123”|

### **Ställ in headers och footers**

Klassen [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) tillhandahåller metoden [**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader(int,%20java.lang.String)) för att lägga till en rubrik och [**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter(int,%20java.lang.String)) för att lägga till en sidfot i en arbetsbok. Skriptet används som ett argument för alla ovan nämnda metoder. Det representerar skriptet som ska användas för rubrik eller sidfot. Detta skript innehåller skriptkommandon för att formatera rubriker eller sidfötter.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **Infoga en grafik i en rubrik eller sidfot**

Klassen [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) har metoderna [**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture(int,%20byte[])) och [**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture(int,%20byte[])) för att lägga till bilder i en arbetsboks rubrik och sidfot. Dessa metoder tar två parametrar:

- **Avsnitt**, avsnittet för rubriken eller sidfoten där bilden kommer att placeras. Det finns tre avsnitt: vänster, mitt och höger, representerade av de numeriska värdena 0, 1 och 2 respektive.
- **Filens indataström**, den grafiska datan. Den binära datan ska skrivas in i bufferten av en byte-array.

Efter att koden har körts och filen har öppnats, kontrollera arbetsbokens rubrik i Microsoft Excel:

1. På **Arkiv**-menyn, välj **Sidlayout**.
1. På Sidlayout-dialogrutan, välj fliken **Rubrik/Sidfot**.

**Infoga en grafik i en rubrik/sidfot** 

![todo:image_alt_text](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **Infoga en grafik i endast förstasidesrubrik**

Klassen [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) har också andra användbara metoder, till exempel [**setPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture(boolean,%20boolean,%20boolean,%20int,%20byte[])), [**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader(int,%20java.lang.String)), [**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter(int,%20java.lang.String)), för att lägga till bilder i en arbetsboks rubrik/sidfot på första sidan. Första sidan är en speciell sida: det är vanligt att man vill att den ska visa speciell information, till exempel en företagslogotyp.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **Ställa in utskriftsalternativ**

Microsoft Excels sidlayoutinställningar erbjuder flera utskriftsalternativ (också kallade arkalternativ) som låter användare styra hur arbetsbokssidorna skrivs ut. Dessa utskriftsalternativ låter användare:

- Välja ett specifikt utskriftsområde på en arbetsbok.
- Skriv ut rubriker.
- Skriv ut rutnät.
- Skriva ut rad- och kolumnrubriker
- Uppnå utkasts kvalitet
- Skriv ut kommentarer.
- Skriv ut cellfel.
- Definiera sidordning.

Alla dessa utskriftsalternativ visas nedan.

**Utskrifts(arks)alternativ** 

![todo:image_alt_text](page-setup-features_5.png)

### **Inställning av utskrifts- och arkalternativ**

Aspose.Cells stöder alla utskriftsalternativ som erbjuds av Microsoft Excel och utvecklare kan enkelt konfigurera dessa alternativ för arbetsböcker med hjälp av egenskaperna som erbjuds av klassen [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Hur dessa egenskaper används diskuteras nedan mer i detalj.

### **Ange utskriftsområde**

Som standard omfattar endast utskriftsområdet alla områden av arbetsboken som innehåller data. Utvecklare kan fastställa ett specifikt utskriftsområde för arbetsboken.

För att välja ett specifikt utskriftsområde, använd egenskapen [**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea) i klassen [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Tilldela en cellintervall som definierar utskriftsområdet till denna egenskap.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **Ställ in utskriftstitlar**

Aspose.Cells låter dig ange att rad- och kolumnrubriker ska upprepas på alla sidor av en utskriven arbetsbok. Gör så genom att använda egenskaperna [**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns) och [**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows) i klassen [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup).

Rader eller kolumner som kommer att upprepas definieras genom att ange deras rad- eller kolumnnummer. Till exempel definieras rader som $1:$2 och kolumner definieras som $A:$B.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **Ange andra utskriftsalternativ**

Klassen [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) tillhandahåller också flera andra egenskaper för att ange allmänna utskriftsalternativ enligt följande:

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines), en boolesk egenskap som anger om rutnät ska skrivas ut eller inte.
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings), en boolesk egenskap som anger om rad- och kolumnrubriker ska skrivas ut eller inte.
- [**setBlackAndWhite**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite), en boolesk egenskap som anger om arbetsbladet ska skrivas ut i svartvitt läge eller inte.
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments), anger om utskriftskommentarer ska visas på arbetsbladet eller i slutet av arbetsbladet.
- [**setPrintDraft**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft), en boolesk egenskap som anger om arbetsbladet ska skrivas ut i utkastkvalitet eller inte.
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), anger om cellfel ska skrivas ut som visas, blankt, streck eller N/A.

För att ange egenskaperna [**PrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) och [**PrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) tillhandahåller även Aspose.Cells två uppräkningar, [**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) och [**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType), som innehåller fördefinierade värden att tilldela egenskaperna [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) och [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) respektive.

De fördefinierade värdena i uppräkningen [**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) beskrivs nedan.

|**Kommentarstyper för utskrift**|**Beskrivning**|
| :- | :- |
|[**PRINT_IN_PLACE**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_IN_PLACE)|Anger att skriva ut kommentarer som visas på arbetsbladet.|
|[**PRINT_NO_COMMENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_NO_COMMENTS)|Anger att inte skriva ut kommentarer.|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_SHEET_END)|Anger att skriva ut kommentarer i slutet av arbetsbladet.|

De fördefinierade värdena i uppräkningen [**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) beskrivs nedan.

|**Feltyper för utskrift**|**Beskrivning**|
| :- | :- |
|[**PRINT_ERRORS_BLANK**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_BLANK)|Anger att inte skriva ut fel.|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DASH)|Anger att skriva ut fel som "--".|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DISPLAYED)|Anger att skriva ut fel som visas.|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_NA)|Anger att skriva ut fel som "#N/A".|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **Ange sidordning**

Klassen [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) tillhandahåller egenskapen [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) som används för att ordna flera sidor för utskrift av ditt arbetsblad. Det finns två möjligheter att ordna sidorna enligt följande:

- **Nedåt sedan över** skriver ut alla sidor nedåt innan några sidor skrivs ut till höger.
- **Över sedan ner** skriver ut sidor från vänster till höger innan några sidor skrivs ut nedanför.

Aspose.Cells tillhandahåller en uppräkning, [**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType), som innehåller alla fördefinierade ordningstyper som ska tilldelas [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) metoden.

De fördefinierade värdena i uppräkningen [**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) beskrivs nedan.

|**Utskriftsordningstyper**|**Beskrivning**|
| :- | :- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN_THEN_OVER)|Skriv ut nedåt, sedan över.|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER_THEN_DOWN)|Skriv ut över, sedan ned.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **Ta bort befintliga skrivareinställningar för arbetsblad i Excel-fil**

Se gärna den här artikeln relaterat till detta ämne.

## **Fortsatta ämnen**
- [Beräkna siduppsättningsskalningsfaktorn](/cells/sv/java/calculate-page-setup-scaling-factor/)
- [Kopiera siduppsättning inställningar från källkalkylblad till destinations kalkylblad](/cells/sv/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Avgöra om sidstorleken för arbetsbladet är automatisk](/cells/sv/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [Hämta Pappersbredd och Höjd från PageSetup på Arbetsbladet](/cells/sv/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [Implementera anpassad pappersstorlek för arbetsblad för rendering](/cells/sv/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Sidlayout- och utskriftsalternativ](/cells/sv/java/page-setup-and-printing-options/)
- [Ta bort befintliga skrivareinställningar för arbetsblad i Excel-fil](/cells/sv/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
