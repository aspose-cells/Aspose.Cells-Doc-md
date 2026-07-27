---
title: Konsolidierungsfunktion mit C++
linktitle: Konsolidierungsfunktion
type: docs
weight: 20
url: /de/cpp/consolidation-function/
description: Erfahren Sie, wie Sie die Konsolidierungsfunktion auf Datenfelder einer Pivot Tabelle mit Aspose.Cells und C++ anwenden.
---

## **Konsolidierungsfunktion**

Mit Aspose.Cells kann die Konsolidierungsfunktion auf Datenfelder (oder Wertefelder) der Pivot-Tabelle angewendet werden. In Microsoft Excel können Sie mit der rechten Maustaste auf das Wertefeld klicken und dann die Option **Wertfeldeinstellungen...** auswählen, und dann den Tab **Werte zusammenfassen nach** auswählen. Von dort aus können Sie eine Konsolidierungsfunktion Ihrer Wahl wie Summe, Anzahl, Durchschnitt, Maximum, Minimum, Produkt, Eindeutige Anzahl usw. auswählen.

Aspose.Cells bietet die Aufzählung [**ConsolidationFunction**](https://reference.aspose.com/cells/cpp/aspose.cells/consolidationfunction/), um die folgenden Konsolidierungsfunktionen zu unterstützen.

- Konsolidierungsfunktion::Durchschnitt
- Konsolidierungsfunktion::Anzahl
- Konsolidierungsfunktion::ZähleNummern
- Konsolidierungsfunktion::EindeutigeAnzahl
- Konsolidierungsfunktion::Max
- Konsolidierungsfunktion::Min
- Konsolidierungsfunktion::Produkt
- Konsolidierungsfunktion::Standardabweichung
- Konsolidierungsfunktion::PopStandardabweichung
- Konsolidierungsfunktion::Summe
- Konsolidierungsfunktion::Varianz
- Konsolidierungsfunktion::PopVarianz

### **Anwendung von ConsolidationFunction auf Datenfelder des Pivot-Tabellen**

Der folgende Code wendet die **Durchschnitt**-Konsolidierungsfunktion auf das erste Datenfeld (oder Wertefeld) und die **DistinctCount**-Konsolidierungsfunktion auf das zweite Datenfeld (oder Wertefeld) an.

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

Die Konsolidierungsfunktion DistinctCount wird nur von Microsoft Excel 2013 unterstützt.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
