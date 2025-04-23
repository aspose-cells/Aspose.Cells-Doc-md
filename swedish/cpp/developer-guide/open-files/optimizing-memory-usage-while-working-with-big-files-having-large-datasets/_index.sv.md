---
title: Optimera minnesanvändning vid arbete med stora filer som innehåller stora dataset med C++
linktitle: Optimera minnesanvändning
type: docs
weight: 180
url: /sv/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
description: Lär dig hur du optimerar minnesanvändningen när du arbetar med stora Excel filer med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

När man bygger en arbetsbok med stora datamängder, eller läser en stor Microsoft Excel-fil, är den totala mängden RAM som processen kommer att ta alltid en oro. Det finns åtgärder som kan anpassas för att hantera utmaningen. Aspose.Cells tillhandahåller vissa relevanta alternativ och API-anrop för att minska, sänka och optimera minnesanvändningen. Det kan också hjälpa processen att fungera effektivare och köra snabbare.

Använd [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) för att optimera minnesanvändningen för celldata och minska den totala minneskostnaden. När man bygger en stor datamängd för celler kan det spara en viss mängd minne jämfört med att använda standardinställningen ([**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/)).

{{% /alert %}}

## **Optimera minne**

### **Läsning av stora Excel-filer**

Det följande exemplet visar hur man läser en stor Microsoft Excel-fil i optimerat läge.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Specify the LoadOptions
    LoadOptions opt;

    // Set the memory preferences
    opt.SetMemorySetting(MemorySetting::MemoryPreference);

    // Instantiate the Workbook
    // Load the Big Excel file having large Data set in it
    Workbook wb(srcDir + u"Book1.xlsx", opt);

    std::cout << "Workbook loaded successfully with memory preference setting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Skrivning av stora Excel-filer**

Det följande exemplet visar hur man skriver en stor datamängd till en arbetsbok i optimerat läge.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook wb;

    // Set the memory preferences
    // Note: This setting cannot take effect for the existing worksheets that are created before using the below line of code
    wb.GetSettings().SetMemorySetting(MemorySetting::MemoryPreference);

    // Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

    // To change the memory setting of existing sheets, please change memory setting for them manually:
    Cells cells = wb.GetWorksheets().Get(0).GetCells();
    cells.SetMemorySetting(MemorySetting::MemoryPreference);

    // Input large dataset into the cells of the worksheet.
    // Your code goes here.
    // .........

    // Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
    cells = wb.GetWorksheets().Add(u"Sheet2").GetCells();

    // Input large dataset into the cells of the worksheet.
    // Your code goes here.
    // .........

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Försiktighet**

Standardalternativet, [**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) tillämpas för alla versioner. För vissa situationer, som att bygga en arbetsbok med en stor datamängd för celler, kan [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) -alternativet optimera minnesanvändningen och minska minneskostnaden för applikationen. Dock kan detta alternativ försämra prestandan i vissa speciella fall som följer.

1. **Åtkomst av celler slumpmässigt och upprepade gånger**: Den mest effektiva sekvensen för att komma åt cellernas samling är cell för cell i en rad, och sedan rad för rad. Särskilt om du får åtkomst till rader/celler via uppräknaren som erhållits från [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) och [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/), kommer prestandan att maximera med [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/).
1. **Infoga & Ta bort celler & rader**: Observera att om det finns många infogning/ta bort-operationer för celler/rader, kommer prestandaförsämringen märkas för *MemoryPreference* läge jämfört med *Normal* läge.
1. **Infogning & Radering av celler & rader**: Observera att om det finns mycket infogning/radering av operationer för celler/rader, kommer prestandanedbrytningen att vara märkbar för *MemoryPreference*-läget jämfört med *Normal*-läget.
