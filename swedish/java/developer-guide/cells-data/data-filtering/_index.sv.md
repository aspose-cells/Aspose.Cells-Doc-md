---
title: Datafiltrering
type: docs
weight: 60
url: /sv/java/data-filtering/
---
{{% alert color="primary" %}}

Microsoft Excel tillhandahåller några bra funktioner för att autofiltrera kalkylbladsdata. Aspose.Cells stöder fullt ut Microsoft Excels autofilterfunktioner. Den här artikeln förklarar hur du använder funktionerna i Microsoft Excel och hur du kodar dem med Aspose.Cells.

{{% /alert %}}

## **Autofiltrera data**

Autofiltrering är det snabbaste sättet att bara välja de objekt från kalkylbladet som du vill visa i en lista. Autofiltreringsfunktionen tillåter användare att filtrera objekt i en lista enligt ett bestämt kriterium. Filtrera baserat på text, siffror eller datum.

### **Autofilter i Microsoft Excel**

Så här aktiverar du autofilterfunktionen i Microsoft Excel:

1. Klicka på rubrikraden i ett kalkylblad.
1. Från**Data**menyn, välj**Filtrera**och då**AutoFilter**.

När du använder ett autofilter på ett kalkylblad visas filteromkopplare (svarta pilar) till höger om kolumnrubrikerna.

1. Klicka på en filterpil för att se en lista med filteralternativ.

Några av autofilteralternativen är:

|**alternativ**|**Beskrivning**|
|:- |:- |
|Allt|Visa alla objekt i listan en gång.|
|Beställnings|Anpassa filterkriterier som innehåller/innehåller inte|
|Filtrera efter färg|Filter baserat på fylld färg|
|Datumfilter|Filtrerar rader baserat på olika kriterier på datum|
|Nummerfilter|Olika typer av filter på siffror som jämförelse, medelvärden och Top 10 etc.|
|Textfilter|Olika filter som börjar med, slutar med, innehåller etc,|
|Blanks/Non Blanks|Dessa filter kan implementeras genom Text Filter Blank|
Användare filtrerar sina kalkylbladsdata manuellt i Microsoft Excel med dessa alternativ.

### **Autofilter med Aspose.Cells**

Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)som representerar en Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)klass innehåller en[**Arbetsbladssamling**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)som ger åtkomst till varje kalkylblad i Excel-filen.

Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)klass. De[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)klass tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att skapa ett autofilter, använd[**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)egendom av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)klass. De[**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)egendom är ett föremål för[**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)klass, som ger[**Räckvidd**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range)egenskap för att ange intervallet av celler som utgör en rubrikrad. Ett autofilter tillämpas på cellintervallet som är rubrikraden.

I varje kalkylblad kan du bara ange ett filterintervall. Detta begränsas av Microsoft Excel. För anpassad datafiltrering, använd[**AutoFilter.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) metod.

I exemplet nedan har vi skapat samma autofilter med Aspose.Cells som vi skapade med Microsoft Excel i avsnittet ovan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **Olika typer av filter**

Aspose.Cells ger flera alternativ för att använda olika typer av filter som färgfilter, datumfilter, nummerfilter, textfilter, tomma filter och inga tomma filter.

##### **Fyllnadsfärg**

Aspose.Cells tillhandahåller en funktion[**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter(int,%20int,%20com.aspose.cells.CellsColor,%20com.aspose.cells.CellsColor)för att filtrera data baserat på fyllnadsfärgsegenskapen för cellerna. I exemplet nedan används en mallfil med olika fyllningsfärger i den första kolumnen på arket för att testa färgfiltreringsfunktionen. Följande filer kan laddas ner för att kontrollera funktionaliteten.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **Datum**

Olika typer av datumfilter kan implementeras som att filtrera alla rader med datum i januari 2018. Följande exempelkod visar detta filter med[**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter(int,%20int,%20int,%20int,%20int,%20int,%20int,%20int)) funktion. Följande filer kan användas för att testa denna funktionalitet.

1. [Datum.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **Dynamiskt datum**

Ibland krävs dynamiska filter baserat på ett datum som att alla celler har datum i januari, oavsett år. I detta fall,[**DynamicFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter(int,%20int))-funktionen används enligt följande exempelkod. Följande filer kan användas för testning.

1. [Datum.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **siffra**

Anpassade filter kan tillämpas med Aspose.Cells som att markera celler med nummer mellan ett givet intervall. Följande exempel visar användningen av[**beställnings()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) funktion för att filtrera siffror. Exempelfiler kan laddas ner från följande länkar.

1. [Antal.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **Text**

Om en kolumn innehåller text och celler ska väljas som innehåller viss text,[**filtrera()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter(int,%20java.lang.String)) funktion kan användas. I följande exempel innehåller mallfilen en lista över länder och en rad ska väljas med ett visst landsnamn. Följande kod visar filtrering av text med hjälp av exempelfilerna nedan.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **Blanks**

Om en kolumn innehåller text så att få celler är tomma, och filter krävs för att endast markera de rader där tomma celler finns,[**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks(int))-funktionen kan användas som visas nedan. Exempelfiler kan laddas ner från följande länkar.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **Icke Blanks**

När celler med någon text ska filtreras, använd[**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks(int)) filterfunktion som visas nedan. Exempelfiler kan laddas ner från följande länkar.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **Anpassat filter med Innehåller**

Excel tillhandahåller anpassade filter som filterrader som innehåller en viss sträng. Den här funktionen är tillgänglig i Aspose.Cells och visas nedan genom att filtrera namnen i exempelfilen. Exempelfiler kan laddas ner från följande länkar.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **Anpassat filter med NotContains**

Excel tillhandahåller anpassade filter som filterrader som inte innehåller någon specifik sträng. Den här funktionen är tillgänglig i Aspose.Cells och visas nedan genom att filtrera namnen i exempelfilen nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **Anpassat filter med BeginsWith**

Excel tillhandahåller anpassade filter som filterrader som börjar med en viss sträng. Den här funktionen är tillgänglig i Aspose.Cells och visas nedan genom att filtrera namnen i exempelfilen nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **Anpassat filter med EndsWith**

Excel tillhandahåller anpassade filter som filterrader som slutar med en viss sträng. Den här funktionen är tillgänglig i Aspose.Cells och visas nedan genom att filtrera namnen i exempelfilen nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **Förhandsämnen**
- [Använd avancerat filter i Microsoft Excel för att visa poster som uppfyller komplexa kriterier](/cells/sv/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Få alla dolda rader efter att ha uppdaterat autofiltret](/cells/sv/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

