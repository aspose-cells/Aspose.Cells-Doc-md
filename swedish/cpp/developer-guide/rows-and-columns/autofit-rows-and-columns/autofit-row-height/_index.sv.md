---
title: Automatisk anpassning av radhöjd vid laddning av fil med C++
linktitle: Autofit radhöjden automatiskt när filen laddas
type: docs
weight: 120
url: /sv/cpp/autofit-row-height/
description: Lär dig hur du anpassar rader vars höjd inte är anpassad med Aspose.Cells och C++.
keywords: Automatisk anpassning av radhöjd vid filinläsning, justera automatiskt radhöjden vid öppnande av Excel fil.
---

## **Möjliga användningsscenario**
Radens höjd matchar automatiskt teckensnittet för innehållet, men när höjden på den cachade raden inte matchar höjden på innehållet i filen, kommer MS Excel att automatiskt justera radhöjden när filen laddas, medan Aspose.Cells inte automatiskt anpassar den för att förbättra prestandan. Om du behöver använda Aspose.Cells-programmet för att automatiskt matcha linjehöjder när du laddar filer kan du åstadkomma detta genom parametern [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/).

Se följande bilddata. Vi kan observera att cachradens höjd i rad 11 är 15, men Excel justerade automatiskt radhöjden när filen laddades.
<br>
<img src="1.png" width=70% />

## **Justera radhöjd med Aspose.Cells**
Om du direkt laddar filen och sparar den till PDF kommer datan inte att visas fullt ut i PDF eftersom dess cachradshöjd endast är 15.
<br>
<img src="2.png" width=70% />
<br>
Om du sätter parametern [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/) till true vid inläsning av filen kommer Aspose.Cells automatiskt att justera radhöjden. Den justerade linjehöjden kan effektivt uppfylla textvisningskraven.
<br>
<img src="3.png" width=70% />

## **C++ exempel kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Define the file path
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file and save it as PDF
    {
        Workbook wb(filePath + u"sample.xlsx");
        wb.Save(filePath + u"out.pdf");
    }

    // Set load options for the second workbook
    LoadOptions loadOptions;
    {
        AutoFitterOptions autoFitterOptions;
        autoFitterOptions.SetOnlyAuto(true);
        loadOptions.SetAutoFitterOptions(autoFitterOptions);
    }

    // Open the existing Excel file with load options and save it as PDF
    {
        Workbook book(filePath + u"sample.xlsx", loadOptions);
        book.Save(filePath + u"out2.pdf");
    }

    std::cout << "PDF files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
