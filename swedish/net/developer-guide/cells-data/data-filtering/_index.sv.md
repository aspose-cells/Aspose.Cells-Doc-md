---
title: Datafiltrering
type: docs
weight: 85
url: /sv/net/data-filtering/
description: Lär dig hur du lägger till datafilter genom att använda Aspose.Cells for .NET API.
keywords: Lägg till filter efter färg, Lägg till datumfilter, Lägg till nummerfilter, Lägg till dynamiskt filter, Lägg till textfilter, Lägg till anpassat filter med Innehåller, Lägg till anpassat filter med NotContains, Lägg till anpassat filter med Börjar med, Lägg till anpassat filter med Slut på
---

{{% alert color="primary" %}}

Microsoft Excel tillhandahåller några bra funktioner för att filtrera arbetsbladsdata. Aspose.Cells stöder fullt ut Microsoft Excels autofilterfunktioner. Den här artikeln förklarar hur man använder funktionerna i Microsoft Excel och hur man kodar dem med hjälp av Aspose.Cells.

{{% /alert %}}

## **Autofilterdata**

Autofiltrering är det snabbaste sättet att välja endast de poster från arbetsbladet som du vill visa i en lista. Autofilterfunktionen gör det möjligt för användare att filtrera poster i en lista enligt ett angivet kriterium. Filtrera baserat på text, nummer eller datum.

### **Autofilter i Microsoft Excel**

För att aktivera autofilterfunktionen i Microsoft Excel:

1. Klicka på den rubrikraden i en arbetsbok.
1. Från menyn **Data**, välj **Filter** och sedan **AutoFilter**.

När du tillämpar ett autofilter på en arbetsbok visas filteromkopplare (svarta pilar) till höger om kolumnrubrikerna.

1. Klicka på en filterpil för att se en lista över filteralternativ.

Några av autofilteralternativen är:

|**Alternativ**|**Beskrivning**|
| :- | :- |
|All|Visa alla poster i listan en gång.|
|Custom|Anpassa filterkriterier som innehåller/inte innehåller|
|Filter by Color|Filter baserat på fyllningsfärg|
|Date Filters|Filtrera rader baserat på olika kriterier på datum|
|Number Filters|Olika typer av filter på nummer som jämförelse, medeltal och Topp 10 etc.|
|Text Filters|Olika filter som börjar med, slutar med, innehåller osv.|
|Blanks/Non Blanks|Dessa filter kan implementeras genom textfilter Tom|

Användare filtrerar manuellt sina arbetsboksdata i Microsoft Excel med dessa alternativ.

### **Autofilter med Aspose.Cells**

Aspose.Cells tillhandahåller en klass, Workbook, som representerar en Excel-fil. Workbook-klassen innehåller en Worksheets-samling som ger åtkomst till varje arbetsbok i Excel-filen.

En arbetsbok representeras av klassen Worksheet. Worksheet-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsböcker. För att skapa ett autofilter, använd AutoFilter-egenskapen i Worksheet-klassen. AutoFilter-egenskapen är en instans av klassen AutoFilter, som ger Range-egenskapen för att ange den rad med celler som utgör en rubrikrad. Ett autofilter appliceras på cellområdet som är rubrikraden.

I varje arbetsbok kan du endast ange ett filterområde. Detta är begränsat av Microsoft Excel. För anpassad datafiltrering, använd AutoFilter.Custom-metoden.

I det angivna exemplet nedan har vi skapat samma autofilter med Aspose.Cells som vi skapade med Microsoft Excel i avsnittet ovan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

#### **Olika typer av filter**

Aspose.Cells tillhandahåller flera alternativ för att använda olika typer av filter som färgfilter, datumfilter, nummerfilter, textfilter, blanka filter och icke-blanka filter.

##### **Fyllfärg**

Aspose.Cells tillhandahåller en funktion AddFillColorFilter för att filtrera data baserat på fyllfärgsegenskapen hos cellerna. I det angivna exemplet nedan används en mallfil med olika fyllfärger i den första kolumnen i arket för att testa färgfiltreringsfunktionen. Exempelfiler kan laddas ner från följande länkar.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

##### **Datum**

Olika typer av datumsfilter kan implementeras för att filtrera alla rader med datum i januari 2018. Följande exempelkod demonstrerar detta filter using AddDateFilter-funktionen. Exempelfiler ges nedan.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

##### **Dynamiskt datum**

Ibland krävs dynamiska filter baserat på datum som alla celler med datum i januari oavsett år. I detta fall används DynamicFilter-funktionen enligt det följande exempelkodet. Exempelfiler ges nedan.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

##### **Nummer**

Anpassade filter kan appliceras med Aspose.Cells som att välja celler med nummer mellan ett givet intervall. Följande exempel demonstrerar användningen av Custom-funktionen för att filtrera nummer. Exempelfiler ges nedan.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

##### **Text**

Om en kolumn innehåller text och celler ska väljas som innehåller särskild text, kan Filter-funktionen användas. I följande exempel, innehåller mallfilen en lista över länder och en rad ska väljas som innehåller ett visst landsnamn. Följande kod demonstrerar filtrering av text. Exempelfiler ges nedan.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

##### **Tomma**

Om en kolumn innehåller text så att några celler är tomma och det krävs ett filter för att välja de rader där tomma celler finns, kan MatchBlanks-funktionen användas enligt nedan demonstrerat. Exempelfiler ges nedan.

1. [Tomma.xlsx](72417324.xlsx)
1. [FiltreradeTomma.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

##### **Ej tomma**

När celler med text ska filtreras, använd MatchNonBlanks filterfunktion enligt nedan. Exempelfiler ges nedan.

1. [Tomma.xlsx](72417324.xlsx)
1. [FiltreradeEjTomma.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

##### **Anpassat filter med Innehåller**

Excel erbjuder anpassade filter som filtrerar rader som innehåller en specifik sträng. Denna funktion är tillgänglig i Aspose.Cells och demonstreras nedan genom att filtrera namnen i provfilen. Exempelfiler ges nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

##### **Anpassat filter med EjInnehåller**

Excel tillhandahåller anpassade filter för att filtrera rader som inte innehåller en specifik sträng. Denna funktion finns i Aspose.Cells och visas nedan genom att filtrera namnen i exempelfilen nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

##### **Anpassat filter med BörjaMed**

Excel tillhandahåller anpassade filter för att filtrera rader som börjar med en specifik sträng. Denna funktion finns i Aspose.Cells och visas nedan genom att filtrera namnen i exempelfilen nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

##### **Anpassat filter med SlutaMed**

Excel erbjuder anpassade filter som filtrerar rader som slutar med en specifik sträng. Denna funktion är tillgänglig i Aspose.Cells och demonstreras nedan genom att filtrera namnen i provfilen nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}

## **Fortsatta ämnen**
- [Tillämpa Avancerat Filter i Microsoft Excel för att Visa Poster som Uppfyller Komplexa Kriterier](/cells/sv/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Hämta alla dolda radindex efter uppdatering av autofilter](/cells/sv/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
{{< app/cells/assistant language="csharp" >}}
