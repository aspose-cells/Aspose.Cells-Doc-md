---
title: Hur man filtrerar tomma eller icke-tomma
type: docs
weight: 85
url: /sv/net/how-to-filter-blanks-and-non-blanks/
description: Lär dig hur du filtrerar tomma och icke-tomma genom att använda Aspose.Cells for .NET API.
keywords: Filter Blanks, Filter Non-Blanks, Filter Blanks in worksheet, Filter Non-Blanks in worksheet, Filter Blanks in excel, Filter Non-Blanks in excel, Filter Blanks and Non-Blanks in excel
---
##  **Möjliga användningsscenarier**
Filtrera data i Excel är ett värdefullt verktyg som förbättrar dataanalys, utforskning och presentation genom att göra det möjligt för användare att fokusera på specifika delmängder av data baserat på deras kriterier, vilket gör den övergripande datamanipuleringen och tolkningsprocessen mer effektiv och effektiv.

##  **Hur man filtrerar tomma eller icke-tomma i Excel**
I Excel kan du enkelt filtrera tomma eller icke-tomma med hjälp av filtreringsalternativen. Så här kan du göra det:

###  **Hur man filtrerar tomrum i Excel**
1. Välj intervall: Klicka på bokstaven i kolumnrubriken för att välja hela kolumnen eller välj intervallet där du vill filtrera tomrum.
1. Öppna filtermenyn: Gå till fliken "Data" i menyfliksområdet.
<br>
<image src="1.png" width="70%" />
1. Filteralternativ: Klicka på knappen "Filter". Detta kommer att lägga till filterpilar till det valda intervallet.
1. Filtrera tomrum: Klicka på filterpilen i kolumnen där du vill filtrera tomrum. Avmarkera alla alternativ utom "Tomrum" och klicka på OK. Detta visar endast de tomma cellerna i den kolumnen.
<br>
<image src="2.png" width="70%" />
1. Resultatet som följer:
<br>
<image src="3.png" width="70%" />

###  **Hur man filtrerar icke-tomma ämnen i Excel**
1. Välj intervall: Klicka på bokstaven i kolumnrubriken för att välja hela kolumnen eller välj intervallet där du vill filtrera icke-tomma.
1. Öppna filtermenyn: Gå till fliken "Data" i menyfliksområdet.
<br>
<image src="1.png" width="70%" />
1. Filteralternativ: Klicka på knappen "Filter". Detta kommer att lägga till filterpilar till det valda intervallet.
1. Filtrera icke-tomma: Klicka på filterpilen i kolumnen du vill filtrera icke-tomma. Avmarkera alla alternativ utom "Non-toms" eller "Custom" och ställ in villkoren därefter. Klicka på OK. Detta visar bara de celler som inte är tomma i den kolumnen.
<br>
<image src="4.png" width="70%" />
1. Resultatet som följer:
<br>
<image src="5.png" width="70%" />

##  **Hur man filtrerar ämnen med Aspose.Cells**
 Om en kolumn innehåller text så att få celler är tomma, och filter krävs för att endast markera de rader där tomma celler finns,[AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchblanks/) och[AutoFilter.AddFilter(int fieldIndex, strängkriterier)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/addfilter/) funktioner kan användas som visas nedan.

 Se följande exempelkod som laddar[exempel på Excel-fil](sample.xlsx) som innehåller lite dummydata. Exempelkoden använder tre metoder för att filtrera tomma ämnen. Den sparar sedan arbetsboken som[utdata Excel-fil](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-blanks.cs" >}}

##  **Hur man filtrerar icke-tomma med Aspose.Cells**

 Se följande exempelkod som laddar[exempel på Excel-fil](sample.xlsx) som innehåller lite dummydata. Efter att ha laddat filen, ring[AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchnonblanks/) funktion för att filtrera icke tomma data och slutligen spara arbetsboken som[utdata Excel-fil](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-non-blanks.cs" >}}

