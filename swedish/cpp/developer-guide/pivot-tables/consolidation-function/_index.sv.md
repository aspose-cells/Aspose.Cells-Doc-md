---
title: Sammanfattningsfunktion med C++
linktitle: Konsolideringsfunktion
type: docs
weight: 20
url: /sv/cpp/consolidation-function/
description: Lär dig hur du använder ConsolidationFunction på datafält i en pivottabell med Aspose.Cells och C++.
---

## **Konsolideringsfunktion**

Aspose.Cells kan användas för att tillämpa konsolideringsfunktion på datafält (eller värdefält) i pivottabellen. I Microsoft Excel kan du högerklicka på värdefältet och sedan välja **Värdefältsinställningar...** alternativet och sedan välja fliken **Sammanfatta värden med**. Där kan du välja valfri konsolideringsfunktion som Summa, Antal, Medel, Max, Min, Produkt, Distinkt antal, etc.

Aspose.Cells tillhandahåller uppräkning för att stödja följande konsolideringsfunktioner.

- ConsolidationFunction::Average
- ConsolidationFunction::Count
- ConsolidationFunction::CountNums
- ConsolidationFunction::DistinctCount
- ConsolidationFunction::Max
- ConsolidationFunction::Min
- ConsolidationFunction::Product
- ConsolidationFunction::StdDev
- ConsolidationFunction::StdDevp
- ConsolidationFunction::Sum
- ConsolidationFunction::Var
- ConsolidationFunction::Varp

### **Tillämpning av ConsolidationFunction på datavärderna i pivottabellen**

Följande kod tillämpar **Medelvärde** konsolideringsfunktion på det första datafältet (eller värdefältet) och **DistinktAntal** konsolideringsfunktion på det andra datafältet (eller värdefältet).

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
    U16String inputFilePath = srcDir + u"Book.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table of the worksheet
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Apply Average consolidation function to first data field
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Average);

    // Apply DistinctCount consolidation function to second data field
    pivotTable.GetDataFields().Get(1).SetFunction(ConsolidationFunction::DistinctCount);

    // Calculate the data to make changes affect
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Distinkt antal konsolideringsfunktionen stöds endast av Microsoft Excel 2013.

{{% /alert %}}
