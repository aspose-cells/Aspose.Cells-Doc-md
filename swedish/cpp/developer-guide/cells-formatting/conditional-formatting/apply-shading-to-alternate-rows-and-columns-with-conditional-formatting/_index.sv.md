---
title: Tillämpa skuggning på varannan rad och kolumn med villkorsformatering med C++
linktitle: Tillämpa skuggning på varannan rad och kolumn
description: Hur man använder Aspose.Cells biblioteket i C++ för att tillämpa villkorsskuggningar för varannan rad och kolumn. Genom att justera dessa kriterier får du mer kontroll över hur cellerna ser ut och visas.
keywords: Aspose.Cells, Villkorsformatering, C++, Varannan rad, Varannan kolumn, Skuggor
type: docs
weight: 30
url: /sv/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells API:er möjliggör att lägga till och manipulera villkorsformateringsregler för [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-objektet. Dessa regler kan anpassas på flera sätt för att få önskad formatering baserat på villkor eller regler. Denna artikel visar hur man använder API:erna Aspose.Cells for C++ för att tillämpa skuggning på varannan rad och kolumn med hjälp av villkorsformatering och Excels inbyggda funktioner.

{{% /alert %}}

Denna artikel använder Excels inbyggda funktioner såsom RAD, KOLUMN och MOD. Här är några detaljer om dessa funktioner för en bättre förståelse av kodsnutten som följer.

- **RAD()**-funktionen returnerar radnumret för en cellreferens. Om referensparametern utelämnas, antar den att referensen är celladressen där RAD-funktionen har skrivits in.
- **KOLUMN()**-funktionen returnerar kolumnnumret för en cellreferens. Om referensparametern utelämnas, antar den att referensen är celladressen där KOLUMN-funktionen har skrivits in.
- **MOD()**-funktionen returnerar resten efter att ett nummer har delats av en divisor, där det första parametern till funktionen är det numeriska värdet vars rest du vill hitta och det andra parametern är det tal som används för att dela in i nummerparametern. Om divisorn är 0 kommer den att returnera felen #DIV/0!.

Låt oss börja skriva kod för att uppnå detta mål med hjälp av API:erna Aspose.Cells for C++.

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

    // Create an instance of Workbook
    Workbook book;

    // Access the Worksheet on which desired rule has to be applied
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add FormatConditions to the instance of Worksheet
    int idx = sheet.GetConditionalFormattings().Add();

    // Access the newly added FormatConditions via its index
    auto conditionCollection = sheet.GetConditionalFormattings().Get(idx);

    // Define a CellsArea on which conditional formatting will be applicable
    // The code creates a CellArea ranging from A1 to I20
    CellArea area = CellArea::CreateCellArea(u"A1", u"I20");

    // Add area to the instance of FormatConditions
    conditionCollection.AddArea(area);

    // Add a condition to the instance of FormatConditions
    // For this case, the condition type is expression, which is based on some formula
    idx = conditionCollection.AddCondition(FormatConditionType::Expression);

    // Access the newly added FormatCondition via its index
    FormatCondition formatCondition = conditionCollection.Get(idx);

    // Set the formula for the FormatCondition
    // Formula uses the Excel's built-in functions as discussed earlier in this article
    formatCondition.SetFormula1(u"=MOD(ROW(),2)=0");

    // Set the background color and pattern for the FormatCondition's Style
    formatCondition.GetStyle().SetBackgroundColor(Color::Blue());
    formatCondition.GetStyle().SetPattern(BackgroundType::Solid);

    // Save the result on disk
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Följande ögonblicksbild visar det resulterande kalkylarket som är laddat i Excel-applikationen.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

För att applicera nyanser på alternativa kolumner, behöver du bara ändra formeln **=MOD(RAD(),2)=0** till **=MOD(KOLUMN(),2)=0**, det vill säga; istället för att få radindexet, modifiera formeln för att hämta kolumnindexet. 
Det resulterande kalkylarket kommer i detta fall att se ut som följer.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
{{< app/cells/assistant language="cpp" >}}
