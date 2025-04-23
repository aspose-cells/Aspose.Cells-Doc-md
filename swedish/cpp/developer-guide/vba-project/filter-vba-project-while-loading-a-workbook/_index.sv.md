---
title: Filtrera VBA projekt vid inläsning av en arbetsbok med C++
linktitle: Filtrera VBA projekt vid inläsning av en arbetsbok
type: docs
weight: 140
url: /sv/cpp/filter-vba-project-while-loading-a-workbook/
description: Lär dig hur du filtrerar VBA projekt när du laddar en Excel arbetsbok med Aspose.Cells och C++.
---

## **Filtrera VBA-projekt vid inläsning av en Excel-arbetsbok i C++**

Vissa .xlsm/.xslb filer har ett extremt stort antal makron (eller mycket, mycket långa makron). Aspose.Cells laddar ostört denna (meta)data när du öppnar sådana arbetsböcker. Du kan dock kontrollera detta med [**LoadDataFilterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions) när du verkligen behöver enbart extrahera bladnamn för ett stort antal arbetsböcker och därigenom hoppa över sådant onödigt innehåll. Denna filterfunktion introduceras genom ett nytt alternativ, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions).

## **Exempelkod**

Följande exempelkod laddar en arbetsbok så att endast VBA filtreras. En testfil för att testa denna funktion kan hämtas från följande länk:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Set the load options, we do not want to load VBA
    LoadOptions loadOptions(LoadFormat::Auto);
    LoadFilter loadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::VBA);
    loadOptions.SetLoadFilter(&loadFilter);

    // Create workbook object from sample excel file using load options
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleMacroEnabledWorkbook.xlsm";
    Workbook book(inputFilePath, loadOptions);

    // Save the output in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    U16String outputFilePath = outputDir + u"OutputSampleMacroEnabledWorkbook.xlsm";
    book.Save(outputFilePath, SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
