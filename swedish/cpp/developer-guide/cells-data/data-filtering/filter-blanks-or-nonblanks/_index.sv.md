---
title: Hur man filtrerar tomma eller icke tomma med C++
linktitle: Hur man filtrerar tomma eller icke tomma.
type: docs
weight: 85
url: /sv/cpp/how-to-filter-blanks-and-non-blanks/
description: Lär dig hur du filtrerar tomma och icke tomma med hjälp av API et Aspose.Cells for C++.
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

## **Hur man filterar tomma med hjälp av Aspose.Cells**
Om en kolumn innehåller text så att några celler är tomma, och filter krävs för att endast välja de rader där tomma celler finns, kan funktionerna [AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchblanks/) och [AutoFilter.AddFilter(int fieldIndex, string criteria)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/addfilter/) användas enligt nedan. 

Se följande exemplarkod som laddar den [exempel Excel-filen](sample.xlsx) som innehåller lite dummydata. Exempelkoden använder tre metoder för att filtrera tomma. Sedan sparar den arbetsboken som [utdata Excel-filen](FilteredBlanks.xlsx). 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Method 1: Call MatchBlanks function to apply the filter
    // worksheet.GetAutoFilter().MatchBlanks(1);

    // Method 2: Call AddFilter function and set criteria to ""
    // worksheet.GetAutoFilter().AddFilter(1, u"");

    // Method 3: Call AddFilter function and set criteria to nullptr
    worksheet.GetAutoFilter().AddFilter(1, nullptr);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(u"FilteredBlanks.xlsx");

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Hur man filtrerar icke-tomma med hjälp av Aspose.Cells**

Se följande exempel på kod som laddar filen [exempel-Excel](sample.xlsx) som innehåller några dummy-data. Efter att ha laddat filen, anropa funktionen [AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchnonblanks/) för att filtrera icke-tomma data, och spara slutligen arbetsboken som [utdata Excel-fil](FilteredNonBlanks.xlsx). 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook by opening an existing Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchNonBlanks function to apply the filter on the second column (index 1)
    worksheet.GetAutoFilter().MatchNonBlanks(1);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(u"FilteredNonBlanks.xlsx");

    std::cout << "Filtered non-blanks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```


{{< app/cells/assistant language="cpp" >}}
