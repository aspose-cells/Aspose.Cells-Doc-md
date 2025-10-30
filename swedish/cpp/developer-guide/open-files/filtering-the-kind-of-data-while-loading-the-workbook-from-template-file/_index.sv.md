---
title: Filtrering av datatyp när du laddar arbetsboken från mallfil med C++
linktitle: Filtrera data vid laddning av arbetsbok
type: docs
weight: 400
url: /sv/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: Lär dig hur du filtrerar specifika datatyper vid laddning av arbetsbok från en mallfil med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Ibland vill du specificera vilken typ av data som ska laddas när du konstruerar arbetsboken från mallfilen. Filtrering av inläst data kan förbättra prestanda för ditt speciella syfte, särskilt när du använder [LightCells API:er](/cells/sv/cpp/using-lightcells-api/). Använd egenskapen [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) för detta ändamål.

{{% /alert %}}

Följande exempelkod laddar endast formobjekt när arbetsboken laddas från [mallfilen](5115552.xlsx) som du kan ladda ned från länken. Följande skärmbild visar innehållet i [mallfilen](5115552.xlsx) och förklarar också att datan i rött och med gul bakgrund inte kommer att laddas eftersom egenskapen [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) har ställts in till [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Följande skärmbild visar [utdata PDF](5115555.pdf) som du kan ladda ned från länken. Här kan du se att datan i rött och gul bakgrund inte finns men alla former är där.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

```c++
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

    // Set the load options, we only want to load shapes and do not want to load data
    LoadOptions loadOptions(LoadFormat::Xlsx);
    loadOptions.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Create workbook object from sample excel file using load options
    Workbook workbook(srcDir + u"sampleFilterChars.xlsx", loadOptions);

    // Save the output in pdf format
    workbook.Save(outDir + u"sampleFilterChars_out.pdf", SaveFormat::Pdf);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
