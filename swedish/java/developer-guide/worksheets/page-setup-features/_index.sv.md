---
title: Sidinställningsfunktioner
type: docs
weight: 40
url: /sv/java/page-setup-features/
---
Ibland är det nödvändigt att konfigurera sidinställningar för kalkylblad för att styra utskriften. Dessa sidinställningar erbjuder olika alternativ.

**Sidalternativ** 

![todo:image_alt_text](page-setup-features_1.png)

Alternativ för sidinställningar stöds fullt ut i Aspose.Cells. Den här artikeln förklarar hur du ställer in sidalternativ med Aspose.Cells.

## **Ställa in sidalternativ**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , som representerar en Microsoft Excel-fil. Klassen Workbook innehåller en kalkylbladssamling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass.

Klassen Worksheet tillhandahåller egenskapen PageSetup, som används för att ställa in sidinställningar. Egenskapen PageSetup är faktiskt ett objekt av klassen PageSetup som gör det möjligt att ställa in sidlayoutalternativ för ett utskrivet kalkylblad. Klassen PageSetup tillhandahåller olika egenskaper som används för att ställa in sidinställningar. Några av dessa egenskaper diskuteras nedan.

### **Sidorientering**

Sidorienteringen kan ställas in på stående eller liggande med hjälp av[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) klass'[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) metod. De[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) metoden tar[**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) uppräkning som en parameter. Medlemmarna i[**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) uppräkningar listas nedan.

|**Sidorienteringstyper**|**Beskrivning**|
|:- |:- |
|[**LANDSKAP**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|Landskapsorientering|
|[**PORTRÄTT**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|Stående format|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **Skalningsfaktor**

 Det är möjligt att minska eller förstora ett kalkylblads storlek genom att justera skalfaktorn med[**setZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom) metod för[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) klass.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **FitToPages-alternativ**

 För att anpassa innehållet i kalkylbladet till ett visst antal sidor, använd[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) klass'[**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) och[**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide) metoder. Dessa metoder används också för att skala kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **Pappersformat**

 Ställ in pappersstorleken som kalkylbladen ska skrivas ut till med hjälp av[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) klass'[**Pappersformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize) fast egendom. Egenskapen PaperSize accepterar ett av de fördefinierade värdena i[**PaperSizeType**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType) uppräkning, listad nedan.

|**Pappersstorlekstyper**|**Beskrivning**|
|:- |:- |
|Papper 10x14|10 tum x 14 tum.|
|Papper 11x17|11 tum x 17 tum.|
|PapperA3|A3 (297 mm x 420 mm)|
|PapperA4|A4 (210 mm x 297 mm)|
|PaperA4Small|A4 Small (210 mm x 297 mm)|
|PapperA5|A5 (148 mm x 210 mm)|
|PapperB3|B3 (13,9 x 19,7 tum)|
|PapperB4|B4 (250 mm x 354 mm)|
|PapperB5|B5 (182 mm x 257 mm)|
|PaperBusinessCard|Visitkort (90 mm x 55 mm)|
|Pappersark|C storlek blad|
|Pappersark|D storlek blad|
|Papperskuvert10|Kuvert #10 (4-1/8 tum x 9-1/2 tum)|
|Papperskuvert11|Kuvert #11 (4-1/2 tum x 10-3/8 tum)|
|Papperskuvert12|Kuvert #12 (4-1/2 tum x 11 tum)|
|Papperskuvert14|Kuvert #14 (5 tum x 11-1/2 tum)|
|Papperskuvert 9|Kuvert #9 (3-7/8 tum x 8-7/8 tum)|
|PaperEnvelopeB4|Kuvert B4 (250 mm x 353 mm)|
|PaperEnvelopeB5|Kuvert B5 (176 mm x 250 mm)|
|PaperEnvelopeB6|Kuvert B6 (176 mm x 125 mm)|
|PaperEnvelopeC3|Kuvert C3 (324 mm x 458 mm)|
|PaperEnvelopeC4|Kuvert C4 (229 mm x 324 mm)|
|PaperEnvelopeC5|Kuvert C5 (162 mm x 229 mm)|
|PaperEnvelopeC6|Kuvert C6 (114 mm x 162 mm)|
|PaperEnvelopeC65|Kuvert C65 (114 mm x 229 mm)|
|PaperEnvelopeDL|Kuvert DL (110 mm x 220 mm)|
|PaperEnvelopeItalien|Kuvert Italien (110 mm x 230 mm)|
|PaperEnvelopeMonarch|Envelope Monarch (3-7/8 tum x 7-1/2 tum)|
|PaperEnvelopePersonligt|Kuvert (3-5/8 tum x 6-1/2 tum)|
|PaperESheet|E-storlek ark|
|PaperExecutive|Executive (7-1/2 tum x 10-1/2 tum)|
|PaperFanfoldLegalGerman|German Legal Fanfold (8-1/2 tum x 13 tum)|
|PaperFanfoldStdGerman|German Standard Fanfold (8-1/2 tum x 12 tum)|
|PaperFanfoldUS|US Standard Fanfold (14-7/8 tum x 11 tum)|
|PaperFolio|Folio (8-1/2 tum x 13 tum)|
|PaperLedger|Ledbok (17 tum x 11 tum)|
|Paper Legal|Legal (8-1/2 tum x 14 tum)|
|PaperLetter|Letter (8-1/2 tum x 11 tum)|
|PaperLetterSmall|Letter Small (8-1/2 tum x 11 tum)|
|PaperNote|Obs (8-1/2 tum x 11 tum)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|PaperStatement|Statement (5-1/2 tum x 8-1/2 tum)|
|PaperTabloid|Tabloid (11 tum x 17 tum)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **Utskriftskvalitet**

 Ställ in utskriftskvaliteten för de arbetsblad som ska skrivas ut med[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) klass'[**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality) metod. Mätenheten för utskriftskvalitet är punkter per tum (DPI).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **Första sidnummer**

 Starta numreringen av kalkylbladssidor med hjälp av[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) klass'[**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber) metod. Metoden setFirstPageNumber ställer in sidnumret på den första kalkylbladssidan och följande sidor numreras i stigande ordning.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **Ställa in marginaler**

Aspose.Cells stöder fullt ut Microsoft Excels sidinställningar. Utvecklare kan behöva konfigurera sidinställningar för kalkylblad för att styra utskriftsprocessen. Det här ämnet diskuterar hur man använder Aspose.Cells för att konfigurera sidmarginaler.

**Sidmarginaler i Microsoft Excel**

![todo:image_alt_text](page-setup-features_2.png)

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Microsoft Excel-fil. Klassen Workbook innehåller Worksheets-samlingen som ger åtkomst till varje kalkylblad i en Excel-fil. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass.

 Klassen Worksheet tillhandahåller egenskapen PageSetup, som används för att ställa in sidinställningar. Attributet PageSetup är ett objekt för[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) klass som gör det möjligt att ställa in olika sidlayoutalternativ för ett utskrivet kalkylblad. Klassen PageSetup tillhandahåller olika egenskaper och metoder som används för att ställa in sidinställningar.

### **Sidmarginaler**

 Ställ in marginalerna (vänster, höger, topp, botten) på en sida med[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) klassmedlemmar. Några av metoderna som används för att ange sidmarginaler listas nedan:

- [**setLeftMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **Centrera på sidan**

 Det är möjligt att centrera något på en sida horisontellt och vertikalt. De[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) klass har medlemmar för detta ändamål:[**ställ in mitten horisontellt**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) och[**setCenterVertikalt**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **Marginaler för sidhuvud och sidfot**

 Ställ in sidhuvuds- och sidfotsmarginaler med[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) medlemmar som t.ex[**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) och[**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **Ställa in sidhuvuden och sidfötter**

Sidhuvuden och sidfötter är avsnitten av text och bilder ovanför den övre marginalen eller under den nedre marginalen på en sida. Det är möjligt att lägga till sidhuvuden och sidfötter till kalkylblad också. Sidhuvuden och sidfötter kan användas för att visa all slags användbar information, till exempel sidnummer, författarens namn, dokumenttitel eller datum och tid. Sidhuvuden och sidfötter hanteras också med hjälp av dialogrutan Utskriftsformat.

**Dialogrutan Utskriftsformat** 

![todo:image_alt_text](page-setup-features_3.png)

Aspose.Cells gör det möjligt att lägga till sidhuvud och sidfot till kalkylbladen under körning, men det rekommenderas att sidhuvuden och sidfötter ställs in manuellt i en fördesignad fil för utskrift. Du kan använda Microsoft Excel som ett GUI-verktyg för att enkelt ställa in sidhuvuden och sidfötter för att minska utvecklingstiden. Aspose.Cells kan importera filen och reservera dessa inställningar.

För att lägga till sidhuvuden och sidfötter under körning tillhandahåller Aspose.Cells speciella klasser och några skriptkommandon för att styra formateringen.

### **Skriptkommandon**

Skriptkommandon är speciella kommandon som tillhandahålls av Aspose.Cells som tillåter utvecklare att formatera sidhuvuden och sidfötter.

|**Skriptkommandon**|**Beskrivning**|
|:- |:- |
|&P|Aktuellt sidnummer.|
|&G|En bild.|
|&N|Det totala antalet sidor.|
|&D|Det aktuella datumet.|
|&T|Den aktuella tiden.|
|&A|Arbetsbladets namn.|
|&F|Filnamnet utan sökvägen.|
|&"\<FontName>"|Ett teckensnittsnamn. Till exempel: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Ett teckensnittsnamn med en stil. Till exempel: &"Arial,Fet"|
|&\<FontSize>|Representerar teckenstorlek. Till exempel: "&14abc". Men om detta kommando följs av ett vanligt nummer som ska skrivas ut i rubriken, bör detta separeras med ett mellanslag från teckenstorleken. Till exempel: "&14 123".|

### **Ställ in sidhuvuden och sidfötter**

 De[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) klass tillhandahåller metod[**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader(int,%20java.lang.String) för att lägga till en rubrik och[**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter(int,%20java.lang.String)) för att lägga till en sidfot i ett kalkylblad. Skriptet används som argument för alla ovan nämnda metoder. Det representerar skriptet som ska användas för sidhuvud eller sidfot. Det här skriptet innehåller skriptkommandon för att formatera sidhuvuden eller sidfötter.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **Infoga en grafik i en sidhuvud eller sidfot**

 De[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) klass har metoderna[**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture(int,%20byte[]) ) och[**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture(int,%20byte[])) för att lägga till bilder i ett kalkylblads sidhuvud och sidfot. Dessa metoder tar två parametrar:

- **Sektion**, den del av sidhuvudet eller sidfoten där bilden kommer att placeras. Det finns tre sektioner: vänster, mitten och höger, representerade av de numeriska värdena 0, 1 respektive 2.
- **File InputStream**, de grafiska uppgifterna. Den binära datan bör skrivas in i bufferten i en byte-array.

Efter att ha kört koden och öppnat filen, kontrollera kalkylbladets rubrik i Microsoft Excel:

1.  På**Fil** menyn, välj**Utskriftsformat**.
1.  I dialogrutan Utskriftsformat väljer du**Sidhuvud/sidfot** flik.

**Infoga en grafik i en sidhuvud/sidfot** 

![todo:image_alt_text](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **Infoga en grafik endast i första sidans sidhuvud**

 De[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) class har också andra användbara metoder, till exempel[**setPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture(boolean,%20boolean,%20boolean,%20int,%20byte[])), [**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader(int,%20java.lang.String)), [**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter(int,%20java.lang.String)), för att lägga till bilder i ett kalkylblads sidhuvud/sidfot på första sidan. Den första sidan är en speciell sida: det är vanligt att man vill att den ska visa speciell information, till exempel en företagslogotyp.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **Ställa in utskriftsalternativ**

Microsoft Excels sidinställningar ger flera utskriftsalternativ (även kallade arkalternativ) som låter användare styra hur kalkylbladssidor skrivs ut. Dessa utskriftsalternativ tillåter användare att:

- Välj ett specifikt utskriftsområde på ett kalkylblad.
- Skriv ut titlar.
- Skriv ut rutnät.
- Skriv ut rad- och kolumnrubriker
- Uppnå dragkvalitet.
- Skriv ut kommentarer.
- Utskriftscellfel.
- Definiera sidordning.

Alla dessa utskriftsalternativ visas nedan.

**Alternativ för utskrift (ark).** 

![todo:image_alt_text](page-setup-features_5.png)

### **Ställa in utskrifts- och arkalternativ**

 spose.Cells stöder alla utskriftsalternativ som erbjuds av Microsoft Excel och utvecklare kan enkelt konfigurera dessa alternativ för kalkylblad med hjälp av egenskaperna som erbjuds av[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)klass. Hur dessa egenskaper används diskuteras mer i detalj nedan.

### **Ställ in utskriftsområde**

Som standard innehåller endast utskriftsområdet alla delar av kalkylbladet som innehåller data. Utvecklare kan skapa ett specifikt utskriftsområde i kalkylbladet.

 För att välja ett specifikt utskriftsområde, använd[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) klass'[**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea) fast egendom. Tilldela den här egenskapen ett cellområde som definierar utskriftsområdet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **Ställ in utskriftsrubriker**

 Aspose.Cells låter dig ange rad- och kolumnrubriker som ska upprepas på alla sidor i ett utskrivet kalkylblad. För att göra det, använd[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) klass'[**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns) och[**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows) egenskaper.

Raderna eller kolumnerna som kommer att upprepas definieras genom att skicka deras rad- eller kolumnnummer. Till exempel definieras rader som $1:$2 och kolumner definieras som $A:$B.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **Ställ in andra utskriftsalternativ**

 De[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) class tillhandahåller även flera andra egenskaper för att ställa in allmänna utskriftsalternativ enligt följande:

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines), en boolesk egenskap som definierar om rutnät ska skrivas ut eller inte.
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings), en boolesk egenskap som definierar om rad- och kolumnrubriker ska skrivas ut eller inte.
- [**setBlackAndWhite**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite), en boolesk egenskap som definierar om kalkylblad ska skrivas ut i svartvitt läge eller inte.
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments), definierar om utskriftskommentarerna ska visas på kalkylbladet eller i slutet av kalkylbladet.
- [**setPrintDraft**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft), en boolesk egenskap som definierar om kalkylblad ska skrivas ut i utkastkvalitet eller inte.
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), definierar om cellfel ska skrivas ut som visas, tomt, streck eller ej.

 För att ställa in[**Skriv ut Kommentarer**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) och[**PrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) egenskaper, Aspose.Cells ger också två uppräkningar,[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) och[**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) som innehåller fördefinierade värden som ska tilldelas till[**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) och[**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) fastigheter respektive.

 De fördefinierade värdena i[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) uppräkning beskrivs nedan.

|**Skriv ut Kommentarstyper**|**Beskrivning**|
|:- |:- |
|[**PRINT_IN_PLACE**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_IN_PLACE)|Anger att kommentarer ska skrivas ut som de visas på kalkylbladet.|
|[**PRINT_NO_COMMENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_NO_COMMENTS)|Anger att kommentarer inte ska skrivas ut.|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_SHEET_END)|Anger att kommentarer ska skrivas ut i slutet av kalkylbladet.|

 De fördefinierade värdena för[**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) uppräkning beskrivs nedan.

|**Typer av utskriftsfel**|**Beskrivning**|
|:- |:- |
|[*PRINT_ERRORS_BLANK*](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_BLANK)|Anger att inte skriva ut fel.|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DASH)|Anger utskriftsfel som "--".|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DISPLAYED)|Anger utskriftsfel som visas.|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_NA)|Anger utskriftsfel som "#N/A".|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **Ställ in sidordning**

 De[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) klass ger[**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) egenskap som används för att beställa flera sidor i ditt kalkylblad som ska skrivas ut. Det finns två möjligheter att beställa sidorna enligt följande:

- **Ner och sedan över** skriver ut alla sidor innan du skriver ut några sidor till höger.
- **Över sedan ner** skriver ut sidor från vänster till höger innan några sidor nedan skrivs ut.

 Aspose.Cells tillhandahåller en uppräkning,[**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) , som innehåller alla fördefinierade ordertyper som ska tilldelas[**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) metod.

 De fördefinierade värdena för[**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) uppräkning beskrivs nedan.

|**Skriv ut beställningstyper**|**Beskrivning**|
|:- |:- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN_THEN_OVER)|Skriv ut och sedan över.|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER_THEN_DOWN)|Skriv ut över och sedan ner.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **Ta bort befintliga skrivarinställningar för arbetsblad i Excel-fil**

Se den här artikeln om detta ämne.

## **Förhandsämnen**
- [Beräkna skalningsfaktor för sidinställningar](/cells/sv/java/calculate-page-setup-scaling-factor/)
- [Kopiera inställningar för sidinställningar från källarbetsbladet till målarbetsbladet](/cells/sv/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Bestäm om arbetsbladets pappersstorlek är Automatisk](/cells/sv/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [Få papperets bredd och höjd från PageSetup av arbetsbladet](/cells/sv/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [Implementera anpassad pappersstorlek på arbetsbladet för rendering](/cells/sv/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Sidinställningar och utskriftsalternativ](/cells/sv/java/page-setup-and-printing-options/)
- [Ta bort befintliga skrivarinställningar för arbetsblad i Excel-fil](/cells/sv/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
