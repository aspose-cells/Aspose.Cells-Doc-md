---
title: Läs Axis etiketter efter att ha beräknat diagrammet med C++
linktitle: Läs av axeletiketter efter att ha beräknat diagrammet
description: Lär dig hur du läser av axel etiketter i Aspose.Cells for C++ efter att ha beräknat diagrammet. Vår guide visar hur du får åtkomst och hämtar axel etiketter, inklusive deras formatering och positionering.
keywords: Aspose.Cells for C++, diagram, axel etiketter, beräkning, läsning, åtkomst, hämtning, formatering, positionering.
type: docs
weight: 90
url: /sv/cpp/read-axis-labels-after-calculating-the-chart/
---

## **Möjliga användningsscenario**

Du kan läsa av axeletiketterna för ditt diagram efter att ha beräknat dess värden med hjälp av [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/)-metoden. Använd [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/getaxistexts/)-metoden för detta ändamål som kommer att returnera listan över axeletiketter.

## **Läs av axeletiketter efter att ha beräknat diagrammet**

Vänligen se följande kodexempel som laddar in den [exempel Excel-filen](ReadAxisLabels.xlsx) och läser kategoriaxlarna i diagrammet på den första arbetsbladet. Den skriver sedan ut värdena för axelmärkena på konsolen. Se konsolresultatet för kodexemplet nedan för referens.

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"ReadAxisLabels.xlsx");

    Worksheet ws = wb.GetWorksheets().Get(0);

    Chart ch = ws.GetCharts().Get(0);

    ch.Calculate();

    Vector<U16String> lstLabels = ch.GetCategoryAxis().GetAxisTexts();

    std::wcout << L"Category Axis Labels: " << std::endl;
    std::wcout << L"---------------------" << std::endl;

    for (int32_t i = 0; i < lstLabels.GetLength(); ++i)
    {
        std::wcout << reinterpret_cast<const wchar_t*>(lstLabels[i].GetData()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsoloutput**

{{< highlight cpp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
