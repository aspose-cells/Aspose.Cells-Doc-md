---
title: Förkorta beräkningstiden för Cell.Calculate metoden med C++
linktitle: Förkorta beräkningstiden för Cell.Calculate
description: Den här artikeln introducerar hur man använder Aspose.Cells biblioteket för att minska beräkningstiden för cellberäkningsmetoder i Microsoft Excel. Genom att ladda en befintlig Excel fil eller skapa en ny kan vi använda de metoder som tillhandahålls av Aspose.Cells för att optimera cellberäkningsmetoden och förbättra dess prestanda. Slutligen sparar vi den modifierade Excel filen på disk.
keywords: Aspose.Cells, Excel, Cellberäkningsmetoder, optimering, prestanda, minskning av beräkningstid
type: docs
weight: 100
url: /sv/cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Möjliga användningsscenario**

Vanligtvis rekommenderar vi användare att anropa [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)-metoden en gång och sedan hämta de beräknade värdena för enskilda celler. Men ibland vill användare inte beräkna hela arbetsboken. De vill bara beräkna en enskild cell. Aspose.Cells tillhandahåller [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/)-egenskapen som du kan ställa till **falskt** och det kommer att minska beräkningstiden för enskilda celler avsevärt. För eftersom den rekursiva egenskapen är inställd på **true**, så beräknas alla beroenden för cellerna varje gång. Men när den är **falskt**, beräknas beroende celler bara en gång och beräknas inte igen vid efterföljande anrop.

## **Minska beräkningstiden för Cell.Calculate() metoden**

Följande exempel kod illustrerar användningen av [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/)-egenskapen. Kör gärna denna kod med den givna [exempel excel filen](5113710.xlsx) och kontrollera dess konsolutmatning. Du kommer att märka att inställningen av den rekursiva egenskapen till **falskt** minskar beräkningstiden avsevärt. Läs också kommentarerna för en bättre förståelse av denna egenskap.

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

void TestCalcTimeRecursive(bool isRecursive) {
    Workbook* workbook = new Workbook();
    CalculationOptions options;
    options.SetRecursive(isRecursive);

    auto start = std::chrono::high_resolution_clock::now();
    workbook->CalculateFormula(&options);
    auto end = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    std::cout << "Time (recursive=" << isRecursive << "): " << duration << " ms" << std::endl;

    delete workbook;
}

int main() {
    Aspose::Cells::Startup();

    TestCalcTimeRecursive(true);
    TestCalcTimeRecursive(false);

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std::chrono;

void TestCalcTimeRecursive(bool rec) {
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"sample.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(0);
    CalculationOptions opts;
    opts.SetRecursive(rec);

    auto start = high_resolution_clock::now();
    for (int i = 0; i < 1000000; i++) {
        ws.GetCells().Get(u"A1").Calculate(opts);
    }
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(stop - start);
    long estimatedTime = duration.count() / 1000;
    std::cout << "Recursive " << rec << ": " << estimatedTime << " seconds" << std::endl;
}

int main() {
    Aspose::Cells::Startup();
    TestCalcTimeRecursive(true);
    TestCalcTimeRecursive(false);
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **Konsoloutput**

Det här är konsolutdata för ovanstående exempel kod när den körs med den givna [exempel excel filen](5113710.xlsx) på vår maskin. Observera att din utdata kan skilja sig, men den förflutna tiden efter att ha ställt in den rekursiva egenskapen till **falskt** kommer alltid att vara mindre än vid inställning till **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
