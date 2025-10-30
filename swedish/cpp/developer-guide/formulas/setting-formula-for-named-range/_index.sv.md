---
title: Ställ in formel för namngiven område med C++
linktitle: Ange formel för namngivet område
type: docs
weight: 20
url: /sv/cpp/setting-formula-for-named-range/
description: Lär dig hur du ställer in formler för namngivna områden i Excel filer med Aspose.Cells och C++.
---

## **Ange formel för namngivet område**
Som Excel-applikationen ger Aspose.Cells API:er möjlighet att specificera en formel för ett namngivet område medan du använder dess [GetRefersTo()](https://reference.aspose.com/cells/cpp/aspose.cells/range/getrefersto/) egenskap. Det finns många användningsscenarier för denna funktion, några av vilka är detaljerade nedan.

### **Ange enkel formel för namngivet område**
Enkel formel skulle kunna vara en hänvisning till en annan cell i samma (eller annan) kalkylblad. Följande exempel skapar ett namngivet område i en ny kalkyl och anger dess hänvisning till en annan cell.

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

    // Get the WorksheetCollection
    WorksheetCollection worksheets = book.GetWorksheets();

    // Add a new Named Range with name "NewNamedRange"
    int index = worksheets.GetNames().Add(u"NewNamedRange");

    // Access the newly created Named Range
    Name name = worksheets.GetNames().Get(index);

    // Set RefersTo property of the Named Range to a formula. Formula references another cell in the same worksheet
    name.SetRefersTo(u"=Sheet1!$A$3");

    // Set the formula in the cell A1 to the newly created Named Range
    worksheets.Get(0).GetCells().Get(u"A1").SetFormula(u"NewNamedRange");

    // Insert the value in cell A3 which is being referenced in the Named Range
    worksheets.Get(0).GetCells().Get(u"A3").PutValue(u"This is the value of A3");

    // Calculate formulas
    book.CalculateFormula();

    // Save the result in XLSX format
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Named range created and formula calculated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Ange komplex formel för namngivet område**
En komplex formel kan vara vad som helst, till exempel en dynamiskt område eller en formel som sträcker sig över flera celler i olika kalkylblad. Följande exempel skapar ett dynamiskt område med hjälp av INDEX-funktionen för att hämta värdet från en lista baserat på dess plats.

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

    // Get the WorksheetCollection
    WorksheetCollection worksheets = book.GetWorksheets();

    // Add a new Named Range with name "data"
    int index = worksheets.GetNames().Add(u"data");

    // Access the newly created Named Range from the collection
    Name data = worksheets.GetNames().Get(index);

    // Set RefersTo property of the Named Range to a cell range in same worksheet
    data.SetRefersTo(u"=Sheet1!$A$1:$A$10");

    // Add another Named Range with name "range"
    index = worksheets.GetNames().Add(u"range");

    // Access the newly created Named Range from the collection
    Name range = worksheets.GetNames().Get(index);

    // Set RefersTo property to a formula using the Named Range data
    range.SetRefersTo(u"=INDEX(data,Sheet1!$A$1,1):INDEX(data,Sheet1!$A$1,9)");

    // Save the workbook
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Named ranges created and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Här är ytterligare ett exempel som använder ett namngivet område för att summera värden från 2 celler i olika kalkylblad.

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

    // Get the WorksheetCollection
    WorksheetCollection worksheets = book.GetWorksheets();

    // Insert some data in cell A1 of Sheet1
    worksheets.Get(u"Sheet1").GetCells().Get(u"A1").PutValue(10);

    // Add a new Worksheet and insert a value to cell A1
    worksheets.Get(worksheets.Add()).GetCells().Get(u"A1").PutValue(10);

    // Add a new Named Range with name "range"
    int index = worksheets.GetNames().Add(u"range");

    // Access the newly created Named Range from the collection
    Name range = worksheets.GetNames().Get(index);

    // Set RefersTo property of the Named Range to a SUM function
    range.SetRefersTo(u"=SUM(Sheet1!$A$1,Sheet2!$A$1)");

    // Insert the Named Range as formula to 3rd worksheet
    worksheets.Get(worksheets.Add()).GetCells().Get(u"A1").SetFormula(u"range");

    // Calculate formulas
    book.CalculateFormula();

    // Save the result in XLSX format
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Output file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
