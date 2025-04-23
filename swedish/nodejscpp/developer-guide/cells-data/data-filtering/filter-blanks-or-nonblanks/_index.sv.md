---
title: Hur man filtrerar tomma eller icke tomma.
type: docs
weight: 85
url: /sv/nodejs-cpp/how-to-filter-blanks-and-non-blanks/
description: Lär dig hur man filtrerar tomma och icke tomma med hjälp av API Aspose.Cells for Node.js via C++.
keywords: Filtrera tomma, filtrera icke tomma, filtrera tomma i kalkylblad, filtrera icke tomma i kalkylblad, filtrera tomma i excel, filtrera icke tomma i excel, filtrera tomma och icke tomma i excel
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

## **Hur man filtrerar tomma med Aspose.Cells for Node.js via C++**
Om en kolumn innehåller text så att några celler är tomma, och filter krävs för att endast välja de rader där tomma celler finns, kan funktionerna [**AutoFilter.matchBlanks(number)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#matchBlanks-number-) och [**AutoFilter.addFilter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#addFilter-number-string-) användas som demonstreras nedan. 

Se följande exemplarkod som laddar den [exempel Excel-filen](sample.xlsx) som innehåller lite dummydata. Exempelkoden använder tre metoder för att filtrera tomma. Sedan sparar den arbetsboken som [utdata Excel-filen](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FilterBlanks.js" >}}


## **Hur man filtrerar icke-tomma med Aspose.Cells for Node.js via C++**

Se följande exempel som laddar den [exempel-Excel-filen](sample.xlsx) som innehåller några dummydata. Efter att ha laddat filen, anropa funktionen [AutoFilter.matchNonBlanks(number)](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#matchNonBlanks-number-) för att filtrera icke-tom data, och spara sedan arbetsboken som [utdata Excel-fil](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FilterNonBlanks.js" >}}

