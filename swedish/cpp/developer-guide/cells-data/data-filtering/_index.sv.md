---
title: Filtrering av data med C++
linktitle: Datafiltrering
type: docs
weight: 85
url: /sv/cpp/data-filtering/
description: Lär dig hur man lägger till datafiltrering med hjälp av Aspose.Cells for C++ API et.
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

Aspose.Cells tillhandahåller en klass, `Workbook` som representerar en Excel-fil. `Workbook`-klassen innehåller en samling `Worksheets` som ger tillgång till varje kalkylblad i Excel-filen.

Ett kalkylblad representeras av `Worksheet`-klassen. `Worksheet`-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att skapa ett autofilter använd `AutoFilter`-egenskapen i `Worksheet`-klassen. `AutoFilter`-egenskapen är ett objekt av `AutoFilter`-klassen, som ger egenskapen `Range` för att specificera cellområdet som utgör en rubrikrad. Ett autofilter tillämpas på cellområdet som är rubrikraden.

I varje kalkylblad kan du endast ange ett filterområde. Detta är begränsat av Microsoft Excel. För anpassad datar filtering, använd metoden `AutoFilter.Custom`.

I det angivna exemplet nedan har vi skapat samma autofilter med Aspose.Cells som vi skapade med Microsoft Excel i avsnittet ovan.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range of the heading row
    worksheet.GetAutoFilter().SetRange(u"A1:B1");

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Olika typer av filter**

Aspose.Cells tillhandahåller flera alternativ för att använda olika typer av filter som färgfilter, datumfilter, nummerfilter, textfilter, blanka filter och icke-blanka filter.

##### **Fyllfärg**

Aspose.Cells tillhandahåller funktionen `AddFillColorFilter` för att filtrera data baserat på fyllningsfärgens egenskap i cellerna. I exemplet nedan används en mallfil med olika fyllningsfärger i den första kolumnen för att testa färgfilterfunktionen. Exempelfiler kan laddas ner från följande länkar.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiating a Workbook object
    Workbook workbook(srcDir + u"ColouredCells.xlsx");

    // Instantiating a CellsColor object for foreground color
    CellsColor clrForeground = workbook.CreateCellsColor();
    clrForeground.SetColor(Color::Red());

    // Instantiating a CellsColor object for background color
    CellsColor clrBackground = workbook.CreateCellsColor();
    clrBackground.SetColor(Color::White());

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call AddFillColorFilter function to apply the filter
    worksheet.GetAutoFilter().AddFillColorFilter(0, BackgroundType::Solid, clrForeground, clrBackground);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outDir + u"FilteredColouredCells.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Datum**

Olika typer av datfilter kan implementeras, som att filtrera alla rader med datum i januari 2018. Följande exempel kod demonstrerar detta filter med `AddDateFilter`-funktionen. Exempelfiler bifogas nedan.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call AddDateFilter function to apply the filter
    worksheet.GetAutoFilter().AddDateFilter(0, DateTimeGroupingType::Month, 2018, 1, 0, 0, 0, 0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Date filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Dynamiskt datum**

Ibland krävs dynamiska filter baserade på datum, t.ex. alla celler med datum i januari oavsett år. I detta fall används `DynamicFilter`-funktionen som visas i följande exempel. Exempelfiler bifogas nedan.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDynamicDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call DynamicFilter function to apply the filter
    worksheet.GetAutoFilter().Dynamic_Filter(0, DynamicFilterType::January);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Dynamic filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Nummer**

Anpassade filter kan tillämpas med Aspose.Cells, som att välja celler med nummer inom ett givet intervall. Följande exempel visar användningen av `Custom()`-funktionen för att filtrera nummer. Exempelfiler bifogas nedan.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Number.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"FilteredNumber.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call Custom function to apply the filter
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::GreaterOrEqual, 5, true, FilterOperatorType::LessOrEqual, 10);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Text**

Om en kolumn innehåller text och celler ska väljas som innehåller ett visst textvärde, kan `Filter()`-funktionen användas. I exemplet nedan innehåller mallfilen en lista med länder och rader ska väljas som innehåller ett specifikt land. Följande kod demonstrerar filtrering av text. Exempelfiler bifogas nedan.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Text.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredText.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call Filter function to apply the filter
    worksheet.GetAutoFilter().Filter(0, u"Angola");

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Tomma**

Om en kolumn innehåller text och några celler är tomma, och filtrering krävs för att välja bara de rader där tomma celler finns, kan `MatchBlanks()`-funktionen användas som visas nedan. Exempelfiler bifogas nedan.

1. [Tomma.xlsx](72417324.xlsx)
1. [FiltreradeTomma.xlsx](72417325.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiating a Workbook object
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchBlanks function to apply the filter
    worksheet.GetAutoFilter().MatchBlanks(0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outDir + u"FilteredBlank.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Ej tomma**

När celler med någon form av text ska filtreras, använd `MatchNonBlanks`-filtreringsfunktionen som demonstreras nedan. Exempelfiler bifogas nedan.

1. [Tomma.xlsx](72417324.xlsx)
1. [FiltreradeEjTomma.xlsx](72417326.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object and open the Excel file
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchNonBlanks function to apply the filter
    worksheet.GetAutoFilter().MatchNonBlanks(0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outDir + u"FilteredNonBlank.xlsx");

    std::cout << "Non-blank filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Anpassat filter med Innehåller**

Excel erbjuder anpassade filter som filtrerar rader som innehåller en specifik sträng. Denna funktion är tillgänglig i Aspose.Cells och demonstreras nedan genom att filtrera namnen i provfilen. Exempelfiler ges nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows containing string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::Contains, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Anpassat filter med EjInnehåller**

Excel tillhandahåller anpassade filter för att filtrera rader som inte innehåller en specifik sträng. Denna funktion finns i Aspose.Cells och visas nedan genom att filtrera namnen i exempelfilen nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows containing string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::NotContains, u"Be");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File filtered and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Anpassat filter med BörjaMed**

Excel tillhandahåller anpassade filter för att filtrera rader som börjar med en specifik sträng. Denna funktion finns i Aspose.Cells och visas nedan genom att filtrera namnen i exempelfilen nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows starting with string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::BeginsWith, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Anpassat filter med SlutaMed**

Excel erbjuder anpassade filter som filtrerar rader som slutar med en specifik sträng. Denna funktion är tillgänglig i Aspose.Cells och demonstreras nedan genom att filtrera namnen i provfilen nedan.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows end with string "ia"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::BeginsWith, u"ia");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Fortsatta ämnen**
- [Tillämpa Avancerat Filter i Microsoft Excel för att Visa Poster som Uppfyller Komplexa Kriterier](/cells/sv/cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Hämta alla dolda radindex efter uppdatering av autofilter](/cells/sv/cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
