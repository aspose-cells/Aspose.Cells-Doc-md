---
title: Datafiltrering
type: docs
weight: 60
url: /sv/java/data-filtering/
---

{{% alert color="primary" %}}

Microsoft Excel tillhandahåller några bra funktioner för att filtrera arbetsbladsdata. Aspose.Cells stöder fullt ut Microsoft Excels autofilterfunktioner. Den här artikeln förklarar hur man använder funktionerna i Microsoft Excel och hur man kodar dem med hjälp av Aspose.Cells.

{{% /alert %}}

## **Autofilterdata**

Autofiltrering är det snabbaste sättet att välja endast de poster från arbetsbladet som du vill visa i en lista. Autofilterfunktionen gör det möjligt för användare att filtrera poster i en lista enligt ett angivet kriterium. Filtrera baserat på text, nummer eller datum.

### **Autofilter i Microsoft Excel**

För att aktivera autofilterfunktionen i Microsoft Excel:

1. Klicka på den rubrikraden i en arbetsbok.
1. Från **Data**-menyn väljer du **Filter** och sedan **Autofilter**.

När du tillämpar ett autofilter på en arbetsbok visas filteromkopplare (svarta pilar) till höger om kolumnrubrikerna.

1. Klicka på en filterpil för att se en lista över filteralternativ.

Några av autofilteralternativen är:

|**Alternativ**|**Beskrivning**|
| :- | :- |
|All|Visa alla poster i listan en gång.|
|Custom|Anpassa filterkriterier som innehåller/inte innehåller|
|Filter by Color|Filter baserat på fyllningsfärg|
|Date Filters|Filtrera rader baserat på olika kriterier på datum|
|Number Filters|Olika typer av filter för nummer såsom jämförelse, medelvärden och Topp 10 osv.
|Text Filters|Olika filter som börjar med, slutar med, innehåller osv.|
|Blanks/Non Blanks|Dessa filter kan implementeras genom textfilter Tom|
Användare filtrerar manuellt sina arbetsboksdata i Microsoft Excel med dessa alternativ.

### **Autofilter med Aspose.Cells**

Aspose.Cells tillhandahåller en klass, {0 som representerar en Excel-fil. {1}klassen innehåller en {2}som ger åtkomst till varje kalkylblad i Excel-filen.

En arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad. För att skapa en autofilter, använd [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)-egenskapen för klassen [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Egenskapen [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) är ett objekt av klassen [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter), som tillhandahåller [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range)-egenskapen för att ange området för celler som utgör en rubrikrad. En autofilter tillämpas på området med celler som utgör rubrikraden.

I varje arbetsblad kan du endast ange ett filterområde. Detta är begränsat av Microsoft Excel. För anpassad datatfiltrering, använd metoden [**AutoFilter.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom-int-int-java.lang.Object-).

I det angivna exemplet nedan har vi skapat samma autofilter med Aspose.Cells som vi skapade med Microsoft Excel i avsnittet ovan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **Olika typer av filter**

Aspose.Cells tillhandahåller flera alternativ för att använda olika typer av filter som färgfilter, datumfilter, nummerfilter, textfilter, blanka filter och icke-blanka filter.

##### **Fyllfärg**

Aspose.Cells tillhandahåller en funktion [**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter-int-int-com.aspose.cells.CellsColor-com.aspose.cells.CellsColor-) för att filtrera data baserat på fyllningsfärgsegenskapen hos cellerna. I det givna exemplet används en mallfil med olika fyllningsfärger i den första kolumnen på arket för att testa färgfiltreringsfunktionen. Följande filer kan hämtas för att kontrollera funktionaliteten.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **Datum**

Olika typer av datumfilter kan implementeras, som att filtrera alla rader med datum i januari 2018. Följande kodexempel demonstrerar detta filter med användning av funktionen [**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter-int-int-int-int-int-int-int-int-). Följande filer kan användas för att testa denna funktionalitet.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **Dynamiskt datum**

Ibland krävs dynamiska filter baserat på ett datum, som alla celler med datum i januari oavsett år. I detta fall används funktionen [**DynamicFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter-int-int-) enligt det följande kodexemplet. Följande filer kan användas för att testa.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **Nummer**

Anpassade filter kan tillämpas med hjälp av Aspose.Cells, t.ex. genom att välja celler med nummer mellan ett givet intervall. Följande exempel visar användningen av [**custom()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom-int-int-java.lang.Object-)-funktionen för att filtrera nummer. Exempelfilerna kan laddas ner från följande länkar.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **Text**

Om en kolumn innehåller text och celler ska väljas som innehåller särskild text, kan [**filter()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter-int-java.lang.String-)-funktionen användas. I följande exempel innehåller mallfilen en lista med länder och raden ska väljas som innehåller ett specifikt land. Följande kod visar filtrering av text med hjälp av de bifogade exempelfilerna.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **Tomma**

Om en kolumn innehåller text så att några celler är tomma, och filtrering krävs för att endast välja de rader där tomma celler finns, kan [**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks-int-)-funktionen användas enligt nedan. Exempelfilerna kan laddas ner från följande länkar.

1. [Tomma.xlsx](72417324.xlsx)
1. [FiltreradeTomma.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **Ej tomma**

När celler med text ska filtreras, använd [**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks-int-)-filterfunktionen enligt nedan. Exempelfilerna kan laddas ner från följande länkar.

1. [Tomma.xlsx](72417324.xlsx)
1. [FiltreradeEjTomma.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **Anpassat filter med Innehåller**

Excel tillhandahåller anpassade filter för att filtrera rader som innehåller en specifik sträng. Denna funktion finns i Aspose.Cells och visas nedan genom att filtrera namnen i exempelfilen. Exempelfilerna kan laddas ner från följande länkar.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **Anpassat filter med EjInnehåller**

Excel tillhandahåller anpassade filter för att filtrera rader som inte innehåller en specifik sträng. Denna funktion finns i Aspose.Cells och visas nedan genom att filtrera namnen i exempelfilen nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **Anpassat filter med BörjaMed**

Excel tillhandahåller anpassade filter för att filtrera rader som börjar med en specifik sträng. Denna funktion finns i Aspose.Cells och visas nedan genom att filtrera namnen i exempelfilen nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **Anpassat filter med SlutaMed**

Excel tillhandahåller anpassade filter för att filtrera rader som slutar med en specifik sträng. Denna funktion finns i Aspose.Cells och visas nedan genom att filtrera namnen i exempelfilen nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **Fortsatta ämnen**
- [Tillämpa Avancerat Filter i Microsoft Excel för att Visa Poster som Uppfyller Komplexa Kriterier](/cells/sv/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Hämta alla dolda radindex efter uppdatering av autofilter](/cells/sv/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

{{< app/cells/assistant language="java" >}}
