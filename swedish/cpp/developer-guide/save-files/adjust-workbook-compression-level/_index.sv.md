---
title: Justera arbetsbocks kompressionsnivå med C++
linktitle: Justera arbetsbokens komprimeringsnivå
type: docs
weight: 180
url: /sv/cpp/adjust-workbook-compression-level/
description: Lär dig hur du justerar kompressionsnivån för en arbetsbok med Aspose.Cells for C++ för att optimera filstorlek och bearbetningstid.
---

## **Justera arbetsbokens kompressionsnivå**

Utvecklare kan justera arbetsbokens kompressionsnivå när de arbetar med större arbetsböcker. Utvecklare kan prioritera mindre filstorlekar framför bearbetningstid eller vice versa. Aspose.Cells tillhandahåller [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) uppräkningen som du kan använda för att ställa in arbetsbokens kompressionsnivå. Uppräkningen [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) tillhandahåller följande medlemmar.

- Nivå1: Den snabbaste men minst effektiva kompressionen.
- Nivå2: Lite långsammare, men bättre än nivå 1.
- Nivå3: Lite långsammare, men bättre än nivå 2.
- Nivå4: Lite långsammare, men bättre än nivå 3.
- Nivå5: Lite långsammare än nivå 4, men med bättre kompression.
- Nivå6: En bra balans mellan hastighet och kompressionseffektivitet.
- Nivå7: Ganska bra kompression!
- Nivå8: Bättre kompression än nivå 7!
- Nivå9: "Bästa" kompressionen, där bäst innebär största minskningen av indataströmmens storlek. Detta är även den långsammaste kompressionen.

Följande kodsnutt demonstrerar användningen av [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) uppräkningen och jämför konverteringstiden för Nivå1, Nivå6 och Nivå9. Du kan också jämföra storlekarna på de genererade filerna.

```cpp
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std::chrono;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"LargeSampleFile.xlsx");

    // Create XlsbSaveOptions object
    XlsbSaveOptions options;

    // Set compression level to 1 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level1);
    auto start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_1_out.xlsb", options);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 1 Elapsed Time: " << duration.count() << std::endl;

    // Set compression level to 6 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level6);
    start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_6_out.xlsb", options);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 6 Elapsed Time: " << duration.count() << std::endl;

    // Set compression level to 9 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level9);
    start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_9_out.xlsb", options);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 9 Elapsed Time: " << duration.count() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
