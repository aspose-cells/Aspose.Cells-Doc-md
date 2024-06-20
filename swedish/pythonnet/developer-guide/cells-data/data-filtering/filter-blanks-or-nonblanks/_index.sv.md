---
title: Hur man filtrerar tomma eller icke tomma.
type: docs
weight: 85
url: /sv/python-net/how-to-filter-blanks-and-non-blanks/
description: Lär dig hur man filtrerar tomma och icke tomma genom att använda Aspose.Cells for Python via .NET API.
keywords: Python Excel bibliotek, Python Filter Blanks, Python Filter Non Blanks, Python Filter Blanks i kalkylblad, Python Filter Non Blanks i kalkylblad, Python Filter Blanks i Excel, Python Filter Non Blanks i Excel, Python Filter Blanks och Non Blanks i Excel
---

## **Möjliga användningsscenario**
Filtrering av data i Excel är ett värdefullt verktyg som förbättrar dataanalys, utforskning och presentation genom att möjliggöra för användare att fokusera på specifika delmängder av data baserat på deras kriterier, vilket gör hela datahanterings- och tolkningsprocessen mer effektiv och effektiv.

## **Hur man filtrerar tomma eller icke-tomma i Excel**
I Excel kan du enkelt filtrera tomma eller icke-tomma med hjälp av filtreringsalternativen. Så här kan du göra det:

### **Hur man filtrerar tomma i Excel**
1. Välj intervallet: Klicka på bokstaven i kolumnrubriken för att välja hela kolumnen eller välj intervallet där du vill filtrera bort tomma.
1. Öppna filtermenyn: Gå till fliken "Data" i menyfliken.
<br>
<image src="1.png" width="70%" />
1. Filteralternativ: Klicka på knappen "Filter". Detta lägger till filterpilar i det valda intervallet.
1. Filtrera tomma: Klicka på filterpilen i kolumnen där du vill filtrera bort tomma. Avmarkera alla alternativ utom "Tomma" och klicka på OK. Detta visar endast de tomma cellerna i den kolumnen.
<br>
<image src="2.png" width="70%" />
1. Resultatet är som följer:
<br>
<image src="3.png" width="70%" />

### **Hur man filtrerar icke-tomma i Excel**
1. Välj intervallet: Klicka på bokstaven i kolumnrubriken för att välja hela kolumnen eller välj intervallet där du vill filtrera icke-tomma.
1. Öppna filtermenyn: Gå till fliken "Data" i menyfliken.
<br>
<image src="1.png" width="70%" />
1. Filteralternativ: Klicka på knappen "Filter". Detta lägger till filterpilar i det valda intervallet.
1. Filtrera icke-tomma: Klicka på filterpilen i kolumnen där du vill filtrera icke-tomma. Avmarkera alla alternativ utom "Icke-tomma" eller "Anpassat" och ställ in villkoren därefter. Klicka på OK. Detta visar endast cellerna som inte är tomma i den kolumnen.
<br>
<image src="4.png" width="70%" />
1. Resultatet är som följer:
<br>
<image src="5.png" width="70%" />

## **Hur man filtrerar tomma med hjälp av Aspose.Cells for Python Excel Library**
Om en kolumn innehåller text så att några celler är tomma och filtrering krävs för att endast välja de rader där tomma celler finns, [AutoFilter.match_blanks(field_index)](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/match_blanks/#int) och [AutoFilter.add_filter(field_index, criteria)](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/add_filter/#int)funktioner kan användas som visas nedan. 

Se följande exemplarkod som laddar den [exempel Excel-filen](sample.xlsx) som innehåller lite dummydata. Exempelkoden använder tre metoder för att filtrera tomma. Sedan sparar den arbetsboken som [utdata Excel-filen](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filter-blanks.py" >}}

## **Hur man filtrerar icke-tomma med hjälp av Aspose.Cells för Python Excel Library**

Se följande exemplarkod som laddar den [exempel Excel-filen](sample.xlsx) som innehåller lite dummydata. Efter att ha laddat filen, anropas [AutoFilter.match_non_blanks(field_index)](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/match_non_blanks/#int)funktionen för att filtrera icke-tomma data, och slutligen sparas arbetsboken som [utdata Excel-filen](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filter-non-blanks.py" >}}

