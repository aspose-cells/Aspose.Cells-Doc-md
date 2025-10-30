---
title: Datafiltrering
type: docs
weight: 85
url: /sv/python-net/data-filtering/
description: Lär dig hur man lägger till datamängdsfilter genom att använda Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Lägg till filter efter färg, Lägg till datumfilter, Lägg till numeriska filter, Lägg till dynamiskt filter, Lägg till textfilter, Lägg till anpassat filter med Innehåller, Lägg till anpassat filter med Innehåller inte, Lägg till anpassat filter med Börjar med, Lägg till anpassat filter med Slutar med
---

{{% alert color="primary" %}}

Microsoft Excel erbjuder några bra funktioner för att automatiskt filtrera kalkylbladsdata. Aspose.Cells for Python via .NET stöder fullt ut Microsoft Excels autofilterfunktioner. Den här artikeln förklarar hur man använder funktionerna i Microsoft Excel och hur man kodar dem med hjälp av Aspose.Cells for Python via .NET.

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

### **Autofilter med Aspose.Cells for Python Excel Library**

Aspose.Cells for Python via .NET tillhandahåller en klass, Arbetsbok, som representerar en Excel-fil. Arbetsboksklassen innehåller en Kalkylbladssamling som möjliggör åtkomst till varje kalkylblad i Excel-filen.

En arbetsbok representeras av klassen Worksheet. Worksheet-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsböcker. För att skapa ett autofilter, använd AutoFilter-egenskapen i Worksheet-klassen. AutoFilter-egenskapen är en instans av klassen AutoFilter, som ger Range-egenskapen för att ange den rad med celler som utgör en rubrikrad. Ett autofilter appliceras på cellområdet som är rubrikraden.

I varje arbetsbok kan du endast ange ett filterområde. Detta är begränsat av Microsoft Excel. För anpassad datafiltrering, använd AutoFilter.Custom-metoden.

I exemplet nedan har vi skapat samma autofilter med Aspose.Cells for Python via .NET som vi skapade med Microsoft Excel i avsnittet ovan.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterData-1.py" >}}

#### **Olika typer av filter**

Aspose.Cells for Python via .NET erbjuder flera alternativ för att tillämpa olika typer av filter som färgfilter, datorfilter, numeriskt filter, textfilter, tomma filter och icke-tomma filter.

##### **Fyllfärg**

Aspose.Cells for Python via .NET erbjuder en funktion för att lägga till fyllnadsfärgfilter för att filtrera data baserat på cellernas fyllnadsfärgsegenskap. I exemplet nedan används en mallfil som har olika fyllnadsfärger i den första kolumnen i arket för att testa färgfiltreringsfunktionen. Exempelfilerna kan laddas ner från följande länkar.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterColor-1.py" >}}

##### **Datum**

Olika typer av datumsfilter kan implementeras för att filtrera alla rader med datum i januari 2018. Följande exempelkod demonstrerar detta filter using AddDateFilter-funktionen. Exempelfiler ges nedan.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDate-1.py" >}}

##### **Dynamiskt datum**

Ibland krävs dynamiska filter baserat på datum som alla celler med datum i januari oavsett år. I detta fall används DynamicFilter-funktionen enligt det följande exempelkodet. Exempelfiler ges nedan.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDynamicFilter-1.py" >}}

##### **Nummer**

Anpassade filter kan användas med Aspose.Cells for Python via .NET såsom att välja celler som har nummer mellan en given omfattning. Följande exempel demonstrerar användningen av Custom() funktionen för att filtrera nummer. Exempelfiler ges nedan.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNumber-1.py" >}}

##### **Text**

Om en kolumn innehåller text och celler ska väljas som innehåller särskild text, kan Filter-funktionen användas. I följande exempel, innehåller mallfilen en lista över länder och en rad ska väljas som innehåller ett visst landsnamn. Följande kod demonstrerar filtrering av text. Exempelfiler ges nedan.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterText-1.py" >}}

##### **Tomma**

Om en kolumn innehåller text så att några celler är tomma och det krävs ett filter för att välja de rader där tomma celler finns, kan MatchBlanks-funktionen användas enligt nedan demonstrerat. Exempelfiler ges nedan.

1. [Tomma.xlsx](72417324.xlsx)
1. [FiltreradeTomma.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterBlank-1.py" >}}

##### **Ej tomma**

När celler med text ska filtreras, använd MatchNonBlanks filterfunktion enligt nedan. Exempelfiler ges nedan.

1. [Tomma.xlsx](72417324.xlsx)
1. [FiltreradeEjTomma.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNonBlank-1.py" >}}

##### **Anpassat filter med Innehåller**

Excel tillhandahåller anpassade filter som filterrader som innehåller någon specifik sträng. Den här funktionen finns i Aspose.Cells for Python via .NET och demonstreras nedan genom att filtrera namnen i den angivna exempelfilen. Exempelfiler ges nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-Contains-1.py" >}}

##### **Anpassat filter med EjInnehåller**

Excel tillhandahåller anpassade filter som filterrader som inte innehåller någon specifik sträng. Den här funktionen finns i Aspose.Cells for Python via .NET och demonstreras nedan genom att filtrera namnen i den angivna exempelfilen.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-NotContains-1.py" >}}

##### **Anpassat filter med BörjaMed**

Excel tillhandahåller anpassade filter som filterrader som börjar med någon specifik sträng. Den här funktionen finns i Aspose.Cells for Python via .NET och demonstreras nedan genom att filtrera namnen i den angivna exempelfilen.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterBeginsWith-1.py" >}}

##### **Anpassat filter med SlutaMed**

Excel tillhandahåller anpassade filter som filterrader som slutar med någon specifik sträng. Den här funktionen finns i Aspose.Cells for Python via .NET och demonstreras nedan genom att filtrera namnen i den angivna exempelfilen.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterEndsWith-1.py" >}}

## **Fortsatta ämnen**
- [Tillämpa Avancerat Filter i Microsoft Excel för att Visa Poster som Uppfyller Komplexa Kriterier](/cells/sv/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Hämta alla dolda radindex efter uppdatering av autofilter](/cells/sv/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
{{< app/cells/assistant language="python-net" >}}
