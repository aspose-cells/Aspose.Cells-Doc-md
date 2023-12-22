---
title: Datafiltrering
type: docs
weight: 85
url: /sv/net/data-filtering/
description: Lär dig hur du lägger till datafilter genom att använda Aspose.Cells for .NET API.
keywords: Add Filter by Color, Add Date Filters, Add Number Filters, Add Dynamic Filter, Add Text Filters, Add custom filter with Contains, Add custom filter with NotContains, Add custom filter with BeginsWith, Add custom filter with EndsWith
---
{{% alert color="primary" %}}

Microsoft Excel tillhandahåller några bra funktioner för att autofiltrera kalkylbladsdata. Aspose.Cells stöder fullt ut Microsoft Excels autofilterfunktioner. Den här artikeln förklarar hur du använder funktionerna i Microsoft Excel och hur du kodar dem med Aspose.Cells.

{{% /alert %}}

##  **Autofiltrera data**

Autofiltrering är det snabbaste sättet att bara välja de objekt från kalkylbladet som du vill visa i en lista. Autofiltreringsfunktionen tillåter användare att filtrera objekt i en lista enligt ett bestämt kriterium. Filtrera baserat på text, siffror eller datum.

###  **Autofilter i Microsoft Excel**

Så här aktiverar du autofilterfunktionen i Microsoft Excel:

1. Klicka på rubrikraden i ett kalkylblad.
1.  Från**Data** menyn, välj**Filtrera** och sedan *Autofilter**.

När du använder ett autofilter på ett kalkylblad visas filteromkopplare (svarta pilar) till höger om kolumnrubrikerna.

1. Klicka på en filterpil för att se en lista med filteralternativ.

Några av autofilteralternativen är:

|**alternativ**|**Beskrivning**|
| :- | :- |
|Allt|Visa alla objekt i listan en gång.|
|Beställnings|Anpassa filterkriterier som innehåller/innehåller inte|
|Filtrera efter färg|Filter baserat på fylld färg|
|Datumfilter|Filtrerar rader baserat på olika kriterier på datum|
|Nummerfilter|Olika typer av filter på siffror som jämförelse, medelvärden och Top 10 etc.|
|Textfilter|Olika filter som börjar med, slutar med, innehåller etc,|
|Blanks/Non Blanks|Dessa filter kan implementeras genom Text Filter Blank|

Användare filtrerar sina kalkylbladsdata manuellt i Microsoft Excel med dessa alternativ.

###  **Autofilter med Aspose.Cells**

Aspose.Cells tillhandahåller en klass, arbetsbok som representerar en Excel-fil. Klassen Workbook innehåller en kalkylbladssamling som ger åtkomst till varje kalkylblad i Excel-filen.

Ett kalkylblad representeras av klassen Worksheet. Klassen Worksheet tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att skapa ett autofilter, använd egenskapen AutoFilter för klassen Worksheet. AutoFilter-egenskapen är ett objekt i klassen AutoFilter, som tillhandahåller Range-egenskapen för att ange intervallet av celler som utgör en rubrikrad. Ett autofilter tillämpas på cellintervallet som är rubrikraden.

I varje kalkylblad kan du bara ange ett filterintervall. Detta begränsas av Microsoft Excel. För anpassad datafiltrering, använd metoden AutoFilter.Custom.

I exemplet nedan har vi skapat samma autofilter med Aspose.Cells som vi skapade med Microsoft Excel i avsnittet ovan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

####  **Olika typer av filter**

Aspose.Cells ger flera alternativ för att använda olika typer av filter som färgfilter, datumfilter, nummerfilter, textfilter, tomma filter och inga tomma filter.

#####  **Fyllnadsfärg**

Aspose.Cells tillhandahåller en funktion AddFillColorFilter för att filtrera data baserat på fyllningsfärgsegenskapen för cellerna. I exemplet nedan används en mallfil med olika fyllningsfärger i den första kolumnen på arket för att testa färgfiltreringsfunktionen. Exempelfiler kan laddas ner från följande länkar.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

#####  **Datum**

Olika typer av datumfilter kan implementeras som att filtrera alla rader med datum i januari 2018. Följande exempelkod visar detta filter med AddDateFilter-funktionen. Exempelfiler ges nedan.

1. [Datum.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

#####  **Dynamiskt datum**

Ibland krävs dynamiska filter baserat på datum som att alla celler har datum i januari, oavsett år. I det här fallet används DynamicFilter-funktionen som anges i följande exempelkod. Exempelfiler ges nedan.

1. [Datum.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

#####  **siffra**

Anpassade filter kan tillämpas med Aspose.Cells som att markera celler med nummer mellan ett givet intervall. Följande exempel visar användningen av Custom()-funktionen för att filtrera siffror. Exempelfiler ges nedan.

1. [Antal.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

#####  **Text**

Om en kolumn innehåller text och celler ska väljas som innehåller viss text, kan Filter()-funktionen användas. I följande exempel innehåller mallfilen en lista över länder och en rad ska väljas med ett visst landsnamn. Följande kod visar filtrering av text. Exempelfiler ges nedan.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

#####  **Blanks**

Om en kolumn innehåller text så att få celler är tomma, och filter krävs för att välja de rader endast där tomma celler finns, kan MatchBlanks()-funktionen användas som visas nedan. Exempelfiler ges nedan.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

#####  **Icke Blanks**

När celler som har någon text ska filtreras, använd MatchNonBlanks filterfunktion som visas nedan. Exempelfiler ges nedan.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

#####  **Anpassat filter med Innehåller**

Excel tillhandahåller anpassade filter som filterrader som innehåller en viss sträng. Den här funktionen är tillgänglig i Aspose.Cells och visas nedan genom att filtrera namnen i exempelfilen. Exempelfiler ges nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

#####  **Anpassat filter med NotContains**

Excel tillhandahåller anpassade filter som filterrader som inte innehåller någon specifik sträng. Den här funktionen är tillgänglig i Aspose.Cells och visas nedan genom att filtrera namnen i exempelfilen nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

#####  **Anpassat filter med BeginsWith**

Excel tillhandahåller anpassade filter som filterrader som börjar med en viss sträng. Den här funktionen är tillgänglig i Aspose.Cells och visas nedan genom att filtrera namnen i exempelfilen nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

#####  **Anpassat filter med EndsWith**

Excel tillhandahåller anpassade filter som filterrader som slutar med någon specifik sträng. Den här funktionen är tillgänglig i Aspose.Cells och visas nedan genom att filtrera namnen i exempelfilen nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}

##  **Förhandsämnen**
- [Använd avancerat filter av Microsoft Excel för att visa poster som uppfyller komplexa kriterier](/cells/sv/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Få alla dolda rader efter att ha uppdaterat autofiltret](/cells/sv/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
