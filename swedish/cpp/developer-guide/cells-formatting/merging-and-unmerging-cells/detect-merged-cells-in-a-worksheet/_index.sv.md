---
title: Detektera sammanfogade celler i ett kalkylblad med C++
linktitle: Upptäck Sammanfogade Celler
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylblad. Det stöder att upptäcka sammanfogade celler i ett kalkylblad, vilket gör det enkelt för användare att identifiera och manipulera dessa celler. Denna artikel kommer att introducera hur man använder Aspose.Cells biblioteket för att upptäcka sammanfogade celler.
keywords: Aspose.Cells, Arbetsblad, Sammanfoga celler, Upptäcka, Identifiera, Fungera
type: docs
weight: 80
url: /sv/cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Den här artikeln ger information om hur man får sammanfogade cellområden i ett arbetsblad.

Aspose.Cells låter dig få sammanfogade cellområden i ett arbetsblad. Du kan också dela upp dem. Den här artikeln visar det enklaste koden att använda **Aspose.Cells API** för att utföra uppgiften.

{{% /alert %}}

Komponenten tillhandahåller [**Cells::GetMergedAreas()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmergedareas/)-metoden som kan hämta alla sammanfogade celler. Följande kodexempel visar hur du kan upptäcka sammanfogade celler i ett kalkylblad.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleInput.xlsx");

    Worksheet wkSheet = workbook.GetWorksheets().Get(u"Sheet2");

    wkSheet.GetCells().Clear();

    Vector<CellArea> areas = wkSheet.GetCells().GetMergedAreas();

    for (int i = 0; i < areas.GetLength(); ++i)
    {
        int frow = areas[i].StartRow;
        int fcol = areas[i].StartColumn;
        int erow = areas[i].EndRow;
        int ecol = areas[i].EndColumn;

        int trows = erow - frow + 1;
        int tcols = ecol - fcol + 1;

        wkSheet.GetCells().UnMerge(frow, fcol, trows, tcols);
    }

    U16String outputPath = outDir + u"MergeTrial.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Worksheet processing completed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
