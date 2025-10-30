---
title: Beräkna formulär med C++
linktitle: Beräkna formler
description: Denna artikel introducerar hur man använder Aspose.Cells bibliotek för att beräkna formler i Microsoft Excel med C++. Genom att ladda en befintlig Excel fil eller skapa en ny kan vi använda Aspose.Cells metoder för att beräkna formeln och få resultatet. Slutligen sparar vi den modifierade Excel filen till disk.
keywords: Aspose.Cells, Excel, formler, beräkningar, Direkt Beräkning av Formel, Beräkna formler upprepade gånger, lägga till formler.
type: docs
weight: 125
url: /sv/cpp/calculate-formulas/
---

## **Lägga till formler och beräkna resultat**

Aspose.Cells har en inbäddad formelberäkningsmotor. Den kan inte bara omberäkna formler importerade från designermallar utan också stödjer beräkning av resultaten av formler som läggs till vid körning.

Aspose.Cells stödjer de flesta av de formler eller funktioner som ingår i Microsoft Excel (Läs [en lista över de funktioner som stöds av beräkningsmotorn](/cells/sv/cpp/supported-formula-functions/)). Dessa funktioner kan användas via API:erna eller designer kalkylblad. Aspose.Cells stöder ett stort antal matematiska, sträng-, boolean-, datum/tids-, statistiska, databas-, uppslags- och referensformler.

Använd [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/)-egenskapen eller [**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/)-metoderna i [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-klassen för att lägga till en formel till en cell. När du tillämpar en formel, börja alltid strängen med ett likhetstecken (=) som du gör när du skapar en formel i Microsoft Excel, och använd ett komma (,) för att avgränsa funktionsparametrar.

För att beräkna resultaten av formler kan användaren anropa [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) metoden i [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klassen, som bearbetar alla formler inbäddade i en Excel-fil. Eller, användaren kan anropa [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) metoden i [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen, som bearbetar alla formler inbäddade i ett blad. Alternativt kan användaren också anropa [**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/) metoden i [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) klassen, som processar formeln för en Cell:

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add values to cells
    worksheet.GetCells().Get(u"A1").PutValue(1);
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(3);

    // Add a SUM formula to cell A4
    worksheet.GetCells().Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Calculate the results of formulas
    workbook.CalculateFormula();

    // Get the calculated value of cell A4
    U16String value = worksheet.GetCells().Get(u"A4").GetStringValue();

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Viktigt att veta för formler**

{{% alert color="primary" %}}

Egenskapen **GetFormula** och metoderna **SetFormula(...)** i [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) klassen fungerar annorlunda än **Calculate**-metoderna i [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) och [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) klasserna. **GetFormula**-egenskapen och **SetFormula(...)**-metoderna lägger helt enkelt till formeln i en cell men beräknar inte resultatet vid körning. För att få formelresultatet, vänligen använd **Calculate**-metoderna.

{{% /alert %}}

## **Direkt beräkning av formel**

Aspose.Cells har en inbyggd formelberäkningsmotor. Förutom att beräkna formler som importerats från en designfil kan Aspose.Cells också beräkna formelresultat direkt.

Ibland måste du beräkna formelresultat direkt utan att lägga till dem i ett kalkylblad. Värdena för cellerna som används i formeln finns redan i ett kalkylblad, och allt du behöver är att hitta resultatet av dessa värden baserat på någon Microsoft Excel-formel utan att lägga till formeln i ett kalkylblad.

Du kan använda Aspose.Cells formelberäknings-API:er för {0} till {1} för att {2} resultaten av sådana formler utan att lägga till dem i kalkylbladet:

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

    // Create a workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put 20 in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.PutValue(20);

    // Put 30 in cell A2
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.PutValue(30);

    // Calculate the Sum of A1 and A2
    Aspose::Cells::Object results = worksheet.CalculateFormula(u"=Sum(A1:A2)");

    // Print the output
    std::cout << "Value of A1: " << cellA1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Value of A2: " << cellA2.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Result of Sum(A1:A2): " << results.ToString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

Ovanstående kod ger följande utmatning:
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Hur man räknar ut formler upprepade gånger**

När det finns många formler i arbetsboken och användaren behöver beräkna dem upprepade gånger med att endast modifiera en liten del av dem kan det vara hjälpsamt för prestandan att aktivera formelberäkningskedjan: [**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/cpp/aspose.cells/formulasettings/getenablecalculationchain/).

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the template workbook
    Workbook workbook(srcDir + u"book1.xls");

    // Print the time before formula calculation
    auto start = std::chrono::system_clock::now();
    std::time_t start_time = std::chrono::system_clock::to_time_t(start);
    std::cout << "Start time: " << std::ctime(&start_time);

    // Set the CreateCalcChain as true
    workbook.GetSettings().GetFormulaSettings().SetEnableCalculationChain(true);

    // Calculate the workbook formulas
    workbook.CalculateFormula();

    // Print the time after formula calculation
    auto end = std::chrono::system_clock::now();
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);
    std::cout << "End time: " << std::ctime(&end_time);

    // Change the value of one cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"newvalue");

    // Re-calculate those formulas which depend on cell A1
    workbook.CalculateFormula();

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Viktigt att veta**

{{% alert color="primary" %}}

Som standard är beräkningskedjan inaktiverad. Eftersom skapandet av kedjan också kräver extra tid kan den första gången du beräknar formler ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)) ta mer CPU-tid och minnesutrymme jämfört med att beräkna formler utan kedja. Om användaren inte behöver beräkna formler upprepade gånger bör det rekommenderade beteendet vara att beräkna formeln direkt utan att skapa en beräkningskedja.

{{% /alert %}}

## **Avancerade ämnen**
- [Lägg till celler i Microsoft Excel Formelövervakningsfönstret](/cells/sv/cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Beräkning av IFNA-funktionen med Aspose.Cells](/cells/sv/cpp/calculating-ifna-function-using-aspose-cells/)
- [Beräkning av Array Formula av Data Tables](/cells/sv/cpp/calculation-of-array-formula-of-data-tables/)
- [Beräkning av Excel 2016 MINIFS och MAXIFS funktioner](/cells/sv/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Minska tiden för beräkning av Cell.Calculate-metoden](/cells/sv/cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Direkt beräkning av anpassad funktion utan att skriva den i en kalkylblad](/cells/sv/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementera anpassad beräkningsmotor för att förlänga standardberäkningsmotorn för Aspose.Cells](/cells/sv/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Returnera en rad med värden med hjälp av AbstractCalculationEngine](/cells/sv/cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Inställning av Formelberäkningsläge för Arbetsbok](/cells/sv/cpp/setting-formula-calculation-mode-of-workbook/)
- [Användning av FormulaText-funktionen i Aspose.Cells](/cells/sv/cpp/using-formulatext-function-in-aspose-cells/)
{{< app/cells/assistant language="cpp" >}}
